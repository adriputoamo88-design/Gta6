# -*- coding: utf-8 -*-
"""Episodio del lunes 23/11/2026.
Fuentes: Output Lag, GTA6Bugs, Nerdism, TechyGeeksHome, Beebom (fallos y soluciones comunitarias; Rockstar sin lista oficial; parches 1.002.000 y 1.002.001);
Rockstar (lanzamiento solo un jugador, junio 2026), Notebookcheck / gtasix.org / timesaver.gg (GTA 6 Online sin fecha; Zelnick 9/11/2026).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e07-cierres-y-progreso": "Lunes 23/11 · 18:00", "s07-cuando-sale-online": "Lunes 23/11 · 21:00"}

VIDEOS = [
dict(
 slug="e07-cierres-y-progreso",
 theme="retro",
 title="¿GTA 6 se CIERRA o PIERDES progreso? Cómo evitarlo en PS5 y Xbox",
 thumb=dict(top="GTA 6", big="¿SE TE\nCIERRA?", tag="CÓMO NO PERDER\nTU PARTIDA", icon="warning"),
 tags=["gta 6 se cierra","gta 6 crash","gta 6 error ps5","gta 6 no funciona","gta 6 perder progreso","gta 6 guardado","gta 6 bugs","gta 6 parche","gta 6 xbox error","gta 6 español"],
 desc="Algunos jugadores sufren cierres de GTA 6 o pierden progreso porque el autoguardado era antiguo. Rockstar aún no ha publicado una lista oficial de errores, pero estos pasos ayudan: actualizar, reiniciar del todo, liberar espacio y guardar a mano.",
 scenes=[
  dict(t="title", h="¿SE TE CIERRA GTA 6?", s="Cómo evitar cierres y no perder tu partida",
       say="Si GTA 6 se te ha cerrado de golpe, o has perdido una misión entera de progreso, no eres el único. Te cuento qué está pasando y qué puedes hacer."),
  dict(t="icon", icon="search", h="SIN LISTA OFICIAL", s="Rockstar no ha publicado errores conocidos",
       say="Lo primero: Rockstar todavía no ha publicado una lista oficial de errores conocidos ni un parche para los cierres. Lo que sigue son las soluciones en las que coinciden las guías y los jugadores.", chapter="Situación"),
  dict(t="tip", n=1, h="Actualiza consola y juego", s="Primero el sistema, luego el parche",
       say="Uno. Actualiza primero el sistema de la consola y después el juego. En PS5, muchos fallos de la noche del lanzamiento venían de no tener instalada la actualización de sistema que Sony pidió.", chapter="Soluciones"),
  dict(t="tip", n=2, h="Reinicio completo", s="Apaga del todo, no modo reposo",
       say="Dos. Haz un reinicio completo: apaga la consola del todo, no la dejes en modo reposo, espera unos segundos y vuelve a encenderla."),
  dict(t="tip", n=3, h="Deja espacio libre", s="El juego y sus parches necesitan margen",
       say="Tres. Deja espacio libre en el disco. Con un juego de más de doscientos gigas y sus parches, ir justo de espacio da problemas."),
  dict(t="tip", n=4, h="Reinstala si sigue", s="Último recurso: borra y descarga de nuevo",
       say="Cuatro. Si los cierres siguen, como último recurso, reinstala el juego. Las partidas guardadas se guardan aparte, pero por si acaso, si tienes copia en la nube, comprueba que está al día antes."),
  dict(t="icon", icon="disk", h="GUARDA A MANO", s="No te fíes solo del autoguardado",
       say="Y lo más importante para no perder progreso: guarda a mano a menudo, sobre todo antes de una misión larga. Varios jugadores han tenido que repetir misiones porque el último autoguardado era más antiguo de lo que pensaban.", chapter="No perder progreso"),
  dict(t="icon", icon="swap", h="SI UNA MISIÓN FALLA", s="Carga una partida anterior",
       say="Si el juego se cierra siempre en el mismo punto de una misión, prueba a cargar una partida de antes de empezarla. A algunos jugadores les ha funcionado."),
  dict(t="icon", icon="warning", h="¿SE CIERRA TODO?", s="Si pasa en otros juegos: soporte técnico",
       say="Y si la consola se apaga también con otros juegos, el problema puede ser del hardware: en ese caso, contacta con el soporte de PlayStation o de Xbox."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s07-cuando-sale-online",
 theme="neon", short=True, short_title="¿Cuándo sale GTA 6 Online?",
 title="¿Cuándo sale GTA 6 ONLINE? 🌐",
 thumb=dict(top="GTA 6", big="¿Y EL\nONLINE?", tag="SIN FECHA", icon="globe"),
 tags=["gta 6 online","gta 6 online fecha","cuando sale gta 6 online","gta 6 multijugador","gta 6 shorts","gta online 2"],
 desc="GTA 6 salió solo con modo historia y Rockstar no ha anunciado fecha para su modo online. Las estimaciones que hablan de 2027 no están confirmadas.",
 scenes=[
  dict(t="icon", icon="globe", h="¿Y EL ONLINE?", s="GTA 6 salió solo con modo historia",
       say="¿Cuándo sale GTA 6 Online? GTA 6 ha salido solo con modo historia, y Rockstar no ha anunciado fecha para el online. Ni fecha, ni nombre."),
  dict(t="stat", big="¿2027?", label="Estimaciones no oficiales", small="Rockstar no lo ha confirmado", icon="clock",
       say="Hay quien habla de dos mil veintisiete, pero son estimaciones, nada oficial. Take-Two dice que esas noticias llegarán de Rockstar a su debido tiempo."),
  dict(t="icon", icon="bell", h="TE AVISAMOS", s="En cuanto haya fecha oficial",
       say="Sígueme y te aviso en cuanto haya fecha oficial."),
 ]),
]
