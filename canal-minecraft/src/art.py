# -*- coding: utf-8 -*-
"""Gráficos originales del canal, todos dibujados por código.

- Texturas de bloque procedurales de 16x16 (no se usa ninguna textura del juego).
- Cubos isométricos en 3D que giran.
- Sprites en pixel art diseñados para el canal.
- Fondos animados: superficie, cueva, cueva de hielo y noche.
"""
import math, os, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
W, H = 1920, 1080

PIX = "PixelifySans.ttf"; SILK = "Silkscreen-Bold.ttf"; P2P = "PressStart2P.ttf"
MB = "Montserrat-Black.ttf"; MX = "Montserrat-ExtraBold.ttf"; MR = "Montserrat-Regular.ttf"

GOLD = (255, 214, 64); WHITE = (255, 255, 255); INK = (16, 14, 20)

THEMES = {
    "superficie": dict(acc=(118, 214, 72), acc2=GOLD, panel=(14, 22, 12), music="aventura"),
    "cueva":      dict(acc=(84, 232, 218), acc2=GOLD, panel=(10, 12, 18), music="cueva"),
    "hielo":      dict(acc=(140, 210, 255), acc2=(255, 255, 255), panel=(8, 16, 30), music="hielo"),
    "noche":      dict(acc=(176, 120, 255), acc2=GOLD, panel=(12, 8, 24), music="noche"),
    "end":        dict(acc=(200, 130, 255), acc2=(240, 236, 170), panel=(14, 6, 24), music="noche"),
    "nether":     dict(acc=(255, 122, 60), acc2=GOLD, panel=(26, 6, 6), music="cueva"),
}


@lru_cache(None)
def font(name, size):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    if name == PIX:
        f.set_variation_by_name("Bold")
    return f


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def vgrad(w, h, stops):
    ys = np.linspace(0, 1, h)[:, None]
    n = len(stops) - 1
    f = ys * n; i = np.minimum(f.astype(int), n - 1); fr = f - i
    st = np.array(stops, dtype=np.float32)
    col = st[i[:, 0]] * (1 - fr) + st[i[:, 0] + 1] * fr
    arr = np.repeat(col[:, None, :], w, axis=1)
    return Image.fromarray(arr.astype(np.uint8), "RGB")


# ================================================================ texto
def text_img(txt, fname, size, fill=WHITE, shadow=True, shadow_col=None, stroke=0, stroke_fill=INK,
             max_w=None, spacing=0.10, align="left", glow=None, glow_r=14, outline=0, outline_col=INK):
    """Texto RGBA recortado. Sombra dura desplazada (estilo pixel) opcional."""
    f = font(fname, size)
    lines = txt.split("\n")
    while max_w:
        widest = max(f.getbbox(l, stroke_width=stroke)[2] for l in lines)
        if widest <= max_w or size < 18:
            break
        size = int(size * 0.94); f = font(fname, size)
    asc, desc = f.getmetrics(); lh = int((asc + desc) * (1 + spacing))
    widths = [f.getbbox(l, stroke_width=stroke)[2] for l in lines]
    so = max(2, size // 11) if shadow else 0
    pad = (glow_r * 2 if glow else 0) + stroke + so + 6
    w = max(widths) + pad * 2; h = lh * len(lines) + pad * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    sc = shadow_col or lerp(fill, (0, 0, 0), 0.75)
    for i, l in enumerate(lines):
        x = pad + ((max(widths) - widths[i]) // 2 if align == "center" else 0); y = pad + i * lh
        if shadow:
            d.text((x + so, y + so), l, font=f, fill=sc + (255,), stroke_width=stroke, stroke_fill=sc)
        d.text((x, y), l, font=f, fill=fill + (255,), stroke_width=stroke, stroke_fill=stroke_fill)
    if outline:
        # contorno por dilatación de la máscara (el trazo de FreeType descoloca las tildes de las fuentes pixel)
        pad_o = outline + 2
        big = Image.new("RGBA", (im.width + pad_o * 2, im.height + pad_o * 2), (0, 0, 0, 0)); big.alpha_composite(im, (pad_o, pad_o))
        m = big.getchannel("A").point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(outline * 2 + 1))
        ol = Image.new("RGBA", big.size, outline_col + (0,)); ol.putalpha(m)
        ol.alpha_composite(big); im = ol
    if glow:
        a = im.getchannel("A").filter(ImageFilter.GaussianBlur(glow_r))
        g = Image.new("RGBA", im.size, glow + (0,)); g.putalpha(a.point(lambda v: min(255, int(v * 1.3))))
        g.alpha_composite(im); im = g
    return im.crop(im.getbbox())


def wrap(txt, fname, size, max_w):
    f = font(fname, size); out = []
    for para in txt.split("\n"):
        cur = ""
        for wd in para.split():
            t = (cur + " " + wd).strip()
            if f.getbbox(t)[2] > max_w and cur:
                out.append(cur); cur = wd
            else:
                cur = t
        out.append(cur)
    return "\n".join(out)


def add_glow(im, color, r=16, k=1.4):
    pad = r * 2
    big = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0)); big.alpha_composite(im, (pad, pad))
    a = big.getchannel("A").filter(ImageFilter.GaussianBlur(r)).point(lambda v: min(255, int(v * k)))
    g = Image.new("RGBA", big.size, color + (0,)); g.putalpha(a); g.alpha_composite(big)
    return g


