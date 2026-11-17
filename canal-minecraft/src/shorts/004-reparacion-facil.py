# -*- coding: utf-8 -*-
# Short de guía. Datos comprobados: ver src/videos/004-como-conseguir-reparacion.py.
SHORT = dict(
    slug="004-reparacion-facil",
    date="2026-11-18",
    theme="superficie",
    title="Cómo conseguir REPARACIÓN fácil en Minecraft (truco del atril) 📚 #minecraft #shorts",
    desc="El truco del atril para conseguir Reparación con un aldeano bibliotecario, paso a paso. En mundos normales, sin el experimento de reequilibrio del comercio.",
    tags=["minecraft", "reparacion minecraft", "mending", "aldeano bibliotecario", "truco del atril", "minecraft aldeanos", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #reparacion",
    scenes=[
        dict(t="title", h="REPARACIÓN FÁCIL", badge="TRUCO", splash="¡Para siempre!", hero=("sprite", "book"), glint=True,
             say="Así se consigue Reparación, el mejor encantamiento de Minecraft, sin depender de la suerte."),
        dict(t="bullets", h="NECESITAS",
             items=[(("sprite", "emerald"), "Un aldeano sin oficio"), (("sprite", "lectern"), "Un atril"),
                    (("sprite", "emerald"), "Esmeraldas"), (("sprite", "book"), "Un libro")],
             say="Necesitas un aldeano sin oficio, un atril, esmeraldas y un libro."),
        dict(t="tip", n="1", badge="PASO 1", h="Pon el atril a su lado", hero=("sprite", "lectern"),
             say="Encierra al aldeano y pon el atril a su lado: se convertirá en bibliotecario."),
        dict(t="tip", n="2", badge="PASO 2", h="¿No vende Reparación?", s="Rompe el atril y vuelve a ponerlo", hero=("sprite", "pick_iron"),
             say="Mira sus ofertas. Si no vende Reparación, rompe el atril y vuelve a ponerlo: sus ofertas cambian."),
        dict(t="card", warn=True, h="NO COMERCIES ANTES", s="Un solo intercambio y sus ofertas se quedan fijas", hero=("sprite", "emerald"), glowcol=(60, 220, 120),
             say="Repite hasta que salga. Pero no comercies con él antes, o sus ofertas se quedarán fijas para siempre."),
        dict(t="card", badge="PASO 3", h="COMPRA Y COMBINA", s="Libro + pico en un yunque. (En mundos sin el experimento de comercio)", hero=("sprite", "book"), glint=True,
             say="Compra el libro y júntalo con tu pico en un yunque. Sígueme para más trucos de Minecraft."),
    ],
)
