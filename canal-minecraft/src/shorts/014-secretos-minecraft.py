# -*- coding: utf-8 -*-
# Short de curiosidades. Comprobado el 22/11/2026 (Minecraft Wiki; funcionan en Java y Bedrock):
# - Etiqueta con el nombre "jeb_" en una oveja: cambia de color continuamente.
# - Nombre "Dinnerbone" (o "Grumm"): el mob se muestra boca abajo.
# - Un rayo convierte a un cerdo en piglin zombificado y a un creeper en creeper cargado (explosión más fuerte).
# - Los creepers huyen de los gatos (y ocelotes).
SHORT = dict(
    slug="014-secretos-minecraft",
    date="2026-11-23",
    theme="noche",
    title="5 SECRETOS de Minecraft que casi nadie conoce 🤫 #minecraft #shorts",
    desc="Nombres secretos que cambian a los mobs, lo que hace un rayo con los cerdos y los creepers, y la mejor alarma anti-creeper.",
    tags=["minecraft", "secretos minecraft", "curiosidades minecraft", "jeb_", "dinnerbone", "creeper cargado", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #curiosidades",
    scenes=[
        dict(t="title", h="5 SECRETOS", badge="CURIOSIDADES", splash="¿Lo sabías?", hero=("sprite", "name_tag"),
             say="Cinco secretos de Minecraft que casi nadie conoce. El último es mi favorito."),
        dict(t="tip", n="1", badge="ETIQUETA", h="Nombre: jeb_", s="La oveja cambia de color sin parar", hero=("sprite", "name_tag"),
             say="Uno: con una etiqueta, ponle a una oveja el nombre jeb con guion bajo. Cambiará de color sin parar."),
        dict(t="tip", n="2", badge="ETIQUETA", h="Nombre: Dinnerbone", s="El mob se pone boca abajo", hero=("sprite", "name_tag"),
             say="Dos: si le pones Dinnerbone a cualquier mob, se pone boca abajo."),
        dict(t="tip", n="3", badge="RAYO", h="Rayo + cerdo", s="= piglin zombificado", hero=("sprite", "lightning"),
             say="Tres: si a un cerdo le cae un rayo, se convierte en un piglin zombificado."),
        dict(t="tip", n="4", badge="RAYO", h="Rayo + creeper", s="= creeper cargado: explota más fuerte", hero=("sprite", "lightning"),
             say="Cuatro: si el rayo cae sobre un creeper, se carga, y su explosión es mucho más fuerte."),
        dict(t="tip", n="5", badge="ALARMA", h="Los gatos asustan a los creepers", s="Ten uno en casa", hero=("sprite", "heart"),
             say="Y cinco: los creepers huyen de los gatos. Tener un gato en casa es la mejor alarma. Sígueme para más secretos."),
    ],
)
