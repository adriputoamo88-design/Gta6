# -*- coding: utf-8 -*-
# Short de noticia. Comprobado el 25/11/2026:
# - Mojang publicó "Minecraft 26.4 Pre-Release 1" el 24/11/2026 (artículo en minecraft.net, recogido por Endgame Tools y walkthroughs.net).
# - Es una versión de Java centrada en corregir errores; no añade contenido nuevo.
# - No hay fecha oficial de lanzamiento: la wiki indica el cuarto trimestre de 2026; diciembre es una estimación.
# - Contenido de The Deep Freeze: ver src/shorts/001-the-deep-freeze.py.
SHORT = dict(
    slug="019-deep-freeze-pre-release",
    date="2026-11-26",
    theme="hielo",
    title="THE DEEP FREEZE ya está CERCA: sale la Pre-Release 1 🧊 #minecraft #shorts",
    desc="Mojang ha publicado la primera Pre-Release de Minecraft 26.4 (The Deep Freeze) para Java. Qué significa, qué trae la actualización y qué se sabe de la fecha.",
    tags=["minecraft", "the deep freeze", "minecraft 26.4", "pre-release", "minecraft noticias", "actualizacion minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #thedeepfreeze",
    scenes=[
        dict(t="title", h="¡YA CASI ESTÁ!", badge="NOTICIA", splash="¡Pre-Release!", hero=("cube", "packed_ice"),
             say="The Deep Freeze está cada vez más cerca: ya ha salido su primera versión preliminar."),
        dict(t="card", badge="24 DE NOVIEMBRE", h="PRE-RELEASE 1", s="Para Java. Corrige errores, no añade novedades", hero=("cube", "snow_bricks"),
             say="El 24 de noviembre salió la Pre-Release 1 de la 26.4 para Java. No trae contenido nuevo: se centra en corregir errores."),
        dict(t="card", badge="¿QUÉ SIGNIFICA?", h="LA FASE FINAL", s="Después suele llegar la versión definitiva", hero=("sprite", "hourglass"),
             say="¿Y eso qué significa? Que estamos en la fase final: después de las pre-releases suele llegar la versión definitiva."),
        dict(t="card", warn=True, h="FECHA SIN CONFIRMAR", s="Oficial: antes de fin de año. La comunidad apuesta por diciembre", hero=("sprite", "hourglass"), glowcol=(140, 210, 255),
             say="Mojang todavía no ha dado la fecha exacta. Lo oficial es que llegará antes de que acabe el año, y la comunidad apuesta por diciembre."),
        dict(t="bullets", h="LO QUE LLEGA",
             items=[(("cube", "packed_ice"), "Cuevas de hielo"), (("sprite", "frostbite"), "El Frostbite"),
                    (("cube", "snow_bricks"), "Ladrillos de hielo y nieve"), (("sprite", "disc"), "Listas en los tocadiscos")],
             say="Recuerda lo que trae: cuevas de hielo, el Frostbite, nuevos ladrillos de hielo y de nieve, y listas de reproducción en los tocadiscos. Sígueme y te aviso en cuanto salga."),
    ],
)
