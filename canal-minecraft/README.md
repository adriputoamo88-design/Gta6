# BLOQUE A BLOQUE · Canal de Minecraft en español

Canal de Minecraft con **2 Shorts nuevos al día** (YouTube Shorts, TikTok, Reels). Cada Short trae guion, voz en off, animaciones, gráficos en pixel art, música, efectos de sonido, subtítulos grandes, portada, título, descripción y etiquetas.

## Shorts (formato principal)
Vídeo vertical de 1080x1920 que dura menos de 60 s. El diseño respeta las zonas de la app: arriba y abajo van los textos de YouTube y a la derecha los botones.

| # | Publicar | Título | Duración |
|---|---|---|---|
| 001 | 17/11 14:00 | La NUEVA actualización de Minecraft da MIEDO 🥶 | 41 s |
| 002 | 17/11 19:00 | Así encuentras DIAMANTES en Minecraft (la capa EXACTA) 💎 | 38 s |
| 003 | 18/11 14:00 | Los 5 MEJORES encantamientos de Minecraft (el nº 1 no sale en la mesa) ✨ | 37 s |
| 004 | 18/11 19:00 | Cómo conseguir REPARACIÓN fácil en Minecraft (truco del atril) 📚 | 32 s |
| 005 | 19/11 14:00 | Cómo encontrar una FORTALEZA en Minecraft (y abrir el portal del End) 👁️ | 39 s |
| 006 | 19/11 19:00 | Cómo matar al ENDER DRAGON paso a paso 🐉 | 44 s |
| 007 | 20/11 14:00 | Tu PRIMER viaje al NETHER: 5 cosas que debes saber 🔥 | 44 s |
| 008 | 20/11 19:00 | Cómo encontrar NETHERITE rápido en Minecraft (la capa EXACTA) ⛏️ | 41 s |
| 009 | 21/11 14:00 | Cómo conseguir ÉLITROS en Minecraft (las alas) 🪽 | 43 s |
| 010 | 21/11 19:00 | Las 5 POCIONES más útiles de Minecraft (y cómo hacerlas) 🧪 | 41 s |
| 011 | 22/11 14:00 | 5 formas de conseguir EXPERIENCIA rápido en Minecraft ✨ | 39 s |
| 012 | 22/11 19:00 | Cómo hacer un FARO en Minecraft (y todos sus poderes) 🔦 | 41 s |
| 013 | 23/11 14:00 | Cómo funciona una GRANJA DE HIERRO en Minecraft (Java) ⚙️ | 36 s |
| 014 | 23/11 19:00 | 5 SECRETOS de Minecraft que casi nadie conoce 🤫 | 31 s |
| 015 | 24/11 14:00 | Cámaras de DESAFÍO: llaves, Breeze y cómo conseguir la MAZA 🔨 | 47 s |
| 016 | 24/11 19:00 | La HISTORIA de Minecraft en 40 segundos 📜 | 40 s |
| 017 | 25/11 14:00 | Cómo entrar en una CIUDAD ANTIGUA sin despertar al WARDEN 🤫 | 43 s |
| 018 | 25/11 19:00 | 5 trucos de SUPERVIVENCIA que nadie te contó 🛡️ | 32 s |

