# -*- coding: utf-8 -*-
"""Miniaturas (1280x720), banner (2560x1440), avatar (800x800) y metadatos de YouTube.

Uso:  python3 branding.py [prefijo ...]     -> miniaturas + metadatos de esos vídeos (o de todos)
      python3 branding.py canal             -> banner, avatar y descripción del canal
"""
import json, os, sys
from PIL import Image, ImageDraw
import art
from art import THEMES, GOLD, WHITE, INK, text_img, add_glow, bevel_box, label_box, sprite, cube, SILK, MX, MB
from content import VIDEOS, CHANNEL, HANDLE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TH = os.path.join(ROOT, "miniaturas"); CAN = os.path.join(ROOT, "canal"); META = os.path.join(ROOT, "metadatos")


def hero_img(spec, size):
    if spec[0] == "cube":
        return cube(spec[1], spec[2] if len(spec) > 2 else None, size)
    return sprite(spec[1], size)


def thumb(v):
    th = THEMES[v["theme"]]; t = v["thumb"]; acc = th["acc"]
    im = art.Background(v["theme"], seed=5).frame(2.0).resize((1280, 720), Image.LANCZOS).convert("RGBA")
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    for x in range(820):
        d.line([(x, 0), (x, 720)], fill=(0, 0, 0, int(205 * (1 - x / 820) ** 1.2)))
    im.alpha_composite(sh)
    # héroe grande a la derecha (y un segundo más pequeño)
    h1 = add_glow(hero_img(t["hero"], 470 if t["hero"][0] == "cube" else 420), acc, 34, 1.1)
    im.alpha_composite(h1, (1280 - h1.width + 40, 360 - h1.height // 2 + 30))
    if t.get("hero2"):
        h2 = add_glow(hero_img(t["hero2"], 230), GOLD if t["hero2"][0] == "sprite" else acc, 20, 1.0)
        im.alpha_composite(h2, (1280 - h1.width - 40, 720 - h2.height - 10))
    y = 30
    if t.get("top"):
        b = label_box(t["top"], SILK, 38, fill=GOLD, fg=INK, padx=22, pady=12)
        im.alpha_composite(b, (36, y)); y += b.height + 10
    lines = t["big"].split("\n"); size = 150
    while True:
        imgs = [text_img(l, SILK, size, fill=WHITE, outline=8, shadow_col=(0, 0, 0)) for l in lines]
        gap = max(4, size // 18)
        hh = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
        if max(i.width for i in imgs) <= 800 and hh <= 430: break
        size = int(size * 0.94)
    yy = y
    for li in imgs:
        im.alpha_composite(li, (26, yy)); yy += li.height + gap
    y += hh
    if t.get("tag"):
        tg = label_box(t["tag"], SILK, 46, fill=acc, fg=INK, padx=26, pady=14, b=8)
        tg = tg.rotate(3, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(tg, (36, min(720 - tg.height - 24, y + 4)))
    os.makedirs(TH, exist_ok=True)
    im.convert("RGB").save(os.path.join(TH, v["slug"] + ".jpg"), quality=92)


def banner():
    th = THEMES["superficie"]
    bg = art.Background("superficie", seed=9).frame(3.0).resize((2560, 1440), Image.LANCZOS).convert("RGBA")
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.rectangle([0, 500, 2560, 940], fill=(0, 0, 0, 120)); bg.alpha_composite(sh)
    t = text_img(CHANNEL, SILK, 170, fill=WHITE, outline=6, shadow_col=(0, 0, 0), max_w=1440)
    bg.alpha_composite(t, (1280 - t.width // 2, 560))
    s = text_img("MINECRAFT EN ESPAÑOL  ·  GUÍAS  ·  TRUCOS  ·  NOVEDADES", MB, 46, fill=GOLD, shadow_col=(0, 0, 0), max_w=1440)
    bg.alpha_composite(s, (1280 - s.width // 2, 580 + t.height + 10))
    s2 = text_img("2 VÍDEOS NUEVOS CADA DÍA", SILK, 40, fill=WHITE)
    bg.alpha_composite(s2, (1280 - s2.width // 2, 600 + t.height + s.height + 20))
    for spec, x in [(("cube", "grass_top", "grass_side"), 290), (("cube", "deep_diamond_ore"), 2270)]:
        c = cube(spec[1], spec[2] if len(spec) > 2 else None, 300); bg.alpha_composite(c, (x - 150, 570))
    os.makedirs(CAN, exist_ok=True)
    bg.convert("RGB").save(os.path.join(CAN, "banner_2560x1440.jpg"), quality=93)


def avatar():
    bg = art.vgrad(800, 800, [(40, 110, 50), (14, 40, 20)]).convert("RGBA")
    c = add_glow(cube("grass_top", "grass_side", 520), (160, 255, 120), 30, 0.8)
    bg.alpha_composite(c, (400 - c.width // 2, 380 - c.height // 2))
    p = sprite("pick_diamond", 300); bg.alpha_composite(p, (440, 440))
    os.makedirs(CAN, exist_ok=True)
    bg.convert("RGB").save(os.path.join(CAN, "avatar_800x800.png"))


CHANNEL_DESC = f"""{CHANNEL} · Minecraft en español, explicado claro y al grano.

Cada día, 2 vídeos nuevos:
⛏️ Guías para sobrevivir y progresar más rápido
💎 Trucos, granjas y encantamientos que funcionan de verdad
🧊 Todas las novedades de cada actualización, contadas en pocos minutos

Información comprobada en Java y Bedrock. Si algo cambia, lo actualizamos.

Canal no oficial. Minecraft es una marca de Mojang Synergies AB / Microsoft. Este canal no está afiliado ni patrocinado por Mojang ni por Microsoft."""

FOOTER = """
—————————————
🔔 Suscríbete y activa la campanita: 2 vídeos nuevos de Minecraft cada día.
📌 Información comprobada para la fecha de publicación ({date}). Válido para Java y Bedrock salvo que se indique lo contrario.

Canal no oficial. Minecraft es una marca de Mojang Synergies AB / Microsoft. Este canal no está afiliado ni patrocinado por Mojang ni por Microsoft. Los gráficos, la música y la voz de este vídeo son de creación propia.

#Minecraft #MinecraftEspañol {extra}"""


def metadata(v):
    m = json.load(open(os.path.join(ROOT, "build", v["slug"] + "-meta.json")))
    chap = "\n".join(f"{a} {b}" for a, b in m["chapters"]) if len(m["chapters"]) >= 3 else ""
    dd = "/".join(reversed(v["date"].split("-")))
    extra = v.get("hashtags", "")
    desc = v["desc"] + ("\n\n⏱️ Capítulos\n" + chap if chap else "") + "\n" + FOOTER.format(date=dd, extra=extra.strip())
    txt = (f"TÍTULO:\n{v['title']}\n\nDESCRIPCIÓN:\n{desc}\n\nETIQUETAS (copiar en 'Etiquetas'):\n{', '.join(v['tags'])}\n\n"
           f"ARCHIVOS:\n  vídeo: videos/{v['slug']}.mp4\n  miniatura: miniaturas/{v['slug']}.jpg\n  subtítulos (español): subtitulos/{v['slug']}.srt\n"
           f"DURACIÓN: {int(m['duration'] // 60)}:{int(m['duration'] % 60):02}\n"
           "CONFIGURACIÓN: Idioma: Español · Categoría: Videojuegos · No es contenido para niños · "
           "Contenido alterado o sintético: SÍ (voz generada por IA)\n")
    os.makedirs(META, exist_ok=True)
    open(os.path.join(META, v["slug"] + ".txt"), "w", encoding="utf-8").write(txt)
    return dict(slug=v["slug"], date=v["date"], title=v["title"], duration=round(m["duration"], 1), tags=v["tags"], description=desc)


def all_metadata():
    allm = []
    for v in VIDEOS:
        if os.path.exists(os.path.join(ROOT, "build", v["slug"] + "-meta.json")):
            allm.append(metadata(v))
        elif os.path.exists(os.path.join(META, v["slug"] + ".txt")):
            pass
    old = {}
    p = os.path.join(META, "todos.json")
    if os.path.exists(p):
        old = {x["slug"]: x for x in json.load(open(p, encoding="utf-8"))}
    for x in allm: old[x["slug"]] = x
    json.dump(sorted(old.values(), key=lambda x: x["slug"]), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


SHORT_FOOTER = """
🔔 Sígueme: 2 Shorts nuevos de Minecraft cada día.
Canal no oficial. Minecraft es una marca de Mojang Synergies AB / Microsoft. Gráficos, música y voz de creación propia.

{hashtags}"""


def short_metadata(want=()):
    from content import SHORTS
    sm = os.path.join(ROOT, "shorts", "metadatos"); os.makedirs(sm, exist_ok=True)
    for i, v in enumerate(SHORTS):
        if want and not any(v["slug"].startswith(a) for a in want): continue
        mp = os.path.join(ROOT, "build", f"short-{v['slug']}-meta.json")
        if not os.path.exists(mp): continue
        m = json.load(open(mp))
        n = int(v["slug"][:3]); hora = "14:00" if n % 2 == 1 else "19:00"
        dd = "/".join(reversed(v["date"].split("-")))
        desc = v["desc"] + "\n" + SHORT_FOOTER.format(hashtags=v["hashtags"])
        txt = (f"TÍTULO (máx. 100 caracteres):\n{v['title']}\n\nDESCRIPCIÓN:\n{desc}\n\nETIQUETAS:\n{', '.join(v['tags'])}\n\n"
               f"PUBLICAR: {dd} a las {hora}\nARCHIVOS:\n  short: shorts/{v['slug']}.mp4\n  portada: shorts/portadas/{v['slug']}.jpg\n"
               f"  subtítulos: shorts/subtitulos/{v['slug']}.srt\nDURACIÓN: {m['duration']:.0f} s\n"
               "CONFIGURACIÓN: Idioma: Español · No es contenido para niños · Contenido alterado o sintético: SÍ (voz generada por IA)\n")
        open(os.path.join(sm, v["slug"] + ".txt"), "w", encoding="utf-8").write(txt)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "shorts":
        short_metadata(args[1:])
    elif args == ["canal"]:
        banner(); avatar()
        os.makedirs(CAN, exist_ok=True)
        open(os.path.join(CAN, "descripcion_canal.txt"), "w", encoding="utf-8").write(CHANNEL_DESC + "\n")
    else:
        for v in VIDEOS:
            if not args or any(v["slug"].startswith(a) for a in args):
                thumb(v)
        all_metadata()
