# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 21/11/2026 (Minecraft Wiki; mecánica estable en Java y Bedrock):
# - Receta: 5 de cristal, 3 de obsidiana y 1 estrella del Nether (la suelta el Wither).
# - Base: pirámide de bloques de hierro, oro, esmeralda, diamante o netherita. 1 piso = 9 bloques; 4 pisos = 9+25+49+81 = 164.
# - Poderes: velocidad, prisa minera, resistencia, salto y fuerza; con 4 pisos, regeneración o nivel II del principal.
# - Se activa pagando con un lingote de hierro u oro, una esmeralda, un diamante o un lingote de netherita.
# - El haz necesita ver el cielo (los bloques opacos encima lo bloquean).
SHORT = dict(
    slug="012-como-hacer-faro",
    date="2026-11-22",
    theme="noche",
    title="Cómo hacer un FARO en Minecraft (y todos sus poderes) 🔦 #minecraft #shorts",
    desc="La receta del faro, cómo montar la pirámide (de 9 a 164 bloques), todos sus poderes y cómo activarlo.",
    tags=["minecraft", "faro minecraft", "como hacer un faro", "beacon minecraft", "estrella del nether", "piramide faro", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #faro",
    scenes=[
        dict(t="title", h="EL FARO", badge="GUÍA", splash="¡Superpoderes!", hero=("cube", "beacon"),
             say="El faro te da superpoderes, como velocidad o prisa minera. Así se fabrica."),
        dict(t="bullets", h="LA RECETA",
             items=[(("cube", "glass"), "5 de cristal"), (("cube", "obsidian"), "3 de obsidiana"),
                    (("sprite", "nether_star"), "1 estrella del Nether (la suelta el Wither)")],
             say="Necesitas cinco bloques de cristal, tres de obsidiana y una estrella del Nether, que suelta el Wither al derrotarlo."),
        dict(t="stat", big="164", label="bloques", small="Pirámide de 4 pisos de hierro, oro, esmeralda, diamante o netherita", hero=("cube", "iron_block"),
             say="Ponlo encima de una pirámide de bloques de hierro, oro, esmeralda, diamante o netherita. Con un piso de nueve bloques ya funciona. La pirámide completa, de cuatro pisos, son ciento sesenta y cuatro."),
        dict(t="bullets", h="LOS PODERES",
             items=["Velocidad", "Prisa minera", "Resistencia", "Salto", "Fuerza", "Con 4 pisos: regeneración o nivel II"],
             say="Puedes elegir velocidad, prisa minera, resistencia, salto o fuerza. Y con los cuatro pisos desbloqueas regeneración, o subir el poder a nivel dos."),
        dict(t="card", badge="ACTÍVALO", h="PAGA CON UN LINGOTE", s="Hierro, oro, netherita, esmeralda o diamante. Y cielo despejado", hero=("sprite", "gold_ingot"),
             say="Para activarlo, dale un lingote de hierro, de oro o de netherita, una esmeralda o un diamante. Y deja el cielo despejado encima, o el rayo no saldrá. Sígueme para más guías."),
    ],
)
