# -*- coding: utf-8 -*-
"""Episodio del miércoles 18/11/2026 (víspera del lanzamiento). Plantilla para episodios diarios.
Escenas disponibles: title, stat, bullets, steps, icon, tip, qa, map, card, duo, vs, timeline, outro (ver content.py).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e01-checklist-ultima-hora": "Miércoles 18/11 · 18:00", "s01-a-que-hora-sale": "Miércoles 18/11 · 21:00"}

VIDEOS = [
dict(
 slug="e01-checklist-ultima-hora",
 theme="neon",
 title="GTA 6 sale MAÑANA: CHECKLIST de última hora para jugar a las 00:00",
 thumb=dict(top="GTA 6", big="SALE\nMAÑANA", tag="CHECKLIST\nÚLTIMA HORA", icon="clock"),
 tags=["gta 6","gta 6 mañana","gta 6 hora","gta 6 precarga","gta 6 a que hora sale","gta 6 lanzamiento","gta 6 checklist","gta 6 ps5","gta 6 xbox","gta 6 español"],
 desc="GTA 6 sale mañana, 19 de noviembre, a las 00:00 hora local. Repasa este checklist para no quedarte sin jugar: precarga, espacio, actualizaciones, ajustes y spoilers.",
 scenes=[
  dict(t="title", h="GTA 6 SALE MAÑANA", s="Checklist de última hora para jugar a las 00:00",
       say="Mañana sale GTA 6. Si quieres jugar a las doce en punto sin sorpresas, repasa este checklist ahora. Son seis cosas y te llevan diez minutos."),
  dict(t="stat", big="00:00", label="Jueves 19 de noviembre", small="Hora local de tu país", icon="clock",
       say="Recuerda: el juego se desbloquea a medianoche, hora local, en la noche del miércoles al jueves.", chapter="Hora"),
  dict(t="tip", n=1, h="Comprueba la precarga", s="Biblioteca de juegos · estado de la descarga",
       say="Uno. Si lo compraste en digital, entra en tu biblioteca y comprueba que la precarga está completa al cien por cien.", chapter="Checklist"),
  dict(t="tip", n=2, h="Deja espacio libre", s="Más de 200 GB + margen para el parche",
       say="Dos. Deja espacio libre de sobra. Además del juego, el día uno suele llegar una actualización."),
  dict(t="tip", n=3, h="Edición física: código", s="Canjéalo hoy, no a medianoche",
       say="Tres. Si tienes la edición física, recuerda que trae un código. Canjéalo hoy y empieza la descarga, no esperes a medianoche."),
  dict(t="tip", n=4, h="Actualiza la consola", s="Sistema y mando al día",
       say="Cuatro. Actualiza el sistema de la consola y el mando hoy. Lo último que quieres a las doce es una actualización obligatoria."),
  dict(t="tip", n=5, h="Modo reposo con descargas", s="Para que el parche baje solo",
       say="Cinco. Deja la consola en modo reposo con las descargas activadas, para que el parche se instale solo."),
  dict(t="tip", n=6, h="Silencia spoilers", s="Jason, Lucía, GTA 6…",
       say="Y seis. Silencia ya las palabras clave en tus redes. Mañana va a haber spoilers por todas partes."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s01-a-que-hora-sale",
 theme="sunset", short=True, short_title="¿A qué hora sale GTA 6?",
 title="¿A qué hora sale GTA 6? 🕛",
 thumb=dict(top="GTA 6", big="¿A QUÉ\nHORA?", tag="EN 30\nSEGUNDOS", icon="clock"),
 tags=["gta 6","gta 6 hora","a que hora sale gta 6","gta 6 shorts","gta 6 españa","gta 6 mexico"],
 desc="GTA 6 se desbloquea a las 00:00 hora local del jueves 19 de noviembre en PS5 y Xbox Series X|S.",
 scenes=[
  dict(t="stat", big="00:00", label="Hora local de tu país", small="Jueves 19 de noviembre", icon="clock",
       say="¿A qué hora sale GTA 6? A las doce de la noche, hora local de tu país, del miércoles al jueves diecinueve de noviembre."),
  dict(t="bullets", h="SALE EN", items=["PlayStation 5", "Xbox Series X|S"],
       say="Sale en PlayStation 5 y Xbox Series X y S. Deja la precarga hecha y nos vemos en Leonida."),
  dict(t="icon", icon="bell", h="SÍGUENOS", s="Guías de GTA 6 cada día",
       say="Sígueme para más guías de GTA 6 cada día."),
 ]),
]
