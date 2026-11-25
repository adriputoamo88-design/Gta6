# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 25/11/2026 (Minecraft Wiki "Slime" y "Chunk"):
# - Alrededor de 1 de cada 10 chunks es un chunk de slime; en ellos aparecen slimes por debajo de Y 40.
# - Java: F3 + G muestra los bordes de los chunks; /seed muestra la semilla, que se usa en buscadores de chunks de slime.
# - Bedrock: los chunks de slime no dependen de la semilla (son los mismos en todos los mundos).
# - En los pantanos aparecen slimes en la superficie por la noche.
SHORT = dict(
    slug="020-chunks-de-slime",
    date="2026-11-26",
    theme="cueva",
    title="Cómo encontrar CHUNKS DE SLIME en Minecraft (Java y Bedrock) 🟢 #minecraft #shorts",
    desc="Qué son los chunks de slime, cómo verlos en Java con F3+G y la semilla, por qué en Bedrock es más fácil y dónde encontrar slimes sin cavar.",
    tags=["minecraft", "chunks de slime", "slime chunk", "como encontrar slimes", "bolas de slime", "granja de slime", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #slime",
    scenes=[
        dict(t="title", h="CHUNKS DE SLIME", badge="GUÍA", splash="¡Bolas de slime!", hero=("sprite", "slimeball"),
             say="Así encuentras los chunks de slime, para tener bolas de slime sin parar."),
        dict(t="card", badge="¿QUÉ SON?", h="1 DE CADA 10 CHUNKS", s="Ahí aparecen slimes bajo la capa Y 40", hero=("sprite", "slimeball"),
             say="Uno de cada diez chunks es un chunk de slime: ahí aparecen slimes bajo tierra, por debajo de la capa Y 40."),
        dict(t="card", badge="JAVA", h="F3 + G", s="Muestra los bordes de los chunks", hero=("sprite", "map"),
             say="En Java, pulsa F3 más G para ver los bordes de los chunks."),
        dict(t="card", badge="JAVA", h="USA TU SEMILLA", s="Escribe /seed y métela en un buscador de chunks de slime", hero=("sprite", "book"),
             say="Y la forma más rápida: escribe barra seed para ver la semilla de tu mundo, y métela en un buscador de chunks de slime de internet."),
        dict(t="card", badge="BEDROCK", h="MÁS FÁCIL AÚN", s="Los chunks de slime son los mismos en todos los mundos", hero=("sprite", "emerald"),
             say="En Bedrock es aún más fácil: los chunks de slime no dependen de la semilla, son los mismos en todos los mundos."),
        dict(t="card", badge="SIN CAVAR", h="BUSCA UN PANTANO", s="De noche aparecen slimes en la superficie", hero=("cube", "grass_top", "grass_side"),
             say="Y si no quieres cavar, busca un pantano: por la noche también aparecen slimes en la superficie. Sígueme para más guías."),
    ],
)
