# -*- coding: utf-8 -*-
"""Gráficos originales dibujados por código: fondos, iconos, siluetas, mapa ilustrativo."""
import math, os, random
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
W, H = 1920, 1080

THEMES = {
    "sunset": dict(sky=[(28, 6, 58), (150, 30, 110), (255, 120, 70)], sun=[(255, 230, 90), (255, 60, 140)], acc=(255, 64, 150), acc2=(255, 205, 70), grid=(255, 80, 190)),
    "neon":   dict(sky=[(8, 4, 28), (55, 18, 110), (210, 50, 170)], sun=[(255, 120, 220), (120, 60, 255)], acc=(0, 225, 255), acc2=(255, 70, 210), grid=(0, 220, 255)),
    "danger": dict(sky=[(18, 0, 10), (105, 8, 30), (240, 80, 40)], sun=[(255, 210, 60), (255, 40, 40)], acc=(255, 60, 70), acc2=(255, 210, 0), grid=(255, 90, 60)),
    "money":  dict(sky=[(0, 22, 18), (8, 80, 56), (110, 200, 110)], sun=[(255, 240, 120), (60, 220, 120)], acc=(70, 255, 150), acc2=(255, 215, 0), grid=(80, 255, 160)),
    "ocean":  dict(sky=[(4, 16, 46), (10, 80, 130), (50, 205, 210)], sun=[(255, 240, 180), (255, 110, 190)], acc=(0, 235, 215), acc2=(255, 120, 200), grid=(0, 240, 220)),
    "retro":  dict(sky=[(30, 0, 52), (230, 50, 140), (255, 175, 80)], sun=[(255, 245, 120), (255, 70, 160)], acc=(255, 100, 200), acc2=(80, 235, 255), grid=(80, 235, 255)),
}


@lru_cache(None)
def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

ANTON = "Anton.ttf"; BEBAS = "BebasNeue.ttf"; MB = "Montserrat-Black.ttf"; MX = "Montserrat-ExtraBold.ttf"; MR = "Montserrat-Regular.ttf"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def vgrad(w, h, stops):
    im = Image.new("RGB", (1, h))
    n = len(stops) - 1
    for y in range(h):
        f = y / max(1, h - 1) * n
        i = min(int(f), n - 1)
        im.putpixel((0, y), lerp(stops[i], stops[i + 1], f - i))
    return im.resize((w, h))


# ---------------------------------------------------------------- texto
def text_img(txt, fname, size, fill=(255, 255, 255), stroke=0, stroke_fill=(0, 0, 0), glow=None, glow_r=18, max_w=None, spacing=0.12, align="left"):
    """Devuelve RGBA recortado con el texto (multi-línea con \n). Ajusta tamaño si max_w."""
    f = font(fname, size)
    lines = txt.split("\n")
    while max_w:
        widest = max(f.getbbox(l, stroke_width=stroke)[2] for l in lines)
        if widest <= max_w or size < 20:
            break
        size = int(size * 0.94); f = font(fname, size)
    asc, desc = f.getmetrics()
    lh = int((asc + desc) * (1 + spacing))
    widths = [f.getbbox(l, stroke_width=stroke)[2] for l in lines]
    pad = glow_r * 2 + stroke + 6 if glow else stroke + 6
    w = max(widths) + pad * 2; h = lh * len(lines) + pad * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = pad + ((max(widths) - widths[i]) // 2 if align == "center" else 0)
        d.text((x, pad + i * lh), l, font=f, fill=fill + (255,), stroke_width=stroke, stroke_fill=stroke_fill)
    if glow:
        a = im.getchannel("A").filter(ImageFilter.GaussianBlur(glow_r))
        g = Image.new("RGBA", im.size, glow + (0,)); g.putalpha(a.point(lambda v: min(255, int(v * 1.6))))
        g.alpha_composite(im); im = g
    return im.crop(im.getbbox())


def wrap(txt, fname, size, max_w):
    f = font(fname, size); words = txt.split(); lines = []; cur = ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if f.getbbox(t)[2] > max_w and cur:
            lines.append(cur); cur = wd
        else:
            cur = t
    if cur: lines.append(cur)
    return "\n".join(lines)


def rrect(w, h, r, fill, outline=None, ow=0):
    s = 2
    im = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * s - 1, h * s - 1], r * s, fill=fill, outline=outline, width=ow * s)
    return im.resize((w, h), Image.LANCZOS)


