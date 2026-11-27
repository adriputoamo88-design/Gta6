# -*- coding: utf-8 -*-
"""Episodio del viernes 27/11/2026.
Fuentes: timesaver.gg, EGamers, 6cheats, GTA-Zone, RetroBroker, gmtreks (propiedades: casas francas por historia, solo garajes comprables,
sin negocios; número y precios de garajes según guías, aproximados); Nacionale, EndgameTools, TechWiser, JokingJoystick (Black Friday:
sin rebaja oficial en PS Store ni Microsoft Store; descuentos sueltos en tiendas y claves de terceros con riesgo).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e11-comprar-casas": "Viernes 27/11 · 18:00", "s11-black-friday": "Viernes 27/11 · 21:00"}

VIDEOS = [
dict(
 slug="e11-comprar-casas",
 theme="retro",
 title="¿Se pueden COMPRAR CASAS en GTA 6? Propiedades, garajes y negocios",
 thumb=dict(top="GTA 6", big="¿CASAS?", tag="LO QUE SE PUEDE\nCOMPRAR", icon="pin"),
 tags=["gta 6 comprar casas","gta 6 propiedades","gta 6 garajes","gta 6 negocios","gta 6 casas","gta 6 refugios","gta 6 safehouse","gta 6 que comprar","gta 6 dinero en que gastar","gta 6 español"],
 desc="¿Se pueden comprar casas o negocios en GTA 6? Te explicamos qué propiedades hay: los refugios que se desbloquean con la historia, los garajes que sí se pueden comprar y por qué no hay negocios como en GTA 5. Los precios y cantidades son aproximados según las guías.",
 scenes=[
  dict(t="title", h="¿SE PUEDEN COMPRAR CASAS?", s="Propiedades en GTA 6, explicadas",
       say="Una de las preguntas que más se repiten: ¿se pueden comprar casas en GTA 6? La respuesta corta te va a sorprender, sobre todo si vienes de GTA 5."),
  dict(t="icon", icon="pin", h="CASAS: NO", s="Los refugios llegan con la historia",
       say="Casas, no. Los refugios de Jason y Lucía se desbloquean a medida que avanzas en la historia, no se compran.", chapter="Casas"),
  dict(t="icon", icon="car", h="GARAJES: SÍ", s="Lo único que puedes comprar",
       say="Lo que sí puedes comprar son garajes. Es la única propiedad a la venta, y sirven para guardar tu colección de coches.", chapter="Garajes"),
  dict(t="steps", h="CÓMO COMPRARLOS", items=["Avanza al capítulo 2", "Abre la app inmobiliaria del móvil", "Elige el garaje y paga"],
       say="Se desbloquean en el segundo capítulo. A partir de ahí, abre la aplicación inmobiliaria del móvil y elige el que quieras."),
  dict(t="stat", big="~8", label="Garajes a la venta", small="Precios aproximados según las guías", icon="money",
       say="Según las guías, hay unos ocho garajes, con precios que van de unos pocos miles a varias decenas de miles de dólares. Y comprarlos todos da un trofeo.", chapter="Precios"),
  dict(t="icon", icon="bag", h="NEGOCIOS: NO", s="A diferencia de GTA 5: sin ingresos pasivos",
       say="¿Y negocios? Tampoco. No hay clubes, ni puertos deportivos, ni tiendas que te den dinero cada semana. Y las tiendas de la edición Ultimate son ventajas de acceso, no negocios tuyos.", chapter="Negocios"),
  dict(t="icon", icon="money", h="¿EN QUÉ GASTAR?", s="Armas, mejoras, coches y garajes",
       say="Entonces, ¿en qué gastar el dinero? En armas, mejoras, ropa para despistar a la policía, y garajes para tus mejores coches."),
  dict(t="icon", icon="question", h="POR CONFIRMAR", s="Número exacto de refugios",
       say="Un apunte: las guías no coinciden en cuántos refugios hay en total, si cuatro o cinco. Cuando esté claro, te lo cuento."),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s11-black-friday",
 theme="danger", short=True, short_title="¿GTA 6 rebajado en Black Friday?",
 title="¿GTA 6 REBAJADO en Black Friday? 🏷️",
 thumb=dict(top="GTA 6", big="¿BLACK\nFRIDAY?", tag="LA VERDAD", icon="money"),
 tags=["gta 6","gta 6 black friday","gta 6 oferta","gta 6 descuento","gta 6 shorts","gta 6 precio"],
 desc="GTA 6 no tiene rebaja oficial en PlayStation Store ni Microsoft Store por Black Friday. Algunas tiendas tienen descuentos puntuales; cuidado con las claves de vendedores no oficiales.",
 scenes=[
  dict(t="icon", icon="money", h="¿REBAJADO?", s="En las tiendas oficiales: no",
       say="¿GTA 6 está rebajado por Black Friday? En PlayStation Store y en Microsoft Store, no. Sigue a precio completo."),
  dict(t="icon", icon="warning", h="OJO CON LAS CLAVES", s="Vendedores no oficiales = riesgo",
       say="Alguna tienda tiene descuentos puntuales, pero cuidado con las claves baratas de vendedores no oficiales: pueden dar problemas."),
  dict(t="icon", icon="bell", h="TE AVISO", s="Cuando haya oferta de verdad",
       say="Sígueme y te aviso cuando haya una oferta de verdad."),
 ]),
]
