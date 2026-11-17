# -*- coding: utf-8 -*-
"""Shorts verticales (1080x1920, menos de 60 s).  Uso:  python3 render_short.py [prefijo ...]

Diseño pensado para la interfaz de YouTube Shorts / TikTok / Reels:
  - arriba (y < 230) y abajo (y > 1500) la app pone sus textos: ahí no va nada importante;
  - a la derecha (x > 940, y 900-1650) están los botones: el contenido queda centrado-izquierda;
  - subtítulos grandes de 2-3 palabras en el centro (y ~ 1265), que es donde se lee un Short.
"""
import math, os, random, subprocess, sys, json, zlib
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw

import art
from art import (THEMES, GOLD, WHITE, INK, text_img, wrap, add_glow, bevel_box, label_box, gui_panel, slot, sprite,
                 cube, tile, SILK, MB, MX, MR)
import audio
from render import Item, clamp, ease, back, reveal_times, hero_dyn, badge, srt_time, lerp_col
from content import SHORTS, CHANNEL, HANDLE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build"); OUT = os.path.join(ROOT, "shorts"); SUBS = os.path.join(OUT, "subtitulos")
COV = os.path.join(OUT, "portadas")
W, H = 1080, 1920
FPS = 30
PAD_BEFORE, PAD_AFTER = 0.08, 0.22
SPEED = 1.12
PANEL = (50, 250, 1030, 1110)
CX = 520            # centro horizontal del contenido (un poco a la izquierda por los botones de la app)
CAP_Y = 1270


