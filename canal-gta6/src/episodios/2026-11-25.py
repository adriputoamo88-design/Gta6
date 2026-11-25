# -*- coding: utf-8 -*-
"""Episodio del miércoles 25/11/2026.
Fuentes: Beebom, Red Bull, LibertyCity, Gamelevate (habilidad Concentración / Focus: L3+R3, cámara lenta, puntos débiles,
medidor que se gasta, mejora con estadísticas; detalles como colores o diferencias entre personajes varían según la guía);
GamesRadar, PC Games Hardware y TweakTown (ports no oficiales para PC retirados; Take-Two DMCA; sin versión oficial para PC).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e09-concentracion-guia": "Miércoles 25/11 · 18:00", "s09-pc-no-descargues": "Miércoles 25/11 · 21:00"}

VIDEOS = [
dict(
 slug="e09-concentracion-guia",
 theme="sunset",
 title="CONCENTRACIÓN en GTA 6: cómo usar la CÁMARA LENTA (y mejorarla)",
 thumb=dict(top="GTA 6", big="CÁMARA\nLENTA", tag="GUÍA DE\nCONCENTRACIÓN", icon="clock"),
 tags=["gta 6 concentracion","gta 6 focus","gta 6 camara lenta","gta 6 habilidad especial","gta 6 jason habilidad","gta 6 lucia habilidad","gta 6 como apuntar","gta 6 guia combate","gta 6 trucos combate","gta 6 español"],
 desc="La Concentración es la habilidad de cámara lenta de GTA 6, compartida por Jason y Lucía. Te explicamos cómo se activa, para qué sirve dentro y fuera de los tiroteos, cómo se recarga y cómo mejorarla. Algunos detalles varían según la guía: compruébalos en el tutorial del juego.",
 scenes=[
  dict(t="title", h="CONCENTRACIÓN", s="La cámara lenta de GTA 6, explicada",
       say="La concentración es una de las mecánicas que más ha elogiado la crítica de GTA 6. Pero mucha gente no la usa bien. Te explico cómo funciona y cómo sacarle partido."),
  dict(t="icon", icon="duo", h="LA COMPARTEN LOS DOS", s="Jason y Lucía usan la misma habilidad",
       say="Lo primero: al principio se pensaba que cada protagonista tendría una habilidad distinta, pero las guías coinciden en que Jason y Lucía comparten la misma: la concentración.", chapter="Qué es"),
  dict(t="steps", h="CÓMO SE ACTIVA", items=["Pulsa los dos sticks a la vez", "PS5: L3 + R3", "Xbox: LS + RS"],
       say="Para activarla, pulsa los dos sticks a la vez: L3 y R3 en PS5, o LS y RS en Xbox. El juego te la enseña en una misión del primer capítulo.", chapter="Cómo se activa"),
  dict(t="icon", icon="search", h="EN COMBATE", s="Ralentiza el tiempo y marca puntos débiles",
       say="En combate, ralentiza el tiempo y te marca los puntos débiles de los enemigos. Ojo: no dispara por ti. Te da tiempo e información, y el resto lo pones tú.", chapter="En combate"),
  dict(t="icon", icon="car", h="TAMBIÉN AL VOLANTE", s="Y para detectar cosas a tu alrededor",
       say="Y no solo sirve para disparar: también funciona en los vehículos, y fuera del combate te ayuda a detectar puntos de interés y a la policía."),
  dict(t="icon", icon="chart", h="EL MEDIDOR", s="Se gasta al usarla · vigila la barra",
       say="Cada vez que la usas, gastas un medidor que aparece arriba a la izquierda. Úsala en el momento clave, no al primer disparo.", chapter="El medidor"),
  dict(t="icon", icon="star", h="CÓMO MEJORARLA", s="Sube la estadística en el menú de Jason y Lucía",
       say="Para mejorarla, sube la estadística correspondiente desde el menú de Jason y Lucía. Cuanto más alta, más tiempo puedes mantener la cámara lenta. Y ojo: algunas guías dicen que si dejas a un personaje mucho tiempo sin usar, se recupera más despacio.", chapter="Cómo mejorarla"),
  dict(t="icon", icon="question", h="DETALLES POR CONFIRMAR", s="Algunas guías no coinciden",
       say="Un aviso: hay detalles en los que las guías no coinciden, como el significado exacto de cada color o si hay diferencias entre personajes. Para eso, lo mejor es el tutorial del propio juego."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s09-pc-no-descargues",
 theme="danger", short=True, short_title="¿GTA 6 en PC? No descargues eso",
 title="¿GTA 6 en PC? NO descargues ESO ⚠️",
 thumb=dict(top="GTA 6", big="¿EN PC?", tag="NO LO\nDESCARGUES", icon="warning"),
 tags=["gta 6","gta 6 pc","gta 6 pc descargar","gta 6 port pc","gta 6 shorts","gta 6 estafa"],
 desc="No hay versión oficial de GTA 6 para PC. Los ports no oficiales han sido retirados por Take-Two y cualquier 'descarga' es un riesgo para tu ordenador.",
 scenes=[
  dict(t="icon", icon="warning", h="NO HAY VERSIÓN DE PC", s="Rockstar no la ha anunciado",
       say="¿GTA 6 en PC? Cuidado. Rockstar no ha anunciado ninguna versión oficial para ordenador."),
  dict(t="icon", icon="search", h="PORTS RETIRADOS", s="Take-Two ha tumbado los proyectos no oficiales",
       say="Los proyectos no oficiales que intentaban hacerlo funcionar se han cerrado, y Take-Two ha pedido retirar sus repositorios."),
  dict(t="icon", icon="bell", h="NO LO DESCARGUES", s="Puede ser un virus o una estafa",
       say="Si ves una web que te ofrece descargar GTA 6 para PC, no lo hagas: puede ser un virus o una estafa. Sígueme y te aviso cuando salga de verdad."),
 ]),
]
