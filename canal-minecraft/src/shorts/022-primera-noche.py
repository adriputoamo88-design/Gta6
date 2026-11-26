# -*- coding: utf-8 -*-
# Short de supervivencia para principiantes. Comprobado el 26/11/2026 (Minecraft Wiki; Java y Bedrock):
# - Un día completo dura 20 minutos; la parte de día, unos 10.
# - Madera -> mesa de trabajo y herramientas; piedra -> herramientas de piedra.
# - 1 carbón (o carbón vegetal) + 1 palo = 4 antorchas.
# - Cama = 3 de lana + 3 tablones; dormir salta la noche y fija el punto de reaparición.
SHORT = dict(
    slug="022-primera-noche",
    date="2026-11-27",
    theme="superficie",
    title="Tu PRIMERA NOCHE en Minecraft: qué hacer en 10 minutos 🌙 #minecraft #shorts",
    desc="Los cinco pasos para sobrevivir a tu primera noche en Minecraft: madera, piedra, antorchas, cama y refugio.",
    tags=["minecraft", "primera noche minecraft", "minecraft principiantes", "como empezar en minecraft", "minecraft supervivencia", "consejos minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #principiantes",
    scenes=[
        dict(t="title", h="TU PRIMERA NOCHE", badge="PRINCIPIANTES", splash="¡Sobrevive!", hero=("sprite", "bed"),
             say="Lo que tienes que hacer en tus primeros diez minutos de Minecraft para sobrevivir a la primera noche."),
        dict(t="tip", n="1", badge="MADERA", h="Tala árboles", s="Mesa de trabajo y primeras herramientas", hero=("cube", "log_top", "log"),
             say="Uno: tala árboles. Con la madera haces una mesa de trabajo y tus primeras herramientas."),
        dict(t="tip", n="2", badge="PIEDRA", h="Pico de piedra", s="Y una espada de piedra", hero=("sprite", "pick_stone"),
             say="Dos: consigue piedra y hazte un pico y una espada de piedra."),
        dict(t="tip", n="3", badge="LUZ", h="Carbón y antorchas", s="1 carbón + 1 palo = 4 antorchas", hero=("sprite", "torch"),
             say="Tres: busca carbón. Con un carbón y un palo haces cuatro antorchas."),
        dict(t="tip", n="4", badge="DORMIR", h="Fabrica una cama", s="3 de lana + 3 tablones", hero=("sprite", "bed"),
             say="Cuatro: consigue tres de lana de las ovejas y fabrica una cama con tres tablones. Dormir te salta la noche."),
        dict(t="tip", n="5", badge="PLAN B", h="Refugio", s="Sin cama: cava un hueco, tápalo y pon una antorcha", hero=("cube", "dirt"),
             say="Y cinco: si llega la noche sin cama, cava un refugio, tápalo y pon una antorcha dentro. Sígueme para más trucos de principiante."),
    ],
)
