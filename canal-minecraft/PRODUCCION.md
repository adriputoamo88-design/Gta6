# Producción diaria: 2 vídeos al día

Este es el proceso que se sigue cada día para sacar los 2 vídeos. Sirve igual si lo hace Claude con la tarea programada o si lo haces tú a mano.

**Tarea programada:** se ejecuta cada día a las 8:41 (hora de España) y prepara los 2 vídeos **del día siguiente**. Así siempre tienes un día de margen para revisarlos y programarlos.

## 0. Preparar el entorno (solo si el contenedor es nuevo)
```bash
pip install kokoro-onnx soundfile scipy pillow numpy
mkdir -p /home/user/tts && cd /home/user/tts
curl -sSLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sSLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```

## 1. Elegir los temas
1. Busca novedades de Minecraft de las últimas 24-48 h (snapshots, Preview de Bedrock, anuncios de Mojang). Si hay algo importante, uno de los dos vídeos es la noticia.
2. El resto sale de `temas.md`, en orden. Alterna guía y noticia o curiosidad.

## 2. Escribir el guion
- Un archivo por vídeo: `src/videos/NNN-slug.py`. Copia uno existente como plantilla y sigue la numeración.
- Al principio del archivo, en un comentario, pon las fuentes y la fecha en que se comprobó la información.
- **Nada inventado.** Lo que solo se ha visto en versiones de prueba se dice como tal ("en las snapshots…"). Si un dato no se puede comprobar, no entra.
- Duración: 1:45-3:00 (11-14 escenas). Los primeros 5 segundos tienen que enganchar: un problema, una promesa o un dato sorprendente.
- El texto de `say` es lo que dice la voz y aparece como subtítulo. Para las palabras en inglés, añade cómo se pronuncian en `PRON` (en `src/audio.py`).
- Plantillas de escena (`t`): `title`, `news`, `bullets`, `stat`, `tip`, `icon`, `vs`, `mob`, `hotbar`, `ylevel`, `branch`, `outro`.
  - Visuales disponibles: cubos `("cube", "textura")` y sprites `("sprite", "nombre")`. Puedes ver la lista en `src/art.py` (`tex()` y `SPRITE_MAPS`).
- Termina siempre con una escena `outro` que haga una pregunta para los comentarios + `OUTRO`.

## 3. Renderizar
```bash
cd src
python3 render.py NNN NNN      # vídeo(s) en videos/, subtítulos en subtitulos/
python3 branding.py NNN NNN    # miniatura en miniaturas/ y metadatos en metadatos/
```
Tarda unos 5-8 minutos por vídeo. Puedes lanzar los dos a la vez.

## 4. Revisar antes de publicar
- Saca fotogramas de cada escena y comprueba que no haya textos cortados ni elementos que se solapen.
- Comprueba que el título, la miniatura y lo que se dice en el vídeo coinciden.
- Revisa la duración y los capítulos en `metadatos/NNN-....txt`.

## 5. Entregar
- Marca los temas como publicados en `temas.md`.
- Haz commit y push de: `src/videos/`, `videos/`, `miniaturas/`, `subtitulos/`, `metadatos/` y `temas.md`.

## Horario de publicación recomendado (España)
| Vídeo | Hora | Por qué |
|---|---|---|
| 1 (guía) | 14:00 | Hora de comer y salida de clase |
| 2 (noticia o curiosidad) | 19:00 | Pico de audiencia de la tarde |

En YouTube Studio puedes subir los dos a la vez y programarlos con "Programar".
