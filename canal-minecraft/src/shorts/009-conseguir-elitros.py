# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 20/11/2026 (mecánicas estables en Java y Bedrock; Minecraft Wiki):
# - Al derrotar al dragón aparece un portal de acceso (end gateway); se entra lanzando una perla de Ender dentro.
# - Lleva a las islas exteriores, donde están las ciudades del End (torres de púrpur).
# - Solo las ciudades con barco del End tienen élitros: están en un marco dentro del barco, junto a dos cofres.
# - Los proyectiles de los shulkers dan Levitación; la leche quita los efectos; la caída lenta evita el daño.
# - Para volar: saltar y volver a pulsar saltar en el aire con los élitros puestos; los cohetes dan impulso.
SHORT = dict(
    slug="009-conseguir-elitros",
    date="2026-11-21",
    theme="end",
    title="Cómo conseguir ÉLITROS en Minecraft (las alas) 🪽 #minecraft #shorts",
    desc="Después del dragón: cómo entrar a las islas exteriores del End, qué ciudad del End tiene élitros, cómo protegerte de los shulkers y cómo volar.",
    tags=["minecraft", "elitros minecraft", "como conseguir elitros", "ciudad del end", "barco del end", "shulker", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #elitros",
    scenes=[
        dict(t="title", h="ÉLITROS", badge="GUÍA", splash="¡A volar!", hero=("sprite", "elytra"),
             say="Así se consiguen los élitros, las alas de Minecraft. Pero antes tienes que haber derrotado al dragón."),
        dict(t="card", badge="PASO 1", h="EL PORTAL PEQUEÑO", s="Lanza una perla de Ender dentro", hero=("sprite", "ender_pearl"),
             say="Al matar al dragón aparece un pequeño portal flotante. Lanza una perla de Ender dentro y te llevará a las islas exteriores del End."),
        dict(t="card", badge="PASO 2", h="UNA CIUDAD CON BARCO", s="Solo esas guardan los élitros", hero=("cube", "purpur"),
             say="Busca una ciudad del End: torres moradas muy altas. Solo las que tienen un barco flotante al lado guardan los élitros."),
        dict(t="card", warn=True, h="CUIDADO CON LOS SHULKERS", s="Te hacen levitar. La leche lo quita", hero=("sprite", "bucket_milk"), glowcol=(220, 200, 255),
             say="Cuidado con los shulkers: sus disparos te hacen levitar, y luego caes. Lleva leche, que quita la levitación, o pociones de caída lenta."),
        dict(t="card", badge="PASO 3", h="DENTRO DEL BARCO", s="En un marco en la pared, junto a dos cofres", hero=("sprite", "elytra"),
             say="Entra en el barco: los élitros están colgados en un marco en la pared, junto a dos cofres con buen botín."),
        dict(t="card", badge="PARA VOLAR", h="SALTA DOS VECES", s="Y con cohetes, vas mucho más rápido", hero=("sprite", "firework"),
             say="Para volar, póntelos, salta y vuelve a pulsar saltar en el aire. Con cohetes de fuegos artificiales irás mucho más rápido. Sígueme para más guías."),
    ],
)