def add_glow(im, color, r=16, k=1.5):
    pad = r * 2
    big = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    big.alpha_composite(im, (pad, pad))
    a = big.getchannel("A").filter(ImageFilter.GaussianBlur(r)).point(lambda v: min(255, int(v * k)))
    g = Image.new("RGBA", big.size, color + (0,)); g.putalpha(a)
    g.alpha_composite(big)
    return g


# ---------------------------------------------------------------- fondo
def skyline_layer(width, seed, color):
    rnd = random.Random(seed)
    h = 420
    im = Image.new("RGBA", (width, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x = 0
    while x < width:
        bw = rnd.randint(40, 120); bh = rnd.randint(80, 360)
        d.rectangle([x, h - bh, x + bw, h], fill=color + (255,))
        if rnd.random() < 0.25:
            d.rectangle([x + bw // 2 - 3, h - bh - 40, x + bw // 2 + 3, h - bh], fill=color + (255,))
        for wy in range(h - bh + 14, h - 10, 22):
            for wx in range(x + 8, x + bw - 8, 16):
                if rnd.random() < 0.18:
                    d.rectangle([wx, wy, wx + 6, wy + 9], fill=(255, 220, 160, 150))
        x += bw + rnd.randint(0, 14)
    return im


def palm(h, color):
    s = 2; W_ = int(h * 0.9)
    im = Image.new("RGBA", (W_ * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = W_ * s // 2; top = int(h * s * 0.18)
    # tronco curvado
    pts = []
    for i in range(30):
        t = i / 29; x = cx + int(math.sin(t * 1.4) * W_ * s * 0.12); y = h * s - t * (h * s - top)
        pts.append((x, y))
    for i in range(len(pts) - 1):
        wdt = int((1 - i / 30) * 26 * s + 8 * s)
        d.line([pts[i], pts[i + 1]], fill=color + (255,), width=wdt)
    tx, ty = pts[-1]
    for ang in [-170, -140, -110, -70, -40, -10, 20, 200]:
        a = math.radians(ang); L = h * s * 0.42
        path = []
        for i in range(20):
            t = i / 19
            px = tx + math.cos(a) * L * t
            py = ty + math.sin(a) * L * t + (t ** 2) * L * 0.45
            path.append((px, py))
        for i in range(len(path) - 1):
            wdt = int((1 - i / 20) * 30 * s + 4)
            d.line([path[i], path[i + 1]], fill=color + (255,), width=wdt)
    return im.resize((W_, h), Image.LANCZOS)


class Background:
    def __init__(self, theme, seed=1):
        th = THEMES[theme]; self.th = th
        horizon = 700
        sky = vgrad(W, horizon, th["sky"])
        base = Image.new("RGB", (W, H), (10, 4, 22)); base.paste(sky, (0, 0))
        # sol con franjas
        R = 300; sun = vgrad(R * 2, R * 2, th["sun"]).convert("RGBA")
        m = Image.new("L", (R * 2, R * 2), 0); md = ImageDraw.Draw(m); md.ellipse([0, 0, R * 2, R * 2], fill=255)
        for i in range(7):
            y = int(R * 1.05 + i * (R * 0.95 / 7)); md.rectangle([0, y, R * 2, y + 6 + i * 3], fill=0)
        sun.putalpha(m)
        sun = add_glow(sun, th["sun"][1], r=50, k=0.9)
        base.paste(sun, (W // 2 - sun.width // 2, horizon - R - 60 - (sun.height - 2 * R) // 2), sun)
        # estrellas
        rnd = random.Random(seed); d = ImageDraw.Draw(base)
        for _ in range(160):
            x, y = rnd.randint(0, W), rnd.randint(0, 330); c = rnd.randint(150, 255)
            d.point((x, y), fill=(c, c, c))
        self.base = base; self.horizon = horizon
        dark = lerp(th["sky"][0], (0, 0, 0), 0.35)
        self.city_far = skyline_layer(W + 800, seed + 3, lerp(th["sky"][1], (0, 0, 0), 0.55))
        self.city = skyline_layer(W + 800, seed + 7, dark)
        p = palm(560, (8, 2, 14)); self.palms = [(p, 30, horizon - 520), (p.transpose(Image.FLIP_LEFT_RIGHT), W - p.width - 20, horizon - 480)]
        # suelo: rejilla animada (bucle de 30 frames)
        self.floor = []
        fh = H - horizon
        for k in range(30):
            fl = vgrad(W, fh, [(12, 3, 26), (4, 1, 10)]).convert("RGBA"); fd = ImageDraw.Draw(fl)
            gc = th["grid"]
            for i in range(-30, 31):
                x0 = W // 2 + i * 34; x1 = W // 2 + i * 260
                fd.line([(x0, 0), (x1, fh)], fill=gc + (110,), width=2)
            for j in range(14):
                z = (j + k / 30.0)
                y = int(fh * (z / 14) ** 2.2)
                fd.line([(0, y), (W, y)], fill=gc + (int(40 + 120 * (z / 14)),), width=2)
            fd.line([(0, 0), (W, 0)], fill=gc + (255,), width=3)
            self.floor.append(fl.convert("RGB"))

    def frame(self, t):
        im = self.base.copy()
        off_far = int(t * 6) % 800; off = int(t * 14) % 800
        im.paste(self.city_far.crop((off_far, 0, off_far + W, 420)), (0, self.horizon - 420 + 10), self.city_far.crop((off_far, 0, off_far + W, 420)))
        c = self.city.crop((off, 0, off + W, 420)); im.paste(c, (0, self.horizon - 380), c)
        im.paste(self.floor[int(t * 30) % 30], (0, self.horizon))
        for p, x, y in self.palms:
            im.paste(p, (x, y), p)
        return im


# ---------------------------------------------------------------- iconos
def icon(name, S=320, col=(255, 255, 255), acc=(255, 80, 160)):
    s = 4; N = S * s
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = col + (255,); a = acc + (255,); lw = int(N * 0.06)
    def circ(cx, cy, r, **kw): d.ellipse([cx - r, cy - r, cx + r, cy + r], **kw)
    def txt(t, size, fill=c, fn=ANTON):
        f = font(fn, int(size)); bb = d.textbbox((0, 0), t, font=f)
        d.text(((N - bb[2] - bb[0]) / 2, (N - bb[3] - bb[1]) / 2 - bb[1] * 0.0), t, font=f, fill=fill)
    if name == "clock":
        circ(N / 2, N / 2, N * 0.42, outline=c, width=lw)
        for i in range(12):
            ag = i / 12 * 2 * math.pi; r1, r2 = N * 0.33, N * 0.38
            d.line([(N / 2 + math.cos(ag) * r1, N / 2 + math.sin(ag) * r1), (N / 2 + math.cos(ag) * r2, N / 2 + math.sin(ag) * r2)], fill=c, width=lw // 2)
        d.line([(N / 2, N / 2), (N / 2, N * 0.2)], fill=a, width=lw); d.line([(N / 2, N / 2), (N * 0.68, N * 0.6)], fill=c, width=lw)
        circ(N / 2, N / 2, lw * 0.8, fill=a)
    elif name in ("money", "bag"):
        if name == "bag":
            d.ellipse([N * 0.15, N * 0.3, N * 0.85, N * 0.95], fill=c); d.polygon([(N * 0.35, N * 0.1), (N * 0.65, N * 0.1), (N * 0.58, N * 0.33), (N * 0.42, N * 0.33)], fill=c)
            d.line([(N * 0.36, N * 0.33), (N * 0.64, N * 0.33)], fill=a, width=lw)
            f = font(ANTON, int(N * 0.45)); bb = d.textbbox((0, 0), "$", font=f); d.text(((N - bb[2]) / 2, N * 0.62 - (bb[3] + bb[1]) / 2), "$", font=f, fill=a)
        else:
            circ(N / 2, N / 2, N * 0.44, fill=a); circ(N / 2, N / 2, N * 0.36, outline=c, width=lw // 2)
            txt("$", N * 0.55, fill=c)
    elif name == "disk":
        d.rounded_rectangle([N * 0.08, N * 0.3, N * 0.92, N * 0.7], radius=N * 0.05, outline=c, width=lw)
        for i in range(6): d.rectangle([N * (0.16 + i * 0.07), N * 0.62, N * (0.19 + i * 0.07), N * 0.7], fill=c)
        d.rectangle([N * 0.18, N * 0.38, N * 0.5, N * 0.54], fill=a)
        circ(N * 0.78, N * 0.46, N * 0.04, fill=a)
    elif name == "box":
        d.polygon([(N * .5, N * .12), (N * .9, N * .3), (N * .5, N * .48), (N * .1, N * .3)], fill=a)
        d.polygon([(N * .1, N * .3), (N * .5, N * .48), (N * .5, N * .9), (N * .1, N * .72)], fill=c)
        d.polygon([(N * .9, N * .3), (N * .5, N * .48), (N * .5, N * .9), (N * .9, N * .72)], fill=lerp(col, (0, 0, 0), .35) + (255,))
    elif name == "globe":
        circ(N / 2, N / 2, N * 0.42, outline=c, width=lw)
        d.ellipse([N * 0.32, N * 0.08, N * 0.68, N * 0.92], outline=c, width=lw // 2)
        d.line([(N * 0.08, N / 2), (N * 0.92, N / 2)], fill=c, width=lw // 2)
        d.line([(N * 0.15, N * 0.3), (N * 0.85, N * 0.3)], fill=c, width=lw // 3); d.line([(N * 0.15, N * 0.7), (N * 0.85, N * 0.7)], fill=c, width=lw // 3)
        d.line([(N * 0.15, N * 0.85), (N * 0.85, N * 0.15)], fill=a, width=lw)
    elif name == "warning":
        d.polygon([(N / 2, N * 0.06), (N * 0.96, N * 0.9), (N * 0.04, N * 0.9)], fill=a)
        d.polygon([(N / 2, N * 0.2), (N * 0.84, N * 0.83), (N * 0.16, N * 0.83)], fill=(20, 0, 10, 255))
        d.rounded_rectangle([N * 0.46, N * 0.36, N * 0.54, N * 0.64], radius=N * 0.03, fill=c); circ(N / 2, N * 0.73, N * 0.045, fill=c)
    elif name == "search":
        circ(N * 0.42, N * 0.42, N * 0.28, outline=c, width=lw); d.line([(N * 0.62, N * 0.62), (N * 0.9, N * 0.9)], fill=a, width=int(lw * 1.6))
        txt("?", N * 0.38, fill=a) if False else None
    elif name == "trophy":
        d.pieslice([N * 0.2, N * 0.0, N * 0.8, N * 0.62], 0, 180, fill=a); d.rectangle([N * 0.2, N * 0.08, N * 0.8, N * 0.31], fill=a)
        d.arc([N * 0.04, N * 0.12, N * 0.34, N * 0.42], 90, 270, fill=a, width=lw // 2); d.arc([N * 0.66, N * 0.12, N * 0.96, N * 0.42], 270, 90, fill=a, width=lw // 2)
        d.rectangle([N * 0.45, N * 0.6, N * 0.55, N * 0.78], fill=a); d.rounded_rectangle([N * 0.28, N * 0.78, N * 0.72, N * 0.9], radius=N * .02, fill=c)
    elif name == "bell":
        d.pieslice([N * 0.2, N * 0.12, N * 0.8, N * 0.72], 180, 360, fill=c); d.rectangle([N * 0.2, N * 0.42, N * 0.8, N * 0.7], fill=c)
        d.polygon([(N * 0.2, N * 0.7), (N * 0.8, N * 0.7), (N * 0.9, N * 0.78), (N * 0.1, N * 0.78)], fill=c)
        circ(N / 2, N * 0.86, N * 0.07, fill=a); circ(N / 2, N * 0.1, N * 0.05, fill=c)
    elif name == "star":
        pts = []
        for i in range(10):
            r = N * 0.46 if i % 2 == 0 else N * 0.19; ag = -math.pi / 2 + i * math.pi / 5
            pts.append((N / 2 + math.cos(ag) * r, N * 0.53 + math.sin(ag) * r))
        d.polygon(pts, fill=a)
    elif name == "car":
        d.rounded_rectangle([N * 0.04, N * 0.45, N * 0.96, N * 0.7], radius=N * 0.08, fill=a)
        d.polygon([(N * 0.24, N * 0.47), (N * 0.36, N * 0.26), (N * 0.66, N * 0.26), (N * 0.8, N * 0.47)], fill=a)
        d.polygon([(N * 0.3, N * 0.45), (N * 0.39, N * 0.31), (N * 0.5, N * 0.31), (N * 0.5, N * 0.45)], fill=(20, 10, 30, 255))
        d.polygon([(N * 0.54, N * 0.45), (N * 0.54, N * 0.31), (N * 0.64, N * 0.31), (N * 0.74, N * 0.45)], fill=(20, 10, 30, 255))
        for x in (0.25, 0.75): circ(N * x, N * 0.7, N * 0.11, fill=(15, 8, 25, 255)); circ(N * x, N * 0.7, N * 0.05, fill=c)
    elif name == "chart":
        for i, hh in enumerate([0.25, 0.4, 0.35, 0.6, 0.8]):
            d.rectangle([N * (0.1 + i * 0.17), N * (0.9 - hh), N * (0.22 + i * 0.17), N * 0.9], fill=c)
        d.line([(N * 0.1, N * 0.6), (N * 0.35, N * 0.45), (N * 0.55, N * 0.5), (N * 0.85, N * 0.15)], fill=a, width=lw)
        d.polygon([(N * 0.92, N * 0.06), (N * 0.92, N * 0.26), (N * 0.74, N * 0.12)], fill=a)
    elif name == "swap":
        d.line([(N * 0.15, N * 0.35), (N * 0.8, N * 0.35)], fill=c, width=lw); d.polygon([(N * 0.92, N * 0.35), (N * 0.72, N * 0.2), (N * 0.72, N * 0.5)], fill=c)
        d.line([(N * 0.85, N * 0.68), (N * 0.2, N * 0.68)], fill=a, width=lw); d.polygon([(N * 0.08, N * 0.68), (N * 0.28, N * 0.53), (N * 0.28, N * 0.83)], fill=a)
    elif name == "question":
        circ(N / 2, N / 2, N * 0.44, fill=a); txt("?", N * 0.62, fill=c)
    elif name == "film":
        d.rounded_rectangle([N * 0.1, N * 0.4, N * 0.9, N * 0.88], radius=N * 0.03, fill=c)
        d.polygon([(N * 0.1, N * 0.36), (N * 0.86, N * 0.14), (N * 0.9, N * 0.27), (N * 0.14, N * 0.48)], fill=a)
        for i in range(4): d.polygon([(N * (0.22 + i * 0.17), N * 0.32), (N * (0.3 + i * 0.17), N * 0.3), (N * (0.24 + i * 0.17), N * 0.42), (N * (0.16 + i * 0.17), N * 0.44)], fill=(20, 10, 30, 255))
    elif name == "phone":
        d.rounded_rectangle([N * 0.28, N * 0.06, N * 0.72, N * 0.94], radius=N * 0.07, fill=c)
        d.rounded_rectangle([N * 0.32, N * 0.14, N * 0.68, N * 0.82], radius=N * 0.02, fill=a)
        for i in range(3):
            d.rounded_rectangle([N * 0.36, N * (0.2 + i * 0.2), N * 0.64, N * (0.34 + i * 0.2)], radius=N * .02, fill=lerp(acc, (255, 255, 255), .5) + (255,))
    elif name == "pin":
        d.pieslice([N * 0.2, N * 0.05, N * 0.8, N * 0.65], 180, 360, fill=a); d.polygon([(N * 0.2, N * 0.35), (N * 0.8, N * 0.35), (N / 2, N * 0.95)], fill=a)
        d.ellipse([N * 0.2, N * 0.05, N * 0.8, N * 0.65], fill=a); circ(N / 2, N * 0.35, N * 0.12, fill=c)
    elif name == "palm":
        p = palm(N, a[:3]); im.alpha_composite(p.resize((N, N)), (0, 0))
    elif name == "controller":
        d.rounded_rectangle([N * 0.06, N * 0.28, N * 0.94, N * 0.68], radius=N * 0.18, fill=c)
        d.ellipse([N * 0.04, N * 0.4, N * 0.36, N * 0.9], fill=c); d.ellipse([N * 0.64, N * 0.4, N * 0.96, N * 0.9], fill=c)
        d.rectangle([N * 0.2, N * 0.4, N * 0.26, N * 0.6], fill=a); d.rectangle([N * 0.13, N * 0.47, N * 0.33, N * 0.53], fill=a)
        for (x, y) in [(0.72, 0.4), (0.8, 0.48), (0.72, 0.56), (0.64, 0.48)]: circ(N * x, N * y, N * 0.035, fill=a)
    elif name == "duo":
        im.alpha_composite(silhouette("jason", N, acc).resize((int(N * 0.62), int(N * 0.62))), (0, int(N * 0.38)))
        im.alpha_composite(silhouette("lucia", N, acc).resize((int(N * 0.62), int(N * 0.62))), (int(N * 0.38), int(N * 0.38)))
    elif name == "vs":
        circ(N / 2, N / 2, N * 0.44, fill=a); txt("VS", N * 0.5, fill=c)
    return im.resize((S, S), Image.LANCZOS)


def silhouette(who, S=600, rim=(255, 80, 160)):
    s = 2; N = S * s
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    body = (14, 6, 24, 255)
    if who == "lucia":
        d.ellipse([N * 0.3, N * 0.1, N * 0.7, N * 0.62], fill=body)  # pelo largo
        d.rectangle([N * 0.3, N * 0.35, N * 0.7, N * 0.72], fill=body)
    d.ellipse([N * 0.36, N * 0.14, N * 0.64, N * 0.5], fill=body)  # cabeza
    if who == "jason":
        d.ellipse([N * 0.35, N * 0.12, N * 0.65, N * 0.32], fill=body)
    d.rectangle([N * 0.45, N * 0.45, N * 0.55, N * 0.62], fill=body)  # cuello
    d.rounded_rectangle([N * 0.1, N * 0.58, N * 0.9, N * 1.2], radius=N * 0.2, fill=body)  # hombros
    im = im.resize((S, S), Image.LANCZOS)
    a = im.getchannel("A")
    edge = ImageChops.subtract(a, a.filter(ImageFilter.MinFilter(9)))
    rimg = Image.new("RGBA", im.size, rim + (0,)); rimg.putalpha(edge.filter(ImageFilter.GaussianBlur(2)).point(lambda v: min(255, v * 3)))
    glow = Image.new("RGBA", im.size, rim + (0,)); glow.putalpha(a.filter(ImageFilter.GaussianBlur(26)).point(lambda v: int(v * 0.7)))
    out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.alpha_composite(glow); out.alpha_composite(im); out.alpha_composite(rimg)
    return out


# ---------------------------------------------------------------- mapa ilustrativo
REGIONS = [  # nombre, (x,y) normalizado, etiquetas
    ("VICE CITY", (0.86, 0.74), ["Ciudad", "Playas", "Neón"], True),
    ("LEONIDA KEYS", (0.60, 0.965), ["Islas", "Barcos", "Pesca"], True),
    ("GRASSRIVERS", (0.68, 0.72), ["Pantanos", "Caimanes", "Manglares"], False),
    ("PORT GELLHORN", (0.18, 0.16), ["Moteles", "Costa", "Decadencia"], True),
    ("AMBROSIA", (0.6, 0.42), ["Industria", "Lago", "Refinería"], True),
    ("MOUNT KALAGA", (0.62, 0.11), ["Bosques", "Montaña", "Caza"], True),
]
LAND = [(0.02, 0.10), (0.30, 0.09), (0.45, 0.07), (0.58, 0.02), (0.74, 0.05), (0.80, 0.18), (0.85, 0.34), (0.91, 0.5), (0.95, 0.64),
        (0.96, 0.76), (0.9, 0.86), (0.8, 0.91), (0.7, 0.88), (0.62, 0.79), (0.53, 0.66), (0.49, 0.53), (0.44, 0.41), (0.36, 0.31),
        (0.26, 0.25), (0.14, 0.23), (0.04, 0.21)]


def map_image(MW, MH, acc, land=(30, 70, 90)):
    s = 2
    im = Image.new("RGBA", (MW * s, MH * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pts = [(x * MW * s, y * MH * s) for x, y in LAND]
    d.polygon(pts, fill=land + (235,))
    for i in range(9):  # cayos
        t = i / 8; x = 0.78 - t * 0.33; y = 0.93 + math.sin(t * 2.4) * 0.035
        d.ellipse([x * MW * s - 16, y * MH * s - 8, x * MW * s + 16, y * MH * s + 8], fill=land + (235,))
    lx, ly = 0.7, 0.5
    d.ellipse([lx * MW * s - 50, ly * MH * s - 40, lx * MW * s + 50, ly * MH * s + 40], fill=(10, 30, 60, 255))  # lago
    d.line(pts + [pts[0]], fill=acc + (255,), width=6)
    im = im.resize((MW, MH), Image.LANCZOS)
    return add_glow(im, acc, r=14, k=1.0)
