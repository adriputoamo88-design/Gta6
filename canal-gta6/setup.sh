#!/usr/bin/env bash
# Prepara la sesión para producir vídeos (idempotente).
# Si al final imprime "export PYTHONPATH=...", ejecuta esa línea antes de renderizar.
PKGS="kokoro-onnx soundfile scipy numpy pillow fonttools"
check() { python3 -c "import kokoro_onnx, scipy, soundfile, PIL, numpy" 2>/dev/null; }
check || python3 -m pip install -q $PKGS 2>&1 | grep -v WARNING
if ! check; then
  python3 -m pip install -q --target /home/user/pydeps $PKGS 2>&1 | grep -v WARNING
  export PYTHONPATH=/home/user/pydeps; check && echo "export PYTHONPATH=/home/user/pydeps"
fi
TTS_DIR=${TTS_DIR:-/home/user/tts}; mkdir -p "$TTS_DIR"
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -s "$TTS_DIR/kokoro-v1.0.onnx" ] || curl -sSL -o "$TTS_DIR/kokoro-v1.0.onnx" $B/kokoro-v1.0.onnx
[ -s "$TTS_DIR/voices-v1.0.bin" ] || curl -sSL -o "$TTS_DIR/voices-v1.0.bin" $B/voices-v1.0.bin
command -v ffmpeg >/dev/null || (apt-get update -q && apt-get install -y -q ffmpeg espeak-ng)
check && echo "setup ok" || echo "SETUP FALLÓ"
