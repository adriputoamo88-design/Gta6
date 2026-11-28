# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 28/11/2026 (Minecraft Wiki; Java y Bedrock):
# - Lobo: huesos. Gato: bacalao o salmón crudo. Caballo: montarlo con la mano vacía hasta que salgan corazones (luego silla de montar).
# - Loro: semillas; las galletas son venenosas para él.
# - Zorro: se crían dos adultos con bayas dulces y la cría confía en el jugador.
SHORT = dict(
    slug="026-domesticar-animales",
    date="2026-11-29",
    theme="superficie",
    title="Cómo DOMESTICAR animales en Minecraft (lobo, gato, caballo, loro y zorro) 🐾 #minecraft #shorts",
    desc="Qué necesitas para domesticar un lobo, un gato, un caballo, un loro y un zorro en Minecraft, y lo que nunca debes darle a un loro.",
    tags=["minecraft", "domesticar animales", "como domesticar un lobo", "como domesticar un gato", "domesticar caballo", "mascotas minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #mascotas",
    scenes=[
        dict(t="title", h="DOMESTICA ANIMALES", badge="GUÍA", splash="¡Mascotas!", hero=("sprite", "heart"),
             say="Cómo domesticar los animales más útiles de Minecraft."),
        dict(t="tip", n="1", badge="LOBO", h="Huesos", s="Hasta que salgan corazones. Te defenderá", hero=("sprite", "bone"),
             say="Uno: al lobo, dale huesos hasta que aparezcan corazones. Te defenderá."),
        dict(t="tip", n="2", badge="GATO", h="Pescado crudo", s="Bacalao o salmón. Y asusta a los creepers", hero=("sprite", "heart"),
             say="Dos: al gato, dale bacalao o salmón crudo. Y además asusta a los creepers."),
        dict(t="tip", n="3", badge="CABALLO", h="Móntalo", s="Con la mano vacía, hasta que salgan corazones", hero=("sprite", "apple"),
             say="Tres: al caballo, móntate con la mano vacía una y otra vez, hasta que salgan corazones. Luego ponle una silla de montar."),
        dict(t="tip", n="4", badge="LORO", h="Semillas", s="¡Nunca le des galletas!", hero=("sprite", "seeds"),
             say="Cuatro: al loro, dale semillas. Nunca le des galletas: son venenosas para él."),
        dict(t="tip", n="5", badge="ZORRO", h="Cría dos zorros", s="Con bayas dulces: la cría confía en ti", hero=("sprite", "heart"),
             say="Y cinco: el zorro es el más difícil. Cría dos zorros adultos con bayas dulces, y la cría confiará en ti. Sígueme para más guías."),
    ],
)
