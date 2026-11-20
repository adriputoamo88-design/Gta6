# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 20/11/2026 (recetas estables en Java y Bedrock; Minecraft Wiki):
# - Soporte para pociones, con polvo de blaze como combustible. Botella de agua + verruga del Nether = poción rara.
# - Poción rara + zanahoria dorada = visión nocturna; + azúcar = velocidad; + polvo de blaze = fuerza;
#   + crema de magma = resistencia al fuego; + rodaja de sandía reluciente = curación.
# - Redstone alarga la duración, polvo de piedra luminosa sube el nivel y pólvora la convierte en arrojadiza.
SHORT = dict(
    slug="010-pociones-utiles",
    date="2026-11-21",
    theme="noche",
    title="Las 5 POCIONES más útiles de Minecraft (y cómo hacerlas) 🧪 #minecraft #shorts",
    desc="La base de casi todas las pociones y las recetas de visión nocturna, velocidad, fuerza, resistencia al fuego y curación. Más los trucos de la redstone, la piedra luminosa y la pólvora.",
    tags=["minecraft", "pociones minecraft", "como hacer pociones", "recetas de pociones", "pocion de curacion", "pocion de fuerza", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #pociones",
    scenes=[
        dict(t="title", h="5 POCIONES", badge="GUÍA", splash="¡Útiles!", hero=("sprite", "potion"), glint=True,
             say="Las cinco pociones más útiles de Minecraft, y cómo hacerlas."),
        dict(t="bullets", h="LA BASE",
             items=[(("sprite", "blaze_powder"), "Polvo de blaze: el combustible del soporte"),
                    (("sprite", "potion"), "Agua + verruga del Nether = poción rara")],
             say="La base de casi todas: en el soporte para pociones, con polvo de blaze como combustible, mezcla una botella de agua con verruga del Nether. Así sale la poción rara."),
        dict(t="tip", n="5", badge="RECETA", h="Visión nocturna", s="Poción rara + zanahoria dorada", hero=("sprite", "carrot_gold"),
             say="Cinco: visión nocturna, con zanahoria dorada. Ves en las cuevas y bajo el agua."),
        dict(t="tip", n="4", badge="RECETA", h="Velocidad", s="Poción rara + azúcar", hero=("sprite", "potion"),
             say="Cuatro: velocidad, con azúcar."),
        dict(t="tip", n="3", badge="RECETA", h="Fuerza", s="Poción rara + polvo de blaze", hero=("sprite", "blaze_powder"),
             say="Tres: fuerza, con polvo de blaze. Más daño en cada golpe."),
        dict(t="tip", n="2", badge="RECETA", h="Resistencia al fuego", s="Poción rara + crema de magma", hero=("sprite", "potion_fire"),
             say="Dos: resistencia al fuego, con crema de magma. Imprescindible en el Nether."),
        dict(t="tip", n="1", badge="RECETA", h="Curación", s="Poción rara + rodaja de sandía reluciente", hero=("sprite", "potion_heal"), glint=True,
             say="Y uno: curación, con rodaja de sandía reluciente. Te cura al instante."),
        dict(t="card", badge="BONUS", h="MÁS FUERTES", s="Redstone: duran más · Piedra luminosa: más nivel · Pólvora: arrojadizas", hero=("cube", "glowstone"),
             say="Bonus: añade redstone para que duren más, polvo de piedra luminosa para que sean más fuertes, y pólvora para lanzarlas. Sígueme para más trucos."),
    ],
)
