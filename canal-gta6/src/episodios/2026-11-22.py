# -*- coding: utf-8 -*-
"""Episodio del domingo 22/11/2026.
Fuentes: GTABase, GGRecon, HappyGamer, Leonida Waypoint, Wisevoter (nota de usuarios de Metacritic ~5,2-5,6, PS Store ~4,8/5);
ScreenRant, GameRiv, Dexerto, Output Lag (duración: ~50 h historia, 5 capítulos, 80+ con extras; HowLongToBeat aún con pocos datos).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e06-critica-vs-usuarios": "Domingo 22/11 · 17:00", "s06-cuanto-dura": "Domingo 22/11 · 21:00"}

VIDEOS = [
dict(
 slug="e06-critica-vs-usuarios",
 theme="neon",
 title="GTA 6: un 99 de la CRÍTICA… y un 5 de los USUARIOS. ¿Qué está pasando?",
 thumb=dict(top="GTA 6", big="99 VS 5", tag="¿QUÉ ESTÁ\nPASANDO?", icon="question"),
 tags=["gta 6 metacritic usuarios","gta 6 review bombing","gta 6 nota usuarios","gta 6 5.4","gta 6 polemica","gta 6 critica","gta 6 opiniones","gta 6 merece la pena","gta 6 ps store","gta 6 español"],
 desc="GTA 6 tiene un 99 de la crítica en Metacritic, pero la nota de los usuarios ronda el 5 sobre 10. Te explicamos de dónde sale esa diferencia, qué es el review bombing y qué dicen los jugadores que de verdad han comprado el juego. Las cifras cambian a diario.",
 scenes=[
  dict(t="title", h="99 VS 5", s="Crítica contra usuarios en GTA 6",
       say="GTA 6 tiene un noventa y nueve de la crítica en Metacritic. Pero la nota de los usuarios ronda el cinco sobre diez. ¿Cómo puede ser? Vamos a verlo con calma."),
  dict(t="vs", h="LAS DOS NOTAS", lt="CRÍTICA", rt="USUARIOS", left=["99 / 100", "Más de 150 análisis", "Empata el récord histórico"], right=["~5 / 10", "Decenas de miles de votos", "Cambia cada día"],
       say="Por un lado, la crítica: noventa y nueve, con más de ciento cincuenta análisis. Por otro, los usuarios: alrededor de un cinco, con decenas de miles de votos, y una cifra que se mueve cada día.", chapter="Las notas"),
  dict(t="icon", icon="warning", h="REVIEW BOMBING", s="Votos en masa, muchos con un cero",
       say="Varios medios hablan de review bombing: votos negativos en masa, muchos de ellos con un cero. Metacritic no pide demostrar que tienes el juego para votar, así que cualquiera puede puntuarlo.", chapter="Review bombing"),
  dict(t="icon", icon="search", h="SIN CONFIRMAR", s="No hay prueba de una campaña organizada",
       say="Ojo, que no está demostrado que sea una campaña organizada. Ni Rockstar ni Metacritic han dicho nada al respecto."),
  dict(t="bullets", h="LAS QUEJAS REALES", items=["30 FPS en todas las consolas", "Primeros capítulos lentos", "Sin online de salida"],
       say="Porque también hay quejas reales: los treinta fotogramas en todas las consolas, incluida la PS5 Pro, unos primeros capítulos que a algunos se les hacen lentos, y la falta de modo online.", chapter="Quejas reales"),
  dict(t="stat", big="4,8 / 5", label="Nota en PlayStation Store", small="Solo pueden votar quienes lo compraron", icon="star",
       say="¿Y los que de verdad lo han comprado? En la PlayStation Store, donde solo pueden votar los compradores, GTA 6 ronda el cuatro coma ocho sobre cinco.", chapter="Los compradores"),
  dict(t="icon", icon="controller", h="MI CONCLUSIÓN", s="Fíjate en quién vota y por qué",
       say="Mi conclusión: no te fíes de una sola cifra. Mira quién vota y por qué. Si las quejas sobre los treinta fotogramas o el ritmo te importan, tenlas en cuenta. Si no, todo apunta a que vas a disfrutarlo."),
  dict(t="icon", icon="question", h="¿Y TU NOTA?", s="Déjala en los comentarios",
       say="¿Y tú qué nota le pones después de este primer fin de semana? Déjala en los comentarios."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s06-cuanto-dura",
 theme="ocean", short=True, short_title="¿Cuánto dura GTA 6?",
 title="¿Cuánto DURA GTA 6? ⏱️",
 thumb=dict(top="GTA 6", big="¿CUÁNTO\nDURA?", tag="HISTORIA\nY 100%", icon="clock"),
 tags=["gta 6","gta 6 duracion","cuanto dura gta 6","gta 6 horas","gta 6 shorts","gta 6 capitulos"],
 desc="La historia de GTA 6 dura unas 50 horas en 5 capítulos, y más de 80 con actividades secundarias, según los primeros análisis. Aún no hay datos oficiales.",
 scenes=[
  dict(t="stat", big="~50 H", label="Historia principal", small="5 capítulos · según los análisis", icon="clock",
       say="¿Cuánto dura GTA 6? La historia principal, unas cincuenta horas, repartidas en cinco capítulos, según los primeros análisis."),
  dict(t="stat", big="+80 H", label="Con secundarias", small="El 100 % podría rondar las 200 h", icon="trophy",
       say="Con las misiones secundarias, más de ochenta horas. Y completarlo al cien por cien podría rondar las doscientas."),
  dict(t="icon", icon="bell", h="¿CUÁNTO LLEVAS?", s="Cuéntamelo en comentarios",
       say="Son estimaciones, no datos oficiales. ¿Cuántas horas llevas tú? Sígueme para más de GTA 6."),
 ]),
]
