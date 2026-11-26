# -*- coding: utf-8 -*-
"""Episodio del jueves 26/11/2026.
Fuentes: GTABase, KeenGamer, Output Lag, GTA Codex, AlcastHQ, Space4Games (nivel de búsqueda: método común; detalles de 5-6 estrellas
y del cambio de pintura no coinciden y se omiten); TweakTown (PS5 Pro personalizadas de GTA 6 regaladas, no a la venta).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e10-perder-policia": "Jueves 26/11 · 18:00", "s10-ps5-pro-gta6": "Jueves 26/11 · 21:00"}

VIDEOS = [
dict(
 slug="e10-perder-policia",
 theme="neon",
 title="Cómo PERDER a la POLICÍA en GTA 6: el sistema de búsqueda explicado",
 thumb=dict(top="GTA 6", big="PIERDE A\nLA POLI", tag="NIVEL DE\nBÚSQUEDA", icon="star"),
 tags=["gta 6 policia","gta 6 nivel de busqueda","gta 6 como perder a la policia","gta 6 estrellas","gta 6 wanted level","gta 6 escapar policia","gta 6 testigos","gta 6 guia","gta 6 consejos","gta 6 español"],
 desc="La policía de GTA 6 es más lista que nunca. Te explicamos cómo funciona el nivel de búsqueda: qué significan las estrellas, la zona roja del mapa, los testigos y cómo despistarlos cambiando de ropa o de coche. Algunos detalles de los niveles más altos aún no están claros.",
 scenes=[
  dict(t="title", h="PIERDE A LA POLICÍA", s="El sistema de búsqueda de GTA 6",
       say="La policía de GTA 6 no es como la de GTA 5. Si sigues huyendo como siempre, te van a pillar. Te explico cómo funciona el nuevo sistema y cómo despistarlos."),
  dict(t="icon", icon="search", h="TODO EMPIEZA CON TESTIGOS", s="Sin testigo ni cámara, no hay estrellas",
       say="Primero: normalmente solo te buscan si un testigo te ve y te denuncia. Si nadie te ve, ni te graba una cámara, puede que ni siquiera aparezcan las estrellas.", chapter="Testigos"),
  dict(t="vs", h="LAS ESTRELLAS", lt="FIJAS", rt="PARPADEANDO", left=["Te están viendo", "Te persiguen"], right=["Te han perdido", "Pero siguen buscando"],
       say="Las estrellas fijas significan que la policía te está viendo y te persigue. Si parpadean, te han perdido de vista, pero siguen buscándote. No te relajes todavía.", chapter="Las estrellas"),
  dict(t="steps", h="CÓMO ESCAPAR", items=["Rompe la línea de visión", "Sal de la zona roja del mapa", "Espera a que se apaguen las estrellas"],
       say="Para escapar: rompe la línea de visión, por ejemplo metiéndote entre edificios, sal de la zona roja que marca el mapa, y espera fuera hasta que las estrellas desaparezcan.", chapter="Cómo escapar"),
  dict(t="icon", icon="swap", h="CAMBIA DE ASPECTO", s="Ropa, peinado, accesorios y coche",
       say="La policía guarda una ficha de ti: debajo de las estrellas verás qué saben. Por eso ayuda cambiarte de ropa, de peinado o de accesorios, cambiar de coche, y guardar el arma.", chapter="Cambia de aspecto"),
  dict(t="icon", icon="duo", h="SEPARAOS", s="Jason y Lucía por separado llaman menos la atención",
       say="Otro truco que mencionan las guías: separar a Jason y a Lucía. Juntos sois mucho más fáciles de reconocer."),
  dict(t="icon", icon="car", h="CON 3 ESTRELLAS O MÁS", s="Mejor a pie por callejones",
       say="Y con tres estrellas o más en plena ciudad, escapar en coche es muy difícil salvo que sea muy rápido. Las guías recomiendan huir a pie por callejones.", chapter="Niveles altos"),
  dict(t="icon", icon="question", h="POR CONFIRMAR", s="Los niveles más altos y el cambio de pintura",
       say="Ojo: en los niveles más altos, y en si cambiar la pintura del coche te quita la búsqueda, las guías no se ponen de acuerdo. Cuando esté claro, te lo cuento."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s10-ps5-pro-gta6",
 theme="money", short=True, short_title="La PS5 Pro de GTA 6 que no puedes comprar",
 title="La PS5 Pro de GTA 6 que NO puedes comprar 🎮",
 thumb=dict(top="GTA 6", big="PS5 PRO\nGTA 6", tag="SOLO 100", icon="controller"),
 tags=["gta 6","gta 6 ps5 pro","ps5 gta 6 edicion limitada","gta 6 consola","gta 6 shorts","gta 6 rockstar"],
 desc="Según TweakTown, Rockstar ha repartido al menos 100 PS5 Pro personalizadas de GTA 6 a jugadores de los Miami Heat, streamers e influencers. No están a la venta.",
 scenes=[
  dict(t="icon", icon="controller", h="PS5 PRO DE GTA 6", s="Una edición que no está a la venta",
       say="Existe una PS5 Pro de GTA 6… y no la puedes comprar."),
  dict(t="stat", big="100", label="Consolas personalizadas", small="Según TweakTown", icon="star",
       say="Según TweakTown, Rockstar ha repartido al menos cien, primero a jugadores de los Miami Heat y ahora a streamers e influencers."),
  dict(t="icon", icon="bell", h="¿LA QUERRÍAS?", s="Cuéntamelo en comentarios",
       say="¿Tú la querrías? Sígueme para más curiosidades de GTA 6."),
 ]),
]
