# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 28/11/2026 (guías de la "Copper Age"/26.3: Shockbyte, minecraft.pl, Sportskeeda, Gaming Route):
# - Se crea con un bloque de cobre y una calabaza tallada (o calabaza de Halloween) encima; el bloque de cobre se convierte en un cofre de cobre.
# - Saca objetos de los cofres de cobre y los lleva a cofres normales que ya tienen ese objeto, o a cofres vacíos.
# - Se oxida con el tiempo; totalmente oxidado se convierte en estatua. Un panal lo encera (deja de oxidarse) y un hacha raspa el óxido y lo reactiva.
SHORT = dict(
    slug="025-golem-de-cobre",
    date="2026-11-29",
    theme="superficie",
    title="Cómo hacer un GÓLEM DE COBRE (y que ordene tus cofres) 🤖 #minecraft #shorts",
    desc="Cómo crear un gólem de cobre, cómo ordena tus objetos entre cofres, por qué acaba convertido en estatua y cómo evitarlo.",
    tags=["minecraft", "golem de cobre", "copper golem", "como hacer un golem de cobre", "cofre de cobre", "ordenar cofres minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #golemdecobre",
    scenes=[
        dict(t="title", h="GÓLEM DE COBRE", badge="GUÍA", splash="¡Te ordena todo!", hero=("cube", "copper_block"),
             say="El gólem de cobre ordena tus cofres él solo. Así se hace, y así funciona."),
        dict(t="bullets", h="CÓMO SE HACE",
             items=[(("cube", "copper_block"), "1 bloque de cobre"), (("sprite", "pumpkin"), "+ calabaza tallada encima")],
             say="Pon un bloque de cobre y coloca encima una calabaza tallada. Aparece el gólem, y el bloque de cobre se convierte en un cofre de cobre."),
        dict(t="card", badge="CÓMO ORDENA", h="ORDENA SOLO", s="Del cofre de cobre al cofre que ya tiene ese objeto, o a uno vacío", hero=("cube", "planks"),
             say="Mete tus cosas en el cofre de cobre. El gólem las saca y las lleva a los cofres normales que ya tienen ese mismo objeto, o a uno vacío."),
        dict(t="card", warn=True, h="SE OXIDA", s="Se vuelve verde… y acaba convertido en estatua", hero=("cube", "oxidized_copper"), glowcol=(110, 200, 160),
             say="Cuidado: con el tiempo se oxida, se vuelve verde, y al final se queda quieto, convertido en estatua."),
        dict(t="card", badge="LA SOLUCIÓN", h="PANAL Y HACHA", s="Panal: lo encera. Hacha: le quita el óxido", hero=("sprite", "honeycomb"),
             say="Para evitarlo, úsale un panal: así lo enceras y deja de oxidarse. Y si ya es una estatua, ráspala con un hacha para que vuelva a moverse. Sígueme para más guías."),
    ],
)
