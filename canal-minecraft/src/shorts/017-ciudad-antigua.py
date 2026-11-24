# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 24/11/2026 (Minecraft Wiki; contenido de la 1.19 "The Wild", Java y Bedrock):
# - Las ciudades antiguas están en el bioma Oscuridad profunda, a la altura Y -51; ese bioma suele estar bajo montañas.
# - Los sensores de sculk detectan vibraciones; ir agachado no las produce, y caminar sobre lana tampoco.
# - Los chilladores de sculk dan Oscuridad y, al cuarto aviso, invocan al Warden.
# - El Warden es ciego, se guía por vibraciones y olor; es el mob con más vida (más que el Wither y el dragón).
#   Los proyectiles (p. ej. bolas de nieve) crean vibraciones donde caen y lo distraen.
# - Botín: libros con Sigilo veloz (solo aquí), manzanas de oro encantadas, fragmentos de disco y fragmentos de eco
#   (para la brújula de recuperación, que apunta a donde moriste).
SHORT = dict(
    slug="017-ciudad-antigua",
    date="2026-11-25",
    theme="cueva",
    title="Cómo entrar en una CIUDAD ANTIGUA sin despertar al WARDEN 🤫 #minecraft #shorts",
    desc="Dónde están las ciudades antiguas, cómo moverte sin activar el sculk, qué hacer si aparece el Warden y qué botín vas a encontrar.",
    tags=["minecraft", "ciudad antigua", "warden", "oscuridad profunda", "deep dark", "sculk", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #warden",
    scenes=[
        dict(t="title", h="CIUDAD ANTIGUA", badge="GUÍA", splash="¡Silencio!", hero=("cube", "sculk"),
             say="Así entras en una ciudad antigua y sales con el botín sin despertar al Warden."),
        dict(t="stat", big="Y -51", label="Oscuridad profunda", small="Suelen estar bajo las montañas", hero=("cube", "sculk"),
             say="Están en el bioma de la Oscuridad profunda, en la capa Y -51, y suelen estar bajo las montañas."),
        dict(t="card", badge="REGLA Nº 1", h="CAMINA AGACHADO", s="Así el sculk no detecta tus pasos. Sobre lana, tampoco", hero=("sprite", "boots"),
             say="Camina siempre agachado: así los sensores de sculk no detectan tus pasos. Y caminar sobre lana tampoco hace ruido."),
        dict(t="card", warn=True, h="CUIDADO CON LOS CHILLIDOS", s="Al cuarto aviso, aparece el Warden", hero=("sprite", "skull"), glowcol=(60, 200, 210),
             say="Si activas los bloques de sculk que chillan, te dejan a oscuras, y al cuarto aviso aparece el Warden."),
        dict(t="card", badge="SI APARECE", h="NO PELEES", s="Lanza bolas de nieve lejos: irá hacia el ruido", hero=("sprite", "iceball"),
             say="Si aparece, no pelees: tiene más vida que el Wither y el dragón. Es ciego, así que lanza bolas de nieve lejos de ti: irá hacia el ruido."),
        dict(t="bullets", h="EL BOTÍN",
             items=[(("sprite", "book"), "Libros con un encantamiento que solo sale aquí"),
                    (("sprite", "apple_gold"), "Manzanas de oro encantadas"),
                    (("sprite", "disc"), "Fragmentos de disco"),
                    (("sprite", "echo_shard"), "Fragmentos de eco: brújula de recuperación")],
             say="El premio: libros con un encantamiento que solo sale aquí, manzanas de oro encantadas, fragmentos de disco y fragmentos de eco, para la brújula que te lleva a donde moriste. Sígueme para más guías."),
    ],
)
