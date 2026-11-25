# -*- coding: utf-8 -*-
"""Voz (Kokoro TTS en español), música chiptune original y efectos de sonido. Todo generado aquí."""
import hashlib, os, re
import numpy as np
import soundfile as sf
from scipy.signal import lfilter, butter

SR = 24000          # voz
MSR = 44100         # música y efectos
TTS_DIR = os.environ.get("TTS_DIR", "/home/user/tts")
VOICE = "em_alex"
SPEED = 1.08
_k = None

# Pronunciación: lo que se escribe en el subtítulo -> lo que se le pasa a la voz.
PRON = [
    ("Minecraft", "Máincraft"), ("Mojang", "Moyáng"), ("The Deep Freeze", "Di Dip Fríis"), ("Deep Freeze", "Dip Fríis"),
    ("TwitchCon", "Tuích Con"), ("snapshots", "esnápshots"), ("snapshot", "esnápshot"), ("Java", "Yava"),
    ("Bedrock", "Bédrok"), ("Preview", "Príviu"), ("game drop", "guéim drop"), ("game drops", "guéim drops"),
    ("Brittle Ice", "Brítel Áis"), ("Frostbite", "Fróstbait"), ("Hyper Potions", "Jáiper Póshons"),
    ("Warden", "Uórden"), ("sculk", "esculk"), ("F3", "efe tres"), ("1.18", "uno punto dieciocho"),
    ("1.17", "uno punto diecisiete"), ("Netherite", "Néziraít"), ("Nether", "Néder"), ("End", "End"),
    ("Ender Dragon", "Énder Drágon"), ("Pre-Release", "Pri rilís"), ("slimes", "esláims"), ("slime", "esláim"), ("chunks", "chonks"), ("chunk", "chonk"), ("seed", "sid"), ("Breeze", "Bris"), ("breeze", "bris"), ("MineCon", "Máincon"), ("Notch", "Noch"), ("Markus Persson", "Márkus Pérson"), ("1.0", "uno punto cero"), ("Dinnerbone", "Díner bon"), ("jeb", "yeb"), ("shulkers", "shúlkers"), ("shulker", "shúlker"), ("piglins", "píglins"), ("piglin", "píglin"), ("ghasts", "gásts"), ("ghast", "gást"), ("netherita", "neterita"), ("Enderman", "Énderman"), ("blaze", "bléis"), ("blazes", "bléises"), ("creeper", "críper"), ("creepers", "crípers"), ("Ender", "Énder"), ("YouTube", "Yutub"), ("mods", "mods"),
    ("Toque de seda", "Toque de seda"), ("Bloque a Bloque", "Bloque a Bloque"), ("XP", "equis pe"),
]


def tts_text(say):
    t = say
    for a, b in sorted(PRON, key=lambda p: -len(p[0])):
        t = re.sub(r"(?<![\wÁÉÍÓÚáéíóúñ])" + re.escape(a) + r"(?![\wÁÉÍÓÚáéíóúñ])", b, t)
    t = re.sub(r"\bY ?= ?(-?\d+)", lambda m: "i griega " + m.group(1), t)
    t = re.sub(r"\bY (-?\d+)", lambda m: "i griega " + m.group(1), t)
    t = re.sub(r"(?<![\w])-(\d+)", r"menos \1", t)
    t = re.sub(r"(\d+),(\d+)", r"\1 coma \2", t)
    t = t.replace("…", ".").replace("“", "").replace("”", "").replace("«", "").replace("»", "").replace("·", ",")
    return t


def speak(say, out, voice=VOICE, speed=SPEED):
    global _k
    txt = tts_text(say)
    key = hashlib.md5((txt + voice + str(speed)).encode()).hexdigest()[:10]
    path = f"{out}.{key}.wav"
    if not os.path.exists(path):
        if _k is None:
            from kokoro_onnx import Kokoro
            _k = Kokoro(os.path.join(TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(TTS_DIR, "voices-v1.0.bin"))
        a, sr = _k.create(txt, voice=voice, speed=speed, lang="es")
        a = np.asarray(a, dtype=np.float32)
        nz = np.where(np.abs(a) > 0.01)[0]
        if len(nz): a = a[max(0, nz[0] - 1200): nz[-1] + 2400]
        sf.write(path, a, sr)
    a, _ = sf.read(path, dtype="float32")
    return a


# ================================================================ música chiptune original
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}


def midi(n, octv):
    return NOTE[n] + 12 * (octv + 1)


def mhz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def chord(root, minor, octv=3):
    r = midi(root, octv)
    return [r, r + (3 if minor else 4), r + 7]


