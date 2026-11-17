# -*- coding: utf-8 -*-
"""Carga los vídeos a renderizar.
Por defecto: content.py (los 10 vídeos de lanzamiento) con salida en canal-gta6/.
Episodio diario: CANAL_EPISODIO=episodios/2026-11-20.py  -> salida en canal-gta6/diario/2026-11-20/
"""
import importlib.util, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load():
    ep = os.environ.get("CANAL_EPISODIO")
    if not ep:
        from content import VIDEOS
        return VIDEOS, ROOT
    path = os.path.abspath(ep)
    spec = importlib.util.spec_from_file_location("episodio", path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    out = os.path.join(ROOT, "diario", os.path.splitext(os.path.basename(path))[0])
    return mod.VIDEOS, out
