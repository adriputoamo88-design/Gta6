# -*- coding: utf-8 -*-
# Short de supervivencia. Comprobado el 24/11/2026 (Minecraft Wiki; Java y Bedrock):
# - Colocar agua justo antes de aterrizar anula el daño por caída (no en el Nether: el agua se evapora).
# - El escudo bloquea el daño de las explosiones que vienen de frente.
# - En dificultad difícil, los zombis pueden romper puertas de madera; las de hierro solo se abren con redstone (botón, palanca…).
# - La zanahoria dorada es de los alimentos con más saturación del juego.
# - Los aldeanos se pueden meter en una barca y llevarla, también por tierra (más despacio).
SHORT = dict(
    slug="018-trucos-supervivencia",
    date="2026-11-25",
    theme="superficie",
    title="5 trucos de SUPERVIVENCIA que nadie te contó 🛡️ #minecraft #shorts",
    desc="El cubo de agua que te salva de las caídas, el escudo contra los creepers, la puerta que los zombis no rompen, la mejor comida y cómo mover aldeanos.",
    tags=["minecraft", "trucos minecraft", "trucos de supervivencia", "minecraft supervivencia", "minecraft principiantes", "consejos minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #trucos",
    scenes=[
        dict(t="title", h="5 TRUCOS", badge="SUPERVIVENCIA", splash="¡No mueras!", hero=("sprite", "heart"),
             say="Cinco trucos de supervivencia que nadie te contó."),
        dict(t="tip", n="1", badge="CAÍDAS", h="Cubo de agua", s="Colócala justo antes de tocar el suelo", hero=("sprite", "bucket_water"),
             say="Uno: si caes desde muy alto, coloca agua justo antes de tocar el suelo, y no te harás daño."),
        dict(t="tip", n="2", badge="CREEPERS", h="Levanta el escudo", s="Bloquea la explosión si lo miras de frente", hero=("sprite", "shield"),
             say="Dos: si un creeper va a explotar, levanta el escudo mirándolo de frente. Bloquea el daño."),
        dict(t="tip", n="3", badge="ZOMBIS", h="Puertas de hierro", s="En difícil, los zombis rompen las de madera", hero=("cube", "iron_block"),
             say="Tres: en difícil, los zombis pueden romper las puertas de madera. Usa puertas de hierro, con un botón."),
        dict(t="tip", n="4", badge="COMIDA", h="Zanahoria dorada", s="De lo que más te sacia", hero=("sprite", "carrot_gold"),
             say="Cuatro: la zanahoria dorada es de las comidas que más te sacian."),
        dict(t="tip", n="5", badge="ALDEANOS", h="Llévalos en barca", s="También por tierra, aunque más despacio", hero=("sprite", "emerald"),
             say="Y cinco: para llevar un aldeano a tu base, mételo en una barca. Funciona también por tierra, aunque va más despacio. Sígueme para más trucos."),
    ],
)
