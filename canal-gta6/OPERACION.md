# Manual de operación diaria · ZONA LEONIDA

Este archivo lo sigue la tarea programada que lleva el canal cada mañana a las 07:47, hora de España.
**Objetivo diario:** producir **2 piezas listas para subir**: 1 vídeo horizontal (1:30–3:00) y 1 Short vertical (15–45 s).

## Pasos
1. `git fetch origin claude/gta6-channel-videos-gr26ku && git checkout claude/gta6-channel-videos-gr26ku && git pull`
2. `bash canal-gta6/setup.sh` (si imprime una línea `export PYTHONPATH=...`, úsala antes de renderizar)
3. Lee `canal-gta6/diario/REGISTRO.md` para no repetir temas y para ver qué se ha publicado.
4. **Investiga** con WebSearch las noticias de GTA 6 de las últimas 24-48 h y lo que más busca la gente: trucos confirmados, dinero, misiones, secretos, easter eggs, problemas técnicos, parches, online, PC, ventas o récords. Usa fuentes fiables (Rockstar Newswire, Vandal, 3DJuegos, IGN, Eurogamer, GamesRadar…). **Nunca inventes datos.** Si algo no está confirmado, dilo en el guion ("según…", "por confirmar").
5. Elige 2 temas:
   - Uno para el **vídeo largo**: el de mayor demanda de búsqueda que aún no hayamos cubierto.
   - Uno para el **Short**: una respuesta rápida o un dato curioso.
6. Crea `canal-gta6/src/episodios/AAAA-MM-DD.py` con la fecha de hoy, copiando la estructura de `episodios/2026-11-18.py`:
   - slugs: `eNN-…` para el vídeo largo y `sNN-…` para el Short, con la numeración siguiente a la del registro.
   - el Short lleva `short=True`, `short_title=…` y de 2 a 4 escenas.
   - el vídeo largo lleva de 8 a 12 escenas con `chapter=` en las principales y termina con `dict(t="outro", say=OUTRO_SAY)`.
   - usa un `theme` distinto al del día anterior: sunset, neon, danger, money, ocean o retro.
   - rellena `PUBLICAR = {slug: "Día DD/MM · HH:MM"}`. Horas recomendadas en España: vídeo largo a las 18:00 y Short a las 21:00. Los fines de semana, a las 12:00 y a las 20:00.
   - escribe en `say` los números como palabras cuando sean años o precios ("dos mil veintiséis"). Si un nombre en inglés suena mal, añádelo a `PRON` en `content.py`.
7. Renderiza:
   ```bash
   cd canal-gta6/src
   E=episodios/AAAA-MM-DD.py
   CANAL_EPISODIO=$E python3 render.py && CANAL_EPISODIO=$E python3 branding.py && CANAL_EPISODIO=$E python3 branding.py meta
   ```
8. **Control de calidad.** Extrae 3 fotogramas de cada vídeo con ffmpeg y míralos. Comprueba que no hay texto cortado ni solapado, y que hay audio (`ffprobe`). Si algo falla, corrígelo y vuelve a renderizar.
9. Escribe `canal-gta6/diario/AAAA-MM-DD/LEEME.md` con lo que tiene que hacer el dueño del canal:
   - qué subir y a qué hora;
   - dónde está el título, la descripción y las etiquetas (`metadatos/`);
   - la miniatura;
   - los subtítulos;
   - en el Short: subirlo desde el móvil o desde Studio sin miniatura.
10. Añade una línea por pieza a `canal-gta6/diario/REGISTRO.md` con la fecha, el slug, el título y la hora de publicación.
11. Haz commit (sin la carpeta `build/`) y `git push origin claude/gta6-channel-videos-gr26ku`. Si el push a esa rama se rechaza, sube a la rama que te asigne la sesión e indícalo en el resumen.
12. Termina con un resumen breve en español para el dueño: qué temas has elegido y por qué, qué tiene que subir hoy y a qué hora, y qué datos siguen sin confirmar.

## Reglas
- No uses capturas, logotipos, arte ni música de Rockstar u otros. Todo debe ser generado por el motor.
- No toques los 10 vídeos de lanzamiento (`canal-gta6/videos/`).
- Si el dueño deja estadísticas o peticiones en `canal-gta6/diario/PETICIONES.md`, tenlas en cuenta primero.
