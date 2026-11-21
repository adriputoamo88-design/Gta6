# -*- coding: utf-8 -*-
"""Render de los vídeos: python3 render.py [slug ...]  (sin argumentos: todos)."""
import math, os, subprocess, sys, json, zlib
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw

import art
from art import W, H, THEMES, text_img, icon, silhouette, rrect, add_glow, wrap, ANTON, BEBAS, MB, MX, MR
import audio
from content import CHANNEL, HANDLE
import loader
VIDEOS, OUTROOT = loader.load()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build"); OUT = os.path.join(OUTROOT, "videos"); SUBS = os.path.join(OUTROOT, "subtitulos")
FPS = 30
PAD_BEFORE, PAD_AFTER = 0.25, 0.45
WHITE = (255, 255, 255)
PANEL = (90, 100, 1830, 900)


def ease(p):
    p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3


class Item:
    def __init__(self, img, x, y, t0=0.0, kind="up", dur=0.4, center=False):
        if center: x -= img.width // 2
        self.img, self.x, self.y, self.t0, self.kind, self.dur = img, int(x), int(y), t0, kind, dur
        self.cache = {}

    def variant(self, step):
        if step not in self.cache:
            f = step / 8.0; im = self.img
            if self.kind == "pop":
                sc = 0.6 + 0.4 * f + 0.08 * math.sin(f * math.pi)
                im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BILINEAR)
            if step < 8:
                im = im.copy(); a = im.getchannel("A").point(lambda v: int(v * f)); im.putalpha(a)
            self.cache[step] = im
        return self.cache[step]

    def draw(self, frame, t):
        if t < self.t0: return
        p = ease((t - self.t0) / self.dur); step = int(round(p * 8))
        im = self.variant(step); x, y = self.x, self.y
        if self.kind == "up": y += int((1 - p) * 50)
        elif self.kind == "left": x -= int((1 - p) * 90)
        elif self.kind == "right": x += int((1 - p) * 90)
        elif self.kind == "pop": x += (self.img.width - im.width) // 2; y += (self.img.height - im.height) // 2
        frame.paste(im, (x, y), im)


# ---------------------------------------------------------------- escenas
def reveal_times(n, dur, start=0.5, end_frac=0.78):
    if n <= 1: return [start]
    end = max(start + 0.5, dur * end_frac)
    return [start + i * (end - start) / (n - 1) for i in range(n)]


def heading(h, th, y=140, size=96, x=150):
    return Item(text_img(h, ANTON, size, glow=th["acc"], glow_r=14, max_w=1600), x, y, 0.05, "left")


