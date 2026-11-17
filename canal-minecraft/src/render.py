# -*- coding: utf-8 -*-
"""Montaje de los vídeos.  Uso:  python3 render.py [prefijo-slug ...]   (sin argumentos: todos los que no existan)."""
import math, os, subprocess, sys, json, zlib, random
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw

import art
from art import (W, H, THEMES, GOLD, WHITE, INK, text_img, wrap, add_glow, shadowed, bevel_box, label_box, gui_panel,
                 slot, sprite, cube, cube_spin, tile, SILK, PIX, MB, MX, MR)
import audio
from content import VIDEOS, CHANNEL, HANDLE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build"); OUT = os.path.join(ROOT, "videos"); SUBS = os.path.join(ROOT, "subtitulos")
FPS = 30
PAD_BEFORE, PAD_AFTER = 0.25, 0.5
PANEL = (80, 100, 1840, 900)


# ================================================================ animación
def clamp(p): return max(0.0, min(1.0, p))
def ease(p): p = clamp(p); return 1 - (1 - p) ** 3
def back(p):
    p = clamp(p); c = 1.9; return 1 + (c + 1) * (p - 1) ** 3 + c * (p - 1) ** 2
def bounce(p):
    p = clamp(p); n, d = 7.5625, 2.75
    if p < 1 / d: return n * p * p
    if p < 2 / d: p -= 1.5 / d; return n * p * p + 0.75
    if p < 2.5 / d: p -= 2.25 / d; return n * p * p + 0.9375
    p -= 2.625 / d; return n * p * p + 0.984375


class Item:
    """Elemento que entra con animación. kind: up, left, right, pop, fade, drop."""
    def __init__(self, img, x, y, t0=0.0, kind="up", dur=0.45, center=False, sfx=None):
        if center: x -= img.width // 2
        self.img, self.x, self.y, self.t0, self.kind, self.dur, self.sfx = img, int(x), int(y), t0, kind, dur, sfx
        self.cache = {}

    def variant(self, step):
        if step not in self.cache:
            f = step / 10.0; im = self.img
            if self.kind == "pop":
                sc = max(0.05, back(f))
                im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BILINEAR)
            if step < 10 and self.kind != "drop":
                im = im.copy(); a = im.getchannel("A").point(lambda v: int(v * min(1, f * 1.6))); im.putalpha(a)
            self.cache[step] = im
        return self.cache[step]

    def draw(self, fr, t):
        if t < self.t0: return
        p = clamp((t - self.t0) / self.dur); step = int(round(p * 10))
        im = self.variant(step); x, y = self.x, self.y
        if self.kind == "up": y += int((1 - ease(p)) * 60)
        elif self.kind == "left": x -= int((1 - ease(p)) * 110)
        elif self.kind == "right": x += int((1 - ease(p)) * 110)
        elif self.kind == "pop": x += (self.img.width - im.width) // 2; y += (self.img.height - im.height) // 2
        elif self.kind == "drop": y -= int((1 - bounce(p)) * 160)
        fr.paste(im, (x, y), im)


def reveal_times(n, dur, start=0.5, end_frac=0.75):
    if n <= 1: return [start]
    end = max(start + 0.6, dur * end_frac)
    return [start + i * (end - start) / (n - 1) for i in range(n)]


def hero(spec, size):
    """spec: ('cube', top, side) | ('sprite', name)."""
    if spec[0] == "cube":
        return ("spin", cube_spin(spec[1], spec[2] if len(spec) > 2 else None, size))
    return ("img", sprite(spec[1], size))


