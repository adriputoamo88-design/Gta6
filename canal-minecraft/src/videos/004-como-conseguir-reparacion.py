# -*- coding: utf-8 -*-
# Guía. Comprobado el 17/11/2026 (guías de comercio con aldeanos para la 26.3: minecraftmaps.com, syntaxmine.com,
# craftmc.net, villageroll.com).
# - Truco del atril: un bibliotecario con el que NO has comerciado cambia sus ofertas si rompes y vuelves a poner su atril.
#   Con un solo intercambio, el oficio y las ofertas quedan fijos.
# - Atril: 4 losas de madera + 1 estantería. Los aldeanos de bata verde no aceptan oficio.
# - Precio del libro de Reparación en Java: 10-38 esmeraldas + 1 libro.
# - Experimento "reequilibrio del comercio de aldeanos" (opcional, al crear el mundo): Reparación solo en bibliotecarios de pantano.
# - Reparación también puede salir pescando (tesoro) y en libros encantados de cofres de estructuras. Nunca en la mesa.
from content import OUTRO

VIDEO = dict(
    slug="004-como-conseguir-reparacion",
    date="2026-11-18",
    hashtags="#Reparacion #MinecraftGuia",
    theme="superficie",
    title="Cómo conseguir REPARACIÓN fácil en Minecraft (el truco del ATRIL paso a paso)",
    thumb=dict(top="TRUCO FÁCIL", big="REPARACIÓN\nFÁCIL", tag="EL TRUCO DEL ATRIL", hero=("sprite", "book"), hero2=("sprite", "lectern")),
    tags=["minecraft", "reparacion minecraft", "como conseguir reparacion", "mending minecraft", "aldeano bibliotecario",
          "truco del atril", "libro de reparacion", "minecraft aldeanos", "minecraft encantamientos", "minecraft guia",
          "minecraft supervivencia", "minecraft español", "minecraft trucos", "comercio aldeanos"],
    desc=("Reparación es el mejor encantamiento de Minecraft y no sale en la mesa de encantamientos. Te enseñamos el truco más fiable "
          "para conseguirlo: un aldeano bibliotecario y un atril. Paso a paso, qué necesitas, el error que lo arruina todo "
          "y qué cambia si juegas con el experimento de reequilibrio del comercio."),
    scenes=[
        dict(t="title", h="REPARACIÓN FÁCIL", s="El truco del aldeano bibliotecario", badge="GUÍA", splash="¡Para siempre!",
             hero=("sprite", "book"), glint=True,
             say="Reparación es el mejor encantamiento de Minecraft, pero no sale en la mesa de encantamientos. Hoy te enseño el truco más fiable para conseguirlo: un aldeano bibliotecario y un atril. Paso a paso."),
        dict(t="news", badge="¿QUÉ HACE?", h="ARREGLA CON EXPERIENCIA", hero=("sprite", "xp"),
             s="La experiencia que recoges se usa primero para reparar el objeto con Reparación que llevas en la mano o puesto.",
             say="Primero, cómo funciona. Si llevas en la mano o puesto un objeto dañado con Reparación, la experiencia que recoges se usa primero para arreglarlo. Por eso tu mejor pico puede durarte para siempre.",
             chapter="Qué hace"),
        dict(t="bullets", h="LO QUE NECESITAS",
             items=[(("sprite", "lectern"), "Un atril: 4 losas de madera + 1 estantería"),
                    (("sprite", "emerald"), "Esmeraldas: el libro cuesta entre 10 y 38 en Java"),
                    (("sprite", "book"), "Un libro normal para pagar")],
             say="Vas a necesitar un aldeano sin oficio y un atril, que se fabrica con cuatro losas de madera y una estantería. También esmeraldas, porque en Java el libro suele costar entre diez y treinta y ocho, y un libro normal para pagar.",
             chapter="Lo que necesitas"),
        dict(t="tip", n="1", badge="PASO 1", h="Encierra a un aldeano sin oficio", hero=("sprite", "emerald"),
             s="Los de bata verde no sirven: nunca aceptan ningún trabajo.",
             say="Paso uno: busca un aldeano sin oficio y enciérralo, por ejemplo en un hueco de un bloque. Los de bata verde no sirven: nunca aceptan ningún trabajo.",
             chapter="Paso a paso"),
        dict(t="tip", n="2", badge="PASO 2", h="Pon el atril a su lado", hero=("sprite", "lectern"),
             s="Se convierte en bibliotecario. Abre su menú de comercio y mira qué libros ofrece.",
             say="Paso dos: coloca el atril a su lado. En unos segundos verás unas partículas verdes: ya es bibliotecario. Abre su menú de comercio y mira qué libros ofrece."),
        dict(t="tip", n="3", badge="PASO 3", h="¿No sale? Rompe el atril", hero=("sprite", "pick_iron"),
             s="Vuelve a ponerlo: el aldeano pierde el oficio, lo recupera y sus ofertas cambian.",
             say="Paso tres: si no ofrece Reparación, rompe el atril y vuelve a ponerlo. El aldeano pierde el oficio, lo recupera, y sus ofertas cambian. Repite hasta que salga el libro. A veces tarda bastantes intentos, así que paciencia."),
        dict(t="icon", warn=True, h="NO COMERCIES ANTES DE TIEMPO", s="Con un solo intercambio, sus ofertas se quedan fijas para siempre",
             hero=("sprite", "emerald"), glowcol=(60, 220, 120),
             say="Lo más importante: no comercies con él hasta que salga Reparación. En cuanto haces un solo intercambio, el aldeano se queda con ese oficio y esas ofertas para siempre, y el truco ya no funciona.",
             chapter="El error que lo arruina"),
        dict(t="news", badge="PASO 4", h="COMPRA Y COMBINA", hero=("sprite", "book"), glint=True,
             s="Junta el libro con tu pico, tu espada o tu armadura en un yunque.",
             toast=("¡CONSEGUIDO!", "Reparación desbloqueada", "book"),
             say="Paso cuatro: compra el libro, ve a un yunque y júntalo con tu pico, tu espada o tu armadura. Y si además le pones Irrompibilidad tres, tendrás herramientas prácticamente eternas."),
        dict(t="icon", h="OJO SI JUEGAS CON EXPERIMENTOS", s="Con el reequilibrio del comercio activado, solo lo venden los bibliotecarios de pantano",
             hero=("sprite", "book"),
             say="Un aviso: si creaste tu mundo con el experimento de reequilibrio del comercio de aldeanos activado, las reglas cambian, y Reparación solo la venden los bibliotecarios de los pantanos. En un mundo normal, el truco funciona sin problema.",
             chapter="Si usas experimentos"),
        dict(t="bullets", h="OTRAS FORMAS (CON SUERTE)",
             items=["Pescando: a veces sale como tesoro", "En libros encantados de cofres de algunas estructuras", "En la mesa de encantamientos: nunca"],
             say="¿Otras formas? Pescando, a veces sale como tesoro, y también puede aparecer en libros encantados de los cofres de algunas estructuras. Pero eso es pura suerte. El aldeano es lo más fiable."),
        dict(t="outro", h="¿CUÁNTOS INTENTOS?",
             say="¿Cuántas veces tuviste que romper el atril hasta que salió? Cuéntamelo en los comentarios. " + OUTRO),
    ],
)