def build_scene(sc, th, dur, vid):
    t = sc["t"]; acc, acc2 = th["acc"], th["acc2"]; items = []; dyn = []
    if t == "title":
        tag = rrect(420, 64, 32, acc + (255,)); ImageDraw.Draw(tag).text((210, 32), CHANNEL, font=art.font(MB, 30), fill=(10, 5, 20), anchor="mm")
        items.append(Item(tag, W // 2, 250, 0.0, "fade", center=True))
        big = text_img(sc["h"], ANTON, 170, glow=acc, glow_r=22, max_w=1600, align="center")
        items.append(Item(big, W // 2, 520 - big.height // 2 - 40, 0.15, "pop", 0.5, center=True))
        sub = text_img(sc["s"], MX, 52, fill=acc2, max_w=1500, align="center")
        items.append(Item(sub, W // 2, 520 + big.height // 2 + 10 - 40, 0.55, "up", center=True))
    elif t == "stat":
        ic = icon(sc.get("icon", "star"), 300, WHITE, acc); ic = add_glow(ic, acc, 20, 0.8)
        items.append(Item(ic, 230, 500 - ic.height // 2, 0.05, "pop", 0.5))
        big = text_img(sc["big"], ANTON, 250, glow=acc, glow_r=22, max_w=1100)
        items.append(Item(big, 650, 210, 0.2, "left", 0.5))
        items.append(Item(text_img(sc["label"].upper(), MB, 64, fill=WHITE, max_w=1100), 660, 220 + big.height + 10, 0.5, "up"))
        items.append(Item(text_img(sc["small"], MX, 46, fill=acc2, max_w=1100), 660, 220 + big.height + 100, 0.9, "up"))
    elif t in ("bullets", "steps"):
        items.append(heading(sc["h"], th))
        its = sc["items"]; n = len(its); gap = min(130, 560 // max(1, n)); y0 = 300
        times = reveal_times(n, dur)
        for i, txt in enumerate(its):
            fs = 60 if n <= 4 else 50
            row = Image.new("RGBA", (1600, gap), (0, 0, 0, 0)); d = ImageDraw.Draw(row)
            if t == "steps":
                d.rounded_rectangle([0, gap // 2 - 36, 72, gap // 2 + 36], 14, fill=acc + (255,))
                d.text((36, gap // 2), str(i + 1), font=art.font(ANTON, 50), fill=(10, 5, 20), anchor="mm")
            else:
                d.rounded_rectangle([10, gap // 2 - 16, 42, gap // 2 + 16], 6, fill=acc + (255,))
            ti = text_img(txt, MX, fs, max_w=1450)
            row.alpha_composite(ti, (100, max(0, gap // 2 - ti.height // 2)))
            items.append(Item(row, 160, y0 + i * gap, times[i], "left"))
            if t == "steps" and i < n - 1:
                ar = text_img("↓", MB, 40, fill=acc2) if False else None
    elif t == "icon":
        ic = add_glow(icon(sc["icon"], 330, WHITE, acc), acc, 22, 0.8)
        items.append(Item(ic, W // 2, 140, 0.0, "pop", 0.5, center=True))
        h = text_img(sc["h"], ANTON, 130, glow=acc, glow_r=16, max_w=1600, align="center")
        items.append(Item(h, W // 2, 520, 0.3, "up", center=True))
        items.append(Item(text_img(sc["s"], MX, 50, fill=acc2, max_w=1500, align="center"), W // 2, 540 + h.height, 0.6, "up", center=True))
    elif t == "tip":
        num = text_img(f"#{sc['n']}", ANTON, 330, fill=acc, glow=acc, glow_r=24)
        items.append(Item(num, 200, 500 - num.height // 2, 0.0, "pop", 0.45))
        items.append(Item(text_img("CONSEJO", MB, 44, fill=acc2), 760, 290, 0.15, "fade"))
        h = text_img(wrap(sc["h"].upper(), ANTON, 120, 950), ANTON, 120, max_w=1000, spacing=-0.05)
        items.append(Item(h, 760, 350, 0.25, "left"))
        items.append(Item(text_img(wrap(sc["s"], MX, 46, 980), MX, 46, fill=(230, 230, 240), max_w=1000), 765, 380 + h.height, 0.6, "up"))
    elif t == "qa":
        items.append(Item(text_img(f"PREGUNTA {sc['n']}", MB, 46, fill=acc2), W // 2, 200, 0.0, "fade", center=True))
        q = text_img(wrap(sc["q"].upper(), ANTON, 130, 1500), ANTON, 130, glow=acc, glow_r=14, max_w=1600, align="center")
        items.append(Item(q, W // 2, 280, 0.1, "pop", 0.45, center=True))
        at = text_img(sc["a"], MB, 72, fill=(10, 5, 20), max_w=1400)
        box = rrect(at.width + 120, at.height + 60, 30, acc2 + (255,)); box.alpha_composite(at, (60, 30))
        items.append(Item(add_glow(box, acc2, 16, 0.7), W // 2, 330 + q.height + 40, min(1.2, dur * 0.3), "pop", 0.4, center=True))
    elif t == "map":
        MW, MH = 640, 760
        mp = art.map_image(MW, MH, acc)
        mx, my = 230, 115
        items.append(Item(mp, mx, my, 0.0, "fade", 0.6))
        hl = sc.get("hl", [])
        items.append(Item(text_img(sc["h"], ANTON, 120, glow=acc, glow_r=16, max_w=820), 1000, 200, 0.1, "right"))
        items.append(Item(text_img("Mapa ilustrativo · no oficial", MR, 30, fill=(220, 220, 230)), 1005, 820, 0.2, "fade"))
        pad = 14 * 2
        all_pins = range(len(art.REGIONS))
        times = reveal_times(len(hl), dur, 0.6) if len(hl) > 1 else [0.4]
        for i in all_pins:
            name, (nx, ny), tags = art.REGIONS[i][:3]
            px, py = mx + pad + nx * MW, my + pad + ny * MH
            on = i in hl; t0 = times[hl.index(i)] if on and len(hl) > 1 else (0.4 if on else 0.3)
            r = 16 if on else 9
            dot = Image.new("RGBA", (60, 60), (0, 0, 0, 0)); ImageDraw.Draw(dot).ellipse([30 - r, 30 - r, 30 + r, 30 + r], fill=(acc2 if on else (200, 200, 210)) + (255,))
            items.append(Item(dot, px - 30, py - 30, t0, "pop", 0.3))
            if on:
                lab = text_img(name, MB, 30 if len(hl) > 1 else 40, fill=WHITE, stroke=5, stroke_fill=(10, 5, 20))
                right = (nx <= 0.5) if len(hl) == 1 else art.REGIONS[i][3]
                lx = px + 24 if right else px - lab.width - 24
                items.append(Item(lab, lx, py - lab.height // 2, t0 + 0.1, "fade"))
                dyn.append(("pulse", px, py, t0, acc2))
                if len(hl) == 1:
                    for k, tg in enumerate(tags):
                        chip = text_img(tg.upper(), MB, 40, fill=(10, 5, 20))
                        bx = rrect(chip.width + 50, chip.height + 30, 24, acc + (255,)); bx.alpha_composite(chip, (25, 15))
                        items.append(Item(bx, 1005, 420 + k * 115, 0.7 + k * 0.5, "left"))
        if not hl:
            items.append(Item(text_img("Vice City y 5 regiones más", MX, 48, fill=acc2, max_w=800), 1005, 380, 0.6, "up"))
    elif t == "card":
        rim = (80, 200, 255) if sc["who"] == "jason" else (255, 90, 170)
        sil = silhouette(sc["who"], 640, rim)
        items.append(Item(sil, 170, 900 - 640 + 8, 0.0, "up", 0.5))
        items.append(Item(text_img(sc["role"].upper(), MB, 40, fill=acc2), 860, 210, 0.1, "fade"))
        nm = text_img(sc["name"], ANTON, 140, glow=rim, glow_r=16, max_w=950)
        items.append(Item(nm, 860, 260, 0.15, "right"))
        times = reveal_times(len(sc["lines"]), dur, 0.8)
        for i, ln in enumerate(sc["lines"]):
            row = text_img("— " + ln, MX, 44, fill=WHITE, max_w=960)
            items.append(Item(row, 865, 290 + nm.height + 30 + i * 90, times[i], "left"))
    elif t == "duo":
        items.append(Item(text_img(sc["h"], ANTON, 110, glow=acc, glow_r=16, max_w=1500, align="center"), W // 2, 125, 0.05, "pop", 0.45, center=True))
        for k, (who, nm, rim, x) in enumerate([("jason", "JASON", (80, 200, 255), 420), ("lucia", "LUCÍA", (255, 90, 170), 1500)]):
            s = silhouette(who, 520, rim)
            items.append(Item(s, x, 900 - 520 + 8, 0.2 + k * 0.3, "up", 0.5, center=True))
            items.append(Item(text_img(nm, ANTON, 90, fill=WHITE, glow=rim, glow_r=12), x, 300, 0.4 + k * 0.3, "fade", center=True))
        amp = text_img("&", MB, 200, fill=acc2, glow=acc2, glow_r=18)
        items.append(Item(amp, W // 2, 470, 0.9, "pop", 0.4, center=True))
    elif t == "vs":
        items.append(Item(text_img(sc["h"], ANTON, 96, glow=acc, glow_r=14, max_w=1500, align="center"), W // 2, 120, 0.05, "pop", 0.4, center=True))
        lt, rt = sc.get("lt", "GTA 5"), sc.get("rt", "GTA 6")
        for side, (lab, lines, x0, col) in enumerate([(lt, sc["left"], 170, (170, 170, 190)), (rt, sc["right"], 1010, acc)]):
            colp = rrect(740, 560, 30, (0, 0, 0, 120), outline=col + (255,), ow=4)
            items.append(Item(colp, x0, 280, 0.15 + side * 0.15, "up"))
            items.append(Item(text_img(lab, ANTON, 80, fill=col, glow=col if side else None, glow_r=10), x0 + 370, 300, 0.25 + side * 0.15, "fade", center=True))
        n = max(len(sc["left"]), len(sc["right"]))
        times = reveal_times(n * 2, dur, 0.6)
        for i in range(n):
            for side, (lines, x0) in enumerate([(sc["left"], 210), (sc["right"], 1050)]):
                if i < len(lines):
                    items.append(Item(text_img(lines[i], MX, 42, fill=WHITE, max_w=660), x0, 450 + i * 120, times[i * 2 + side], "up"))
        vs = add_glow(icon("vs", 170, (10, 5, 20), acc2), acc2, 16, 0.8)
        items.append(Item(vs, W // 2, 500, 0.4, "pop", 0.4, center=True))
    elif t == "timeline":
        items.append(heading(sc["h"], th))
        its = sc["items"]; n = len(its); x0, x1, y = 260, 1660, 560
        times = reveal_times(n, dur, 0.5)
        bar = Image.new("RGBA", (x1 - x0, 12), acc + (255,))
        items.append(Item(add_glow(bar, acc, 10, 1.0), x0 - 20, y - 26, 0.2, "fade"))
        for i, (yr, lab) in enumerate(its):
            cx = x0 + i * (x1 - x0) / (n - 1)
            dot = Image.new("RGBA", (70, 70), (0, 0, 0, 0)); ImageDraw.Draw(dot).ellipse([5, 5, 65, 65], fill=acc2 + (255,), outline=(10, 5, 20, 255), width=6)
            items.append(Item(dot, cx - 35, y - 35, times[i], "pop", 0.3))
            items.append(Item(text_img(yr, ANTON, 96, fill=WHITE, glow=acc, glow_r=10), cx, y - 190, times[i] + 0.05, "up", center=True))
            items.append(Item(text_img(wrap(lab, MX, 38, 340), MX, 38, fill=acc2, align="center"), cx, y + 60, times[i] + 0.15, "up", center=True))
    elif t == "outro":
        items.append(Item(text_img("¿TE HA SERVIDO?", ANTON, 110, glow=acc, glow_r=14), W // 2, 150, 0.0, "pop", 0.4, center=True))
        btn = rrect(760, 150, 40, (230, 20, 30, 255)); bd = ImageDraw.Draw(btn)
        bell = icon("bell", 90, WHITE, (255, 220, 0)); btn.alpha_composite(bell, (60, 30))
        bd.text((430, 75), "SUSCRÍBETE", font=art.font(ANTON, 86), fill=WHITE, anchor="mm")
        items.append(Item(add_glow(btn, (255, 40, 40), 22, 0.9), W // 2, 380, 0.4, "pop", 0.4, center=True))
        dyn.append(("btnpulse", W // 2, 380 + 22 + 75 + 22, 0.9, (255, 60, 60)))
        items.append(Item(text_img(f"{CHANNEL}  ·  {HANDLE}", MB, 50, fill=WHITE), W // 2, 640, 0.8, "up", center=True))
        items.append(Item(text_img("Nuevos vídeos de GTA 6 cada día", MX, 40, fill=acc2), W // 2, 730, 1.1, "up", center=True))
    return items, dyn


# ---------------------------------------------------------------- subtítulos
def chunks(say, maxc=40):
    words = say.split(); out = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) > maxc and cur:
            out.append(cur); cur = w
        else:
            cur = t
        if cur.endswith((".", "?", "!", ":")) and len(cur) > 18:
            out.append(cur); cur = ""
    if cur: out.append(cur)
    return out


def caption_img(txt, size=46):
    mw = 1700 if size < 60 else 980
    if size >= 60: txt = wrap(txt, MX, size, mw)
    ti = text_img(txt, MX, size, fill=WHITE, stroke=5, stroke_fill=(0, 0, 0), max_w=mw, align="center")
    bx = rrect(ti.width + 50, ti.height + 22, 18, (0, 0, 0, 150)); bx.alpha_composite(ti, (25, 11))
    return bx


def srt_time(s):
    ms = int(round(s * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); se, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{se:02},{ms:03}"


# ---------------------------------------------------------------- vídeo
def render(v):
    slug = v["slug"]; th = THEMES[v["theme"]]
    os.makedirs(os.path.join(BUILD, "tts", slug), exist_ok=True); os.makedirs(OUT, exist_ok=True); os.makedirs(SUBS, exist_ok=True)
    # 1) voz
    segs = []; t = 0.4; voice = []
    voice.append(np.zeros(int(0.4 * audio.SR), np.float32))
    for i, sc in enumerate(v["scenes"]):
        a = audio.speak(sc["say"], os.path.join(BUILD, "tts", slug, f"{i:02}"))
        d = PAD_BEFORE + len(a) / audio.SR + PAD_AFTER + (1.2 if sc["t"] == "outro" else 0)
        segs.append((t, d, PAD_BEFORE, len(a) / audio.SR))
        voice += [np.zeros(int(PAD_BEFORE * audio.SR), np.float32), a, np.zeros(int(round(d * audio.SR)) - int(PAD_BEFORE * audio.SR) - len(a), np.float32)]
        t += d
    total = t + 0.3
    vtrack = np.concatenate(voice); vtrack = np.pad(vtrack, (0, max(0, int(total * audio.SR) - len(vtrack))))
    vwav = os.path.join(BUILD, f"{slug}-voz.wav"); sf.write(vwav, vtrack, audio.SR)
    # 2) música + whoosh
    mus = audio.music(v["theme"], total) * 0.55
    wh = audio.whoosh()
    for (s0, d, _, _) in segs[1:]:
        k = int((s0 - 0.2) * audio.MSR); e = min(len(mus), k + len(wh)); mus[k:e] += wh[:e - k] * 0.8
    mwav = os.path.join(BUILD, f"{slug}-musica.wav"); sf.write(mwav, mus, audio.MSR)
    # 3) subtítulos (SRT + quemados) y capítulos
    caps = []; srt = []
    for i, (sc, (s0, d, pb, alen)) in enumerate(zip(v["scenes"], segs)):
        cs = chunks(sc["say"]); tot = sum(len(c) for c in cs); cur = s0 + pb
        for c in cs:
            cd = alen * len(c) / tot
            caps.append((cur, cur + cd, c)); cur += cd
    for k, (a, b, c) in enumerate(caps):
        srt.append(f"{k + 1}\n{srt_time(a)} --> {srt_time(b)}\n{c}\n")
    open(os.path.join(SUBS, f"{slug}.srt"), "w", encoding="utf-8").write("\n".join(srt))
    chapters = [("0:00", "Intro")]
    for sc, (s0, *_ ) in zip(v["scenes"], segs):
        if sc.get("chapter"): chapters.append((f"{int(s0 // 60)}:{int(s0 % 60):02}", sc["chapter"]))
    os.makedirs(BUILD, exist_ok=True); json.dump(dict(duration=total, chapters=chapters), open(os.path.join(BUILD, f"{slug}-meta.json"), "w"), ensure_ascii=False)
    cap_cache = {}
    # 4) frames
    bg = art.Background(v["theme"], seed=zlib.crc32(slug.encode()) % 1000)
    panel = rrect(PANEL[2] - PANEL[0], PANEL[3] - PANEL[1], 36, (8, 3, 20, 175), outline=th["acc"] + (90,), ow=2)
    wm = text_img(CHANNEL, BEBAS, 44, fill=WHITE, glow=th["acc"], glow_r=8)
    built = [None] * len(segs)
    short = v.get("short", False); OW, OH = (1080, 1920) if short else (W, H)
    if short:
        vbg = bg.frame(0.0).resize((int(1920 * 1920 / 1080), 1920)).crop((int((3413 - 1080) / 2), 0, int((3413 - 1080) / 2) + 1080, 1920))
        vbg = vbg.filter(__import__("PIL.ImageFilter", fromlist=["x"]).GaussianBlur(6))
        vbg = Image.blend(vbg, Image.new("RGB", vbg.size, (8, 3, 20)), 0.45)
        vt = text_img(art.wrap(v.get("short_title", v["title"]).upper(), ANTON, 120, 980), ANTON, 120, glow=th["acc"], glow_r=16, max_w=1000, align="center")
        vbg.paste(vt, (540 - vt.width // 2, 330 - vt.height // 2), vt)
        vwm = text_img(CHANNEL + "  ·  " + HANDLE, MB, 40, fill=th["acc2"]); vbg.paste(vwm, (540 - vwm.width // 2, 1700), vwm)
    out = os.path.join(OUT, f"{slug}.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}", "-r", str(FPS), "-i", "-",
           "-i", vwav, "-i", mwav, "-filter_complex",
           "[1:a]aresample=48000,asplit=2[v][sc];[2:a]aresample=48000[m];"
           "[m][sc]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=350[md];"
           "[v][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    nframes = int(total * FPS); si = 0; ci = 0
    for fi in range(nframes):
        tt = fi / FPS
        while si + 1 < len(segs) and tt >= segs[si + 1][0]: si += 1
        if built[si] is None:
            built[si] = build_scene(v["scenes"][si], th, segs[si][1], v)
            if si > 0: built[si - 1] = None
        items, dyn = built[si]; lt = tt - segs[si][0]
        fr = bg.frame(tt)
        fr.paste(panel, PANEL[:2], panel)
        for it in items: it.draw(fr, lt)
        d = ImageDraw.Draw(fr)
        for (kind, x, y, t0, col) in dyn:
            if lt < t0: continue
            ph = ((lt - t0) % 1.4) / 1.4
            if kind == "pulse":
                r = 16 + ph * 50; d.ellipse([x - r, y - r, x + r, y + r], outline=col, width=max(1, int(6 * (1 - ph))))
            else:
                r = ph * 1.0; w_ = 380 + r * 60; h_ = 75 + r * 30
                d.rounded_rectangle([x - w_, y - h_, x + w_, y + h_], 50, outline=col, width=max(1, int(8 * (1 - ph))))
        # transición: barrido diagonal
        if si > 0 and lt < 0.3:
            p = lt / 0.3; xx = int(-600 + p * (W + 1200))
            d.polygon([(xx - 500, 0), (xx, 0), (xx - 300, H), (xx - 800, H)], fill=th["acc"])
            d.polygon([(xx - 560, 0), (xx - 500, 0), (xx - 800, H), (xx - 860, H)], fill=th["acc2"])
        if not short:
            fr.paste(wm, (40, 24), wm)
            d.rectangle([0, H - 8, int(W * tt / total), H], fill=th["acc"])  # barra de progreso
        while ci < len(caps) and tt > caps[ci][1]: ci += 1
        cap = caps[ci][2] if ci < len(caps) and caps[ci][0] <= tt else None
        if cap and cap not in cap_cache: cap_cache = {cap: caption_img(cap, 64 if short else 46)}
        if short:
            vf = vbg.copy(); vf.paste(fr.crop((60, 70, 1860, 930)).resize((1080, 516), Image.BILINEAR), (0, 600))
            if cap:
                ci_img = cap_cache[cap]; vf.paste(ci_img, (540 - ci_img.width // 2, 1330), ci_img)
            ImageDraw.Draw(vf).rectangle([0, OH - 12, int(OW * tt / total), OH], fill=th["acc"])
            fr = vf
        elif cap:
            ci_img = cap_cache[cap]; fr.paste(ci_img, (W // 2 - ci_img.width // 2, 955 - ci_img.height // 2 + 10), ci_img)
        ff.stdin.write(fr.tobytes())
    ff.stdin.close(); ff.wait()
    print(f"OK {out} ({total:.1f}s)", flush=True)
    return total


if __name__ == "__main__":
    want = sys.argv[1:]
    for v in VIDEOS:
        if not want or any(v["slug"].startswith(w) for w in want):
            render(v)
