# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 19/11/2026 (Minecraft Wiki; mecánicas desde la 1.16/1.20 en Java y Bedrock):
# - Escombros ancestrales: en el Nether, más abundantes alrededor de la capa Y 15. Casi nunca aparecen tocando el aire.
# - Se necesita pico de diamante o de netherita.
# - Resisten las explosiones: las camas (que explotan en el Nether) y la dinamita sirven para abrir huecos sin destruirlos.
# - Fundidos dan restos de netherita; 4 restos + 4 lingotes de oro = 1 lingote de netherita.
# - Mejora del equipo de diamante: mesa de herrería + plantilla de mejora de netherita (cofres de los restos de bastión) + lingote.
SHORT = dict(
    slug="008-encontrar-netherite",
    date="2026-11-20",
    theme="nether",
    title="Cómo encontrar NETHERITE rápido en Minecraft (la capa EXACTA) ⛏️ #minecraft #shorts",
    desc="Dónde están los escombros ancestrales (capa Y 15 del Nether), el truco de las camas, cómo fabricar el lingote de netherita y cómo mejorar tu equipo de diamante.",
    tags=["minecraft", "netherite minecraft", "como encontrar netherite", "escombros ancestrales", "netherita", "y 15 nether", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #netherite",
    scenes=[
        dict(t="title", h="NETHERITE", badge="GUÍA", splash="¡Y 15!", hero=("cube", "debris_top", "debris_side"),
             say="La netherita es el mejor material de Minecraft. Así la encuentras rápido."),
        dict(t="stat", big="Y 15", label="en el Nether", small="Ahí aparecen más escombros ancestrales", hero=("cube", "debris_top", "debris_side"),
             say="Ve al Nether y baja hasta la capa Y 15. Ahí es donde más escombros ancestrales aparecen."),
        dict(t="card", h="PICO DE DIAMANTE", s="Con uno de hierro no los podrás recoger", hero=("sprite", "pick_diamond"),
             say="Necesitas un pico de diamante o mejor. Con uno de hierro no los podrás recoger."),
        dict(t="card", warn=True, badge="TRUCO", h="CAMAS EXPLOSIVAS", s="Los escombros aguantan las explosiones. Protégete bien", hero=("sprite", "bed"), glowcol=(255, 120, 60),
             say="Truco: los escombros aguantan las explosiones. Coloca camas en tu túnel y úsalas: explotan, abren huecos enormes y dejan los escombros a la vista. Eso sí, protégete bien."),
        dict(t="bullets", h="DEL ESCOMBRO AL LINGOTE",
             items=[(("cube", "debris_top", "debris_side"), "Fúndelos: restos de netherita"),
                    (("sprite", "gold_ingot"), "4 restos + 4 lingotes de oro"),
                    (("sprite", "netherite_ingot"), "= 1 lingote de netherita")],
             say="Funde los escombros en un horno. Con cuatro restos de netherita y cuatro lingotes de oro, fabricas un lingote."),
        dict(t="card", badge="MEJORA", h="MESA DE HERRERÍA", s="Equipo de diamante + plantilla de mejora + lingote", hero=("sprite", "sword_netherite"),
             say="Para mejorar tu equipo de diamante, usa una mesa de herrería con una plantilla de mejora, que encontrarás en los restos de bastión. Sígueme para más guías."),
    ],
)
