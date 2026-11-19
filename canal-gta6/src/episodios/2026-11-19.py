# -*- coding: utf-8 -*-
"""Episodio del jueves 19/11/2026 (día de lanzamiento).
Fuentes: Notebookcheck (Metacritic 99, 18/11), Informador, Tom's Guide / Beebom / OutputLag (resúmenes de análisis),
Axios y GV Wire (caída de PSN 18/11 y actualización de sistema recomendada por PlayStation).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e03-metacritic-99": "Jueves 19/11 · 12:00", "s03-no-me-deja-jugar": "Jueves 19/11 · 21:00"}

VIDEOS = [
dict(
 slug="e03-metacritic-99",
 theme="retro",
 title="GTA 6 saca un 99 en METACRITIC: lo que dice la crítica (y sus pegas)",
 thumb=dict(top="GTA 6", big="99", tag="EN METACRITIC\n¿EL MEJOR?", icon="trophy"),
 tags=["gta 6 metacritic","gta 6 nota","gta 6 analisis","gta 6 review","gta 6 critica","gta 6 99","gta 6 ocarina of time","gta 6 opencritic","gta 6 merece la pena","gta 6 español"],
 desc="GTA 6 llega con un 99 en Metacritic y empata con el récord histórico de Zelda: Ocarina of Time. Repasamos qué elogia la crítica, cuáles son sus pegas y si merece la pena. Las notas pueden variar a medida que llegan más análisis.",
 scenes=[
  dict(t="title", h="UN 99 EN METACRITIC", s="Lo que dice la crítica de GTA 6",
       say="GTA 6 no ha llegado con buenas notas, ha llegado con notas históricas. Te cuento qué dice la crítica, qué récord ha igualado y cuáles son sus pocas pegas."),
  dict(t="stat", big="99", label="Metacritic · versión PS5", small="Más de 140 análisis de prensa", icon="trophy",
       say="En la versión de PS5, GTA 6 tiene un noventa y nueve sobre cien en Metacritic, con más de ciento cuarenta análisis de prensa. En OpenCritic ronda el noventa y ocho.", chapter="La nota"),
  dict(t="icon", icon="star", h="RÉCORD HISTÓRICO", s="Empata con Zelda: Ocarina of Time (1998)",
       say="Con ese noventa y nueve, empata con The Legend of Zelda: Ocarina of Time como el juego mejor valorado de la historia de Metacritic, y supera a GTA 4 como el título mejor puntuado de Rockstar.", chapter="El récord"),
  dict(t="bullets", h="NOTAS PERFECTAS", items=["IGN: 10", "GameSpot: 10", "Eurogamer: 5/5", "GamesRadar+: 5/5"],
       say="Entre las notas perfectas están IGN y GameSpot, con un diez, y Eurogamer y GamesRadar, con cinco estrellas de cinco."),
  dict(t="bullets", h="LO QUE MÁS GUSTA", items=["Vice City y Leonida", "Disparos y conducción", "La habilidad de concentración", "Sátira y guion"],
       say="¿Qué es lo que más gusta? El nivel de detalle de Vice City y de Leonida, unos disparos y una conducción con más peso que en GTA 5, una habilidad de cámara lenta llamada concentración, y una sátira que la crítica describe como afilada y muy divertida.", chapter="Lo mejor"),
  dict(t="bullets", h="LAS PEGAS", items=["30 FPS y algunas caídas", "Realismo con curva de aprendizaje", "Sin online de salida", "Empieza despacio"],
       say="¿Y las pegas? Varias críticas señalan caídas por debajo de los treinta fotogramas en algunos momentos. Otras avisan de que su realismo, con coches más frágiles y facturas de reparación, cuesta al principio. Además, no hay online de salida, y la nota más baja, un ochenta, dice que la historia tarda en arrancar.", chapter="Las pegas"),
  dict(t="icon", icon="question", h="¿Y LOS JUGADORES?", s="La nota de usuarios llega en unas 36 horas",
       say="¿Y la nota de los jugadores? Metacritic no permite puntuar a los usuarios hasta pasadas unas treinta y seis horas del lanzamiento, así que en un par de días veremos si coinciden con la prensa."),
  dict(t="icon", icon="controller", h="¿MERECE LA PENA?", s="Si te gustan los mundos abiertos: sí",
       say="Mi conclusión: si te gustan los mundos abiertos y las historias de crimen, todo apunta a que es una compra obligada. Si para ti los sesenta fotogramas son imprescindibles, ten en cuenta ese punto."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s03-no-me-deja-jugar",
 theme="ocean", short=True, short_title="¿GTA 6 no te deja jugar?",
 title="¿GTA 6 NO te deja jugar? Prueba esto 🔧",
 thumb=dict(top="GTA 6", big="¿NO TE\nDEJA JUGAR?", tag="3 SOLUCIONES", icon="warning"),
 tags=["gta 6","gta 6 no funciona","gta 6 error","gta 6 psn caido","gta 6 no me deja jugar","gta 6 shorts"],
 desc="Si GTA 6 no te deja jugar o descargar: actualiza el sistema, revisa el estado de PSN o Xbox y restaura licencias.",
 scenes=[
  dict(t="steps", h="¿NO TE DEJA JUGAR?", items=["Actualiza el sistema", "Mira el estado de PSN o Xbox", "Restaura licencias"],
       say="¿GTA 6 no te deja jugar? Prueba esto. Uno: actualiza el sistema de la consola, PlayStation lo pidió expresamente antes del lanzamiento."),
  dict(t="icon", icon="globe", h="ESTADO DEL SERVICIO", s="Web oficial de PlayStation o Xbox",
       say="Dos: mira el estado del servicio en la web oficial de PlayStation o de Xbox. Ayer PSN tuvo una caída, y si el fallo es suyo, solo toca esperar."),
  dict(t="icon", icon="swap", h="RESTAURAR LICENCIAS", s="PS5: Ajustes › Usuarios y cuentas › Otros",
       say="Y tres: en PS5, entra en Ajustes, Usuarios y cuentas, Otros, y pulsa Restaurar licencias. Sígueme para más ayuda con GTA 6."),
 ]),
]
