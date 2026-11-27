# -*- coding: utf-8 -*-
# Short de supervivencia para principiantes. Comprobado el 27/11/2026 (Minecraft Wiki; Java y Bedrock):
# - Cavar en vertical puede hacerte caer a cuevas o lava.
# - El diamante necesita pico de hierro o mejor; con uno de piedra no suelta nada.
# - Mirar a un Enderman a la cara (sin calabaza tallada) hace que te ataque.
# - Los monstruos aparecen en zonas sin luz de bloques, también dentro de casa.
# - Sin cama, al morir reapareces en el punto de aparición del mundo.
SHORT = dict(
    slug="024-errores-principiante",
    date="2026-11-28",
    theme="noche",
    title="5 ERRORES de principiante en Minecraft (¿cuántos cometes?) ❌ #minecraft #shorts",
    desc="Cinco errores típicos de principiante que te hacen perder la partida en Minecraft, y cómo evitarlos.",
    tags=["minecraft", "errores minecraft", "minecraft principiantes", "consejos minecraft", "minecraft supervivencia", "como no morir minecraft", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #principiantes",
    scenes=[
        dict(t="title", h="5 ERRORES", badge="PRINCIPIANTES", splash="¡No los cometas!", hero=("sprite", "skull"),
             say="Cinco errores de principiante que te hacen perder la partida. ¿Cuántos has cometido tú?"),
        dict(t="tip", n="1", badge="ERROR", h="Cavar en vertical", s="Puedes caer en una cueva o en lava", hero=("sprite", "bucket_lava"),
             say="Uno: cavar en vertical bajo tus pies. Puedes caer a una cueva, o a un lago de lava."),
        dict(t="tip", n="2", badge="ERROR", h="Diamante con pico de piedra", s="Lo rompes y no te da nada", hero=("sprite", "diamond"),
             say="Dos: picar diamantes con un pico de piedra. Rompes el bloque y no te da nada. Necesitas uno de hierro."),
        dict(t="tip", n="3", badge="ERROR", h="Mirar a un Enderman", s="Si lo miras a la cara, te ataca", hero=("sprite", "ender_pearl"),
             say="Tres: mirar a un Enderman a la cara. Se enfada y va a por ti."),
        dict(t="tip", n="4", badge="ERROR", h="Casa a oscuras", s="Los monstruos aparecen donde no hay luz", hero=("sprite", "torch"),
             say="Cuatro: dejar tu casa a oscuras. Los monstruos aparecen donde no hay luz, también dentro."),
        dict(t="tip", n="5", badge="ERROR", h="Morir sin cama", s="Reapareces en el inicio del mundo", hero=("sprite", "bed"),
             say="Y cinco: no dormir nunca en una cama. Si mueres, reapareces en el inicio del mundo, que puede estar lejísimos. Sígueme para más consejos."),
    ],
)
