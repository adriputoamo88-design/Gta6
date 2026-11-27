# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 27/11/2026 (Minecraft Wiki "Happy Ghast", "Dried Ghast", "Harness"; game drop
# "Chase the Skies" de 2025, Java y Bedrock):
# - El ghast seco aparece en los valles de arena de almas del Nether y se fabrica con 8 lágrimas de ghast + 1 arena de almas.
# - En agua se rehidrata en unos 20 minutos y nace una cría de ghast; tarda otros ~20 minutos en crecer; las bolas de nieve aceleran el crecimiento.
# - Arnés = 3 de cuero + 2 de cristal + 1 de lana. Con el arnés, el ghast feliz lleva hasta 4 jugadores.
SHORT = dict(
    slug="023-ghast-feliz",
    date="2026-11-28",
    theme="superficie",
    title="Cómo conseguir un GHAST FELIZ y volar en Minecraft ☁️ #minecraft #shorts",
    desc="Dónde encontrar o cómo fabricar un ghast seco, cómo hacer que nazca y crezca más rápido, la receta del arnés y cuántos jugadores pueden volar a la vez.",
    tags=["minecraft", "ghast feliz", "happy ghast", "como conseguir un ghast feliz", "ghast seco", "arnes minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #ghastfeliz",
    scenes=[
        dict(t="title", h="GHAST FELIZ", badge="GUÍA", splash="¡A volar!", hero=("sprite", "harness"),
             say="Así se consigue un Ghast feliz, un mob al que te puedes subir para volar por el cielo."),
        dict(t="card", badge="PASO 1", h="UN GHAST SECO", s="En los valles de arena de almas, o con 8 lágrimas de ghast + 1 arena de almas", hero=("cube", "soul_sand"),
             say="Primero necesitas un bloque de ghast seco. Se encuentra en los valles de arena de almas del Nether, o se fabrica con ocho lágrimas de ghast y un bloque de arena de almas."),
        dict(t="card", badge="PASO 2", h="PONLO EN AGUA", s="En unos 20 minutos nace un ghast bebé", hero=("sprite", "bucket_water"),
             say="Colócalo en agua y espera: en unos veinte minutos se rehidrata y nace un ghast bebé."),
        dict(t="card", badge="PASO 3", h="QUE CREZCA", s="Dale bolas de nieve y crecerá más rápido", hero=("sprite", "iceball"),
             say="El bebé tarda otros veinte minutos en crecer. Si le das bolas de nieve, crece más rápido."),
        dict(t="bullets", h="EL ARNÉS", items=["3 de cuero", "2 de cristal", "1 de lana"],
             say="Para montarlo, ponle un arnés: se fabrica con tres de cuero, dos de cristal y una lana."),
        dict(t="card", badge="¡LISTO!", h="A VOLAR", s="Caben hasta 4 jugadores", hero=("sprite", "harness"),
             say="Súbete y vuela. Caben hasta cuatro jugadores a la vez. Sígueme para más guías."),
    ],
)