SONGS = {
    #            bpm   progresión (raíz, menor)                                         estilo
    "aventura": (112, [("C", 0), ("G", 0), ("A", 1), ("F", 0)], "bright"),
    "cueva":    (88,  [("A", 1), ("F", 0), ("D", 1), ("E", 0)], "dark"),
    "hielo":    (96,  [("E", 1), ("C", 0), ("G", 0), ("D", 0)], "bells"),
    "noche":    (94,  [("D", 1), ("A#", 0), ("F", 0), ("C", 0)], "dark"),
}


def _env(n, a=0.005, d=0.12, s=0.5, r=0.08, sr=MSR):
    t = np.arange(n) / sr
    e = np.minimum(1, t / max(a, 1e-4))
    e = np.where(t > a, s + (1 - s) * np.exp(-(t - a) / max(d, 1e-4)), e)
    rel = int(r * sr)
    if rel and n > rel: e[-rel:] *= np.linspace(1, 0, rel)
    return e


def _osc(kind, f, n, sr=MSR, duty=0.5):
    t = np.arange(n) / sr
    ph = (t * f) % 1.0
    if kind == "square": return np.where(ph < duty, 1.0, -1.0)
    if kind == "tri": return 4 * np.abs(ph - 0.5) - 1
    if kind == "saw": return 2 * ph - 1
    if kind == "bell": return np.sin(2 * np.pi * f * t + 1.6 * np.sin(2 * np.pi * f * 3.5 * t) * np.exp(-t * 6))
    return np.sin(2 * np.pi * f * t)


def lowpass(x, fc, sr=MSR, order=2):
    b, a = butter(order, fc / (sr / 2)); return lfilter(b, a, x)


