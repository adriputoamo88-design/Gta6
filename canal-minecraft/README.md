# BLOQUE A BLOQUE · Canal de Minecraft en español

Canal de YouTube sobre Minecraft con **2 vídeos nuevos al día**. Cada vídeo trae guion, voz en off, animaciones, gráficos en pixel art, música, efectos de sonido, subtítulos, miniatura, título, descripción con capítulos y etiquetas.

```
canal-minecraft/
├── videos/        ← MP4 listos para subir (1920x1080, 30 fps, H.264 + AAC, -14 LUFS)
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
python3 render.py 002          # vuelve a montar el vídeo 002
python3 branding.py 002        # miniatura y metadatos del 002
python3 branding.py canal      # banner, avatar y descripción del canal
```
Para cambiar un texto, edita `src/videos/NNN-....py` y vuelve a ejecutar `render.py`. La voz solo se vuelve a generar en las escenas que hayas cambiado.
