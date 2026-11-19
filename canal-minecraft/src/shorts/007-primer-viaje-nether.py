# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 19/11/2026 (mecánicas estables en Java y Bedrock; Minecraft Wiki):
# - Portal mínimo: marco de 4x5 sin esquinas = 10 bloques de obsidiana; se enciende con mechero (pedernal y acero).
# - Con al menos una pieza de armadura de oro, los piglins no atacan; se enfadan si abres cofres o picas oro delante de ellos.
# - En el Nether las camas explotan y el agua se evapora al colocarla.
# - Las bolas de fuego de los ghasts se pueden devolver golpeándolas.
# - La poción de resistencia al fuego evita el daño de la lava y del fuego.
# - La brújula normal no funciona en el Nether (gira sin rumbo).
SHORT = dict(
    slug="007-primer-viaje-nether",
    date="2026-11-20",
    theme="nether",
    title="Tu PRIMER viaje al NETHER: 5 cosas que debes saber 🔥 #minecraft #shorts",
    desc="Antes de entrar al Nether por primera vez: cómo hacer el portal, el truco del oro con los piglins, por qué no sirven las camas ni el agua, cómo devolver las bolas de fuego y cómo no perderte.",
    tags=["minecraft", "nether minecraft", "primer viaje al nether", "portal del nether", "piglins", "minecraft supervivencia", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #nether",
    scenes=[
        dict(t="title", h="EL NETHER", badge="GUÍA", splash="¡Quema!", hero=("sprite", "nether_portal"),
             say="Cinco cosas que tienes que saber antes de entrar al Nether por primera vez."),
        dict(t="stat", big="10", label="de obsidiana", small="Marco de 4x5 sin esquinas. Se enciende con un mechero", hero=("cube", "obsidian"),
             say="Para el portal necesitas diez bloques de obsidiana: un marco de cuatro por cinco sin las esquinas. Lo enciendes con un mechero."),
        dict(t="tip", n="1", badge="LO MÁS IMPORTANTE", h="Lleva algo de oro puesto", s="Los piglins no te atacarán", hero=("sprite", "gold_ingot"),
             say="Uno: lleva al menos una pieza de armadura de oro, y los piglins no te atacarán. Pero se enfadan si abres cofres o picas oro delante de ellos."),
        dict(t="tip", n="2", badge="NO FUNCIONA", h="Ni camas ni agua", s="Las camas explotan y el agua se evapora", hero=("sprite", "bed"),
             say="Dos: no intentes dormir, porque las camas explotan. Y el agua se evapora, así que el cubo de agua no te salvará."),
        dict(t="tip", n="3", badge="TRUCO", h="Devuelve las bolas de fuego", s="Golpéalas y vuelven al ghast", hero=("sprite", "sword_diamond"),
             say="Tres: si un ghast te dispara, golpea la bola de fuego para devolvérsela."),
        dict(t="tip", n="4", badge="SEGURO DE VIDA", h="Resistencia al fuego", s="Si caes en la lava, te salva", hero=("sprite", "potion_fire"),
             say="Cuatro: lleva pociones de resistencia al fuego. Si caes en la lava, te salvan la vida."),
        dict(t="tip", n="5", badge="NO TE PIERDAS", h="Apunta tu portal", s="La brújula normal no funciona aquí", hero=("sprite", "map"),
             say="Y cinco: apunta las coordenadas de tu portal, porque la brújula normal no funciona en el Nether. Sígueme para la guía de la netherita."),
    ],
)
