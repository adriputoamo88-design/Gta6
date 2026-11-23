# -*- coding: utf-8 -*-
# Short de curiosidades. Comprobado el 23/11/2026 (Wikipedia "Minecraft", "Mojang Studios", "A Minecraft Movie"):
# - 2009: Markus "Notch" Persson empieza el juego en solitario; primera versión pública en mayo de 2009.
# - 2011: versión 1.0 presentada en la MineCon (18/11/2011).
# - 2014: Microsoft compra Mojang por 2500 millones de dólares.
# - 2023: más de 300 millones de copias vendidas; el videojuego más vendido de la historia.
# - 2025: estreno de "Una película de Minecraft" (abril de 2025), gran éxito de taquilla.
SHORT = dict(
    slug="016-historia-de-minecraft",
    date="2026-11-24",
    theme="superficie",
    title="La HISTORIA de Minecraft en 40 segundos 📜 #minecraft #shorts",
    desc="De un proyecto de una sola persona en 2009 al videojuego más vendido de la historia: los momentos clave de Minecraft.",
    tags=["minecraft", "historia de minecraft", "notch", "mojang", "microsoft minecraft", "pelicula de minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #historia",
    scenes=[
        dict(t="title", h="LA HISTORIA", badge="CURIOSIDADES", splash="¡En 40 s!", hero=("cube", "grass_top", "grass_side"),
             say="La historia de Minecraft en cuarenta segundos."),
        dict(t="tip", n="2009", badge="EL ORIGEN", h="Un solo creador", s="Markus Persson, «Notch»", hero=("cube", "stone"),
             say="2009: Markus Persson, conocido como Notch, empieza a crear Minecraft él solo. La primera versión se publica en mayo."),
        dict(t="tip", n="2011", badge="LANZAMIENTO", h="Versión 1.0", s="Presentada en la MineCon", hero=("cube", "grass_top", "grass_side"),
             say="2011: sale la versión 1.0, presentada en la MineCon."),
        dict(t="tip", n="2014", badge="COMPRA", h="Microsoft compra Mojang", s="Por 2.500 millones de dólares", hero=("sprite", "gold_ingot"),
             say="2014: Microsoft compra Mojang por 2500 millones de dólares."),
        dict(t="tip", n="2023", badge="RÉCORD", h="300 millones de copias", s="El videojuego más vendido de la historia", hero=("sprite", "diamond"),
             say="2023: supera los 300 millones de copias vendidas. Es el videojuego más vendido de la historia."),
        dict(t="tip", n="2025", badge="CINE", h="La película", s="Un éxito en cines de todo el mundo", hero=("sprite", "firework"),
             say="2025: se estrena la película, y es un éxito en cines de todo el mundo."),
        dict(t="card", h="¿Y AHORA?", s="Actualizaciones cada pocos meses", hero=("cube", "packed_ice"),
             say="Y hoy sigue creciendo, con actualizaciones cada pocos meses, como la próxima: The Deep Freeze. Sígueme para más historias de Minecraft."),
    ],
)