- `shorts/NNN-....mp4`: el Short listo para subir.
- `shorts/metadatos/NNN-....txt`: título (con #shorts), descripción, etiquetas y hora de publicación.
- `shorts/portadas/` y `shorts/subtitulos/`: portada y subtítulos SRT.

**Subir un Short:** desde la app de YouTube (botón + → Short → elegir el vídeo), o desde YouTube Studio en el ordenador, porque un vídeo vertical de menos de 3 minutos se publica como Short automáticamente. Copia el título y la descripción del TXT. Marca "Contenido alterado o sintético: Sí". El mismo archivo sirve para TikTok e Instagram Reels.

## Vídeos largos (16:9)
Además hay versiones horizontales más largas (2-2:30 min) de los mismos temas, por si quieres usarlas en el canal principal.

```
canal-minecraft/
├── shorts/        ← SHORTS verticales (1080x1920) + metadatos, portadas y subtítulos
├── videos/        ← vídeos largos horizontales (1920x1080, 30 fps, H.264 + AAC, -14 LUFS)
├── miniaturas/    ← JPG de 1280x720
├── subtitulos/    ← SRT en español (súbelos como subtítulos en YouTube)
├── metadatos/     ← un TXT por vídeo: título, descripción, capítulos y etiquetas para copiar y pegar
├── canal/         ← banner 2560x1440, avatar 800x800 y descripción del canal
├── temas.md       ← temas publicados y próximos
├── PRODUCCION.md  ← cómo se hacen los 2 vídeos de cada día
└── src/           ← motor de vídeo y guiones (src/videos/NNN-slug.py)
```

## Vídeos

| # | Fecha | Título | Duración |
|---|---|---|---|
| 001 | 17/11/2026 | THE DEEP FREEZE: todo lo NUEVO de Minecraft (cuevas de hielo, Frostbite y hielo que se ROMPE) | 2:27 |
| 002 | 17/11/2026 | Cómo encontrar DIAMANTES rápido en Minecraft (la capa EXACTA y el mejor método) | 2:30 |
| 003 | 18/11/2026 | Los 10 MEJORES ENCANTAMIENTOS de Minecraft (y en qué herramienta va cada uno) | 2:31 |
| 004 | 18/11/2026 | Cómo conseguir REPARACIÓN fácil en Minecraft (el truco del ATRIL paso a paso) | 2:09 |

## Cómo subir cada vídeo (YouTube Studio → Crear → Subir vídeos)
1. Sube `videos/NNN-....mp4`.
2. Copia el **título**, la **descripción** y las **etiquetas** de `metadatos/NNN-....txt`.
3. En Miniatura, sube `miniaturas/NNN-....jpg`. Para subir miniaturas personalizadas tienes que verificar la cuenta por teléfono.
4. En Audiencia, marca **No, no es contenido para niños**.
5. En "Contenido alterado o sintético", marca **Sí**, porque la voz está generada por IA.
6. Categoría: **Videojuegos**. Idioma del vídeo: **Español**.
7. En Subtítulos, sube el archivo de `subtitulos/NNN-....srt`.
8. En Pantalla final, añade "Vídeo más reciente" y "Suscribirse" en los últimos 5 segundos. El vídeo ya termina pidiendo la suscripción.
9. Programa la publicación: el vídeo 1 a las **14:00** y el vídeo 2 a las **19:00**.

## Configuración del canal
- **Nombre:** BLOQUE A BLOQUE
- **Identificador:** @BloqueABloqueES. Comprueba que esté libre; si no, prueba @BloqueABloqueMC.
- **Foto de perfil:** `canal/avatar_800x800.png`
- **Banner:** `canal/banner_2560x1440.jpg` (el texto queda dentro de la zona segura)
- **Descripción:** `canal/descripcion_canal.txt`
- **Palabras clave:** minecraft, minecraft español, guías minecraft, trucos minecraft, novedades minecraft, minecraft supervivencia
- **Listas de reproducción:** "Guías de Minecraft", "Novedades de Minecraft" y "Trucos y curiosidades".

## Para que el canal crezca y se pueda monetizar
- **Constancia:** lo que más ayuda es publicar 2 vídeos al día a la misma hora.
- **Tu toque personal:** YouTube puede limitar la monetización de canales con contenido "repetitivo" o producido en serie. Para evitarlo:
  - graba tú la voz siempre que puedas (el guion completo de cada vídeo está en `src/videos/`, en el campo `say`);
  - mezcla estos vídeos animados con gameplay tuyo. Mojang permite publicar y monetizar vídeos con gameplay de Minecraft siguiendo sus normas de uso (Minecraft Usage Guidelines).
- **Shorts:** del vídeo de diamantes salen 3 Shorts muy buenos: la capa Y -59, la minería en ramas y el truco de Fortuna III.
- **Comentarios:** cada vídeo termina con una pregunta. Responde a los primeros comentarios en la primera hora.

## Derechos y material usado
- **Gráficos:** todos (texturas de bloques, cubos 3D, sprites, fondos, interfaz) están **dibujados por código** para este canal. No se usan texturas, logotipos ni capturas de Minecraft. El Frostbite del vídeo 001 es una ilustración propia, y el vídeo lo indica.
- **Música y efectos:** chiptune y efectos generados por código. Son originales, así que no habrá reclamaciones de Content ID.
- **Voz:** Kokoro-82M, con licencia Apache 2.0, que permite el uso comercial.
- **Tipografías:** Silkscreen, Pixelify Sans, Press Start 2P y Montserrat, todas con licencia SIL Open Font License.
- Las descripciones incluyen un aviso: el canal no es oficial y no está afiliado a Mojang ni a Microsoft.

## Regenerar o editar un vídeo
```bash
pip install kokoro-onnx soundfile scipy pillow numpy
# modelo de voz en /home/user/tts (ver PRODUCCION.md)
cd src
python3 render_short.py 002    # vuelve a montar el Short 002 (guion en src/shorts/)
python3 branding.py shorts 002 # metadatos del Short 002
python3 render.py 002          # vuelve a montar el vídeo largo 002
python3 branding.py 002        # miniatura y metadatos del 002
python3 branding.py canal      # banner, avatar y descripción del canal
```
Para cambiar un texto, edita `src/videos/NNN-....py` y vuelve a ejecutar `render.py`. La voz solo se vuelve a generar en las escenas que hayas cambiado.
