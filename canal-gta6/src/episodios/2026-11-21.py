# -*- coding: utf-8 -*-
"""Episodio del sábado 21/11/2026.
Fuentes: guías de dinero de GTABase, Output Lag, G2A News, GTABoom, KeenGamer, HappyGamer (métodos coincidentes; cifras aproximadas);
GameSpot, GamingBible y ComicBook (easter egg del nido en la torre de radio).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e05-dinero-metodos-reales": "Sábado 21/11 · 17:00", "s05-huevo-de-pascua": "Sábado 21/11 · 21:00"}

VIDEOS = [
dict(
 slug="e05-dinero-metodos-reales",
 theme="money",
 title="Cómo GANAR DINERO en GTA 6: los métodos que SÍ funcionan (ya probados)",
 thumb=dict(top="GTA 6", big="DINERO\nRÁPIDO", tag="MÉTODOS\nPROBADOS", icon="bag"),
 tags=["gta 6 dinero","gta 6 como ganar dinero","gta 6 dinero rapido","gta 6 dinero facil","gta 6 money guide","gta 6 bancos","gta 6 vender coches","gta 6 tesoros","gta 6 guia dinero","gta 6 español"],
 desc="Ya con el juego en la calle, estos son los métodos para ganar dinero en GTA 6 en los que coinciden las guías: escondites de bandas, tesoros submarinos, venta de coches y, más adelante, las cámaras acorazadas de los bancos. Las cifras son aproximadas y pueden variar.",
 scenes=[
  dict(t="title", h="DINERO EN GTA 6", s="Los métodos que sí funcionan",
       say="Hace unos días te conté lo que esperábamos sobre el dinero en GTA 6. Ahora, con el juego en la calle, ya sabemos qué métodos funcionan de verdad. Estos son los que recomiendan todas las guías."),
  dict(t="tip", n=1, h="Escondites de bandas", s="Operaciones ilegales marcadas en el mapa",
       say="Uno. Los escondites de bandas, las operaciones ilegales que aparecen en el mapa. Limpias la zona, saqueas todo, cajas fuertes incluidas, y vendes el botín. Las guías hablan de entre mil y dos mil dólares por escondite.", chapter="Escondites"),
  dict(t="tip", n=2, h="Tesoros bajo el agua", s="Casi sin riesgo · muy rentable al principio",
       say="Dos. Las inmersiones en busca de tesoros en barcos hundidos. Varias guías lo consideran el mejor dinero del principio: casi sin riesgo, y suma muy rápido.", chapter="Tesoros"),
  dict(t="tip", n=3, h="Vender coches", s="Se desbloquea en el capítulo 2",
       say="Tres. Vender coches robados. Se desbloquea en el segundo capítulo, y cada encargo lleva solo unos minutos. Elige coches caros y no los destroces por el camino.", chapter="Coches"),
  dict(t="stat", big="BANCOS", label="El gran golpe llega más tarde", small="Cámaras acorazadas · capítulo 4", icon="bag",
       say="Y el gran dinero llega más tarde: según las guías, una misión secundaria del cuarto capítulo abre las cámaras acorazadas de los bancos, con botines de seis cifras. No te lo destripo más.", chapter="Bancos"),
  dict(t="icon", icon="warning", h="DEPOSITA TU DINERO", s="Si mueres o te detienen, pierdes el efectivo",
       say="El consejo más importante: el dinero que llevas encima se pierde si mueres o te detienen. Ingresa el dinero en el banco a menudo, sobre todo antes de un golpe arriesgado.", chapter="Consejo clave"),
  dict(t="icon", icon="search", h="CIFRAS APROXIMADAS", s="Pueden variar según tu partida",
       say="Un apunte: las cantidades que te he dado son aproximadas y cambian según la guía y la partida. Los métodos sí coinciden en todas."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s05-huevo-de-pascua",
 theme="sunset", short=True, short_title="El huevo de Pascua más literal de GTA 6",
 title="Rockstar escondió un HUEVO de Pascua… literal 🥚",
 thumb=dict(top="GTA 6", big="HUEVO\nLITERAL", tag="EASTER EGG", icon="star"),
 tags=["gta 6","gta 6 easter egg","gta 6 secretos","gta 6 huevo","gta 6 shorts","gta 6 vice city"],
 desc="En lo alto de una torre de radio de Vice City hay un nido con huevos pintados. Un easter egg literal descubierto por los jugadores.",
 scenes=[
  dict(t="icon", icon="search", h="UN SECRETO EN VICE CITY", s="En lo alto de una torre de radio",
       say="Rockstar ha escondido en GTA 6 el huevo de Pascua más literal de la historia. En lo alto de una torre de radio de Vice City hay un nido con huevos pintados."),
  dict(t="stat", big="~7 MIN", label="De escalada", small="Hasta llegar arriba", icon="clock",
       say="Subir lleva unos siete minutos. Coge un huevo, tíralo desde arriba, y prepárate para la escena."),
  dict(t="icon", icon="bell", h="¿LO HAS ENCONTRADO?", s="Más secretos de Leonida cada día",
       say="¿Lo has encontrado? Sígueme para más secretos de Leonida."),
 ]),
]
