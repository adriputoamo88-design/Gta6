# -*- coding: utf-8 -*-
"""Episodio del martes 17/11/2026.
Fuentes: Rockstar Newswire 10/11/2026 (vía Insider Gaming, Notebookcheck, GamingBible), Sensor Tower (vía TweakTown), Morgan Stanley (vía TweakTown).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e02-gta-6-30-fps": "Martes 17/11 · 18:00", "s02-reservas-record": "Martes 17/11 · 21:00"}

VIDEOS = [
dict(
 slug="e02-gta-6-30-fps",
 theme="danger",
 title="GTA 6 irá a 30 FPS: lo que ha CONFIRMADO Rockstar (y qué gana la PS5 Pro)",
 thumb=dict(top="GTA 6", big="30 FPS", tag="CONFIRMADO\nPOR ROCKSTAR", icon="controller"),
 tags=["gta 6 30 fps","gta 6 fps","gta 6 60 fps","gta 6 ps5 pro","gta 6 rendimiento","gta 6 xbox series s","gta 6 modo rendimiento","gta 6 graficos","gta 6 pssr","gta 6 español"],
 desc="Rockstar ha confirmado que GTA 6 apunta a 30 fotogramas por segundo en PS5, PS5 Pro y Xbox Series X|S. Te explicamos qué significa, por qué no hay 60 FPS, qué mejoras tiene la PS5 Pro y qué podría cambiar en el futuro.",
 scenes=[
  dict(t="title", h="GTA 6 IRÁ A 30 FPS", s="Lo que ha confirmado Rockstar",
       say="Es oficial: GTA 6 irá a treinta fotogramas por segundo en consolas. Te explico qué ha dicho Rockstar exactamente, por qué no hay sesenta, y qué gana la PS5 Pro."),
  dict(t="stat", big="30 FPS", label="Objetivo en todas las consolas", small="PS5 · PS5 Pro · Xbox Series X|S", icon="controller",
       say="Según el blog oficial de Rockstar publicado el diez de noviembre, GTA 6 apunta a treinta fotogramas por segundo en PS5, en PS5 Pro y en Xbox Series X y S.", chapter="Lo confirmado"),
  dict(t="icon", icon="search", h="¿QUÉ SIGNIFICA?", s="Fluidez estable en vez de máxima",
       say="¿Qué significa esto? Que el juego prioriza un mundo enorme y lleno de detalle, y una imagen estable, antes que la fluidez máxima. Treinta fotogramas es lo mismo a lo que funcionaba GTA 5 en su consola original.", chapter="¿Qué significa?"),
  dict(t="icon", icon="chart", h="EL CUELLO DE BOTELLA", s="La CPU, no la tarjeta gráfica",
       say="¿Y por qué no sesenta? Los análisis técnicos apuntan a la CPU: simular multitudes, tráfico y físicas en un mapa así consume muchísimo procesador, y la CPU de la PS5 Pro es apenas un poco más rápida que la de la PS5 normal.", chapter="¿Por qué no 60?"),
  dict(t="bullets", h="LO QUE GANA LA PS5 PRO", items=["Imagen más nítida con PSSR", "Sombras con ray tracing", "Mismo objetivo: 30 FPS"],
       say="Lo que gana la PS5 Pro, según Rockstar: una imagen más nítida gracias al reescalado PSSR de Sony, y sombras con trazado de rayos. Pero el objetivo de fotogramas es el mismo.", chapter="PS5 Pro"),
  dict(t="icon", icon="question", h="¿Y LA SERIES S?", s="Resolución sin detallar por Rockstar",
       say="¿Y la Xbox Series S? Rockstar no ha detallado la resolución ni los recortes gráficos de cada consola, así que habrá que verlo con el juego en la mano."),
  dict(t="icon", icon="clock", h="¿PARCHE A 60 FPS?", s="No anunciado · no descartado",
       say="¿Llegará un parche a sesenta fotogramas, o un modo intermedio a cuarenta? No está anunciado. Rockstar tampoco lo ha descartado, y GTA 5 y Red Dead Redemption 2 recibieron mejoras años después. Pero hoy, es solo una posibilidad.", chapter="¿Habrá 60 FPS?"),
  dict(t="bullets", h="CONSEJOS PARA JUGAR MEJOR", items=["Activa el modo juego de tu tele", "Revisa el desenfoque de movimiento", "Juega con la consola ventilada"],
       say="Mis consejos: activa el modo juego de tu televisor para reducir el retraso, revisa en los ajustes si puedes bajar el desenfoque de movimiento, y deja la consola bien ventilada.", chapter="Consejos"),
  dict(t="icon", icon="question", h="¿TE IMPORTA?", s="¿30 FPS estables o 60 con menos detalle?",
       say="Y a ti, ¿te importan los treinta fotogramas, o prefieres un mundo así de detallado? Déjamelo en los comentarios."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s02-reservas-record",
 theme="money", short=True, short_title="Reservas de GTA 6: una locura",
 title="Las RESERVAS de GTA 6 son una LOCURA 💸",
 thumb=dict(top="GTA 6", big="+1.000\nMILLONES", tag="EN RESERVAS", icon="money"),
 tags=["gta 6","gta 6 reservas","gta 6 ventas","gta 6 record","gta 6 shorts","gta 6 preorder"],
 desc="Según estimaciones de Sensor Tower, las reservas digitales de GTA 6 superan los 1.000 millones de dólares. Rockstar no ha publicado cifras oficiales.",
 scenes=[
  dict(t="stat", big="+1.000 M$", label="En reservas digitales", small="Estimación de Sensor Tower", icon="money",
       say="Las reservas de GTA 6 son una locura. Según la consultora Sensor Tower, superan los mil millones de dólares solo en digital."),
  dict(t="stat", big="~10 M", label="Copias reservadas", small="Estimación · sin cifra oficial", icon="chart",
       say="Eso serían unos diez millones de copias antes de salir. Ojo: es una estimación, Rockstar no ha dado cifras oficiales."),
  dict(t="icon", icon="bell", h="¿LA TIENES RESERVADA?", s="Cuéntamelo en comentarios",
       say="¿Tú la tienes reservada? Sígueme para más de GTA 6 cada día."),
 ]),
]
