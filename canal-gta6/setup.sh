#!/usr/bin/env bash
# Prepara una sesión nueva para producir vídeos (idempotente).
set -e
pip install -q kokoro-onnx soundfile scipy numpy pillow fonttools 2>&1 | grep -v WARNING || true
TTS_DIR=${TTS_DIR:-/home/user/tts}; mkdir -p "$TTS_DIR"
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -s "$TTS_DIR/kokoro-v1.0.onnx" ] || curl -sSL -o "$TTS_DIR/kokoro-v1.0.onnx" $B/kokoro-v1.0.onnx
[ -s "$TTS_DIR/voices-v1.0.bin" ] || curl -sSL -o "$TTS_DIR/voices-v1.0.bin" $B/voices-v1.0.bin
command -v ffmpeg >/dev/null || (apt-get update -q && apt-get install -y -q ffmpeg espeak-ng)
python3 -c "import kokoro_onnx, scipy, soundfile; print('setup ok')"
