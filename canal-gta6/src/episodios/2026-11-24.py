# -*- coding: utf-8 -*-
"""Episodio del martes 24/11/2026.
Fuentes: notas oficiales de la actualización 01.002.002 (23/11/2026) recogidas por GTABase, TheSixthAxis, Beebom, esports.gg,
RockstarINTEL, Push Square, Vice e Insider Gaming. Tamaños de descarga: cifras reportadas, no oficiales.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e08-primer-parche": "Martes 24/11 · 18:00", "s08-atascado-llamada": "Martes 24/11 · 21:00"}

VIDEOS = [
dict(
 slug="e08-primer-parche",
 theme="ocean",
 title="PRIMER PARCHE de GTA 6 (01.002.002): todo lo que ARREGLA",
 thumb=dict(top="GTA 6", big="PARCHE\n01.002.002", tag="TODO LO QUE\nARREGLA", icon="disk"),
 tags=["gta 6 parche","gta 6 actualizacion","gta 6 update","gta 6 01.002.002","gta 6 patch notes","gta 6 notas del parche","gta 6 autoguardado","gta 6 crash arreglado","gta 6 llamada no llega","gta 6 español"],
 desc="Rockstar ha publicado la primera actualización de GTA 6 tras el lanzamiento, la 01.002.002. Arregla cierres, el autoguardado, llamadas que no llegaban y bloqueaban la historia, el clima atascado y un nivel de búsqueda imposible de quitar. Te explicamos todo y qué hacer si ya estabas afectado.",
 scenes=[
  dict(t="title", h="PRIMER PARCHE", s="Actualización 01.002.002 de GTA 6",
       say="Ya está aquí el primer parche de GTA 6 después del lanzamiento: la actualización cero uno punto cero cero dos punto cero cero dos. Y arregla justo lo que más se estaba quejando la gente."),
  dict(t="stat", big="23 NOV", label="Fecha de publicación", small="Se distribuye por fases", icon="clock",
       say="Rockstar la publicó el veintitrés de noviembre, con notas oficiales. Se está distribuyendo por fases, así que puede que aún no te haya llegado.", chapter="Cuándo"),
  dict(t="bullets", h="LO QUE ARREGLA", items=["Varios cierres del juego", "El fallo del autoguardado", "Llamadas que no llegaban", "Clima que se quedaba atascado", "Búsqueda que no se podía quitar"],
       say="Lo que arregla, según las notas: varios cierres del juego, el fallo que hacía que el autoguardado no funcionara bien, llamadas de teléfono que no llegaban, el clima que se quedaba atascado, y un nivel de búsqueda policial que no había manera de quitarse.", chapter="Lo que arregla"),
  dict(t="icon", icon="disk", h="EL AUTOGUARDADO", s="La causa de muchas misiones perdidas",
       say="Lo del autoguardado es clave: era la razón de que muchos jugadores perdieran misiones enteras. Aun así, hasta que tengas el parche instalado, sigue guardando a mano.", chapter="Autoguardado"),
  dict(t="icon", icon="phone", h="LAS LLAMADAS", s="Algunas eran necesarias para avanzar",
       say="Lo de las llamadas también era grave: algunas eran necesarias para avanzar en la historia o desbloquear misiones, y había jugadores literalmente atascados.", chapter="Llamadas"),
  dict(t="vs", h="TAMAÑO DE DESCARGA", lt="PS5", rt="XBOX", left=["~604 MB", "Cifra reportada"], right=["~1,2-1,6 GB", "Según la fuente"],
       say="En cuanto al tamaño, se habla de unos seiscientos megas en PS5 y entre uno coma dos y uno coma seis gigas en Xbox. Rockstar no da esas cifras en sus notas, así que tómalas como aproximadas.", chapter="Tamaño"),
  dict(t="icon", icon="search", h="LO QUE NO ARREGLA", s="Rendimiento: sigue igual",
       say="¿Lo que no arregla? El rendimiento. No hay cambios en los fotogramas por segundo ni modos gráficos nuevos."),
  dict(t="icon", icon="question", h="SI YA ESTABAS ATASCADO", s="Rockstar no aclara si se arregla solo",
       say="Y si ya tenías una partida atascada, Rockstar no aclara si se soluciona sola. Prueba a cargar un guardado anterior al problema después de actualizar."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s08-atascado-llamada",
 theme="danger", short=True, short_title="¿Atascado esperando una llamada?",
 title="¿ATASCADO en GTA 6 esperando una LLAMADA? 📞",
 thumb=dict(top="GTA 6", big="¿NO TE\nLLAMAN?", tag="YA TIENE\nSOLUCIÓN", icon="phone"),
 tags=["gta 6","gta 6 llamada no llega","gta 6 atascado","gta 6 bug mision","gta 6 shorts","gta 6 parche"],
 desc="Un fallo impedía que llegaran algunas llamadas necesarias para avanzar en GTA 6. La actualización 01.002.002 lo corrige.",
 scenes=[
  dict(t="icon", icon="phone", h="¿NO TE LLAMAN?", s="Un fallo bloqueaba la historia",
       say="¿Estás atascado en GTA 6 esperando una llamada que no llega? No es culpa tuya: era un fallo que bloqueaba la historia."),
  dict(t="steps", h="LA SOLUCIÓN", items=["Instala el parche 01.002.002", "Reinicia el juego", "Si sigue: carga un guardado anterior"],
       say="La solución: instala la actualización cero uno punto cero cero dos punto cero cero dos y reinicia el juego. Si sigue igual, carga un guardado anterior."),
  dict(t="icon", icon="bell", h="MÁS AYUDA", s="Sígueme para no quedarte atascado",
       say="Sígueme para más ayuda con GTA 6."),
 ]),
]