def shadowed(im, off=10, alpha=150):
    """Sombra dura debajo de un sprite."""
    out = Image.new("RGBA", (im.width + off, im.height + off), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda v: v * alpha // 255))
    out.alpha_composite(sh, (off, off)); out.alpha_composite(im, (0, 0))
    return out


# ================================================================ paneles estilo interfaz de bloques
def bevel_box(w, h, fill=(120, 120, 120), light=None, dark=None, b=6, border=INK, alpha=255):
    light = light or lerp(fill, WHITE, 0.45); dark = dark or lerp(fill, (0, 0, 0), 0.45)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], fill=border + (alpha,))
    d.rectangle([b // 2, b // 2, w - 1 - b // 2, h - 1 - b // 2], fill=fill + (alpha,))
    d.rectangle([b // 2, b // 2, w - 1 - b // 2, b // 2 + b - 1], fill=light + (alpha,))
    d.rectangle([b // 2, b // 2, b // 2 + b - 1, h - 1 - b // 2], fill=light + (alpha,))
    d.rectangle([b // 2, h - b // 2 - b, w - 1 - b // 2, h - 1 - b // 2], fill=dark + (alpha,))
    d.rectangle([w - b // 2 - b, b // 2, w - 1 - b // 2, h - 1 - b // 2], fill=dark + (alpha,))
    return im


def label_box(txt, fname=PIX, size=44, fill=(120, 120, 120), fg=WHITE, padx=28, pady=14, b=6):
    t = text_img(txt, fname, size, fill=fg)
    bx = bevel_box(t.width + padx * 2, t.height + pady * 2, fill=fill, b=b)
    bx.alpha_composite(t, (padx, pady))
    return bx


def gui_panel(w, h, tint=(14, 14, 18), alpha=178):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], fill=INK + (230,))
    d.rectangle([5, 5, w - 6, h - 6], fill=tint + (alpha,))
    d.rectangle([5, 5, w - 6, 9], fill=(255, 255, 255, 46)); d.rectangle([5, 5, 9, h - 6], fill=(255, 255, 255, 46))
    d.rectangle([5, h - 10, w - 6, h - 6], fill=(0, 0, 0, 90)); d.rectangle([w - 10, 5, w - 6, h - 6], fill=(0, 0, 0, 90))
    return im


def slot(S=120, sprite=None, sel=False, acc=GOLD):
    im = bevel_box(S, S, fill=(139, 139, 139), light=(55, 55, 55), dark=(255, 255, 255), b=max(4, S // 20), border=(30, 30, 30))
    d = ImageDraw.Draw(im); d.rectangle([S // 10, S // 10, S - S // 10, S - S // 10], fill=(122, 122, 122, 255))
    if sprite is not None:
        sp = sprite.resize((int(S * 0.74), int(S * 0.74)), Image.NEAREST) if sprite.width != int(S * 0.74) else sprite
        im.alpha_composite(sp, ((S - sp.width) // 2, (S - sp.height) // 2))
    if sel:
        o = Image.new("RGBA", (S + 16, S + 16), (0, 0, 0, 0)); od = ImageDraw.Draw(o)
        od.rectangle([0, 0, S + 15, S + 15], outline=WHITE + (255,), width=8); od.rectangle([4, 4, S + 11, S + 11], outline=acc + (255,), width=3)
        o.alpha_composite(im, (8, 8)); im = o
    return im


# ================================================================ texturas procedurales 16x16
def _noise(rng, base, amp, n=16):
    v = rng.integers(-amp, amp + 1, size=(n, n, 1))
    return np.clip(np.array(base)[None, None, :] + v, 0, 255)


def _specks(arr, rng, cols, count, size=(1, 3)):
    n = arr.shape[0]
    for _ in range(count):
        x, y = rng.integers(0, n, 2); s = rng.integers(size[0], size[1] + 1)
        c = cols[rng.integers(0, len(cols))]
        for dx in range(s):
            for dy in range(s):
                if rng.random() < 0.75:
                    arr[(y + dy) % n, (x + dx) % n] = c
    return arr


def _ore(base_arr, rng, c_dark, c_mid, c_light, clusters=5):
    arr = base_arr.copy(); n = 16
    for _ in range(clusters):
        cx, cy = rng.integers(2, 13, 2)
        pts = [(cx, cy), (cx + 1, cy), (cx, cy + 1), (cx + 1, cy + 1)]
        for (x, y) in pts:
            arr[y % n, x % n] = c_mid
        arr[cy % n, cx % n] = c_light
        arr[(cy + 1) % n, (cx + 1) % n] = c_dark
        if rng.random() < 0.6: arr[(cy - 1) % n, cx % n] = c_dark
    return arr


@lru_cache(None)
def tex(name):
    rng = np.random.default_rng(abs(hash(name)) % (2 ** 31) if False else sum(map(ord, name)) * 7919)
    stone = _specks(_noise(rng, (122, 122, 124), 9), rng, [(98, 98, 100), (140, 140, 142), (108, 108, 110)], 22)
    deep = _noise(rng, (72, 72, 80), 7)
    for y in range(0, 16, 3):
        deep[y, :, :] = np.clip(deep[y, :, :] - 14, 0, 255)
    deep = _specks(deep, rng, [(58, 58, 66), (88, 88, 96)], 14)
    if name == "stone": a = stone
    elif name == "deepslate": a = deep
    elif name == "dirt": a = _specks(_noise(rng, (134, 96, 67), 10), rng, [(110, 78, 52), (150, 110, 80), (96, 68, 46)], 26)
    elif name == "grass_top": a = _specks(_noise(rng, (96, 166, 58), 12), rng, [(80, 140, 46), (116, 186, 70)], 30)
    elif name == "grass_side":
        a = _specks(_noise(rng, (134, 96, 67), 10), rng, [(110, 78, 52), (150, 110, 80)], 22)
        g = _specks(_noise(rng, (96, 166, 58), 12), rng, [(80, 140, 46), (116, 186, 70)], 10)
        for x in range(16):
            d = 3 + (1 if rng.random() < 0.5 else 0) + (1 if rng.random() < 0.2 else 0)
            a[:d, x] = g[:d, x]
    elif name == "diamond_ore": a = _ore(stone, rng, (18, 140, 132), (88, 232, 218), (200, 255, 250))
    elif name == "deep_diamond_ore": a = _ore(deep, rng, (18, 140, 132), (88, 232, 218), (200, 255, 250))
    elif name == "iron_ore": a = _ore(stone, rng, (150, 110, 84), (216, 176, 148), (240, 214, 196))
    elif name == "gold_ore": a = _ore(stone, rng, (190, 140, 20), (250, 214, 60), (255, 246, 160))
    elif name == "coal_ore": a = _ore(stone, rng, (24, 24, 24), (46, 46, 48), (70, 70, 72))
    elif name == "redstone_ore": a = _ore(stone, rng, (130, 10, 10), (220, 30, 30), (255, 120, 110))
    elif name == "emerald_ore": a = _ore(stone, rng, (10, 120, 50), (40, 210, 100), (170, 255, 200), 4)
    elif name == "bedrock":
        a = _noise(rng, (84, 84, 84), 50)
        a = _specks(a, rng, [(30, 30, 30), (150, 150, 150), (60, 60, 60)], 40)
    elif name == "lava":
        a = _noise(rng, (222, 104, 18), 16)
        a = _specks(a, rng, [(255, 180, 40), (255, 210, 90), (190, 70, 10)], 30, (1, 4))
    elif name == "water": a = _specks(_noise(rng, (48, 92, 210), 10), rng, [(70, 120, 230), (40, 76, 180)], 22, (1, 4))
    elif name == "obsidian": a = _specks(_noise(rng, (22, 16, 34), 6), rng, [(52, 34, 80), (12, 8, 18), (70, 50, 110)], 24, (1, 3))
    elif name == "packed_ice":
        a = _noise(rng, (142, 182, 246), 8)
        for k in range(5):
            y = rng.integers(0, 16); x0 = rng.integers(0, 10)
            a[y, x0:x0 + rng.integers(3, 7)] = (186, 214, 255)
    elif name == "ice":
        a = _noise(rng, (120, 168, 240), 10)
        for k in range(16):
            a[k, (15 - k) % 16] = (200, 226, 255)
        for k in range(10):
            a[k + 3, (15 - k - 6) % 16] = (176, 210, 255)
    elif name == "snow": a = _specks(_noise(rng, (240, 246, 250), 5), rng, [(222, 232, 244), (255, 255, 255)], 20)
    elif name == "calcite": a = _specks(_noise(rng, (222, 224, 220), 6), rng, [(196, 198, 198), (240, 240, 236), (180, 182, 184)], 24)
    elif name in ("snow_bricks", "ice_bricks", "bricks", "stone_bricks"):
        base = {"snow_bricks": (236, 242, 250), "ice_bricks": (150, 190, 248), "bricks": (150, 74, 60), "stone_bricks": (122, 122, 124)}[name]
        a = _noise(rng, base, 6); mort = lerp(base, (0, 0, 0), 0.22)
        for y in (0, 4, 8, 12): a[y, :] = mort
        for r, y0 in enumerate((0, 4, 8, 12)):
            for x in ((0, 8) if r % 2 == 0 else (4, 12)):
                a[y0:y0 + 4, x] = mort
    elif name == "log":
        a = _noise(rng, (104, 80, 48), 8)
        for x in range(0, 16, 3): a[:, x] = (78, 58, 34)
    elif name == "log_top":
        a = np.zeros((16, 16, 3), np.int64) + np.array((160, 128, 80))
        for y in range(16):
            for x in range(16):
                r = max(abs(x - 7.5), abs(y - 7.5))
                if r > 6.5: a[y, x] = (104, 80, 48)
                elif int(r) % 2 == 0: a[y, x] = (136, 106, 62)
    elif name == "leaves":
        a = _specks(_noise(rng, (58, 120, 40), 18), rng, [(36, 84, 26), (82, 150, 56), (28, 66, 20)], 40)
    elif name == "planks":
        a = _noise(rng, (176, 140, 88), 8)
        for y in (3, 7, 11, 15): a[y, :] = (126, 98, 58)
        for (y0, x) in ((0, 5), (4, 11), (8, 3), (12, 9)): a[y0:y0 + 3, x] = (140, 108, 66)
    elif name == "bookshelf":
        a = _noise(rng, (176, 140, 88), 8)
        for y in (0, 1, 7, 8, 14, 15): a[y, :] = (150, 116, 70) if y in (1, 8, 15) else (176, 140, 88)
        cols = [(150, 40, 40), (50, 70, 150), (60, 120, 50), (120, 60, 140), (140, 100, 50), (40, 110, 120)]
        for y0 in (2, 9):
            x = 1
            while x < 15:
                w_ = 1 if rng.random() < 0.6 else 2; c = cols[rng.integers(0, len(cols))]; top = y0 + (1 if rng.random() < 0.3 else 0)
                a[top:y0 + 5, x:x + w_] = c
                a[top, x:x + w_] = tuple(min(255, v + 50) for v in c)
                x += w_ + (1 if rng.random() < 0.25 else 0)
    elif name == "end_stone":
        a = _specks(_noise(rng, (221, 223, 165), 7), rng, [(200, 200, 140), (236, 236, 190), (190, 190, 130)], 30)
    elif name == "portal_top":
        a = _specks(_noise(rng, (56, 104, 92), 8), rng, [(40, 84, 74), (80, 130, 116)], 20)
        a[4:12, 4:12] = (22, 44, 40); a[5:11, 5:11] = (14, 30, 28)
    elif name == "portal_side":
        a = _specks(_noise(rng, (221, 223, 165), 7), rng, [(200, 200, 140), (236, 236, 190)], 20)
        a[:5, :] = _noise(rng, (56, 104, 92), 8)[:5, :]
        a[5, :] = (36, 70, 62)
    elif name in ("netherrack", "nether_quartz_ore", "nether_gold_ore"):
        a = _specks(_noise(rng, (112, 36, 36), 10), rng, [(84, 22, 24), (140, 54, 50), (70, 16, 18)], 34)
        if name == "nether_quartz_ore": a = _ore(a, rng, (200, 190, 180), (236, 230, 222), (255, 255, 255))
        if name == "nether_gold_ore": a = _ore(a, rng, (190, 140, 20), (250, 214, 60), (255, 246, 160), 6)
    elif name == "glowstone":
        a = _specks(_noise(rng, (232, 190, 104), 14), rng, [(255, 236, 160), (190, 140, 70), (255, 214, 120)], 40, (1, 3))
    elif name == "soul_sand":
        a = _specks(_noise(rng, (84, 64, 52), 8), rng, [(62, 46, 38), (104, 82, 66)], 30)
    elif name in ("debris_side", "debris_top"):
        a = _specks(_noise(rng, (128, 90, 78), 8), rng, [(150, 112, 98), (96, 64, 56)], 20)
        if name == "debris_side":
            for (cx, cy, r) in ((5, 5, 3), (11, 11, 3), (12, 3, 2), (3, 12, 2)):
                for y in range(16):
                    for x in range(16):
                        if abs(math.hypot(x - cx, y - cy) - r) < 0.6: a[y, x] = (72, 46, 40)
        else:
            for y in range(16):
                for x in range(16):
                    rr = max(abs(x - 7.5), abs(y - 7.5))
                    if int(rr) % 3 == 0: a[y, x] = (82, 54, 46)
    elif name == "sand": a = _specks(_noise(rng, (222, 210, 160), 8), rng, [(204, 190, 140), (236, 226, 182)], 30)
    elif name == "crystal":
        a = _noise(rng, (110, 220, 255), 14)
        for k in range(16): a[k, k] = (230, 255, 255)
    else:
        a = stone
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGB")


def tile(name, size):
    return tex(name).resize((size, size), Image.NEAREST)


# ================================================================ cubo isométrico 3D
def _persp_coeffs(dst, src):
    A = []; B = []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


FACES = {  # cara: (normal, esquinas en orden tl, tr, br, bl vistas desde fuera)
    "top": ((0, 1, 0), [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)]),
    "+z": ((0, 0, 1), [(-1, 1, 1), (1, 1, 1), (1, -1, 1), (-1, -1, 1)]),
    "+x": ((1, 0, 0), [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)]),
    "-z": ((0, 0, -1), [(1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)]),
    "-x": ((-1, 0, 0), [(-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (-1, -1, -1)]),
}


def cube(top, side=None, size=300, yaw=45.0, pitch=30.0, glow=None):
    """Render de un bloque con texturas `top`/`side` (nombres de tex()). Devuelve RGBA size x size."""
    side = side or top
    ss = 2; N = size * ss
    out = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    cy, sy = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    cp, sp = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    sc = N / 2 / 1.75

    def proj(p):
        x, y, z = p
        x, z = x * cy - z * sy, x * sy + z * cy           # yaw
        y, z = y * cp - z * sp, y * sp + z * cp           # pitch (cámara mirando desde arriba)
        return (N / 2 + x * sc, N / 2 - y * sc), z

    T = 128
    faces = []
    for fname, (nrm, corners) in FACES.items():
        _, nz = proj(nrm)
        n0 = proj((0, 0, 0))[1]
        depth = nz - n0
        if depth <= 0.01:
            continue
        pts = [proj(c)[0] for c in corners]
        faces.append((depth, fname, pts))
    faces.sort()
    for depth, fname, pts in faces:
        t = tex(top if fname == "top" else side).resize((T, T), Image.NEAREST).convert("RGBA")
        shade = 1.0 if fname == "top" else (0.80 if fname in ("+x", "-x") else 0.62)
        if fname != "top":
            nx = {"+z": (0, 1), "+x": (1, 0), "-z": (0, -1), "-x": (-1, 0)}[fname]
            light = 0.5 + 0.5 * (nx[0] * 0.6 - nx[1] * 0.3 + 0.5)
            shade = 0.55 + 0.33 * max(0.0, min(1.0, light))
        t = Image.fromarray((np.array(t).astype(np.float32) * [shade, shade, shade, 1]).clip(0, 255).astype(np.uint8), "RGBA")
        co = _persp_coeffs(pts, [(0, 0), (T, 0), (T, T), (0, T)])
        warped = t.transform((N, N), Image.PERSPECTIVE, co, resample=Image.NEAREST)
        m = Image.new("L", (N, N), 0); ImageDraw.Draw(m).polygon(pts, fill=255)
        warped.putalpha(m)
        out.alpha_composite(warped)
        ImageDraw.Draw(out).line(pts + [pts[0]], fill=(0, 0, 0, 70), width=ss * 2)
    out = out.resize((size, size), Image.LANCZOS)
    if glow:
        out = add_glow(out, glow, r=size // 10, k=1.0)
        out = out.crop(((out.width - size) // 2, (out.height - size) // 2, (out.width + size) // 2, (out.height + size) // 2))
    return out


@lru_cache(None)
def cube_spin(top, side, size, n=24):
    """Fotogramas de un giro de 90º (el cubo es simétrico, así el bucle es perfecto)."""
    return [cube(top, side, size, yaw=45 + 90 * i / n) for i in range(n)]


# ================================================================ sprites pixel art (diseño propio)
def _grid(n=16):
    return np.zeros((n, n, 4), np.uint8)


def _put(g, x, y, c):
    if 0 <= x < g.shape[1] and 0 <= y < g.shape[0]:
        g[y, x] = tuple(c) + (255,)


def _outline(g, col=(20, 18, 24)):
    a = g[:, :, 3] > 0
    nb = np.zeros_like(a)
    nb[1:, :] |= a[:-1, :]; nb[:-1, :] |= a[1:, :]; nb[:, 1:] |= a[:, :-1]; nb[:, :-1] |= a[:, 1:]
    edge = nb & ~a
    g[edge] = tuple(col) + (255,)
    return g


def _from_map(rows, pal):
    h = len(rows); w = max(len(r) for r in rows)
    g = np.zeros((h, w, 4), np.uint8)
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch in pal:
                g[y, x] = tuple(pal[ch]) + (255,)
    return g


def _pad(g, n=18):
    h, w = g.shape[:2]; out = np.zeros((n, n, 4), np.uint8)
    oy, ox = (n - h) // 2, (n - w) // 2
    out[oy:oy + h, ox:ox + w] = g
    return out


def _tool_head(g, cols, kind):
    m, l, d = cols
    if kind == "pick":
        arc = [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 3), (13, 4),
               (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11)]
        inner = [(6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9)]
        for p in arc: _put(g, *p, l)
        for p in inner: _put(g, *p, m)
        for p in [(4, 2), (13, 11), (5, 3), (12, 10)]: _put(g, *p, d)
        _put(g, 11, 4, d); _put(g, 12, 3, m)
    elif kind == "sword":
        for i in range(8):
            _put(g, 6 + i, 9 - i, l); _put(g, 7 + i, 9 - i, m); _put(g, 6 + i, 10 - i, d)
        _put(g, 14, 1, l); _put(g, 14, 2, m)


def sprite_tool(kind, material="diamond"):
    mats = {"diamond": ((74, 222, 206), (170, 255, 240), (24, 140, 130)),
            "iron": ((206, 206, 210), (250, 250, 250), (130, 130, 136)),
            "gold": ((250, 210, 60), (255, 246, 160), (190, 140, 20)),
            "stone": ((130, 130, 130), (170, 170, 170), (90, 90, 90)),
            "netherite": ((76, 66, 72), (120, 108, 116), (44, 38, 42))}[material]
    g = _grid(16)
    wood, woodd = (150, 108, 60), (100, 70, 38)
    if kind == "pick":
        for i in range(10):
            _put(g, 2 + i, 13 - i, wood); _put(g, 3 + i, 13 - i, woodd)
        _tool_head(g, mats, "pick")
    else:  # espada
        _tool_head(g, mats, "sword")
        for (x, y) in [(3, 8), (4, 9), (5, 10), (6, 11), (7, 12)]: _put(g, x, y, mats[2])
        for (x, y) in [(4, 8), (5, 9), (6, 10), (7, 11)]: _put(g, x, y, mats[0])
        for (x, y) in [(4, 11), (3, 12), (2, 13)]: _put(g, x, y, wood)
        _put(g, 1, 14, mats[0])
    return _outline(_pad(g))


SPRITE_MAPS = {
    "diamond": (["....kkkkkk....", "...kwllmmmk...", "..kwlllmmmdk..", ".kwllllmmmmdk.", "kkkkkkkkkkkkkk",
                 ".kllmmmmmmmdk.", "..kllmmmmmdk..", "...klmmmmdk...", "....klmmdk....", ".....klmdk....", "......kdk.....", ".......k......"],
                dict(k=(14, 70, 66), w=(235, 255, 252), l=(160, 250, 236), m=(74, 222, 206), d=(30, 150, 140))),
    "emerald": (["....kkkk....", "...kwllmk...", "..kwllmmdk..", ".kwlllmmmdk.", ".klllmmmmdk.", ".kllmmmmmdk.", ".klmmmmmmdk.",
                 "..klmmmmdk..", "...klmmdk...", "....kkkk...."],
                dict(k=(8, 60, 24), w=(220, 255, 230), l=(110, 240, 150), m=(40, 200, 96), d=(16, 130, 56))),
    "heart": ([".kk.kk.", "kwrkrrk", "krrrrrk", "krrrrrk", ".krrrk.", "..krk..", "...k..."],
              dict(k=(40, 4, 8), w=(255, 220, 220), r=(230, 30, 40))),
    "torch": (["..y..", ".yoy.", ".oro.", ".yoy.", "..w..", "..w..", "..d..", "..w..", "..d..", "..w..", "..d.."],
              dict(y=(255, 230, 90), o=(255, 150, 30), r=(255, 255, 220), w=(150, 108, 60), d=(100, 70, 38))),
    "apple": (["....g...", "...gb...", ".rrbrrr.", "rwrrrrrr", "rwrrrrrr", "rrrrrrrd", "rrrrrrrd", ".rrrrdd.", "..r..d.."],
              dict(g=(70, 160, 50), b=(90, 60, 30), r=(220, 30, 36), w=(255, 160, 160), d=(150, 16, 20))),
    "bucket_water": (["kkkkkkkkkk", "kbbwbbbbbk", "kbbbbbbbbk", ".kssssssk.", ".ksllsssk.", ".ksssssdk.", "..kssssk..", "..kkkkkk.."],
                     dict(k=(40, 40, 46), b=(60, 110, 230), w=(160, 200, 255), s=(190, 190, 196), l=(240, 240, 244), d=(130, 130, 136))),
    "bucket_lava": (["kkkkkkkkkk", "kooyoooook", "kooooooook", ".kssssssk.", ".ksllsssk.", ".ksssssdk.", "..kssssk..", "..kkkkkk.."],
                    dict(k=(40, 40, 46), o=(240, 110, 20), y=(255, 210, 80), s=(190, 190, 196), l=(240, 240, 244), d=(130, 130, 136))),
    "iceball": ([".kkkk.", "kwllmk", "kllmmk", "klmmdk", "kmmddk", ".kkkk."],
                dict(k=(40, 80, 140), w=(255, 255, 255), l=(210, 236, 255), m=(150, 200, 250), d=(100, 150, 220))),
    "icicle": (["kkkkkkk", "kwllmdk", "kwlmmdk", ".klmdk.", ".klmdk.", ".kwmdk.", "..kmk..", "..kmk..", "..kdk..", "...k..."],
               dict(k=(40, 80, 140), w=(255, 255, 255), l=(210, 236, 255), m=(150, 200, 250), d=(100, 150, 220))),
    "crystal": (["....w......", "...klk.....", "...klk..w..", ".w.klk.klk.", "klk.lmk.klk", "klk.lmk.lmk", "klmklmk.lmk", "klmklmkklmk", "klmklmkklmk", "kkkkkkkkkkk"],
                dict(k=(20, 90, 130), w=(255, 255, 255), l=(170, 240, 255), m=(90, 210, 250), d=(40, 150, 210))),
    "potion": (["...kkk...", "...kck...", "...kgk...", "..kgggk..", ".kpwppppk", "kppwppppk", "kpppppppk", "kpppppddk", ".kpppddk.", "..kkkkk.."],
               dict(k=(30, 30, 40), c=(150, 108, 60), g=(200, 220, 255), w=(255, 255, 255), p=(110, 190, 255), d=(60, 120, 220))),
    "disc": (["...kkkkk...", ".kkddddkk..", ".kdddddddk.", "kddddddwddk", "kddkrrkdwdk", "kddrkkrdddk", "kddkrrkdddk", "kdddddddddk",
              ".kdddddddk.", "..kkdddkk..", "....kkk...."],
             dict(k=(10, 10, 12), d=(40, 40, 48), w=(110, 110, 120), r=(80, 220, 240))),
    "compass": ([".kkkkkk.", "kssssssk", "ksgwrgsk", "ksgrwgsk", "ksgwrgsk", "ksgggg sk".replace(" ", ""), "kssssssk", ".kkkkkk."],
                dict(k=(30, 30, 36), s=(190, 190, 196), g=(80, 80, 90), w=(240, 240, 240), r=(220, 40, 40))),
    "book": (["kkkkkkkkk", "kppppppwk", "kpyyypppk", "kpppppppk", "kppyyyppk", "kpppppppk", "kpppppppk", "kddddddwk", "kkkkkkkkk"],
             dict(k=(30, 10, 40), p=(130, 60, 200), y=(255, 214, 64), d=(90, 30, 150), w=(240, 240, 240))),
    "bed": (["..........", "wwwwrrrrrr", "wwwwrrrrrr", "kkkkkkkkkk", "p........p", "p........p"],
            dict(w=(240, 240, 240), r=(200, 30, 40), k=(120, 20, 26), p=(150, 108, 60))),
    "shield": (["kkkkkkkk", "kwwwwwwk", "kwppppwk", "kwppppwk", "kwppppwk", "kwppppwk", ".kwppwk.", "..kwwk..", "...kk..."],
               dict(k=(40, 30, 20), w=(150, 150, 156), p=(150, 108, 60))),
    "tnt_crate": (["kkkkkkkkkk", "krrrrrrrrk", "kwwwwwwwwk", "kwkkwkkwwk", "kwwwwwwwwk", "krrrrrrrrk", "kkkkkkkkkk"],
                  dict(k=(60, 10, 10), r=(210, 40, 36), w=(230, 230, 230))),
    "frostbite": (["hhhhhhhhhh", "hwhhwhhhwh", "hssssssssh", "ssssssssss", "skkssskkss", "skbsssbkss", "ssssssssss",
                   "sssdddssss", "ssdkkkddss", "ssssssssss"],
                  dict(h=(232, 244, 255), w=(255, 255, 255), s=(126, 170, 196), k=(18, 30, 50), b=(120, 220, 255), d=(90, 130, 160))),
    "zombie_gen": (["hhhhhhhhhh", "hhhhhhhhhh", "ssssssssss", "skkssssskk", "skwssssskw", "ssssssssss", "sssddsssss",
                    "ssdkkkdsss", "ssssssssss", "ssssssssss"],
                   dict(h=(60, 90, 50), s=(96, 140, 80), k=(20, 26, 18), w=(200, 40, 40), d=(70, 104, 60))),
    "skull": ([".kkkkkkkk.", "kwwwwwwwwk", "kwwwwwwwwk", "kwkkwwkkwk", "kwkkwwkkwk", "kwwwkkwwwk", ".kwwwwwwk.", ".kwkwkwkk.", "..kkkkkk.."],
              dict(k=(30, 30, 34), w=(230, 230, 220))),
    "xp": ([".kkkk.", "kyglyk", "kgllgk", "kgllgk", "kyggyk", ".kkkk."],
           dict(k=(40, 80, 10), y=(230, 255, 120), g=(130, 230, 40), l=(220, 255, 160))),
    "clock": ([".kkkkkk.", "kyyyyyyk", "kybbbbyk", "kybwbbyk", "kyrrrryk", "kyyyyyyk", ".kkkkkk."],
              dict(k=(60, 40, 10), y=(250, 210, 60), b=(60, 110, 230), w=(255, 255, 160), r=(30, 120, 40))),
    "boots": (["kkkkk.....", "kwllk.....", "klmmk.....", "klmmk.....", "klmmk.....", "klmmkkkkk.", "klmmmmmlk.", "kmmmmmmmmk", "kddddddddk", "kkkkkkkkkk"],
              dict(k=(14, 70, 66), w=(235, 255, 252), l=(160, 250, 236), m=(74, 222, 206), d=(30, 150, 140))),
    "chestplate": (["kkkk....kkkk", "kllmkkkkmmdk", "klmmmllmmmdk", "kkmmmlmmmmkk", ".kmmmlmmmdk.", ".kmmmlmmmdk.", ".kmmmmmmmdk.", ".kmmmmmmmdk.", ".kkkkkkkkkk."],
                   dict(k=(14, 70, 66), l=(160, 250, 236), m=(74, 222, 206), d=(30, 150, 140))),
    "bow": (["ww.....", "sww....", "s.ww...", "s..ww..", "s...ww.", "s...ww.", "s...ww.", "s...ww.", "s..ww..", "s.ww...", "sww....", "ww....."],
            dict(w=(150, 108, 60), s=(225, 225, 225))),
    "lectern": ([".......kkk", ".....kkwwk", "...kkwwwpk", ".kkwwwpppk", "kppppppPk.", "kkkkpPkk..", "...kpPk...", "...kpPk...", ".kkkpPkkk.", ".kppppppk.", ".kkkkkkkk."],
                dict(k=(60, 40, 20), w=(240, 236, 220), p=(176, 140, 88), P=(126, 98, 58))),
    "ender_pearl": ([".kkkk.", "kmllmk", "kmlmdk", "kmmmdk", "kmmddk", ".kkkk."],
                    dict(k=(10, 40, 40), l=(80, 220, 190), m=(20, 120, 108), d=(10, 74, 66))),
    "eye_ender": (["..kkkk..", ".kgllgk.", "kgggggdk", "kggppgdk", "kggppgdk", "kgggggdk", ".kgggdk.", "..kkkk.."],
                  dict(k=(10, 34, 22), g=(64, 176, 124), l=(160, 244, 196), d=(30, 104, 72), p=(12, 20, 16))),
    "blaze_powder": (["....y....", "...yoy...", "..yooy.y.", ".yoooyoy.", "yooroooy.", "yoooooooy"],
                     dict(y=(255, 222, 80), o=(240, 142, 30), r=(200, 80, 20))),
    "pumpkin": (["....bg....", ".oooooooo.", "oooooooooo", "ookkookkoo", "ookkookkoo", "oooooooooo", "okkkkkkkko", "ooookkoooo", ".oooooooo."],
                dict(o=(232, 132, 22), k=(60, 30, 0), g=(70, 150, 40), b=(110, 76, 30))),
    "end_crystal": (["...kk...", "..kwpk..", ".kwppPk.", "kwpppPPk", "kpppPPPk", ".kpPPPk.", "..kPPk..", "...kk..."],
                    dict(k=(60, 10, 50), w=(255, 230, 250), p=(240, 120, 200), P=(190, 60, 160))),
    "nether_portal": (["oooooo", "oppPpo", "oPpppo", "oppPpo", "opPppo", "oppPpo", "oPpppo", "oooooo"],
                      dict(o=(34, 22, 52), p=(140, 60, 220), P=(196, 130, 255))),
    "gold_ingot": (["..kkkkkkk.", ".kllllllmk", "kllmmmmmdk", "kmmmmmmddk", "kkkkkkkkk."],
                   dict(k=(120, 80, 10), l=(255, 246, 160), m=(250, 210, 60), d=(190, 140, 20))),
    "netherite_ingot": (["..kkkkkkk.", ".kllllllmk", "kllmmmmmdk", "kmmmmmmddk", "kkkkkkkkk."],
                        dict(k=(16, 12, 14), l=(132, 118, 126), m=(80, 70, 76), d=(46, 40, 44))),
    "potion_fire": (["...kkk...", "...kck...", "...kgk...", "..kgggk..", ".kpwppppk", "kppwppppk", "kpppppppk", "kpppppddk", ".kpppddk.", "..kkkkk.."],
                    dict(k=(30, 30, 40), c=(150, 108, 60), g=(200, 220, 255), w=(255, 255, 255), p=(255, 150, 40), d=(220, 90, 20))),
    "hourglass": (["kkkkkkkkk", "kwwwwwwwk", ".kyyyyyk.", "..kyyyk..", "...kyk...", "...kyk...", "..kgygk..", ".kggyggk.", "kgyyyyygk", "kwwwwwwwk", "kkkkkkkkk"],
                  dict(k=(40, 26, 12), w=(150, 108, 60), y=(240, 200, 90), g=(200, 230, 255))),
    "map": (["kkkkkkkkkk", "kppppppppk", "kpggpbbppk", "kpgggpbbpk", "kppgpppbpk", "kpbbppggpk", "kppbbpgppk", "kppppppppk", "kkkkkkkkkk"],
            dict(k=(70, 50, 20), p=(230, 210, 160), g=(90, 160, 60), b=(70, 120, 220))),
    "carrot_gold": (["......gg", ".....gg.", "....yy..", "...yyy..", "..ywy...", ".yyy....", "yyy.....", "y......."],
                    dict(g=(60, 160, 40), y=(250, 205, 40), w=(255, 250, 190))),
    "arrow_down": (["..kkk..", "..kgk..", "..kgk..", "kkkgkkk", ".kgggk.", "..kgk..", "...k..."],
                   dict(k=(20, 20, 20), g=GOLD)),
}


@lru_cache(None)
def sprite(name, S=256, outline=True):
    if name.startswith("pick_"): g = sprite_tool("pick", name[5:])
    elif name.startswith("sword_"): g = sprite_tool("sword", name[6:])
    else:
        rows, pal = SPRITE_MAPS[name]
        g = _from_map(rows, pal)
        n = max(g.shape[0], g.shape[1]) + 2
        g = _pad(g, n)
        if outline and name not in ("frostbite", "zombie_gen"):
            g = _outline(g)
    im = Image.fromarray(g, "RGBA")
    return im.resize((S, int(S * im.height / im.width)), Image.NEAREST)


# ================================================================ fondos animados
def crop_wrap(img, off, w):
    off %= img.width
    if off + w <= img.width:
        return img.crop((off, 0, off + w, img.height))
    a = img.crop((off, 0, img.width, img.height)); b = img.crop((0, 0, w - a.width, img.height))
    out = Image.new(img.mode, (w, img.height)); out.paste(a, (0, 0)); out.paste(b, (a.width, 0))
    return out


def _tint(im, col, k):
    ov = Image.new("RGBA", im.size, col + (int(255 * k),))
    out = im.copy(); out.alpha_composite(Image.composite(ov, Image.new("RGBA", im.size, (0, 0, 0, 0)), im.getchannel("A")))
    return out


def terrain_strip(period, B, base_y, amp, seed, trees=True, hcount=None, kind="grass"):
    """Franja periódica de terreno de bloques (para scroll infinito)."""
    rnd = random.Random(seed)
    cols = period // B
    ph = [rnd.random() * 6.28 for _ in range(3)]
    ks = [1, 3, 7]
    hs = []
    for c in range(cols):
        t = c / cols * 2 * math.pi
        v = sum(math.sin(k * t + p) / (i + 1) for i, (k, p) in enumerate(zip(ks, ph)))
        hs.append(int(round(base_y + v * amp)))
    hh = hcount or 18
    img = Image.new("RGBA", (period, hh * B), (0, 0, 0, 0))
    T = {n: tile(n, B).convert("RGBA") for n in ("grass_side", "dirt", "stone", "log", "leaves", "deepslate", "coal_ore", "iron_ore", "end_stone", "obsidian")}
    for c, h in enumerate(hs):
        top = hh - h
        for r in range(top, hh):
            depth = r - top
            if kind == "end":
                n = "end_stone"
            else:
                n = "grass_side" if depth == 0 else ("dirt" if depth < 3 else ("stone" if rnd.random() > 0.06 else rnd.choice(["coal_ore", "iron_ore"])))
            img.alpha_composite(T[n], (c * B, r * B))
        if kind == "end" and trees and rnd.random() < 0.07 and 2 < c < cols - 3:
            ph_ = rnd.randint(5, min(11, top))
            for k in range(1, ph_ + 1):
                img.alpha_composite(T["obsidian"], (c * B, (top - k) * B)); img.alpha_composite(T["obsidian"], ((c + 1) * B, (top - k) * B))
            continue
        if trees and rnd.random() < 0.09 and 2 < c < cols - 3:
            th_ = rnd.randint(3, 5)
            for k in range(1, th_ + 1):
                img.alpha_composite(T["log"], (c * B, (top - k) * B))
            for dx in range(-2, 3):
                for dy in range(th_ - 1, th_ + 3):
                    if abs(dx) == 2 and dy >= th_ + 1: continue
                    if dx == 0 and dy < th_ + 1: continue
                    if rnd.random() < 0.92:
                        img.alpha_composite(T["leaves"], ((c + dx) * B, (top - dy) * B))
    return img


class Background:
    def __init__(self, theme, seed=1, w=W, h=H):
        self.w, self.h = w, h
        self.theme = theme; self.seed = seed; rnd = random.Random(seed)
        self.parts = []
        if theme in ("superficie", "noche", "end"):
            night = theme in ("noche", "end"); end = theme == "end"
            sky = vgrad(self.w, self.h, [(4, 2, 10), (18, 8, 32), (46, 20, 66)] if end else ([(14, 18, 52), (34, 40, 96), (70, 60, 120)] if night else [(84, 140, 240), (138, 186, 255), (200, 226, 255)]))
            self.base = sky.convert("RGBA")
            d = ImageDraw.Draw(self.base)
            if night:
                for _ in range(220):
                    x, y = rnd.randint(0, self.w), rnd.randint(0, 620); s = rnd.choice([3, 3, 4, 6])
                    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255, rnd.randint(120, 255)))
                mx, my = int(self.w * 0.76), 120
                if not end:
                    d.rectangle([mx, my, mx + 130, my + 130], fill=(236, 236, 214, 255))
                    for (a, b, s) in [(20, 30, 26), (80, 70, 20), (40, 90, 16)]:
                        d.rectangle([mx + a, my + b, mx + a + s, my + b + s], fill=(200, 200, 182, 255))
            else:
                sun = Image.new("RGBA", (180, 180), (255, 246, 160, 255)); ImageDraw.Draw(sun).rectangle([30, 30, 150, 150], fill=(255, 255, 220, 255))
                sun = add_glow(sun, (255, 240, 150), 40, 0.8); self.base.alpha_composite(sun, (int(self.w * 0.73) - 40, 70 - 80))
            fogc = (50, 24, 80) if end else ((60, 60, 120) if night else (170, 205, 255))
            kind = "end" if end else "grass"
            far = terrain_strip(self.w * 2, 40, 7, 3, seed + 1, trees=True, hcount=18 if end else 14, kind=kind)
            self.far = _tint(far, fogc, 0.55 if not night else 0.62)
            near = terrain_strip(self.w * 2, 72, 4, 2, seed + 2, trees=not end, hcount=10, kind=kind)
            self.near = _tint(near, (20, 0, 40) if end else (10, 10, 40), 0.3 if end else 0.35) if night else near
            self.clouds = Image.new("RGBA", (self.w * 2, 300), (0, 0, 0, 0)); cd = ImageDraw.Draw(self.clouds)
            for _ in range(14):
                cx, cy = rnd.randint(0, self.w * 2 - 400), rnd.randint(20, 220)
                for _ in range(rnd.randint(2, 4)):
                    w_, h_ = rnd.randint(4, 9) * 24, rnd.randint(2, 3) * 24; ox = rnd.randint(-3, 3) * 24
                    if not end: cd.rectangle([cx + ox, cy, cx + ox + w_, cy + h_], fill=(255, 255, 255, 120 if night else 215))
            self.mode = "sky"
        else:
            ice = theme == "hielo"
            B = 96
            nether = theme == "nether"
            names = (["packed_ice"] * 6 + ["ice"] * 2 + ["snow", "calcite"]) if ice else (
                (["netherrack"] * 9 + ["nether_quartz_ore", "nether_gold_ore", "glowstone", "soul_sand", "soul_sand"]) if nether else
                (["stone"] * 7 + ["deepslate"] * 4 + ["coal_ore", "iron_ore", "deep_diamond_ore", "gold_ore", "redstone_ore"]))
            wall = Image.new("RGBA", (self.w + B * 8, self.h + B), (0, 0, 0, 255))
            for y in range(0, self.h + B, B):
                for x in range(0, self.w + B * 8, B):
                    wall.alpha_composite(tile(rnd.choice(names), B).convert("RGBA"), (x, y))
            # oscurecer con viñeta y luz cálida/fría
            dark = Image.new("RGBA", wall.size, ((6, 14, 30) if ice else ((22, 4, 4) if nether else (6, 6, 10))) + (150 if ice else 175,))
            wall.alpha_composite(dark)
            light = Image.new("L", wall.size, 0); ld = ImageDraw.Draw(light)
            for _ in range(6):
                x, y = rnd.randint(0, wall.width), rnd.randint(100, self.h)
                r = rnd.randint(220, 380); ld.ellipse([x - r, y - r, x + r, y + r], fill=90 if ice else 110)
            light = light.filter(ImageFilter.GaussianBlur(120))
            lc = Image.new("RGBA", wall.size, (120, 200, 255) if ice else (255, 150, 60)); lc.putalpha(light)
            wall.alpha_composite(lc)
            self.wall = wall
            self.mode = "ice" if ice else "cave"
            # carámbanos arriba / resplandor de lava abajo
            if ice:
                self.top = Image.new("RGBA", (self.w * 2, 260), (0, 0, 0, 0))
                for x in range(0, self.w * 2, 60):
                    if rnd.random() < 0.6:
                        s = sprite("icicle", rnd.choice([60, 72, 90, 120]))
                        self.top.alpha_composite(s, (x + rnd.randint(-10, 10), -rnd.randint(0, 20) if False else 0))
                self.crystals = [(rnd.randint(40, self.w - 120), rnd.randint(500, self.h - 150), rnd.choice([60, 80, 100]), rnd.random() * 6) for _ in range(9)]
                self.cry = {s: add_glow(sprite("crystal", s), (120, 220, 255), 18, 1.2) for s in (60, 80, 100)}
            else:
                self.lava = Image.new("RGBA", (self.w * 2, 96), (0, 0, 0, 0))
                for x in range(0, self.w * 2, 48): self.lava.alpha_composite(tile("lava", 48).convert("RGBA"), (x, 48)); self.lava.alpha_composite(tile("lava", 48).convert("RGBA"), (x, 0))
                gl = Image.new("RGBA", (self.w, 420), (0, 0, 0, 0))
                ga = vgrad(1, 420, [(0, 0, 0), (255, 255, 255)]).convert("L").resize((self.w, 420))
                g2 = Image.new("RGBA", (self.w, 420), (255, 110, 20, 0)); g2.putalpha(ga.point(lambda v: int(v * 0.42)))
                self.lava_glow = g2
        self.parts = [(rnd.random() * self.w, rnd.random() * self.h, rnd.uniform(0.3, 1.0), rnd.choice([4, 6, 8])) for _ in range(70)]

    def frame(self, t):
        if self.mode == "sky":
            im = self.base.copy()
            c = crop_wrap(self.clouds, int(t * 18), self.w); im.alpha_composite(c, (0, 0))
            f = crop_wrap(self.far, int(t * 12), self.w); im.alpha_composite(f, (0, self.h - f.height + 40))
            n = crop_wrap(self.near, int(t * 34), self.w); im.alpha_composite(n, (0, self.h - n.height + 300))
            if self.theme in ("noche", "end"):
                d = ImageDraw.Draw(im)
                for (x, y, sp, s) in self.parts[:25]:
                    yy = (y * 0.5 + 520 + math.sin(t * sp * 2 + x) * 30); xx = (x + t * 20 * sp) % self.w
                    a = int(140 + 110 * math.sin(t * 3 * sp + x))
                    d.rectangle([xx, yy, xx + s, yy + s], fill=((210, 140, 255) if self.theme == "end" else (200, 255, 120)) + (max(0, a),))
            return im.convert("RGB")
        off = int(t * 16) % (self.wall.width - self.w)
        oy = int(30 + math.sin(t * 0.25) * 30)
        im = self.wall.crop((off, oy, off + self.w, oy + self.h)).copy()
        d = ImageDraw.Draw(im)
        if self.mode == "ice":
            top = crop_wrap(self.top, int(t * 16), self.w); im.alpha_composite(top, (0, 0))
            for (x, y, s, ph) in self.crystals:
                g = self.cry[s]; k = 0.6 + 0.4 * math.sin(t * 2 + ph)
                gg = g.copy(); gg.putalpha(g.getchannel("A").point(lambda v, k=k: int(v * k)))
                im.alpha_composite(gg, (int(x - (off % 400) * 0) - g.width // 2, y - g.height // 2))
            for (x, y, sp, s) in self.parts:
                yy = (y + t * 60 * sp) % self.h; xx = (x + math.sin(t * sp + y) * 30) % self.w
                d.rectangle([xx, yy, xx + s, yy + s], fill=(255, 255, 255, int(150 * sp)))
        else:
            lv = crop_wrap(self.lava, int(t * 10), self.w); im.alpha_composite(lv, (0, self.h - 96))
            k = 0.8 + 0.2 * math.sin(t * 2.2)
            g = self.lava_glow.copy(); g.putalpha(self.lava_glow.getchannel("A").point(lambda v: int(v * k)))
            im.alpha_composite(g, (0, self.h - 420 - 60))
            for (x, y, sp, s) in self.parts:
                yy = (y - t * 30 * sp) % self.h; xx = (x + math.sin(t * sp + y) * 20) % self.w
                d.rectangle([xx, yy, xx + s // 2 + 1, yy + s // 2 + 1], fill=(255, 190, 90, int(160 * sp)))
        return im.convert("RGB")


def glint_frames(im, n=24, col=(190, 110, 255), k=0.6):
    """Brillo diagonal morado que recorre un sprite (aspecto de objeto encantado)."""
    a = np.array(im.getchannel("A"), dtype=np.float32) / 255.0
    h, w = a.shape; yy, xx = np.mgrid[0:h, 0:w]
    diag = (xx + yy) / float(w + h)
    out = []
    for i in range(n):
        c = (i / n) * 1.6 - 0.3
        band = np.clip(1 - np.abs(diag - c) / 0.12, 0, 1) + 0.18
        ov = np.zeros((h, w, 4), np.uint8); ov[..., 0], ov[..., 1], ov[..., 2] = col
        ov[..., 3] = (np.clip(band, 0, 1) * a * 255 * k).astype(np.uint8)
        f = im.copy(); f.alpha_composite(Image.fromarray(ov, "RGBA")); out.append(f)
    return out
