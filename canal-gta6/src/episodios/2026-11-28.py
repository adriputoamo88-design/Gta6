# -*- coding: utf-8 -*-
"""Episodio del sábado 28/11/2026.
Fuentes: GamesRadar, GTABase, AltChar, timesaver.gg, GTA Intel, Sportskeeda (actividades; caza y pesca confirmadas por Rockstar;
cifras como nº de carreras o campos de golf no coinciden y se omiten); Beebom / VGC (Rob Nelson, Rockstar North, 26/11/2026:
temían la filtración del gran giro de la historia). SIN SPOILERS.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e12-que-hacer-ademas-historia": "Sábado 28/11 · 12:00", "s12-giro-sin-spoilers": "Sábado 28/11 · 20:00"}

VIDEOS = [
dict(
 slug="e12-que-hacer-ademas-historia",
 theme="ocean",
 title="QUÉ HACER en GTA 6 además de la HISTORIA: actividades para el finde",
 thumb=dict(top="GTA 6", big="QUÉ\nHACER", tag="ADEMÁS DE LA\nHISTORIA", icon="palm"),
 tags=["gta 6 actividades","gta 6 que hacer","gta 6 pesca","gta 6 caza","gta 6 golf","gta 6 carreras","gta 6 minijuegos","gta 6 secundarias","gta 6 mount kalaga","gta 6 español"],
 desc="¿Cansado de misiones? Leonida está llena de cosas que hacer: pesca, caza, buceo, motos de agua, golf, billar, baloncesto, carreras y mucho más. Repasamos las actividades secundarias de GTA 6 para este fin de semana.",
 scenes=[
  dict(t="title", h="QUÉ HACER EN LEONIDA", s="Actividades además de la historia",
       say="Si necesitas un descanso de las misiones, Leonida tiene muchísimo que hacer. Aquí tienes un plan de fin de semana dentro de GTA 6."),
  dict(t="map", h="EN LA NATURALEZA", hl=[5],
       say="Empezamos por la naturaleza. En Mount Kalaga, Rockstar confirmó dos actividades: la caza y la pesca. Y según las guías, la pesca cambia según el tiempo, el tipo de agua y el cebo.", chapter="Caza y pesca"),
  dict(t="icon", icon="search", h="BAJO EL AGUA", s="Buceo y tesoros en barcos hundidos",
       say="Bajo el agua puedes bucear, y ya te conté que los tesoros en barcos hundidos son de las mejores formas de ganar dinero al principio.", chapter="En el agua"),
  dict(t="bullets", h="SOBRE EL AGUA", items=["Motos de agua", "Kayak", "Aerodeslizador en los pantanos"],
       say="Sobre el agua: motos acuáticas, kayak, y el aerodeslizador para recorrer los pantanos de Grassrivers."),
  dict(t="bullets", h="DEPORTES Y MINIJUEGOS", items=["Golf y minigolf", "Billar", "Baloncesto", "Gimnasio"],
       say="Si te van los deportes: golf y minigolf, billar, baloncesto, y hasta el gimnasio.", chapter="Deportes"),
  dict(t="icon", icon="car", h="CARRERAS", s="Callejeras, todoterreno y en el mar",
       say="Para los que quieren velocidad: carreras callejeras, carreras todoterreno y carreras en el mar.", chapter="Carreras"),
  dict(t="icon", icon="star", h="DE NOCHE", s="Clubes y vida nocturna en Vice City",
       say="Y por la noche, Vice City tiene clubes y vida nocturna de sobra. Y en casa, también puedes ver la tele del juego, que está llena de la sátira de Rockstar.", chapter="De noche"),
  dict(t="icon", icon="question", h="¿CUÁL ES TU FAVORITA?", s="Cuéntamelo en comentarios",
       say="Las guías no coinciden en algunas cifras, como el número exacto de carreras o de campos de golf, así que no te las doy todavía. ¿Cuál es tu actividad favorita? Déjamela en los comentarios."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s12-giro-sin-spoilers",
 theme="sunset", short=True, short_title="El giro de GTA 6 que casi se filtra",
 title="Rockstar REZÓ para que no se filtrara ESTE giro 🤫 (sin spoilers)",
 thumb=dict(top="GTA 6", big="EL GIRO", tag="SIN\nSPOILERS", icon="warning"),
 tags=["gta 6","gta 6 giro","gta 6 historia","gta 6 sin spoilers","gta 6 shorts","gta 6 rockstar"],
 desc="Rob Nelson, de Rockstar North, contó a VGC que temían que se filtrara el gran giro de la historia de GTA 6 antes del lanzamiento. Sin spoilers.",
 scenes=[
  dict(t="icon", icon="warning", h="SIN SPOILERS", s="Tranquilo: aquí no se destripa nada",
       say="Tranquilo, sin spoilers. Rockstar tenía miedo de que se filtrara el gran giro de la historia de GTA 6."),
  dict(t="icon", icon="search", h="ROCKSTAR NORTH", s="Entrevista de Rob Nelson con VGC",
       say="Rob Nelson, uno de los jefes de Rockstar North, contó en una entrevista que pasaron el lanzamiento rezando para que no saliera a la luz."),
  dict(t="icon", icon="bell", h="¿YA LO HAS VISTO?", s="No lo cuentes en comentarios",
       say="Y lo consiguieron. ¿Tú ya has llegado? Si es así, no lo cuentes en los comentarios. Sígueme para más de GTA 6."),
 ]),
]
