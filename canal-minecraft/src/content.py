# -*- coding: utf-8 -*-
"""Canal BLOQUE A BLOQUE: carga los guiones de src/videos/NN-slug.py (uno por vídeo).

Cada vídeo es un dict VIDEO con: slug, theme, title, thumb, tags, desc, date, scenes.
Cada escena tiene:
  t    -> plantilla visual: title, news, bullets, stat, tip, icon, vs, mob, hotbar, ylevel, branch, outro
  say  -> lo que dice la voz (y el subtítulo)
  ...  -> parámetros de la plantilla (ver render.py)
Héroes visuales: ("cube", textura_arriba, textura_lado) o ("sprite", nombre). Ver art.py.
"""
import glob, importlib.util, os

CHANNEL = "BLOQUE A BLOQUE"
HANDLE = "@BloqueABloqueES"

OUTRO = ("Suscríbete a Bloque a Bloque y activa la campanita: subimos dos vídeos de Minecraft cada día. "
         "Nos vemos en el siguiente.")

HERE = os.path.dirname(os.path.abspath(__file__))


def _load():
    vids = []
    for p in sorted(glob.glob(os.path.join(HERE, "videos", "[0-9]*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3].replace("-", "_"), p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        vids.append(m.VIDEO)
    return vids


VIDEOS = _load()
