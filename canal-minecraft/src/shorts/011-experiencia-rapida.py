# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 21/11/2026 (mecánicas estables; Minecraft Wiki):
# - Romper menas de carbón, diamante, esmeralda, lapislázuli, redstone y cuarzo del Nether da experiencia (sin Toque de seda).
# - El horno da experiencia al sacar el resultado.
# - Comerciar con aldeanos da experiencia al jugador.
# - Criar animales y pescar dan experiencia.
# - Las granjas con generadores de monstruos (mazmorras) son de las fuentes más rápidas.
# - Cuanto más alto el nivel, más experiencia cuesta subir; la opción de nivel 30 de la mesa solo consume 3 niveles.
SHORT = dict(
    slug="011-experiencia-rapida",
    date="2026-11-22",
    theme="superficie",
    title="5 formas de conseguir EXPERIENCIA rápido en Minecraft ✨ #minecraft #shorts",
    desc="Cinco formas de subir de nivel rápido en Minecraft (minerales, horno, aldeanos, animales y pesca, granjas de mobs) y el truco para no desperdiciar tus niveles.",
    tags=["minecraft", "experiencia minecraft", "como conseguir experiencia", "subir de nivel minecraft", "xp minecraft", "granja de experiencia", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #experiencia",
    scenes=[
        dict(t="title", h="EXPERIENCIA RÁPIDA", badge="GUÍA", splash="¡Nivel 30!", hero=("sprite", "xp"),
             say="Cinco formas de conseguir experiencia rápido en Minecraft."),
        dict(t="tip", n="1", badge="MINERÍA", h="Pica minerales", s="Carbón, diamante, lapislázuli, redstone, cuarzo…", hero=("cube", "coal_ore"),
             say="Uno: pica minerales. El carbón, el diamante, el lapislázuli, la redstone y el cuarzo del Nether dan experiencia al romperlos."),
        dict(t="tip", n="2", badge="HORNO", h="Funde cosas", s="Da experiencia al sacar el resultado", hero=("sprite", "gold_ingot"),
             say="Dos: usa el horno. Te da experiencia cuando sacas lo que has fundido."),
        dict(t="tip", n="3", badge="ALDEANOS", h="Comercia", s="Cada intercambio da experiencia", hero=("sprite", "emerald"),
             say="Tres: comercia con aldeanos. Cada intercambio te da un poco de experiencia."),
        dict(t="tip", n="4", badge="GRANJA Y RÍO", h="Cría animales y pesca", s="Las dos cosas dan experiencia", hero=("sprite", "apple"),
             say="Cuatro: cría animales y pesca. Las dos cosas dan experiencia."),
        dict(t="tip", n="5", badge="LA MÁS RÁPIDA", h="Granja de mobs", s="Con el generador de una mazmorra", hero=("sprite", "skull"),
             say="Y cinco, la más rápida: una granja de mobs con el generador de monstruos de una mazmorra."),
        dict(t="card", warn=True, badge="TRUCO", h="GASTA A NIVEL 30", s="La mesa solo te quita 3 niveles", hero=("sprite", "book"), glint=True,
             say="Truco: gasta tus niveles al llegar a treinta. Cuanto más alto estás, más cuesta subir, y encantar en la mesa solo te quita tres niveles. Sígueme para más trucos."),
    ],
)
