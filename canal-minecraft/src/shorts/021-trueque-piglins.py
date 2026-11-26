# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 26/11/2026 (Minecraft Wiki "Bartering" y "Piglin"; Java y Bedrock):
# - Los piglins adultos hacen trueque con lingotes de oro (lanzándoselos o usándolos sobre ellos); tardan unos segundos y sueltan un objeto aleatorio.
# - Con al menos una pieza de armadura de oro no atacan. Los piglins bebés se quedan el oro sin dar nada.
# - Botín posible: perlas de Ender, pociones (también arrojadizas) de resistencia al fuego, obsidiana, obsidiana llorosa,
#   libros y botas de hierro con Velocidad de alma, cuarzo, cuerda, cuero, grava, arena de almas, entre otros.
SHORT = dict(
    slug="021-trueque-piglins",
    date="2026-11-27",
    theme="nether",
    title="Qué te dan los PIGLINS a cambio de ORO 🟡 #minecraft #shorts",
    desc="Cómo hacer trueque con los piglins, qué hay que llevar para que no te ataquen y qué objetos pueden darte a cambio de oro.",
    tags=["minecraft", "piglins", "trueque piglins", "piglin bartering", "que dan los piglins", "nether minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #piglins",
    scenes=[
        dict(t="title", h="TRUEQUE CON PIGLINS", badge="GUÍA", splash="¡Oro!", hero=("sprite", "gold_ingot"),
             say="¿Qué te dan los piglins a cambio de oro? Algunas cosas valen muchísimo."),
        dict(t="card", badge="CÓMO SE HACE", h="DALE UN LINGOTE", s="A un piglin adulto: lo mira y te tira algo", hero=("sprite", "gold_ingot"),
             say="Lánzale un lingote de oro a un piglin adulto, o dáselo con clic derecho. Lo mirará unos segundos y te tirará algo a cambio."),
        dict(t="card", warn=True, h="LLEVA ORO PUESTO", s="Si no, te atacan. Los bebés se quedan el oro", hero=("sprite", "chestplate_gold"), glowcol=(255, 200, 60),
             say="Lleva al menos una pieza de armadura de oro, o te atacarán. Y cuidado: los piglins bebés se quedan el oro sin darte nada."),
        dict(t="bullets", h="LO MÁS VALIOSO",
             items=[(("sprite", "ender_pearl"), "Perlas de Ender"), (("sprite", "potion_fire"), "Pociones de resistencia al fuego"),
                    (("cube", "obsidian"), "Obsidiana"), (("sprite", "book"), "Libros de Velocidad de alma")],
             say="Lo más valioso: perlas de Ender, pociones de resistencia al fuego, obsidiana y libros de velocidad de alma, un encantamiento muy difícil de conseguir que te hace correr sobre la arena de almas."),
        dict(t="card", badge="Y MÁS", h="ES ALEATORIO", s="Cuarzo, cuerda, cuero, grava, arena de almas…", hero=("cube", "soul_sand"),
             say="También dan cuarzo, cuerda, cuero, grava o arena de almas. Es aleatorio, así que cuanto más oro, más premios. Sígueme para más guías del Nether."),
    ],
)