def stripes(w):
    st = Image.new("RGBA", (w, 26), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    for x in range(-40, w, 56): sd.polygon([(x, 26), (x + 26, 0), (x + 54, 0), (x + 28, 26)], fill=(255, 196, 0, 255))
    return st


def build_scene(sc, th, dur):
    t = sc["t"]; acc, acc2 = th["acc"], th["acc2"]; items = []; dyn = []; sfx = []
    glint = sc.get("glint", False)
    if sc.get("warn"):
        st = stripes(PANEL[2] - PANEL[0] - 10)
        items += [Item(st, PANEL[0] + 5, PANEL[1] + 5, 0.0, "fade"), Item(st, PANEL[0] + 5, PANEL[3] - 31, 0.0, "fade")]
    if t == "title":
        if sc.get("badge"): items.append(Item(badge(sc["badge"], acc), CX, 300, 0.0, "pop", center=True))
        dyn.append(hero_dyn(sc["hero"], 430, CX, 640, 0.0, glow=acc, glint=glint))
        for fs in (120, 104, 92, 80):
            big = text_img(wrap(sc["h"], SILK, fs, 900), SILK, fs, fill=WHITE, max_w=940, align="center", glow=(0, 0, 0), glow_r=14)
            if big.height <= 300: break
        items.append(Item(big, CX, 900, 0.15, "drop", 0.6, center=True, sfx="place"))
        if sc.get("splash"):
            sp = text_img(sc["splash"], SILK, 44, fill=GOLD, shadow_col=(62, 52, 0)).rotate(14, expand=True, resample=Image.BICUBIC)
            sps = {k: sp.resize((int(sp.width * (0.9 + k * 0.015)), int(sp.height * (0.9 + k * 0.015))), Image.BILINEAR) for k in range(12)}
            sx, sy = min(W - 120 - sp.width // 2, CX + big.width // 2 - 40), 880
            def dsplash(fr, lt, sps=sps, sx=sx, sy=sy):
                if lt < 0.8: return
                im = sps[int((math.sin((lt - 0.8) * 7) * 0.5 + 0.5) * 11.99)]; fr.paste(im, (sx - im.width // 2, sy - im.height // 2), im)
            dyn.append(dsplash); sfx.append((0.8, "pop"))
    elif t in ("card", "icon", "news"):
        y = 290
        if sc.get("badge"):
            b = badge(sc["badge"], acc); items.append(Item(b, CX, y, 0.0, "pop", center=True)); y += b.height + 10
        dyn.append(hero_dyn(sc["hero"], 360, CX, y + 210, 0.05, glow=sc.get("glowcol", acc) if sc.get("glow", True) else None, glint=glint))
        y += 440
        h = text_img(wrap(sc["h"], SILK, 76, 900), SILK, 76, fill=WHITE, max_w=920, align="center")
        items.append(Item(h, CX, y, 0.2, "drop", 0.55, center=True, sfx="place")); y += h.height + 16
        if sc.get("s"):
            items.append(Item(text_img(wrap(sc["s"], MX, 42, 880), MX, 42, fill=acc2, max_w=900, align="center"), CX, y, 0.5, "up", center=True))
    elif t == "tip":
        num = text_img(sc["n"], SILK, 250, fill=acc, glow=acc, glow_r=20, max_w=420)
        items.append(Item(num, 300 - num.width // 2, 470 - num.height // 2, 0.0, "pop", 0.45, sfx="ding"))
        if sc.get("hero"): dyn.append(hero_dyn(sc["hero"], 300, 760, 470, 0.15, glint=glint))
        y = 700
        if sc.get("badge"):
            b = badge(sc["badge"], acc2); items.append(Item(b, CX, y, 0.1, "pop", center=True)); y += b.height + 14
        h = text_img(wrap(sc["h"].upper(), SILK, 72, 900), SILK, 72, max_w=920, align="center")
        items.append(Item(h, CX, y, 0.2, "drop", 0.55, center=True, sfx="place")); y += h.height + 14
        if sc.get("s"):
            items.append(Item(text_img(wrap(sc["s"], MX, 40, 880), MX, 40, fill=acc2, max_w=900, align="center"), CX, y, 0.5, "up", center=True))
    elif t == "stat":
        dyn.append(hero_dyn(sc["hero"], 300, CX, 470, 0.0, glow=acc, glint=glint))
        big = text_img(sc["big"], SILK, 190, fill=acc, glow=acc, glow_r=18, max_w=900)
        items.append(Item(big, CX, 650, 0.2, "pop", 0.5, center=True, sfx="ding"))
        items.append(Item(text_img(sc["label"].upper(), SILK, 56, fill=WHITE, max_w=900, align="center"), CX, 660 + big.height, 0.45, "up", center=True))
        if sc.get("small"):
            items.append(Item(text_img(wrap(sc["small"], MX, 40, 880), MX, 40, fill=acc2, max_w=900, align="center"), CX, 760 + big.height, 0.8, "up", center=True))
    elif t == "bullets":
        items.append(Item(text_img(sc["h"], SILK, 70, fill=acc, max_w=900, align="center"), CX, 300, 0.0, "drop", 0.5, center=True))
        its = sc["items"]; n = len(its); gap = min(170, 640 // max(1, n)); y0 = 440
        times = sc.get("times") or reveal_times(n, dur, 0.4, 0.7)
        for i, it in enumerate(its):
            spr, txt = (it if isinstance(it, (list, tuple)) else (None, it))
            S = min(130, gap - 16)
            row = Image.new("RGBA", (920, gap), (0, 0, 0, 0))
            if spr:
                ic = slot(S, sprite(spr[1], int(S * 0.74)) if spr[0] == "sprite" else cube(spr[1], spr[2] if len(spr) > 2 else None, int(S * 0.8)))
                row.alpha_composite(ic, (0, (gap - S) // 2))
            else:
                row.alpha_composite(bevel_box(40, 40, fill=acc, b=5), (30, gap // 2 - 20)); S = 100
            ti = text_img(wrap(txt, MX, 44, 740), MX, 44, max_w=750)
            row.alpha_composite(ti, (S + 28, max(0, gap // 2 - ti.height // 2)))
            items.append(Item(row, 90, y0 + i * gap, times[i], "left", 0.4, sfx="place"))
    elif t == "vs":
        items.append(Item(text_img(sc["h"], SILK, 70, fill=WHITE, max_w=920, align="center"), CX, 290, 0.0, "pop", 0.4, center=True))
        rows = [(sc.get("lt", "ANTES"), sc["left"], 390, (170, 170, 176), sc.get("lhero")), (sc.get("rt", "AHORA"), sc["right"], 760, acc, sc.get("rhero"))]
        for k, (lab, lines, y0, col, hr) in enumerate(rows):
            items.append(Item(gui_panel(900, 320, lerp_col(col, 0.85), 150), 70, y0, 0.1 + k * 0.5, "up"))
            items.append(Item(text_img(lab, SILK, 64, fill=col, max_w=560), 120, y0 + 40, 0.2 + k * 0.5, "left", sfx="pop"))
            if hr: dyn.append(hero_dyn(hr, 190, 820, y0 + 160, 0.3 + k * 0.5, bob=8))
            ln = text_img(wrap("\n".join(lines), MX, 48, 560), MX, 48, fill=WHITE, max_w=580)
            items.append(Item(ln, 124, y0 + 130, 0.45 + k * 0.5, "up"))
        vsb = bevel_box(130, 130, fill=GOLD, b=8); ImageDraw.Draw(vsb).text((65, 68), "VS", font=art.font(SILK, 56), fill=INK + (255,), anchor="mm")
        items.append(Item(vsb, CX, 690, 0.4, "pop", 0.4, center=True, sfx="place"))
    elif t == "mob":
        items.append(Item(badge(sc.get("badge", "NUEVO MOB"), acc), CX, 290, 0.0, "pop", center=True))
        dyn.append(hero_dyn(("sprite", sc["sprite"]), 400, CX, 600, 0.05, bob=8))
        items.append(Item(text_img(sc.get("note", "Ilustración del canal"), MR, 26, fill=(210, 210, 220), shadow=False), CX, 810, 0.4, "fade", center=True))
        nm = text_img(sc["name"], SILK, 100, fill=acc, glow=acc, glow_r=14, max_w=900)
        items.append(Item(nm, CX, 850, 0.2, "drop", 0.55, center=True, sfx="place"))
        if sc.get("s"):
            items.append(Item(text_img(wrap(sc["s"], MX, 40, 880), MX, 40, fill=acc2, max_w=900, align="center"), CX, 870 + nm.height, 0.6, "up", center=True))
    elif t == "hotbar":
        items.append(Item(text_img(sc["h"], SILK, 70, fill=acc, max_w=900, align="center"), CX, 300, 0.0, "drop", 0.5, center=True))
        its = sc["items"]; n = len(its); S = 160 if n <= 5 else 130; gap = 12
        tw = n * S + (n - 1) * gap; x0 = CX - tw // 2; y0 = 600
        times = sc.get("times") or reveal_times(n, dur, 0.5, 0.75)
        sl = []
        for i, (spec, name, desc) in enumerate(its):
            ic = sprite(spec[1], int(S * 0.72)) if spec[0] == "sprite" else cube(spec[1], spec[2] if len(spec) > 2 else None, int(S * 0.82))
            sl.append(x0 + i * (S + gap)); items.append(Item(slot(S, ic), x0 + i * (S + gap), y0, max(0.15, times[i] - 0.25), "drop", 0.45, sfx="place"))
        labels = [text_img(nm, SILK, 46, fill=WHITE) for (_, nm, _) in its]
        descs = [text_img(wrap(d_, MX, 44, 880), MX, 44, fill=acc2, max_w=900, align="center") for (_, _, d_) in its]
        def dhot(fr, lt):
            cur = max([i for i, tt in enumerate(times) if lt >= tt + 0.1] or [-1])
            if cur < 0: return
            x = sl[cur]; d = ImageDraw.Draw(fr)
            d.rectangle([x - 10, y0 - 10, x + S + 9, y0 + S + 9], outline=WHITE, width=8); d.rectangle([x - 3, y0 - 3, x + S + 2, y0 + S + 2], outline=GOLD, width=3)
            lb = labels[cur]; tb = gui_panel(lb.width + 50, lb.height + 34, (30, 6, 60), 230); tb.alpha_composite(lb, (25, 17))
            tx = int(min(max(60, x + S // 2 - tb.width // 2), 1000 - tb.width)); fr.paste(tb, (tx, y0 - 30 - tb.height), tb)
            ds = descs[cur]; fr.paste(ds, (CX - ds.width // 2, y0 + S + 50), ds)
        dyn.append(dhot); sfx += [(tt + 0.1, "click") for tt in times]
    elif t == "ylevel":
        dyn += ylevel(sc, th, dur, items, sfx)
    elif t == "branch":
        dyn += branch(sc, th, dur, items, sfx)
    return items, dyn, sfx


def ylevel(sc, th, dur, items, sfx):
    acc = th["acc"]
    top_y, bot_y = 16, -64; X0, Y0, Y1, SW_ = 140, 300, 1070, 210
    def ypix(y): return Y0 + (top_y - y) / (top_y - bot_y) * (Y1 - Y0)
    col = Image.new("RGBA", (SW_, Y1 - Y0), (0, 0, 0, 0)); B = 42; rnd = random.Random(4)
    for yy in range(0, Y1 - Y0, B):
        lv = top_y - (yy + B / 2) / (Y1 - Y0) * (top_y - bot_y)
        for xx in range(0, SW_, B):
            n = "bedrock" if lv < -60 else (("deep_diamond_ore" if rnd.random() < 0.05 + 0.25 * (-lv / 64) else "deepslate") if lv < 0 else ("diamond_ore" if rnd.random() < 0.03 else "stone"))
            col.alpha_composite(tile(n, B).convert("RGBA"), (xx, yy))
    cb = Image.new("RGBA", (SW_ + 12, Y1 - Y0 + 12), INK + (255,)); cb.alpha_composite(col, (6, 6))
    items.append(Item(cb, X0 - 6, Y0 - 6, 0.0, "fade", 0.4))
    marks = sc["marks"]; times = sc.get("times") or reveal_times(len(marks), dur, 0.5, 0.65)
    for i, (yv, txt, c) in enumerate(marks):
        c = tuple(c) if c else WHITE
        row = Image.new("RGBA", (680, 80), (0, 0, 0, 0)); ImageDraw.Draw(row).rectangle([0, 37, 40, 43], fill=c + (255,))
        lab = text_img(txt, SILK, 40, fill=c, max_w=620); row.alpha_composite(lab, (54, max(0, 40 - lab.height // 2)))
        items.append(Item(row, X0 + SW_ + 8, int(ypix(yv)) - 40, times[i], "left", sfx="pop"))
    target = sc.get("target", -59); tm = sc.get("target_t", dur * 0.45); pick = sprite("pick_diamond", 90)
    def d(fr, lt):
        p = ease((lt - 0.4) / max(0.5, tm - 0.4)); y = ypix(top_y) + (ypix(target) - ypix(top_y)) * p
        fr.paste(pick, (X0 - 100, int(y - 45)), pick)
        if lt > tm:
            ph = ((lt - tm) % 1.2) / 1.2; yy = int(ypix(target))
            ImageDraw.Draw(fr).rectangle([X0 - 8, yy - 16, 1010, yy + 16], outline=GOLD, width=max(2, int(7 * (1 - ph) + 2)))
    sfx.append((tm, "ding"))
    return [d]


def branch(sc, th, dur, items, sfx):
    acc = th["acc"]; C, R, T = 15, 11, 58; X0, Y0 = 105, 420
    bcols = [2, 5, 8, 11]
    seq = []
    for c in range(C - 1):
        seq.append([(c, 5)])
        if c in bcols: seq += [[(c, 5 - k), (c, 5 + k)] for k in range(1, 6)]
    path = {p for s_ in seq for p in s_}; rnd = random.Random(11)
    base = Image.new("RGBA", (C * T + 12, R * T + 12), INK + (255,)); ores = set()
    for r in range(R):
        for c in range(C):
            n = "deepslate"
            if (c, r) not in path and rnd.random() < 0.05: n = "deep_diamond_ore"; ores.add((c, r))
            base.alpha_composite(tile(n, T).convert("RGBA"), (6 + c * T, 6 + r * T))
    floor = Image.new("RGBA", (T, T), (18, 16, 22, 255)); ImageDraw.Draw(floor).rectangle([0, 0, T - 1, T - 1], outline=(40, 36, 44, 255), width=2)
    torch = sprite("torch", T - 10); glow = Image.new("RGBA", (T, T), (0, 0, 0, 0)); ImageDraw.Draw(glow).rectangle([0, 0, T - 1, T - 1], outline=(110, 255, 240, 255), width=5)
    st = {"n": 0, "img": base.copy()}; pend = sc.get("end_frac", 0.7)
    def d(fr, lt):
        n = int(clamp((lt - 0.4) / max(1.0, dur * pend)) * len(seq))
        while st["n"] < n:
            for (c, r) in seq[st["n"]]:
                st["img"].alpha_composite(floor, (6 + c * T, 6 + r * T))
                if r == 5 and c % 4 == 1: st["img"].alpha_composite(torch, (6 + c * T + 5, 6 + r * T + 5))
                for (dc, dr) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (c + dc, r + dr) in ores: st["img"].alpha_composite(glow, (6 + (c + dc) * T, 6 + (r + dr) * T))
            st["n"] += 1
        fr.paste(st["img"], (X0, Y0), st["img"])
        if 0 < n < len(seq):
            c, r = seq[n][0]; pk = sprite("pick_iron", T + 10); fr.paste(pk, (X0 + 1 + c * T, Y0 + 1 + r * T), pk)
    items.append(Item(base, X0, Y0, 0.0, "fade", 0.4))
    items.append(Item(text_img(sc["h"], SILK, 64, fill=acc, max_w=920, align="center"), CX, 285, 0.0, "drop", 0.5, center=True))
    lab = text_img("2 BLOQUES", SILK, 30, fill=GOLD); cw = 2 * T
    dim = Image.new("RGBA", (max(cw, lab.width) + 20, 70), (0, 0, 0, 0)); dd = ImageDraw.Draw(dim); ox = (dim.width - cw) // 2
    for seg in ([(ox, 56), (ox + cw, 56)], [(ox, 46), (ox, 66)], [(ox + cw, 46), (ox + cw, 66)]): dd.line(seg, fill=GOLD + (255,), width=5)
    dim.alpha_composite(lab, ((dim.width - lab.width) // 2, 4))
    items.append(Item(dim, X0 + 6 + 3 * T - ox, Y0 - 72, 0.4 + max(1.0, dur * pend) * 0.4, "pop", sfx="pop"))
    return [d]


# ---------------------------------------------------------------- subtítulos estilo Short
def chunks(say, maxc=17):
    out = []; cur = ""
    for w_ in say.split():
        t = (cur + " " + w_).strip()
        if len(t) > maxc and cur: out.append(cur); cur = w_
        else: cur = t
        if cur.endswith((".", "?", "!", ":", ",")) and len(cur) > 8: out.append(cur); cur = ""
    if cur: out.append(cur)
    return out


def caption_img(txt):
    hot = any(ch.isdigit() for ch in txt)
    clean = txt.rstrip(",.")
    return text_img(clean.upper(), MB, 74, fill=GOLD if hot else WHITE, shadow=False, stroke=9, stroke_fill=(0, 0, 0), max_w=940, align="center")


# ---------------------------------------------------------------- render
def render(v):
    slug = v["slug"]; th = THEMES[v["theme"]]
    for p in (os.path.join(BUILD, "tts-short", slug), OUT, SUBS, COV): os.makedirs(p, exist_ok=True)
    segs = []; t = 0.15; voice = [np.zeros(int(0.15 * audio.SR), np.float32)]
    for i, sc in enumerate(v["scenes"]):
        a = audio.speak(sc["say"], os.path.join(BUILD, "tts-short", slug, f"{i:02}"), speed=SPEED)
        last = i == len(v["scenes"]) - 1
        d = PAD_BEFORE + len(a) / audio.SR + PAD_AFTER + (1.2 if last else 0)
        segs.append((t, d, PAD_BEFORE, len(a) / audio.SR))
        voice += [np.zeros(int(PAD_BEFORE * audio.SR), np.float32), a, np.zeros(int(round(d * audio.SR)) - int(PAD_BEFORE * audio.SR) - len(a), np.float32)]
        t += d
    total = t + 0.1
    vtrack = np.concatenate(voice); vtrack = np.pad(vtrack, (0, max(0, int(total * audio.SR) - len(vtrack))))
    vwav = os.path.join(BUILD, f"short-{slug}-voz.wav"); sf.write(vwav, vtrack, audio.SR)
    events = []
    for i, (sc, (s0, d, _, _)) in enumerate(zip(v["scenes"], segs)):
        _, _, ev = build_scene(sc, th, d); events += [(s0 + tt, nm) for (tt, nm) in ev]
        if i > 0: events.append((s0 - 0.05, "break"))
    mus = audio.music(th["music"], total, seed=zlib.crc32(slug.encode()) % 997)
    mwav = os.path.join(BUILD, f"short-{slug}-musica.wav"); sf.write(mwav, mus, audio.MSR)
    fx = np.zeros(int(total * audio.MSR) + audio.MSR, np.float32); cache = {}
    for (tt, nm) in events:
        if nm not in cache: cache[nm] = audio.sfx(nm)
        x = cache[nm]; k = int(max(0, tt) * audio.MSR); e = min(len(fx), k + len(x)); fx[k:e] += x[:e - k]
    fwav = os.path.join(BUILD, f"short-{slug}-sfx.wav"); sf.write(fwav, fx[:int(total * audio.MSR)], audio.MSR)
    caps = []
    for sc, (s0, d, pb, alen) in zip(v["scenes"], segs):
        cs = chunks(sc["say"]); tot = sum(len(c) + 2 for c in cs); cur = s0 + pb
        for c in cs:
            cd = alen * (len(c) + 2) / tot; caps.append((cur, cur + cd, c)); cur += cd
    open(os.path.join(SUBS, f"{slug}.srt"), "w", encoding="utf-8").write(
        "\n".join(f"{k + 1}\n{srt_time(a)} --> {srt_time(b)}\n{c}\n" for k, (a, b, c) in enumerate(caps)))
    json.dump(dict(duration=total), open(os.path.join(BUILD, f"short-{slug}-meta.json"), "w"))
    bg = art.Background(v["theme"], seed=zlib.crc32(slug.encode()) % 1000, w=W, h=H)
    panel = gui_panel(PANEL[2] - PANEL[0], PANEL[3] - PANEL[1], th["panel"], 182)
    wm = Image.new("RGBA", (520, 70), (0, 0, 0, 0)); wm.alpha_composite(cube("grass_top", "grass_side", 54), (0, 6))
    wm.alpha_composite(text_img(CHANNEL, SILK, 30, fill=WHITE), (64, 18))
    follow = bevel_box(620, 120, fill=(214, 32, 40), b=9); fd = ImageDraw.Draw(follow)
    fd.text((310, 62), "¡SÍGUEME!", font=art.font(SILK, 64), fill=WHITE + (255,), anchor="mm")
    out = os.path.join(OUT, f"{slug}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", vwav, "-i", mwav, "-i", fwav, "-filter_complex",
           "[1:a]aresample=48000,asplit=2[v][sc];[2:a]aresample=48000,volume=0.55[m];[3:a]aresample=48000,volume=0.9[fx];"
           "[m][sc]sidechaincompress=threshold=0.02:ratio=9:attack=15:release=300[md];"
           "[v][md][fx]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    nframes = int(total * FPS); si = 0; ci = 0; built = [None] * len(segs); last_content = None; tiles = None; capc = {}
    TS = 120
    for fi in range(nframes):
        tt = fi / FPS; new = False
        while si + 1 < len(segs) and tt >= segs[si + 1][0]: si += 1; new = True
        if new and last_content is not None:
            rr = random.Random(si)
            tiles = [(c, r, last_content.crop((c * TS, r * TS, c * TS + TS, r * TS + TS)).convert("RGB"), 0.26 * (c * 1.2 + r) / (9 * 1.2 + 16) + rr.random() * 0.05)
                     for r in range(16) for c in range(9)]
        if built[si] is None:
            built[si] = build_scene(v["scenes"][si], th, segs[si][1])
            if si > 0: built[si - 1] = None
        items, dyn, _ = built[si]; lt = tt - segs[si][0]; sc = v["scenes"][si]
        fr = bg.frame(tt).convert("RGBA")
        if sc["t"] != "title": fr.alpha_composite(panel, PANEL[:2])
        for it in items: it.draw(fr, lt)
        for f in dyn: f(fr, lt)
        last_content = fr.copy()
        if si > 0 and tiles is not None and lt < 0.55:
            for (c, r, im, dl) in tiles:
                if lt < dl: fr.paste(im, (c * TS, r * TS))
                elif lt < dl + 0.22:
                    p = (lt - dl) / 0.22; s = int(TS * (1 - 0.45 * p))
                    if s > 4:
                        sm = Image.eval(im.resize((s, s), Image.NEAREST), lambda v_, p=p: int(v_ * (1 - 0.6 * p)))
                        fr.paste(sm, (c * TS + (TS - s) // 2, r * TS + int(p * p * 300)))
        fr.alpha_composite(wm, (40, 150))
        d = ImageDraw.Draw(fr); prog = tt / total
        d.rectangle([0, 0, W, 14], fill=(20, 20, 20, 255)); d.rectangle([0, 2, int(W * prog), 12], fill=(128, 255, 32, 255))
        # botón final de "Sígueme"
        if si == len(segs) - 1 and lt > segs[si][1] - 2.6:
            p = back((lt - (segs[si][1] - 2.6)) / 0.4); fw = max(1, int(follow.width * p)); fh = max(1, int(follow.height * p))
            fi_ = follow.resize((fw, fh), Image.BILINEAR); fr.alpha_composite(fi_, (CX - fw // 2, 1420 - fh // 2))
        while ci < len(caps) and tt > caps[ci][1]: ci += 1
        if ci < len(caps) and caps[ci][0] <= tt:
            c = caps[ci][2]
            if c not in capc: capc = {c: caption_img(c)}
            im = capc[c]; k = clamp((tt - caps[ci][0]) / 0.1); sc_ = 0.85 + 0.15 * k
            if sc_ < 0.999: im = im.resize((int(im.width * sc_), int(im.height * sc_)), Image.BILINEAR)
            fr.alpha_composite(im, (CX - im.width // 2, CAP_Y - im.height // 2))
        if abs(tt - 1.6) < 0.5 / FPS:
            fr.convert("RGB").save(os.path.join(COV, f"{slug}.jpg"), quality=92)
        ff.stdin.write(fr.convert("RGB").tobytes())
    ff.stdin.close(); ff.wait()
    print(f"OK {out} ({total:.1f}s)", flush=True)
    return total


if __name__ == "__main__":
    want = sys.argv[1:]
    for v in SHORTS:
        if (not want and not os.path.exists(os.path.join(OUT, v["slug"] + ".mp4"))) or any(v["slug"].startswith(w) for w in want):
            render(v)
