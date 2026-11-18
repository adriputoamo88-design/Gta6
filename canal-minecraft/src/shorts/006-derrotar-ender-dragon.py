# -*- coding: utf-8 -*-
# Short de guía. Comprobado el 18/11/2026 (mecánicas estables en Java y Bedrock; Minecraft Wiki):
# - Los cristales del End, sobre las torres de obsidiana, curan al dragón; algunos están enjaulados. Explotan al romperse.
# - Una calabaza tallada en la cabeza evita que los Enderman se enfaden al mirarlos.
# - Cuando el dragón se posa en el portal de salida, los golpes en la cabeza hacen el daño completo; su aliento deja una nube que hace daño.
# - En el End (y en el Nether) las camas explotan al intentar dormir.
# - Recompensa: mucha experiencia, el huevo del dragón (primera vez) y un portal de acceso a las islas exteriores (ciudades del End y élitros).
SHORT = dict(
    slug="006-derrotar-ender-dragon",
    date="2026-11-19",
    theme="end",
    title="Cómo matar al ENDER DRAGON paso a paso 🐉 #minecraft #shorts",
    desc="Qué llevar al End, por qué hay que romper primero los cristales, cuándo atacar al dragón y qué consigues al ganar.",
    tags=["minecraft", "ender dragon", "como matar al ender dragon", "dragon del end", "minecraft end", "cristales del end", "minecraft shorts", "minecraft español"],
    hashtags="#minecraft #shorts #minecraftespañol #enderdragon",
    scenes=[
        dict(t="title", h="ENDER DRAGON", badge="GUÍA", splash="¡Paso a paso!", hero=("cube", "end_stone"),
             say="Así derrotas al Ender Dragon, paso a paso."),
        dict(t="hotbar", h="QUÉ LLEVAR",
             items=[(("sprite", "bow"), "ARCO", "Con muchas flechas, o con Infinidad"),
                    (("sprite", "pumpkin"), "CALABAZA TALLADA", "En la cabeza: los Enderman no se enfadan si los miras"),
                    (("cube", "stone"), "BLOQUES", "Para subir a las torres"),
                    (("sprite", "bucket_water"), "CUBO DE AGUA", "Para las caídas"),
                    (("sprite", "apple"), "COMIDA", "Y tu mejor armadura")],
             say="Lleva un arco con muchas flechas, una calabaza tallada en la cabeza, para que los Enderman no se enfaden si los miras, bloques, un cubo de agua y comida."),
        dict(t="card", badge="PASO 1", h="ROMPE LOS CRISTALES", s="Curan al dragón. Y explotan al romperse", hero=("sprite", "end_crystal"), glowcol=(240, 120, 200),
             say="Paso uno: destruye los cristales de encima de las torres de obsidiana, porque curan al dragón. Dispárales con el arco, y a los enjaulados, sube con bloques. Ojo, que explotan."),
        dict(t="tip", n="2", badge="PASO 2", h="Cuando se pose, a la cabeza", s="Y aléjate de su aliento morado", hero=("sprite", "sword_diamond"),
             say="Paso dos: cuando el dragón se pose en el portal del centro, golpéale en la cabeza con la espada. Y aléjate de su aliento morado."),
        dict(t="card", warn=True, h="LAS CAMAS EXPLOTAN", s="Truco de expertos… muy arriesgado", hero=("sprite", "bed"), glowcol=(255, 120, 60),
             say="Truco de expertos: en el End, las camas explotan. Hay quien las usa contra el dragón cuando se posa, pero es muy arriesgado."),
        dict(t="card", badge="RECOMPENSA", h="HUEVO Y PORTAL", s="Mucha experiencia, el huevo del dragón y un portal a las islas exteriores", hero=("sprite", "xp"),
             say="Al ganar te llevas muchísima experiencia, el huevo del dragón y un portal a las islas exteriores, donde están los élitros. Sígueme para más guías."),
    ],
)
