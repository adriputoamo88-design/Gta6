# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 23/11/2026 (Minecraft Wiki; contenido de la 1.21 "Tricky Trials", Java y Bedrock):
# - Cámaras de desafío: estructuras subterráneas de cobre y toba. Los cartógrafos venden mapas de exploración de desafío.
# - Generadores de desafío: al derrotar a todos sus mobs sueltan premios y llaves de desafío.
# - Cada llave abre una bóveda; cada bóveda da premio una sola vez por jugador.
# - El Breeze suelta varas de breeze. Maza = núcleo pesado + vara de breeze.
# - El núcleo pesado sale (con poca probabilidad) en las bóvedas ominosas. Con Mal presagio (botella ominosa) al entrar,
#   los desafíos se vuelven ominosos: más difíciles y con mejores premios.
# - La maza hace más daño cuanto mayor es la caída.
SHORT = dict(
    slug="015-camaras-de-desafio",
    date="2026-11-24",
    theme="cueva",
    title="Cámaras de DESAFÍO: llaves, Breeze y cómo conseguir la MAZA 🔨 #minecraft #shorts",
    desc="Qué son las cámaras de desafío, cómo conseguir llaves, para qué sirven las bóvedas y la receta de la maza, el arma que hace más daño cuanto más alto caes.",
    tags=["minecraft", "camaras de desafio", "trial chambers", "maza minecraft", "como conseguir la maza", "breeze", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #maza",
    scenes=[
        dict(t="title", h="CÁMARAS DE DESAFÍO", badge="GUÍA", splash="¡La maza!", hero=("cube", "copper_block"),
             say="Las cámaras de desafío esconden una de las armas más fuertes de Minecraft: la maza. Así se consigue."),
        dict(t="card", badge="DÓNDE", h="BAJO TIERRA", s="Bloques de cobre y toba. Los cartógrafos venden un mapa", hero=("cube", "tuff_bricks"),
             say="Están bajo tierra, hechas de cobre y toba. Las encontrarás explorando cuevas, o con un mapa de los aldeanos cartógrafos."),
        dict(t="card", badge="PASO 1", h="GENERADORES DE DESAFÍO", s="Derrota a todos sus monstruos: sueltan premios y llaves", hero=("sprite", "trial_key"),
             say="Dentro hay generadores de desafío. Derrota a todos sus monstruos y soltarán premios y llaves de desafío."),
        dict(t="card", badge="PASO 2", h="ABRE LAS BÓVEDAS", s="Cada bóveda da premio una sola vez por jugador", hero=("sprite", "trial_key"),
             say="Con cada llave abres una bóveda. Ojo: cada bóveda solo te da premio una vez."),
        dict(t="card", badge="ENEMIGO", h="EL BREEZE", s="Salta y lanza ráfagas de viento. Suelta varas de breeze", hero=("sprite", "breeze_rod"), glowcol=(170, 210, 255),
             say="Aquí vive el Breeze, que salta y lanza ráfagas de viento. Al derrotarlo suelta varas de breeze."),
        dict(t="bullets", h="LA MAZA",
             items=[(("cube", "heavy_core"), "Núcleo pesado: en bóvedas ominosas (con suerte)"),
                    (("sprite", "breeze_rod"), "+ vara de breeze")],
             say="Para la maza necesitas un núcleo pesado, que sale con suerte en las bóvedas ominosas, y una vara de breeze."),
        dict(t="card", warn=True, badge="MODO DIFÍCIL", h="BOTELLA OMINOSA", s="Desafíos más duros, mejores premios", hero=("sprite", "ominous_bottle"), glowcol=(80, 160, 170),
             say="Para que aparezcan, bebe una botella ominosa antes de entrar: los desafíos serán más duros, pero con mejores premios. Y recuerda: la maza hace más daño cuanto más alto caes. Sígueme para más guías."),
    ],
)
