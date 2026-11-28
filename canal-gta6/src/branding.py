# -*- coding: utf-8 -*-
"""Miniaturas (1280x720), banner (2560x1440), avatar (800x800) y metadatos de YouTube."""
import json, os
from PIL import Image, ImageDraw
import art
from art import THEMES, text_img, icon, add_glow, rrect, silhouette, ANTON, BEBAS, MB, MX
from content import CHANNEL, HANDLE
import loader
VIDEOS, OUTROOT = loader.load()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TH = os.path.join(OUTROOT, "miniaturas"); CAN = os.path.join(ROOT, "canal"); META = os.path.join(OUTROOT, "metadatos")


def thumb(v):
    th = THEMES[v["theme"]]; t = v["thumb"]
    bg = art.Background(v["theme"], seed=5).frame(1.0)
    im = bg.resize((1280, 720)).convert("RGBA")
    # viñeta oscura a la izquierda para legibilidad
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    for x in range(760):
        d.line([(x, 0), (x, 720)], fill=(5, 0, 15, int(200 * (1 - x / 760))))
    im.alpha_composite(sh)
    # icono grande a la derecha
    ic = t["icon"]
    if ic == "duo":
        for who, rim, x in [("jason", (80, 200, 255), 700), ("lucia", (255, 90, 170), 940)]:
            s = silhouette(who, 520, rim); im.alpha_composite(s, (x, 720 - 520 + 40))
    else:
        g = add_glow(icon(ic, 430, (255, 255, 255), th["acc"]), th["acc"], 30, 1.0)
        im.alpha_composite(g, (1280 - g.width - 20, 360 - g.height // 2 + 20))
    # badge
    y = 34
    if t["top"]:
        b = text_img(t["top"], ANTON, 64, fill=(10, 5, 20))
        box = rrect(b.width + 44, b.height + 22, 14, th["acc2"] + (255,)); box.alpha_composite(b, (22, 11))
        im.alpha_composite(box, (40, y)); y += box.height + 6
    lines = t["big"].split("\n"); size = 210 if len(lines) == 1 else 175
    while True:
        imgs = [text_img(l, ANTON, size, fill=(255, 255, 255), stroke=10, stroke_fill=(10, 5, 20), glow=th["acc"], glow_r=18) for l in lines]
        ys = [0]
        for li in imgs[:-1]: ys.append(ys[-1] + li.height - 34)
        hh = ys[-1] + imgs[-1].height
        if max(i.width for i in imgs) <= 780 and hh <= 430: break
        size = int(size * 0.94)
    big = Image.new("RGBA", (max(i.width for i in imgs), hh), (0, 0, 0, 0))
    for k, li in enumerate(imgs): big.alpha_composite(li, (0, ys[k]))
    im.alpha_composite(big, (22, y - 6))
    tag = text_img(t["tag"], MB, 54, fill=(10, 5, 20), max_w=640, spacing=0.0)
    box = rrect(tag.width + 44, tag.height + 26, 16, th["acc"] + (255,)); box.alpha_composite(tag, (22, 13))
    box = box.rotate(2.5, expand=True, resample=Image.BICUBIC)
    im.alpha_composite(box, (40, min(720 - box.height - 26, y + big.height - 20)))
    im.convert("RGB").save(os.path.join(TH, v["slug"] + ".jpg"), quality=92)


def banner():
    th = THEMES["sunset"]
    bg = art.Background("sunset", seed=9).frame(2.0).resize((2560, 1440)).convert("RGBA")
    sh = Image.new("RGBA", bg.size, (5, 0, 15, 0)); d = ImageDraw.Draw(sh)
    d.rectangle([0, 480, 2560, 960], fill=(5, 0, 15, 140)); bg.alpha_composite(sh)
    t = text_img(CHANNEL, ANTON, 230, glow=th["acc"], glow_r=26, align="center")
    bg.alpha_composite(t, (1280 - t.width // 2, 520))
    s = text_img("GTA 6 EN ESPAÑOL  ·  GUÍAS  ·  TRUCOS  ·  NOTICIAS", MB, 52, fill=th["acc2"], align="center")
    bg.alpha_composite(s, (1280 - s.width // 2, 520 + t.height + 6))
    bg.convert("RGB").save(os.path.join(CAN, "banner_2560x1440.jpg"), quality=93)


def avatar():
    th = THEMES["sunset"]
    bg = art.Background("sunset", seed=9).frame(0.0).crop((560, 100, 1360, 900)).convert("RGBA")
    dark = Image.new("RGBA", bg.size, (5, 0, 15, 110)); bg.alpha_composite(dark)
    t = text_img("ZL", ANTON, 430, glow=th["acc"], glow_r=28, stroke=8, stroke_fill=(10, 5, 20))
    bg.alpha_composite(t, (400 - t.width // 2, 400 - t.height // 2))
    bg.convert("RGB").save(os.path.join(CAN, "avatar_800x800.png"))


FOOTER = """
—————————————
📌 Información verificada a fecha de 17/11/2026. Lo que no está confirmado oficialmente se indica en el vídeo.
🔔 Suscríbete y activa la campanita: guías, trucos verificados y novedades de GTA 6 cada día.

Canal no oficial. GTA y Grand Theft Auto son marcas de Take-Two Interactive / Rockstar Games. Este canal no está afiliado ni patrocinado por ellos. Todos los gráficos, la música y la voz de este vídeo son de creación propia.

#GTA6 #GTAVI #Leonida"""


def metadata():
    allm = []
    for v in VIDEOS:
        m = json.load(open(os.path.join(ROOT, "build", v["slug"] + "-meta.json")))
        chap = "\n".join(f"{a} {b}" for a, b in m["chapters"]) if len(m["chapters"]) >= 3 else ""
        desc = v["desc"] + ("\n\n⏱️ Capítulos\n" + chap if chap else "") + "\n" + FOOTER
        txt = (f"TÍTULO:\n{v['title']}{' #Shorts' if v.get('short') else ''}\n\nDESCRIPCIÓN:\n{desc}\n\nETIQUETAS (copiar en 'Etiquetas'):\n{', '.join(v['tags'])}\n\n"
               f"ARCHIVOS:\n  vídeo: videos/{v['slug']}.mp4\n  miniatura: miniaturas/{v['slug']}.jpg\n  subtítulos (español): subtitulos/{v['slug']}.srt\n"
               f"DURACIÓN: {int(m['duration'] // 60)}:{int(m['duration'] % 60):02}\n"
               "CONFIGURACIÓN: Idioma: Español · Categoría: Videojuegos · No es para niños · Contenido alterado/sintético: SÍ (voz generada por IA)\n")
        open(os.path.join(META, v["slug"] + ".txt"), "w", encoding="utf-8").write(txt)
        allm.append(dict(slug=v["slug"], title=v["title"], duration=round(m["duration"], 1), tags=v["tags"], description=desc))
    json.dump(allm, open(os.path.join(META, "todos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    import sys
    for p in (TH, CAN, META): os.makedirs(p, exist_ok=True)
    if "meta" in sys.argv:
        metadata()
    else:
        for v in VIDEOS: thumb(v)
        if OUTROOT == ROOT: banner(); avatar()