def hero_dyn(spec, size, cx, cy, t0=0.0, glow=None, bob=14, speed=1.0, glint=False):
    """Devuelve una función que dibuja el héroe (cubo girando o sprite flotando). glint: brillo de encantamiento."""
    kind, data = hero(spec, size)
    if kind == "img":
        base = art.glint_frames(data) if glint else [data]
        if glow: frames = [add_glow(f, glow, 26, 0.9) for f in base]
        else: frames = [shadowed(f, max(6, size // 26), 110) for f in base]
        im = frames[0]
    else:
        frames = [add_glow(f, glow, 24, 0.7) if glow else f for f in data]
    def draw(fr, lt):
        if lt < t0: return
        p = clamp((lt - t0) / 0.5); sc = back(p)
        yy = cy + math.sin((lt - t0) * 2.2 * speed) * bob
        if kind == "spin":
            img = frames[int((lt - t0) * 14 * speed) % len(frames)]
        else:
            img = frames[int((lt - t0) * 16) % len(frames)] if len(frames) > 1 else im
        if sc < 0.999:
            img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BILINEAR)
        fr.paste(img, (int(cx - img.width / 2), int(yy - img.height / 2)), img)
    return draw


def badge(txt, col):
    return label_box(txt, SILK, 34, fill=col, fg=INK if sum(col) > 380 else WHITE, padx=22, pady=12, b=6)


def heading(txt, th, x=150, y=150, size=76, max_w=1600, col=WHITE):
    return Item(text_img(txt, SILK, size, fill=col, max_w=max_w), x, y, 0.05, "left")


# ================================================================ escenas
def build_scene(sc, th, dur, vid):
    t = sc["t"]; acc, acc2 = th["acc"], th["acc2"]; items = []; dyn = []; sfx = []
    if t == "title":
        if sc.get("hero"):
            dyn.append(hero_dyn(sc["hero"], 320 if sc["hero"][0] == "cube" else 250, W // 2, 330 if sc["hero"][0] == "cube" else 345, 0.0, glow=acc, glint=sc.get("glint", False)))
        if sc.get("badge"):
            items.append(Item(badge(sc["badge"], acc), W // 2, 118, 0.05, "pop", center=True))
        big = text_img(wrap(sc["h"], SILK, 130, 1650), SILK, 130, fill=WHITE, max_w=1700, align="center", glow=(0, 0, 0), glow_r=16)
        items.append(Item(big, W // 2, 500, 0.25, "drop", 0.7, center=True, sfx="place"))
        sub = text_img(sc["s"], MX, 52, fill=acc2, max_w=1500, align="center", glow=(0, 0, 0), glow_r=10)
        items.append(Item(sub, W // 2, 520 + big.height, 0.7, "up", center=True))
        if sc.get("splash"):
            sp = text_img(sc["splash"], SILK, 46, fill=GOLD, shadow_col=(62, 52, 0)).rotate(16, expand=True, resample=Image.BICUBIC)
            sx, sy = W // 2 + big.width // 2 - 60, 470
            sps = {k: sp.resize((int(sp.width * (0.9 + k * 0.015)), int(sp.height * (0.9 + k * 0.015))), Image.BILINEAR) for k in range(12)}
            def dsplash(fr, lt, sps=sps, sx=sx, sy=sy):
                if lt < 1.0: return
                k = int((math.sin((lt - 1.0) * 7) * 0.5 + 0.5) * 11.99); im = sps[k]
                fr.paste(im, (sx - im.width // 2, sy - im.height // 2), im)
            dyn.append(dsplash); sfx.append((1.0, "pop"))
    elif t == "news":
        bx = gui_panel(520, 520, (0, 0, 0), 90)
        items.append(Item(bx, 150, 230, 0.0, "fade"))
        dyn.append(hero_dyn(sc["hero"], 340, 410, 480, 0.15, glow=acc if sc.get("glow", True) else None, glint=sc.get("glint", False)))
        if sc.get("note"):
            items.append(Item(text_img(sc["note"], MR, 26, fill=(200, 200, 210), shadow=False), 410, 770, 0.6, "fade", center=True))
        x0 = 740
        if sc.get("badge"): items.append(Item(badge(sc["badge"], acc), x0, 220, 0.1, "pop"))
        h = text_img(wrap(sc["h"], SILK, 84, 1000), SILK, 84, fill=WHITE, max_w=1020)
        items.append(Item(h, x0, 310, 0.2, "left", sfx="place"))
        body = text_img(wrap(sc["s"], MX, 46, 1000), MX, 46, fill=acc2, max_w=1020)
        items.append(Item(body, x0, 330 + h.height + 10, 0.55, "up"))
        for k, ch in enumerate(sc.get("chips", [])):
            pass
    elif t == "bullets":
        items.append(heading(sc["h"], th, col=acc))
        its = sc["items"]; n = len(its); gap = min(150, 560 // max(1, n)); y0 = 290
        times = sc.get("times") or reveal_times(n, dur)
        for i, it in enumerate(its):
            spr, txt = (it if isinstance(it, (list, tuple)) else (None, it))
            S = min(120, gap - 14)
            row = Image.new("RGBA", (1600, gap), (0, 0, 0, 0))
            if spr:
                ic = slot(S, sprite(spr[1], int(S * 0.74)) if spr[0] == "sprite" else cube(spr[1], spr[2] if len(spr) > 2 else None, int(S * 0.8)))
                row.alpha_composite(ic, (0, (gap - S) // 2))
            else:
                b = bevel_box(40, 40, fill=acc, b=5); row.alpha_composite(b, (40, gap // 2 - 20))
            ti = text_img(wrap(txt, MX, 50 if n <= 4 else 44, 1380), MX, 50 if n <= 4 else 44, max_w=1400)
            row.alpha_composite(ti, (S + 40, max(0, gap // 2 - ti.height // 2)))
            items.append(Item(row, 170, y0 + i * gap, times[i], "left", 0.45, sfx="place"))
    elif t == "stat":
        dyn.append(hero_dyn(sc["hero"], 360, 400, 500, 0.0, glow=acc, glint=sc.get("glint", False)))
        big = text_img(sc["big"], SILK, 190, fill=acc, glow=acc, glow_r=18, max_w=1080)
        items.append(Item(big, 700, 230, 0.2, "pop", 0.5, sfx="ding"))
        items.append(Item(text_img(sc["label"].upper(), SILK, 54, fill=WHITE, max_w=1080), 710, 250 + big.height, 0.5, "up"))
        items.append(Item(text_img(wrap(sc["small"], MX, 44, 1060), MX, 44, fill=acc2, max_w=1080), 710, 340 + big.height, 0.9, "up"))
    elif t == "tip":
        num = text_img(sc["n"], SILK, 230, fill=acc, glow=acc, glow_r=20, max_w=500)
        items.append(Item(num, 330 - num.width // 2, 500 - num.height // 2, 0.0, "pop", 0.5, sfx="ding"))
        if sc.get("hero"): dyn.append(hero_dyn(sc["hero"], 200, 330, 745, 0.4, glint=sc.get("glint", False)))
        items.append(Item(badge(sc.get("badge", "CONSEJO"), acc2), 640, 240, 0.15, "pop"))
        h = text_img(wrap(sc["h"].upper(), SILK, 72, 1080), SILK, 72, max_w=1100)
        items.append(Item(h, 640, 330, 0.25, "left", sfx="place"))
        items.append(Item(text_img(wrap(sc["s"], MX, 46, 1080), MX, 46, fill=acc2, max_w=1100), 645, 360 + h.height, 0.6, "up"))
    elif t == "icon":
        dyn.append(hero_dyn(sc["hero"], 260, W // 2, 300, 0.0, glow=sc.get("glowcol", acc), glint=sc.get("glint", False)))
        if sc.get("warn"):
            stripe = Image.new("RGBA", (PANEL[2] - PANEL[0] - 10, 26), (0, 0, 0, 0)); sd = ImageDraw.Draw(stripe)
            for x in range(-40, stripe.width, 56): sd.polygon([(x, 26), (x + 26, 0), (x + 54, 0), (x + 28, 26)], fill=(255, 196, 0, 255))
            sd.rectangle([0, 0, stripe.width, 26], outline=INK + (255,), width=0)
            items.append(Item(stripe, PANEL[0] + 5, PANEL[1] + 5, 0.0, "fade"))
            items.append(Item(stripe, PANEL[0] + 5, PANEL[3] - 31, 0.0, "fade"))
        h = text_img(wrap(sc["h"], SILK, 92, 1600), SILK, 92, fill=WHITE, max_w=1600, align="center")
        items.append(Item(h, W // 2, 465, 0.3, "drop", 0.6, center=True, sfx="place"))
        items.append(Item(text_img(wrap(sc["s"], MX, 46, 1500), MX, 46, fill=acc2, max_w=1500, align="center"), W // 2, 490 + h.height, 0.7, "up", center=True))
    elif t == "vs":
        items.append(Item(text_img(sc["h"], SILK, 80, fill=WHITE, max_w=1500, align="center"), W // 2, 135, 0.05, "pop", 0.4, center=True))
        cols = [(sc.get("lt", "ANTES"), sc["left"], 170, (170, 170, 176), sc.get("lhero")), (sc.get("rt", "AHORA"), sc["right"], 1010, acc, sc.get("rhero"))]
        n = max(len(sc["left"]), len(sc["right"])); times = reveal_times(n * 2, dur, 0.8)
        for side, (lab, lines, x0, col, hr) in enumerate(cols):
            items.append(Item(gui_panel(740, 600, lerp_col(col, 0.85), 150), x0, 255, 0.15 + side * 0.15, "up"))
            items.append(Item(text_img(lab, SILK, 70, fill=col, max_w=680), x0 + 370, 285, 0.25 + side * 0.2, "pop", center=True, sfx="pop"))
            if hr: dyn.append(hero_dyn(hr, 150, x0 + 370, 470, 0.35 + side * 0.2))
            for i, ln in enumerate(lines):
                items.append(Item(text_img(wrap(ln, MX, 50, 640), MX, 50, fill=WHITE, max_w=660, align="center"), x0 + 370, 590 + i * 100, times[i * 2 + side], "up", center=True))
        vsb = bevel_box(150, 150, fill=GOLD, b=8); ImageDraw.Draw(vsb).text((75, 78), "VS", font=art.font(SILK, 64), fill=INK + (255,), anchor="mm")
        items.append(Item(vsb, W // 2, 480, 0.45, "pop", 0.4, center=True, sfx="place"))
    elif t == "mob":
        bx = gui_panel(520, 560, (0, 0, 0), 90); items.append(Item(bx, 150, 210, 0.0, "fade"))
        dyn.append(hero_dyn(("sprite", sc["sprite"]), 380, 410, 470, 0.1, bob=8))
        items.append(Item(text_img(sc.get("note", "Ilustración del canal"), MR, 26, fill=(200, 200, 210), shadow=False), 410, 790, 0.5, "fade", center=True))
        items.append(Item(badge(sc.get("badge", "NUEVO MOB"), acc), 740, 210, 0.1, "pop"))
        nm = text_img(sc["name"], SILK, 110, fill=acc, glow=acc, glow_r=14, max_w=1000)
        items.append(Item(nm, 740, 290, 0.2, "drop", 0.6, sfx="place"))
        times = sc.get("times") or reveal_times(len(sc["lines"]), dur, 1.0)
        for i, ln in enumerate(sc["lines"]):
            row = Image.new("RGBA", (1050, 90), (0, 0, 0, 0)); row.alpha_composite(bevel_box(30, 30, fill=acc2, b=4), (0, 30))
            tx = text_img(wrap(ln, MX, 42, 980), MX, 42, max_w=1000); row.alpha_composite(tx, (52, max(0, 45 - tx.height // 2)))
            items.append(Item(row, 745, 300 + nm.height + 20 + i * 100, times[i], "left", sfx="pop"))
    elif t == "hotbar":
        items.append(heading(sc["h"], th, col=acc))
        its = sc["items"]; n = len(its); S = 150; gap = 12
        tw = n * S + (n - 1) * gap; x0 = W // 2 - tw // 2; y0 = 430
        times = sc.get("times") or reveal_times(n, dur, 0.6, 0.72)
        slots = []
        for i, (spec, name, desc) in enumerate(its):
            ic = sprite(spec[1], int(S * 0.72)) if spec[0] == "sprite" else cube(spec[1], spec[2] if len(spec) > 2 else None, int(S * 0.82))
            s_ = slot(S, ic); slots.append((ic, x0 + i * (S + gap)))
            items.append(Item(s_, x0 + i * (S + gap), y0, max(0.2, times[i] - 0.25), "drop", 0.5, sfx="place"))
        labels = [text_img(name, SILK, 44, fill=WHITE) for (_, name, _) in its]
        descs = [text_img(wrap(desc, MX, 46, 1500), MX, 46, fill=acc2, max_w=1500, align="center") for (_, _, desc) in its]
        def dhot(fr, lt, times=times, slots=slots, labels=labels, descs=descs):
            cur = -1
            for i, tt in enumerate(times):
                if lt >= tt + 0.15: cur = i
            if cur < 0: return
            x = slots[cur][1]
            d = ImageDraw.Draw(fr)
            d.rectangle([x - 10, y0 - 10, x + S + 9, y0 + S + 9], outline=WHITE, width=8)
            d.rectangle([x - 3, y0 - 3, x + S + 2, y0 + S + 2], outline=GOLD, width=3)
            lb = labels[cur]; tb = gui_panel(lb.width + 50, lb.height + 34, (30, 6, 60), 230)
            tb.alpha_composite(lb, (25, 17))
            tx = int(min(max(120, x + S // 2 - tb.width // 2), W - 120 - tb.width))
            fr.paste(tb, (tx, y0 - 40 - tb.height), tb)
            ds = descs[cur]; fr.paste(ds, (W // 2 - ds.width // 2, y0 + S + 60), ds)
        dyn.append(dhot)
        for tt in times: sfx.append((tt + 0.15, "click"))
    elif t == "ylevel":
        dyn += ylevel_scene(sc, th, dur, items, sfx)
    elif t == "branch":
        dyn += branch_scene(sc, th, dur, items, sfx)
    elif t == "outro":
        dyn.append(hero_dyn(("cube", "grass_top", "grass_side"), 240, 300, 520, 0.2))
        dyn.append(hero_dyn(("sprite", "diamond"), 200, W - 300, 520, 0.4, glow=(84, 232, 218)))
        items.append(Item(text_img(sc.get("h", "¿TE HA SERVIDO?"), SILK, 96, fill=WHITE, glow=(0, 0, 0), glow_r=12), W // 2, 160, 0.0, "drop", 0.6, center=True, sfx="place"))
        btn = bevel_box(820, 160, fill=(214, 32, 40), b=10)
        bd = ImageDraw.Draw(btn); bd.text((410, 84), "SUSCRÍBETE", font=art.font(SILK, 80), fill=WHITE + (255,), anchor="mm")
        items.append(Item(btn, W // 2, 390, 0.5, "pop", 0.45, center=True, sfx="ding"))
        def dbtn(fr, lt):
            if lt < 1.0: return
            ph = ((lt - 1.0) % 1.3) / 1.3; d = ImageDraw.Draw(fr); g = int(ph * 40)
            d.rectangle([W // 2 - 410 - g, 390 - g, W // 2 + 410 + g, 550 + g], outline=(255, 80, 80), width=max(1, int(8 * (1 - ph))))
        dyn.append(dbtn)
        items.append(Item(text_img(f"{CHANNEL}  ·  {HANDLE}", SILK, 50, fill=GOLD), W // 2, 640, 0.9, "up", center=True))
        items.append(Item(text_img("2 vídeos nuevos de Minecraft cada día", MX, 42, fill=WHITE), W // 2, 730, 1.2, "up", center=True))
    # toast tipo "logro" (opcional en cualquier escena)
    if sc.get("toast"):
        dyn.append(toast_dyn(sc["toast"], th, dur)); sfx.append((0.9, "ding"))
    for it in items:
        if it.sfx: sfx.append((it.t0 + (0.25 if it.kind == "drop" else 0.0), it.sfx))
    return items, dyn, sfx


def lerp_col(c, k):
    return tuple(int(v * (1 - k)) for v in c)


def toast_dyn(tt, th, dur):
    ttl, body, spr = tt
    tw, thh = 640, 130
    box = gui_panel(tw, thh, (24, 24, 30), 235)
    ic = sprite(spr, 84); box.alpha_composite(ic, (24, (thh - ic.height) // 2))
    box.alpha_composite(text_img(ttl, SILK, 28, fill=GOLD), (130, 22))
    box.alpha_composite(text_img(wrap(body, MX, 30, 480), MX, 30, fill=WHITE, max_w=490), (130, 64))
    t0, t1 = 0.9, max(1.5, dur - 0.7)
    def d(fr, lt):
        if lt < t0 or lt > t1 + 0.4: return
        p = ease((lt - t0) / 0.35) if lt < t1 else 1 - ease((lt - t1) / 0.35)
        x = int(W - 30 - tw * p - 10 * (1 - p)); x = W - int((tw + 40) * p)
        fr.paste(box, (x, 112), box)
    return d


# ---------------------------------------------------------------- diagrama de capas (Y)
def ylevel_scene(sc, th, dur, items, sfx):
    acc, acc2 = th["acc"], th["acc2"]
    top_y, bot_y = 16, -64
    X0, Y0, Y1, SW = 230, 215, 860, 200
    def ypix(y): return Y0 + (top_y - y) / (top_y - bot_y) * (Y1 - Y0)
    col = Image.new("RGBA", (SW, Y1 - Y0), (0, 0, 0, 0))
    B = 46; rnd = random.Random(4)
    for yy in range(0, Y1 - Y0, B):
        ylev = top_y - (yy + B / 2) / (Y1 - Y0) * (top_y - bot_y)
        for xx in range(0, SW, B):
            if ylev < -60: n = "bedrock"
            elif ylev < 0: n = "deep_diamond_ore" if rnd.random() < (0.05 + 0.25 * (-ylev / 64)) else "deepslate"
            else: n = "diamond_ore" if rnd.random() < 0.03 else "stone"
            col.alpha_composite(tile(n, B).convert("RGBA"), (xx, yy))
    colb = Image.new("RGBA", (SW + 12, Y1 - Y0 + 12), INK + (255,)); colb.alpha_composite(col, (6, 6))
    items.append(Item(colb, X0 - 6, Y0 - 6, 0.0, "fade", 0.5))
    # marcas
    marks = sc["marks"]  # (y, texto, color)
    times = sc.get("times") or reveal_times(len(marks), dur, 0.8, 0.7)
    for i, (yv, txt, c) in enumerate(marks):
        c = tuple(c) if c else WHITE
        row = Image.new("RGBA", (600, 70), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
        rd.rectangle([0, 33, 40, 39], fill=c + (255,))
        lab = text_img(txt, SILK, 30, fill=c, max_w=540); row.alpha_composite(lab, (52, max(0, 36 - lab.height // 2)))
        items.append(Item(row, X0 + SW + 6, int(ypix(yv)) - 36, times[i], "left", sfx="pop"))
    # barras de abundancia (ilustrativas: más diamantes cuanto más abajo)
    BX = 1060; bands = list(range(16, -64, -8))
    items.append(Item(text_img("DIAMANTES POR CAPA", SILK, 34, fill=acc), BX, Y0 - 50, 0.3, "fade"))
    bt = reveal_times(len(bands), dur, 0.5, 0.45)
    for k, yb in enumerate(bands):
        mid = yb - 4
        f = max(0.05, (16 - mid) / 80.0) ** 1.1
        if mid < -60: f *= 0.6
        wpx = int(40 + f * 640)
        bar = bevel_box(wpx, int((Y1 - Y0) / len(bands)) - 10, fill=lerp_col(acc, 0.15) if -64 <= mid <= -50 else (90, 110, 120), b=5)
        items.append(Item(bar, BX, int(ypix(yb)) + 5, bt[k], "left", 0.4))
    items.append(Item(text_img("Gráfico ilustrativo", MR, 24, fill=(190, 190, 200), shadow=False), BX, Y1 + 8, 1.0, "fade"))
    if sc.get("h"):
        items.append(Item(text_img(sc["h"], SILK, 60, fill=acc), X0 - 80, 125, 0.05, "left"))
    # marcador que baja hasta la capa objetivo
    target = sc.get("target", -59); tm = sc.get("target_t", dur * 0.35)
    arrow = sprite("pick_diamond", 90)
    def dmark(fr, lt):
        p = ease((lt - 0.6) / max(0.5, tm - 0.6))
        y = ypix(top_y) + (ypix(target) - ypix(top_y)) * p
        fr.paste(arrow, (X0 - 105, int(y - 45)), arrow)
        if lt > tm:
            ph = ((lt - tm) % 1.2) / 1.2; d = ImageDraw.Draw(fr); yy = int(ypix(target))
            d.rectangle([X0 - 8, yy - 14, BX + 700, yy + 14], outline=GOLD, width=max(2, int(7 * (1 - ph) + 2)))
    sfx.append((tm, "ding"))
    return [dmark]


# ---------------------------------------------------------------- minería en ramas (vista cenital)
def branch_scene(sc, th, dur, items, sfx):
    acc, acc2 = th["acc"], th["acc2"]
    C, R, T = 21, 11, 52
    X0, Y0 = 150, 300
    rnd = random.Random(11)
    branch_cols = [2, 5, 8, 11, 14, 17]
    seq = []
    for c in range(C - 1):
        seq.append([(c, 5)])
        if c in branch_cols:
            for k in range(1, 6): seq.append([(c, 5 - k), (c, 5 + k)])
    path = {p for step in seq for p in step}
    base = Image.new("RGBA", (C * T + 12, R * T + 12), INK + (255,))
    ores = set()
    for r in range(R):
        for c in range(C):
            n = "deepslate"
            if (c, r) not in path and rnd.random() < 0.045: n = "deep_diamond_ore"; ores.add((c, r))
            base.alpha_composite(tile(n, T).convert("RGBA"), (6 + c * T, 6 + r * T))
    floor = Image.new("RGBA", (T, T), (18, 16, 22, 255)); fd = ImageDraw.Draw(floor); fd.rectangle([0, 0, T - 1, T - 1], outline=(40, 36, 44, 255), width=2)
    torch = sprite("torch", T - 10)
    carved = set(); state = {"n": 0, "img": base.copy()}
    glow = Image.new("RGBA", (T, T), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.rectangle([0, 0, T - 1, T - 1], outline=(110, 255, 240, 255), width=5)
    p_end = sc.get("end_frac", 0.62)
    def dbranch(fr, lt):
        p = clamp((lt - 0.6) / max(1.0, dur * p_end))
        n = int(p * len(seq))
        while state["n"] < n:
            for (c, r) in seq[state["n"]]:
                carved.add((c, r)); state["img"].alpha_composite(floor, (6 + c * T, 6 + r * T))
                if (c, r) == (c, 5) and c % 4 == 1: state["img"].alpha_composite(torch, (6 + c * T + 5, 6 + r * T + 5))
                for (dc, dr) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (c + dc, r + dr) in ores: state["img"].alpha_composite(glow, (6 + (c + dc) * T, 6 + (r + dr) * T))
            state["n"] += 1
        fr.paste(state["img"], (X0, Y0), state["img"])
        if n < len(seq) and n > 0:
            c, r = seq[min(n, len(seq) - 1)][0]
            pk = sprite("pick_iron", T + 10); fr.paste(pk, (X0 + 6 + c * T - 5, Y0 + 6 + r * T - 5), pk)
    items.append(Item(base, X0, Y0, 0.0, "fade", 0.4))
    # cota "2 bloques" entre la rama 1 y la 2
    lab = text_img("2 BLOQUES", SILK, 30, fill=GOLD)
    cx = X0 + 6 + 3 * T; cw = 2 * T
    dim = Image.new("RGBA", (max(cw, lab.width) + 20, 90), (0, 0, 0, 0)); dd = ImageDraw.Draw(dim)
    ox = (dim.width - cw) // 2
    dd.line([(ox, 70), (ox + cw, 70)], fill=GOLD + (255,), width=5); dd.line([(ox, 58), (ox, 82)], fill=GOLD + (255,), width=5); dd.line([(ox + cw, 58), (ox + cw, 82)], fill=GOLD + (255,), width=5)
    dim.alpha_composite(lab, ((dim.width - lab.width) // 2, 10))
    tdim = 0.6 + max(1.0, dur * p_end) * 0.35
    items.append(Item(dim, cx - ox, Y0 - 92, tdim, "pop", sfx="pop"))
    items.append(Item(text_img(sc["h"], SILK, 64, fill=acc), X0, 125, 0.05, "left"))
    tx = X0 + C * T + 60
    lines = sc.get("lines", [])
    lt_ = sc.get("times") or reveal_times(len(lines), dur, 1.0, 0.7)
    for i, ln in enumerate(lines):
        im = text_img(wrap(ln, MX, 40, 480), MX, 40, fill=acc2 if i % 2 == 0 else WHITE, max_w=500)
        items.append(Item(im, tx, 330 + i * 160, lt_[i], "left", sfx="pop"))
    return [dbranch]


# ================================================================ subtítulos
def chunks(say, maxc=42):
    words = say.split(); out = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if len(t) > maxc and cur:
            out.append(cur); cur = w_
        else:
            cur = t
        if cur.endswith((".", "?", "!", ":")) and len(cur) > 18:
            out.append(cur); cur = ""
    if cur: out.append(cur)
    return out


def caption_img(txt):
    ti = text_img(txt, MX, 46, fill=WHITE, shadow=False, stroke=5, stroke_fill=(0, 0, 0), max_w=1700)
    bx = Image.new("RGBA", (ti.width + 50, ti.height + 24), (0, 0, 0, 150)); bx.alpha_composite(ti, (25, 12))
    return bx


def srt_time(s):
    ms = int(round(s * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); se, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{se:02},{ms:03}"


# ================================================================ vídeo
def render(v):
    slug = v["slug"]; th = THEMES[v["theme"]]
    for p in (os.path.join(BUILD, "tts", slug), OUT, SUBS): os.makedirs(p, exist_ok=True)
    # 1) voz
    segs = []; t = 0.5; voice = [np.zeros(int(0.5 * audio.SR), np.float32)]
    for i, sc in enumerate(v["scenes"]):
        a = audio.speak(sc["say"], os.path.join(BUILD, "tts", slug, f"{i:02}"))
        d = PAD_BEFORE + len(a) / audio.SR + PAD_AFTER + (1.6 if sc["t"] == "outro" else 0) + sc.get("extra", 0)
        segs.append((t, d, PAD_BEFORE, len(a) / audio.SR))
        voice += [np.zeros(int(PAD_BEFORE * audio.SR), np.float32), a, np.zeros(int(round(d * audio.SR)) - int(PAD_BEFORE * audio.SR) - len(a), np.float32)]
        t += d
    total = t + 0.3
    vtrack = np.concatenate(voice); vtrack = np.pad(vtrack, (0, max(0, int(total * audio.SR) - len(vtrack))))
    vwav = os.path.join(BUILD, f"{slug}-voz.wav"); sf.write(vwav, vtrack, audio.SR)
    # 2) escenas (se construyen una vez para conocer los efectos de sonido)
    events = []
    for i, (sc, (s0, d, _, _)) in enumerate(zip(v["scenes"], segs)):
        _, _, ev = build_scene(sc, th, d, v)
        events += [(s0 + tt, nm) for (tt, nm) in ev]
        if i > 0: events.append((s0 - 0.05, "break"))
    # 3) música y efectos
    mus = audio.music(th["music"], total, seed=zlib.crc32(slug.encode()) % 997)
    mwav = os.path.join(BUILD, f"{slug}-musica.wav"); sf.write(mwav, mus, audio.MSR)
    fx = np.zeros(int(total * audio.MSR) + audio.MSR, np.float32); cache = {}
    for (tt, nm) in events:
        if nm not in cache: cache[nm] = audio.sfx(nm)
        x = cache[nm]; k = int(max(0, tt) * audio.MSR); e = min(len(fx), k + len(x)); fx[k:e] += x[:e - k]
    fwav = os.path.join(BUILD, f"{slug}-sfx.wav"); sf.write(fwav, fx[:int(total * audio.MSR)], audio.MSR)
    # 4) subtítulos y capítulos
    caps = []; srt = []
    for sc, (s0, d, pb, alen) in zip(v["scenes"], segs):
        cs = chunks(sc["say"]); tot = sum(len(c) for c in cs); cur = s0 + pb
        for c in cs:
            cd = alen * len(c) / tot; caps.append((cur, cur + cd, c)); cur += cd
    for k, (a, b, c) in enumerate(caps):
        srt.append(f"{k + 1}\n{srt_time(a)} --> {srt_time(b)}\n{c}\n")
    open(os.path.join(SUBS, f"{slug}.srt"), "w", encoding="utf-8").write("\n".join(srt))
    chapters = [("0:00", "Intro")]
    for sc, (s0, *_) in zip(v["scenes"], segs):
        if sc.get("chapter"): chapters.append((f"{int(s0 // 60)}:{int(s0 % 60):02}", sc["chapter"]))
    json.dump(dict(duration=total, chapters=chapters), open(os.path.join(BUILD, f"{slug}-meta.json"), "w"), ensure_ascii=False)
    # 5) fotogramas
    bg = art.Background(v["theme"], seed=zlib.crc32(slug.encode()) % 1000)
    panel = gui_panel(PANEL[2] - PANEL[0], PANEL[3] - PANEL[1], th["panel"], 178)
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(shade)
    for y in range(H):
        sd.line([(0, y), (W, y)], fill=(0, 0, 0, int(70 + 60 * abs(y - H / 2) / (H / 2))))
    wm_c = cube("grass_top", "grass_side", 58)
    wm = Image.new("RGBA", (520, 70), (0, 0, 0, 0)); wm.alpha_composite(wm_c, (0, 4))
    wm.alpha_composite(text_img(CHANNEL, SILK, 32, fill=WHITE), (68, 16))
    xpbar = Image.new("RGBA", (W, 16), (0, 0, 0, 0))
    out = os.path.join(OUT, f"{slug}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", vwav, "-i", mwav, "-i", fwav, "-filter_complex",
           "[1:a]aresample=48000,asplit=2[v][sc];[2:a]aresample=48000,volume=0.50[m];[3:a]aresample=48000,volume=0.9[fx];"
           "[m][sc]sidechaincompress=threshold=0.02:ratio=9:attack=15:release=380[md];"
           "[v][md][fx]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    nframes = int(total * FPS); si = 0; ci = 0; built = [None] * len(segs)
    prev_content = None; last_content = None; tiles = None; cap_cache = {}
    TS = 120
    for fi in range(nframes):
        tt = fi / FPS
        new_scene = False
        while si + 1 < len(segs) and tt >= segs[si + 1][0]:
            si += 1; new_scene = True
        if new_scene and last_content is not None:
            prev_content = last_content
            rr = random.Random(si)
            tiles = [(c, r, prev_content.crop((c * TS, r * TS, c * TS + TS, r * TS + TS)).convert("RGB"), 0.30 * (c + r * 1.2) / (16 + 9 * 1.2) + rr.random() * 0.06)
                     for r in range(9) for c in range(16)]
        if built[si] is None:
            built[si] = build_scene(v["scenes"][si], th, segs[si][1], v)
            if si > 0: built[si - 1] = None
        items, dyn, _ = built[si]; lt = tt - segs[si][0]; sc = v["scenes"][si]
        fr = bg.frame(tt).convert("RGBA")
        if sc["t"] in ("title", "outro"):
            fr.alpha_composite(shade)
        else:
            fr.alpha_composite(panel, PANEL[:2])
        for it in items: it.draw(fr, lt)
        for f in dyn: f(fr, lt)
        last_content = fr.copy()
        # transición: la escena anterior se rompe en bloques que caen
        if si > 0 and tiles is not None and lt < 0.62:
            fr = fr.copy()
            for (c, r, im, dl) in tiles:
                if lt < dl:
                    fr.paste(im, (c * TS, r * TS))
                elif lt < dl + 0.24:
                    p = (lt - dl) / 0.24; s = int(TS * (1 - 0.45 * p))
                    if s > 4:
                        sm = im.resize((s, s), Image.NEAREST)
                        sm = Image.eval(sm, lambda v, p=p: int(v * (1 - 0.6 * p)))
                        fr.paste(sm, (c * TS + (TS - s) // 2, r * TS + int(p * p * 260)))
        fr.alpha_composite(wm, (34, 22))
        d = ImageDraw.Draw(fr)
        # barra de experiencia = progreso
        prog = tt / total
        d.rectangle([0, H - 16, W, H], fill=(20, 20, 20, 255))
        d.rectangle([0, H - 13, int(W * prog), H - 3], fill=(128, 255, 32, 255))
        d.rectangle([0, H - 13, int(W * prog), H - 10], fill=(200, 255, 140, 255))
        for k in range(1, 18): x = int(W * k / 18); d.rectangle([x - 2, H - 13, x + 1, H - 3], fill=(20, 20, 20, 255))
        while ci < len(caps) and tt > caps[ci][1]: ci += 1
        if ci < len(caps) and caps[ci][0] <= tt:
            c = caps[ci][2]
            if c not in cap_cache: cap_cache = {c: caption_img(c)}
            im = cap_cache[c]; fr.alpha_composite(im, (W // 2 - im.width // 2, 965 - im.height // 2))
        ff.stdin.write(fr.convert("RGB").tobytes())
    ff.stdin.close(); ff.wait()
    print(f"OK {out} ({total:.1f}s)", flush=True)
    return total


if __name__ == "__main__":
    want = sys.argv[1:]
    for v in VIDEOS:
        if (not want and not os.path.exists(os.path.join(OUT, v["slug"] + ".mp4"))) or any(v["slug"].startswith(w) for w in want):
            render(v)
