# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 22/11/2026 (Minecraft Wiki "Iron Golem" y guías de granjas; ver fuentes en el mensaje del día):
# - JAVA: los aldeanos invocan gólems cuando entran en pánico (al ver un zombi) o cotillean; necesitan haber dormido
#   hace poco (unos 20 minutos de juego). Las granjas pequeñas usan 3 aldeanos con cama y un zombi que no los alcance.
# - El espacio donde aparece el gólem tiene que estar libre.
# - Cada gólem de hierro suelta 3-5 lingotes de hierro.
# - BEDROCK: el pánico no sirve; los gólems aparecen en aldeas con al menos 10 aldeanos y 20 camas.
SHORT = dict(
    slug="013-granja-de-hierro",
    date="2026-11-23",
    theme="superficie",
    title="Cómo funciona una GRANJA DE HIERRO en Minecraft (Java) ⚙️ #minecraft #shorts",
    desc="El truco de los 3 aldeanos y el zombi para que aparezcan gólems de hierro, cómo recoger el hierro y qué cambia en Bedrock.",
    tags=["minecraft", "granja de hierro", "iron farm", "golem de hierro", "granja de hierro minecraft java", "minecraft granjas", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #granjadehierro",
    scenes=[
        dict(t="title", h="GRANJA DE HIERRO", badge="JAVA", splash="¡Sin picar!", hero=("cube", "iron_block"),
             say="Hierro sin picar. Así funciona una granja de hierro en Minecraft Java."),
        dict(t="stat", big="3", label="aldeanos", small="Cada uno con su cama, y que hayan dormido hace poco", hero=("sprite", "bed"),
             say="Necesitas tres aldeanos, cada uno con su cama. Tienen que haber dormido hace poco para poder invocar gólems."),
        dict(t="card", warn=True, h="UN ZOMBI QUE LOS ASUSTE", s="Que lo vean, pero que no pueda llegar a ellos", hero=("sprite", "skull"), glowcol=(120, 220, 120),
             say="Pon un zombi donde lo vean pero no los pueda alcanzar. Al asustarse, los aldeanos invocan gólems de hierro."),
        dict(t="card", badge="RECOGIDA", h="LAVA Y TOLVA", s="Agua que los lleve a la lava y una tolva con cofre debajo", hero=("sprite", "bucket_lava"), glowcol=(255, 140, 40),
             say="Los gólems aparecen cerca. Con agua, llévalos hasta una cuchilla de lava, y pon debajo una tolva con un cofre para recoger el hierro."),
        dict(t="stat", big="3-5", label="lingotes", small="Por cada gólem", hero=("sprite", "iron_ingot"),
             say="Cada gólem suelta entre tres y cinco lingotes de hierro."),
        dict(t="card", badge="OJO", h="¿Y EN BEDROCK?", s="Ahí no funciona así: hace falta una aldea con 10 aldeanos y 20 camas", hero=("sprite", "emerald"),
             say="Ojo: en Bedrock no funciona así. Allí necesitas una aldea con al menos diez aldeanos y veinte camas. Sígueme para más granjas."),
    ],
)
