# -*- coding: utf-8 -*-
# Short de guía. Datos comprobados: ver src/videos/002-como-encontrar-diamantes.py.
SHORT = dict(
    slug="002-diamantes",
    date="2026-11-17",
    theme="cueva",
    title="Así encuentras DIAMANTES en Minecraft (la capa EXACTA) 💎 #minecraft #shorts",
    desc="La mejor capa para los diamantes desde la 1.18 es la Y -59. Cómo ver tu altura, el método de minería en ramas y el truco de Fortuna III.",
    tags=["minecraft", "diamantes minecraft", "como encontrar diamantes", "y -59", "capa de diamantes", "mineria en ramas", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #diamantes",
    scenes=[
        dict(t="title", h="DIAMANTES", badge="GUÍA", splash="¡Y -59!", hero=("cube", "deep_diamond_ore"),
             say="Si buscas diamantes en la capa once, estás perdiendo el tiempo."),
        dict(t="vs", h="ANTES VS AHORA", lt="ANTES", rt="AHORA", left=["Capa Y 11-12"], right=["Capa Y -59"],
             lhero=("cube", "diamond_ore"), rhero=("cube", "deep_diamond_ore"),
             say="Desde la 1.18, los diamantes están mucho más abajo."),
        dict(t="ylevel", target=-59,
             marks=[(16, "Y 16: empiezan", None), (0, "Y 0", None), (-53, "Y -53: menos lava", (255, 170, 60)), (-59, "Y -59: LA MEJOR", (255, 214, 64))],
             say="La mejor capa es la Y -59, justo encima de la roca madre. Si quieres evitar la lava, quédate en la Y -53."),
        dict(t="card", h="MIRA TU ALTURA", s="Java: F3  ·  Bedrock: «Mostrar coordenadas»", hero=("sprite", "map"),
             say="Para ver tu altura, en Java pulsa F3, y en Bedrock activa Mostrar coordenadas."),
        dict(t="branch", h="MINERÍA EN RAMAS",
             say="Ahora haz un túnel largo y, cada tres bloques, abre ramas a los lados, dejando dos bloques de pared entre ellas."),
        dict(t="stat", big="x4", label="Con Fortuna III", small="Hasta 4 diamantes por mena", hero=("sprite", "book"), glint=True,
             say="Y si picas con Fortuna tres, cada mena puede soltar hasta cuatro diamantes."),
        dict(t="card", warn=True, h="NUNCA CAVES HACIA ABAJO", s="Baja en escalera", hero=("sprite", "bucket_lava"), glowcol=(255, 140, 40),
             say="Eso sí: nunca caves en vertical, baja en escalera. Sígueme para más trucos."),
    ],
)