def music(theme, seconds, seed=7):
    bpm, prog, style = SONGS[theme]
    rng = np.random.default_rng(seed)
    beat = 60.0 / bpm; bar = beat * 4; nb = int(MSR * bar)
    bars = 8
    L = nb * bars
    lead = np.zeros(L); bass = np.zeros(L); pad = np.zeros(L); drums = np.zeros(L)
    step = beat / 2                           # corcheas
    ns = int(step * MSR)
    for b in range(bars):
        root, minor = prog[b % len(prog)]
        ch = chord(root, minor, 3)
        s0 = b * nb
        # pad suave
        for m in ch:
            for det in (-0.004, 0.004):
                x = _osc("saw" if style != "bells" else "tri", mhz(m + 12) * (1 + det), nb) * 0.03
                pad[s0:s0 + nb] += x * _env(nb, a=0.35, d=1.0, s=0.8, r=0.3)
        # bajo
        pat = [0, 0, 7, 0, 0, 0, 7, 12] if style == "bright" else [0, -1, -1, 0, 7, -1, 0, -1]
        for k, iv in enumerate(pat):
            if iv < 0: continue
            n = int(ns * 0.9); f = mhz(ch[0] - 12 + iv)
            x = _osc("tri", f, n) * 0.30 * _env(n, d=0.18, s=0.4)
            bass[s0 + k * ns: s0 + k * ns + n] += x
        # melodía / arpegio
        scale = sorted(set([(c % 12) for c in ch] + [(ch[0] + 2) % 12, (ch[0] + (8 if minor else 9)) % 12]))
        sub = 2 if style == "bells" else 1   # semicorcheas en "bells"
        nst = 8 * sub; sl = int(ns / sub)
        for k in range(nst):
            if style == "dark" and rng.random() < 0.45: continue
            if style == "bright" and rng.random() < 0.18: continue
            if k % (2 * sub) == 0:
                m = ch[(k // (2 * sub)) % 3] + 24
            else:
                m = 12 * 5 + scale[rng.integers(0, len(scale))]
                if m < ch[0] + 12: m += 12
            if style == "bells":
                m = ch[[0, 1, 2, 1][k % 4]] + 24 + (12 if (k // 4) % 2 else 0)
            n = int(sl * (0.95 if style != "dark" else 2.5)); n = min(n, L - (s0 + k * sl))
            if style == "bright":
                x = _osc("square", mhz(m), n, duty=0.25) * 0.05 * _env(n, d=0.09, s=0.25)
            elif style == "bells":
                x = _osc("bell", mhz(m), n) * 0.09 * _env(n, d=0.25, s=0.0, r=0.02)
            else:
                x = _osc("bell", mhz(m), n) * 0.08 * _env(n, d=0.35, s=0.0, r=0.05)
            lead[s0 + k * sl: s0 + k * sl + n] += x
        # batería
        for q in range(4):
            p0 = s0 + int(q * beat * MSR)
            if style == "bright" or q in (0, 2) or (style == "bells" and q in (0, 2)):
                n = int(0.22 * MSR); t = np.arange(n) / MSR
                kick = np.sin(2 * np.pi * (45 + 110 * np.exp(-t * 35)) * t) * np.exp(-t * 11) * (0.55 if style == "bright" else 0.4)
                drums[p0:p0 + n] += kick[:len(drums[p0:p0 + n])]
            if q in (1, 3) and style != "dark":
                n = int(0.16 * MSR)
                sn = rng.standard_normal(n) * np.exp(-np.arange(n) / MSR * 22) * 0.12
                drums[p0:p0 + n] += lowpass(sn, 6000)[:len(drums[p0:p0 + n])]
            for hh in ((0.5,) if style == "dark" else (0.0, 0.5)):
                h0 = p0 + int(hh * beat * MSR); n = int(0.03 * MSR)
                hat = np.diff(rng.standard_normal(n + 1)) * np.exp(-np.arange(n) / MSR * 120) * 0.035
                drums[h0:h0 + n] += hat[:len(drums[h0:h0 + n])]
    lead = lowpass(lead, 5200)
    # eco en el lead
    d = int(beat * 0.75 * MSR); echo = np.zeros_like(lead); echo[d:] = lead[:-d] * 0.35
    mix = lead + echo + bass + lowpass(pad, 2600) + drums
    n = int(seconds * MSR)
    out = np.tile(mix, n // L + 1)[:n]
    f = int(1.5 * MSR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    out /= np.max(np.abs(out)) + 1e-9
    return (out * 0.5).astype(np.float32)


# ================================================================ efectos
def _norm(x, g):
    return (x / (np.max(np.abs(x)) + 1e-9) * g).astype(np.float32)


def sfx(name, seed=1):
    rng = np.random.default_rng(seed)
    if name == "pop":        # aparece un elemento
        n = int(0.09 * MSR); t = np.arange(n) / MSR
        x = np.sin(2 * np.pi * (300 + 700 * np.exp(-t * 40)) * t) * np.exp(-t * 45)
        return _norm(x, 0.35)
    if name == "place":      # "colocar bloque": golpe sordo + crujido
        n = int(0.14 * MSR); t = np.arange(n) / MSR
        thud = np.sin(2 * np.pi * (90 + 60 * np.exp(-t * 50)) * t) * np.exp(-t * 30)
        b, a = butter(2, [300 / (MSR / 2), 2500 / (MSR / 2)], btype="band")
        crunch = lfilter(b, a, rng.standard_normal(n)) * np.exp(-t * 55)
        return _norm(thud * 0.8 + crunch * 0.6, 0.45)
    if name == "break":      # transición: bloque que se rompe + barrido
        n = int(0.42 * MSR); t = np.arange(n) / MSR; x = np.zeros(n)
        b, a = butter(2, [400 / (MSR / 2), 3800 / (MSR / 2)], btype="band")
        for k in range(4):
            s = int(k * 0.035 * MSR); m = int(0.08 * MSR)
            x[s:s + m] += lfilter(b, a, rng.standard_normal(m)) * np.exp(-np.arange(m) / MSR * 50) * (1 - k * 0.18)
        wh = rng.standard_normal(n); out = np.zeros(n); ch = 512
        for i in range(0, n, ch):
            fc = 400 + 4500 * (i / n)
            bb, aa = butter(2, [fc * 0.6 / (MSR / 2), min(0.99, fc * 1.4 / (MSR / 2))], btype="band")
            out[i:i + ch] = lfilter(bb, aa, wh[i:i + ch])
        x += out * np.sin(np.linspace(0, np.pi, n)) ** 2 * 0.5
        return _norm(x, 0.42)
    if name == "ding":       # logro / dato clave
        n = int(0.7 * MSR); t = np.arange(n) / MSR; x = np.zeros(n)
        for k, f in enumerate((mhz(88), mhz(95))):
            s = int(k * 0.09 * MSR)
            x[s:] += np.sin(2 * np.pi * f * t[:n - s]) * np.exp(-t[:n - s] * 6) + 0.3 * np.sin(2 * np.pi * f * 2 * t[:n - s]) * np.exp(-t[:n - s] * 9)
        return _norm(x, 0.30)
    if name == "click":
        n = int(0.03 * MSR); t = np.arange(n) / MSR
        return _norm(np.sin(2 * np.pi * 1800 * t) * np.exp(-t * 200), 0.25)
    raise ValueError(name)
