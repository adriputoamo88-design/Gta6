# -*- coding: utf-8 -*-
"""Voz (Kokoro TTS, voz en español) y música synthwave original generada por código."""
import hashlib, os, re
import numpy as np
import soundfile as sf

from content import PRON

SR = 24000
TTS_DIR = os.environ.get("TTS_DIR", "/home/user/tts")
_k = None


def tts_text(say):
    t = say
    for a, b in sorted(PRON, key=lambda p: -len(p[0])):
        t = re.sub(r"(?<![\wÁÉÍÓÚáéíóúñ])" + re.escape(a) + r"(?![\wÁÉÍÓÚáéíóúñ])", b, t)
    t = t.replace("…", ".").replace("“", "").replace("”", "")
    return t


def speak(say, out, voice="em_alex", speed=1.06):
    global _k
    key = hashlib.md5((tts_text(say) + voice + str(speed)).encode()).hexdigest()[:10]
    path = f"{out}.{key}.wav"
    if not os.path.exists(path):
        if _k is None:
            from kokoro_onnx import Kokoro
            _k = Kokoro(os.path.join(TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(TTS_DIR, "voices-v1.0.bin"))
        a, sr = _k.create(tts_text(say), voice=voice, speed=speed, lang="es")
        a = np.asarray(a, dtype=np.float32)
        # recorta silencios extremos
        nz = np.where(np.abs(a) > 0.01)[0]
        if len(nz): a = a[max(0, nz[0] - 1200): nz[-1] + 2400]
        sf.write(path, a, sr)
    a, sr = sf.read(path, dtype="float32")
    return a


# ---------------------------------------------------------------- música
MSR = 44100
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}


def hz(n, octv):
    return 440.0 * 2 ** ((NOTE[n] + 12 * (octv - 4) - 9) / 12)


def chord_freqs(root, minor):
    r = NOTE[root]
    iv = [0, 3, 7, 10] if minor else [0, 4, 7, 11]
    return [440.0 * 2 ** ((r + i + 12 * (3 - 4) - 9) / 12) for i in iv]


PROGS = {
    "sunset": (100, [("A", 1), ("F", 0), ("C", 0), ("G", 0)]),
    "neon":   (108, [("F#", 1), ("D", 0), ("A", 0), ("E", 0)]),
    "danger": (96,  [("D", 1), ("A#", 0), ("F", 0), ("C", 0)]),
    "money":  (104, [("C", 1), ("G#", 0), ("D#", 0), ("A#", 0)]),
    "ocean":  (98,  [("E", 1), ("C", 0), ("G", 0), ("D", 0)]),
    "retro":  (112, [("B", 1), ("G", 0), ("D", 0), ("A", 0)]),
}


def lowpass(x, a):
    from scipy.signal import lfilter
    return lfilter([a], [1, a - 1], x)


def music(theme, seconds):
    bpm, prog = PROGS[theme]
    beat = 60.0 / bpm; bar = beat * 4
    n_bar = int(MSR * bar)
    rng = np.random.default_rng(7)
    loop = np.zeros(n_bar * 4, dtype=np.float64)
    t_bar = np.arange(n_bar) / MSR
    for bi, (root, minor) in enumerate(prog):
        seg = np.zeros(n_bar)
        fr = chord_freqs(root, minor)
        # pad (sierras desafinadas)
        for f in fr:
            for det in (-0.003, 0.003):
                ph = (t_bar * f * 2 * (1 + det)) % 1.0
                seg += (2 * ph - 1) * 0.05
        env = np.minimum(1, t_bar / 0.4) * np.minimum(1, (bar - t_bar) / 0.3)
        seg *= env
        # bajo en corcheas
        bf = fr[0] / 2
        for k in range(8):
            s0 = int(k * beat / 2 * MSR); s1 = int(s0 + beat / 2 * MSR * 0.9)
            tt = np.arange(s1 - s0) / MSR
            ph = (tt * bf) % 1.0
            seg[s0:s1] += (2 * ph - 1) * 0.16 * np.exp(-tt * 5)
        # arpegio
        for k in range(16):
            s0 = int(k * beat / 4 * MSR); s1 = min(n_bar, s0 + int(beat / 4 * MSR))
            tt = np.arange(s1 - s0) / MSR; f = fr[[0, 1, 2, 3, 2, 1, 0, 2][k % 8]] * 4
            seg[s0:s1] += np.sign(np.sin(2 * np.pi * f * tt)) * 0.025 * np.exp(-tt * 18)
        loop[bi * n_bar:(bi + 1) * n_bar] = seg
    loop = lowpass(loop, 0.25)
    # batería
    nb = len(loop); spb = int(beat * MSR)
    for k in range(16):
        s0 = k * spb
        tt = np.arange(int(0.25 * MSR)) / MSR
        kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * 0.5
        e = min(nb, s0 + len(kick)); loop[s0:e] += kick[:e - s0]
        if k % 2 == 1:
            sn = rng.standard_normal(int(0.2 * MSR)) * np.exp(-np.arange(int(0.2 * MSR)) / MSR * 18) * 0.18
            e = min(nb, s0 + len(sn)); loop[s0:e] += sn[:e - s0]
        for hh in (0, 0.5):
            h0 = s0 + int(hh * spb); hl = int(0.04 * MSR)
            hat = np.diff(rng.standard_normal(hl + 1)) * np.exp(-np.arange(hl) / MSR * 90) * 0.05
            e = min(nb, h0 + hl); loop[h0:e] += hat[:e - h0]
    n = int(seconds * MSR)
    out = np.tile(loop, n // nb + 1)[:n]
    fade = int(2 * MSR)
    out[:fade] *= np.linspace(0, 1, fade); out[-fade:] *= np.linspace(1, 0, fade)
    out /= np.max(np.abs(out)) + 1e-9
    return (out * 0.5).astype(np.float32)


def whoosh(sr=MSR, dur=0.45):
    rng = np.random.default_rng(3)
    n = int(sr * dur); x = rng.standard_normal(n)
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    from scipy.signal import butter, lfilter
    out = np.zeros(n); chunk = 512
    for i in range(0, n, chunk):
        fc = 300 + 5000 * (i / n)
        b, a = butter(2, [fc / (sr / 2) * 0.6, min(0.99, fc / (sr / 2) * 1.4)], btype="band")
        out[i:i + chunk] = lfilter(b, a, x[i:i + chunk])
    out = out * env
    return (out / (np.max(np.abs(out)) + 1e-9) * 0.35).astype(np.float32)
