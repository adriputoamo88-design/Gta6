# -*- coding: utf-8 -*-
"""Episodio del viernes 20/11/2026.
Fuentes: GameSpot, GamesRadar, TweakTown, Shacknews y Red Bull (trucos: 61, se desbloquean al acabar la historia, móvil + L1/R1, desactivan trofeos);
Sensor Tower vía Men's Journal, The Statesman y Noticias RCN (ventas estimadas del primer día). Take-Two (800 M$ de GTA V en 24 h, 2013).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content import OUTRO_SAY

PUBLICAR = {"e04-trucos-confirmados": "Viernes 20/11 · 15:00", "s04-record-ventas": "Viernes 20/11 · 21:00"}

VIDEOS = [
dict(
 slug="e04-trucos-confirmados",
 theme="danger",
 title="TRUCOS de GTA 6 CONFIRMADOS: cómo se DESBLOQUEAN y cómo se ponen (PS5 y Xbox)",
 thumb=dict(top="GTA 6", big="TRUCOS\nREALES", tag="CÓMO SE\nDESBLOQUEAN", icon="phone"),
 tags=["gta 6 trucos","trucos gta 6 ps5","trucos gta 6 xbox","gta 6 cheats","gta 6 como poner trucos","gta 6 truco dinero","gta 6 trucos desbloquear","gta 6 61 trucos","gta 6 claves","gta 6 español"],
 desc="Ya sabemos cómo funcionan los trucos de GTA 6: hay 61, se desbloquean al terminar la historia y se introducen con el móvil. Te explicamos cómo verlos, cómo ponerlos en PS5 y Xbox, y qué pasa con los trofeos. Algunas guías no coinciden en ciertos códigos: compruébalos en el menú del juego.",
 scenes=[
  dict(t="title", h="TRUCOS CONFIRMADOS", s="Cómo se desbloquean y cómo se ponen",
       say="El otro día te contamos que no había lista oficial de trucos. Ahora que el juego ha salido, ya sabemos cómo funcionan, y tienen una sorpresa que no le va a gustar a todo el mundo."),
  dict(t="stat", big="61", label="Trucos en el juego", small="Según GameSpot, GamesRadar y TweakTown", icon="phone",
       say="Según medios como GameSpot, GamesRadar o TweakTown, GTA 6 tiene sesenta y un trucos en PS5 y en Xbox.", chapter="Cuántos hay"),
  dict(t="icon", icon="warning", h="LA SORPRESA", s="Se desbloquean al terminar la historia",
       say="La sorpresa: no puedes usarlos desde el principio. Los trucos se desbloquean cuando terminas la historia principal. Y algunos piden además completar un reto aparte.", chapter="Cómo se desbloquean"),
  dict(t="icon", icon="swap", h="EN CADA PARTIDA", s="Si empiezas de nuevo, se vuelven a bloquear",
       say="Ojo, que esto va por partida: si empiezas un guardado nuevo, los trucos vuelven a estar bloqueados hasta que acabes otra vez la historia."),
  dict(t="steps", h="DÓNDE VER LA LISTA", items=["Abre el mapa", "Pestaña Progreso", "Desplázate a la derecha", "Menú Trucos"],
       say="Para ver la lista, abre el mapa, entra en la pestaña de progreso y desplázate del todo a la derecha: ahí está el menú de trucos, con todos sus códigos.", chapter="Dónde verlos"),
  dict(t="steps", h="CÓMO SE PONEN", items=["Cruceta arriba: saca el móvil", "Mantén L1 + R1 (LB + RB en Xbox)", "Introduce la combinación"],
       say="Para ponerlos: pulsa arriba en la cruceta para sacar el móvil, mantén pulsados L1 y R1, o LB y RB en Xbox, e introduce la combinación con la cruceta. A diferencia de GTA 4 y GTA 5, ya no se marcan números de teléfono.", chapter="Cómo se ponen"),
  dict(t="stat", big="$250.000", label="Truco de dinero", small="Arriba, dcha., abajo, izq., arriba, izq., abajo, dcha.", icon="money",
       say="Y sí: esta vez hay truco de dinero. Doscientos cincuenta mil dólares con arriba, derecha, abajo, izquierda, arriba, izquierda, abajo, derecha. Recuerda, solo después de acabar la historia.", chapter="Truco de dinero"),
  dict(t="icon", icon="trophy", h="ADIÓS TROFEOS", s="Usar un truco desactiva trofeos y logros",
       say="Importante: usar cualquier truco desactiva los trofeos y los logros. Si vas a por el platino, guarda antes en otra ranura."),
  dict(t="icon", icon="search", h="CUIDADO CON LAS LISTAS", s="Algunos códigos no coinciden entre guías",
       say="Y un aviso: las listas de internet no coinciden en algunos códigos. La referencia buena es el menú de trucos del propio juego. Y nada de webs que te pidan la contraseña: eso sigue siendo una estafa.", chapter="Aviso"),
  dict(t="outro", say=OUTRO_SAY),
 ]),
dict(
 slug="s04-record-ventas",
 theme="money", short=True, short_title="El primer día de GTA 6 en ventas",
 title="GTA 6 ha DESTROZADO el récord de GTA 5 💥",
 thumb=dict(top="GTA 6", big="RÉCORD", tag="PRIMER DÍA", icon="chart"),
 tags=["gta 6","gta 6 ventas","gta 6 record","gta 6 primer dia","gta 6 shorts","gta 6 millones"],
 desc="Según estimaciones de Sensor Tower, GTA 6 habría superado los 1.800 millones de dólares en su primer día. GTA 5 hizo 800 millones en 24 horas en 2013. Rockstar no ha publicado cifras oficiales.",
 scenes=[
  dict(t="stat", big="800 M$", label="GTA 5 · primeras 24 h", small="Récord de 2013", icon="trophy",
       say="En dos mil trece, GTA 5 hizo ochocientos millones de dólares en sus primeras veinticuatro horas. Era el récord."),
  dict(t="stat", big="+1.800 M$", label="GTA 6 · primer día", small="Estimación de Sensor Tower", icon="chart",
       say="GTA 6, según las estimaciones de Sensor Tower, habría superado los mil ochocientos millones el primer día. Más del doble."),
  dict(t="icon", icon="bell", h="SIN CIFRA OFICIAL", s="Rockstar aún no ha dado datos",
       say="Rockstar todavía no ha dado cifras oficiales. Sígueme y te lo cuento cuando las publique."),
 ]),
]
