# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 18/11/2026 (mecánicas estables en Java y Bedrock; Minecraft Wiki):
# - Ojo de Ender = perla de Ender + polvo de blaze (sin forma). Las perlas las sueltan los Enderman; el polvo sale de las varas de blaze (fortalezas del Nether).
# - Al lanzarlo vuela hacia la fortaleza más cercana; tiene un 20 % de probabilidad de romperse (1 de cada 5).
# - Cuando estás encima, el ojo baja hacia el suelo.
# - El portal del End tiene 12 marcos; cada uno puede venir ya con ojo. Se activa al llenar todos.
SHORT = dict(
    slug="005-encontrar-fortaleza",
    date="2026-11-19",
    theme="cueva",
    title="Cómo encontrar una FORTALEZA en Minecraft (y abrir el portal del End) 👁️ #minecraft #shorts",
    desc="Cómo fabricar ojos de Ender, seguirlos hasta la fortaleza y activar el portal del End. Paso a paso y sin perder ojos de más.",
    tags=["minecraft", "fortaleza minecraft", "como encontrar una fortaleza", "ojo de ender", "portal del end", "minecraft end", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #fortaleza",
    scenes=[
        dict(t="title", h="FORTALEZA", badge="GUÍA", splash="¡Al End!", hero=("sprite", "eye_ender"),
             say="Así encuentras una fortaleza en Minecraft, el único camino para llegar al End."),
        dict(t="bullets", h="OJOS DE ENDER",
             items=[(("sprite", "ender_pearl"), "Perla de Ender: la sueltan los Enderman"),
                    (("sprite", "blaze_powder"), "Polvo de blaze: sale de las varas de blaze del Nether")],
             say="Primero, fabrica ojos de Ender. Cada uno lleva una perla de Ender, que sueltan los Enderman, y polvo de blaze, que sale de las varas de los blaze del Nether."),
        dict(t="card", badge="PASO 1", h="LÁNZALO AL AIRE", s="Vuela hacia la fortaleza más cercana", hero=("sprite", "eye_ender"),
             say="Lanza un ojo al aire: volará hacia la fortaleza más cercana. Camina en esa dirección y recógelo."),
        dict(t="stat", big="1/5", label="se rompen", small="Lleva ojos de sobra", hero=("sprite", "eye_ender"),
             say="Pero cuidado: de media, uno de cada cinco se rompe al lanzarlo. Lleva ojos de sobra."),
        dict(t="card", warn=True, badge="PASO 2", h="SI SE HUNDE, CAVA", s="Estás encima: baja en escalera", hero=("sprite", "pick_iron"), glowcol=(255, 200, 60),
             say="Cuando el ojo deja de avanzar y baja hacia el suelo, estás encima de la fortaleza. Cava en escalera, nunca en vertical."),
        dict(t="stat", big="12", label="marcos", small="Pon un ojo en cada marco vacío", hero=("cube", "portal_top", "portal_side"),
             say="Dentro, busca la sala del portal. Tiene doce marcos: pon un ojo en cada marco vacío y se activará. Sígueme para la guía del dragón."),
    ],
)
