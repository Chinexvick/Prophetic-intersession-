"""Original revival-worship underscore for the 58s website video.
Key of D, 72 BPM, progression Bm - G - D - A (vi-IV-I-V).
Sections follow the video's scenes:
  0-4.8   intro swell (pads + shimmer)
  4.8-9.4 slogan: sub bass + soft half-time kick enters
  9.4-14  domain typing: filtered pad, riser into the reveal
  14-46   main: full groove (kick, sub, piano arps, soft hats), sidechained pads
  46-51   breakdown under the convener's quote (pads + piano, no drums)
  51-58   end card: impact, full chord, long tail
"""
import numpy as np
from scipy import signal
from pedalboard import Pedalboard, Reverb, Chorus, Compressor, Limiter, LowpassFilter, HighpassFilter, Delay, Gain
from scipy.io import wavfile

SR = 44100
DUR = 58.0
N = int(SR * DUR)
t_all = np.arange(N) / SR
rng = np.random.default_rng(3)

BPM = 72
BEAT = 60 / BPM
BAR = 4 * BEAT

def note(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)

# chord voicings (MIDI). D2=38 B1=35 G1=31 A1=33
CHORDS = [  # (bass root, pad notes, arp notes)
    (35, [59, 62, 66, 71], [71, 74, 78, 83]),   # Bm
    (31, [55, 59, 62, 67], [67, 71, 74, 79]),   # G
    (38, [57, 62, 66, 69], [69, 74, 78, 81]),   # D
    (33, [57, 61, 64, 69], [69, 73, 76, 81]),   # A
]

def chord_at(time):
    return CHORDS[int(time // BAR) % 4]

def env_ar(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def section_gain(points):
    """piecewise-linear automation from [(time, value), ...]"""
    ts, vs = zip(*points)
    return np.interp(t_all, ts, vs)

def add(buf, start, x):
    i = int(start * SR)
    if i >= N: return
    x = x[: N - i]
    buf[i:i + len(x)] += x

# ---------------------------------------------------------------- pads
pad = np.zeros(N)
nbars = int(np.ceil(DUR / BAR)) + 1
for b in range(nbars):
    start = b * BAR - 0.6               # overlap for legato swells
    length = BAR + 1.8
    n = int(length * SR)
    tt = np.arange(n) / SR
    _, notes, _ = CHORDS[b % 4]
    x = np.zeros(n)
    for m in notes:
        f = note(m)
        for d in (-0.11, -0.04, 0.0, 0.05, 0.12):          # detuned supersaw
            ph = rng.uniform(0, 2 * np.pi)
            x += signal.sawtooth(2 * np.pi * f * (1 + d / 100 * 6) * tt + ph) * 0.2
        x += np.sin(2 * np.pi * f / 2 * tt) * 0.35          # warm sub-octave sine
    x *= env_ar(n, 1.1, 1.6)
    add(pad, max(start, 0), x[int(max(0, -start) * SR):])
pad = signal.sosfilt(signal.butter(2, 1600, 'low', fs=SR, output='sos'), pad)

# ---------------------------------------------------------------- piano / bell arps
arp = np.zeros(N)
def bell(f, length=2.2):
    n = int(length * SR); tt = np.arange(n) / SR
    x = (np.sin(2*np.pi*f*tt) + .35*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*6) + .12*np.sin(2*np.pi*3.01*f*tt)*np.exp(-tt*9))
    return x * np.exp(-tt * 2.4) * env_ar(n, 0.004, 0.2)
pattern = [0, 2, 1, 3, 2, 1, 3, 2]      # eighth-note arp order
eighth = BEAT / 2
t = 0.0
while t < DUR:
    _, _, an = chord_at(t)
    k = int(round(t / eighth))
    vel = 0.9 if k % 2 == 0 else 0.6
    add(arp, t, bell(note(an[pattern[k % 8]])) * vel)
    t += eighth

# ---------------------------------------------------------------- sub bass
bass = np.zeros(N)
for b in range(nbars):
    start = b * BAR
    root, _, _ = CHORDS[b % 4]
    n = int((BAR + 0.15) * SR); tt = np.arange(n) / SR
    f = note(root + 12) if root < 34 else note(root)       # keep around 55-75 Hz
    x = np.sin(2*np.pi*f*tt) + 0.25*np.sin(2*np.pi*2*f*tt)
    x = np.tanh(x * 1.6) * env_ar(n, 0.03, 0.25)
    add(bass, start, x)

# ---------------------------------------------------------------- drums
def kick():
    n = int(0.55 * SR); tt = np.arange(n) / SR
    f = 45 + 95 * np.exp(-tt * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-tt * 6.5)
    click = rng.normal(0, 1, n) * np.exp(-tt * 300) * 0.25
    return np.tanh((x + click) * 1.8)
def hat():
    n = int(0.09 * SR); tt = np.arange(n) / SR
    x = rng.normal(0, 1, n) * np.exp(-tt * 55)
    return signal.sosfilt(signal.butter(4, 7000, 'high', fs=SR, output='sos'), x)
def rim():
    n = int(0.25 * SR); tt = np.arange(n) / SR
    x = (rng.normal(0, 1, n) * np.exp(-tt * 30)) * .5 + np.sin(2*np.pi*190*tt) * np.exp(-tt*25)
    return signal.sosfilt(signal.butter(2, [300, 5000], 'band', fs=SR, output='sos'), x)

kicks = np.zeros(N); hats = np.zeros(N); rims = np.zeros(N)
side = np.ones(N)                                        # sidechain ducking envelope
K, Hh, R = kick(), hat(), rim()
def duck(at):
    i = int(at * SR); n = int(0.45 * SR)
    seg = 1 - 0.55 * np.exp(-np.arange(n) / SR * 9)
    j = min(N, i + n); side[i:j] = np.minimum(side[i:j], seg[: j - i])

# half-time kick in the slogan, full groove in the main section
t = 4.8
while t < 9.2:
    add(kicks, t, K * 0.8); duck(t); t += 2 * BEAT
t = 14.0
beat_i = 0
while t < 45.6:
    bar_pos = beat_i % 4
    if bar_pos in (0, 2):
        add(kicks, t, K); duck(t)
    if bar_pos == 3 and (beat_i // 4) % 2 == 1:           # pickup kick every other bar
        add(kicks, t + BEAT * 0.5, K * 0.6); duck(t + BEAT * 0.5)
    if bar_pos in (1, 3) and t > 20:
        add(rims, t, R * 0.5)
    if t > 21:
        add(hats, t, Hh * 0.22); add(hats, t + BEAT / 2, Hh * 0.35)
    t += BEAT; beat_i += 1

# ---------------------------------------------------------------- FX: risers, impact, shimmer
fx = np.zeros(N)
def riser(start, end, peak=0.5):
    n = int((end - start) * SR); tt = np.linspace(0, 1, n)
    noise = rng.normal(0, 1, n)
    out = np.zeros(n); chunk = 2048
    for i in range(0, n, chunk):                              # sweeping band-pass
        fc = 300 + 7000 * tt[i] ** 2
        sos = signal.butter(2, [fc * .7, min(fc * 1.4, SR / 2 - 100)], 'band', fs=SR, output='sos')
        out[i:i + chunk] = signal.sosfilt(sos, noise[i:i + chunk])
    add(fx, start, out * tt ** 2 * peak)
riser(0.0, 4.8, 0.35)
riser(11.0, 14.0, 0.5)
riser(48.6, 51.0, 0.55)
def impact(at, amt=1.0):
    n = int(3.5 * SR); tt = np.arange(n) / SR
    f = 30 + 70 * np.exp(-tt * 8)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6)
    add(fx, at, np.tanh(boom * 2) * 0.9 * amt)
    add(kicks, at, K * 1.1 * amt)
impact(4.8, 0.6); impact(14.0, 0.9); impact(51.0, 1.0)
# shimmer: high octave sines in the intro and outro
shim = np.zeros(N)
for (a, b_) in ((0.0, 5.0), (51.0, 58.0)):
    n = int((b_ - a) * SR); tt = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * note(m) * tt + rng.uniform(0, 6)) for m in (86, 90, 93))
    shim[int(a*SR):int(a*SR)+n] += x * env_ar(n, 2.0, 2.5) * 0.08

# ---------------------------------------------------------------- automation per section
g_pad = section_gain([(0,0),(3.5,.5),(4.8,.75),(9.4,.75),(10,.4),(13.6,.6),(14,1),(46,1),(46.6,.55),(50.8,.6),(51,1.1),(56,.9),(58,0)])
g_arp = section_gain([(0,0),(4.8,0),(6,.35),(9.4,.35),(10,.15),(14,.55),(22,.75),(46,.8),(46.6,.55),(51,.7),(57,.3),(58,0)])
g_bass = section_gain([(0,0),(4.7,0),(4.8,.9),(9.3,.9),(9.6,.3),(13.9,.4),(14,1),(46,1),(46.6,.45),(50.9,.45),(51,1),(56,.6),(58,0)])
lp_open = section_gain([(0,500),(4.8,1300),(9.4,1300),(10,650),(14,1900),(46,1900),(46.5,1000),(51,2300),(58,1200)])

# time-varying low-pass on pads (block processing)
pad_f = np.zeros(N); blk = 4096; zi = None
for i in range(0, N, blk):
    fc = float(lp_open[i])
    sos = signal.butter(2, fc, 'low', fs=SR, output='sos')
    if zi is None: zi = signal.sosfilt_zi(sos) * 0
    pad_f[i:i+blk], zi = signal.sosfilt(sos, pad[i:i+blk], zi=zi)

pad_mix = pad_f * g_pad * side * 0.32
arp_mix = arp * g_arp * 0.16
bass_mix = bass * g_bass * 0.33
drum_mix = kicks * 0.55 + hats * 0.5 + rims * 0.18

def fx_chain(x, *plugins):
    return Pedalboard(list(plugins))(x.astype(np.float32)[None, :], SR)[0]

pad_mix = fx_chain(pad_mix, Chorus(rate_hz=0.3, depth=0.25, mix=0.4), Reverb(room_size=0.82, damping=0.7, wet_level=0.38, dry_level=0.75, width=1.0), LowpassFilter(5000))
arp_mix = fx_chain(arp_mix, HighpassFilter(250), Delay(delay_seconds=BEAT * 0.75, feedback=0.35, mix=0.3), Reverb(room_size=0.8, damping=0.6, wet_level=0.42, dry_level=0.65))
shim = fx_chain(shim * 0.5, Reverb(room_size=0.88, damping=0.5, wet_level=0.6, dry_level=0.3))
fx_mix = fx_chain(fx * 0.5, Reverb(room_size=0.9, wet_level=0.4, dry_level=0.7))
drum_mix = fx_chain(drum_mix, Compressor(threshold_db=-12, ratio=3, attack_ms=10, release_ms=120), Reverb(room_size=0.4, wet_level=0.12, dry_level=0.95))

mix = pad_mix + arp_mix + bass_mix + drum_mix + shim + fx_mix
# stereo width: Haas-style spread of pads/arps
L = mix + 0.12 * np.roll(pad_mix + arp_mix, int(0.011 * SR))
Rr = mix + 0.12 * np.roll(pad_mix + arp_mix, int(0.017 * SR))
st = np.stack([L, Rr]).astype(np.float32)
st = Pedalboard([HighpassFilter(28), Compressor(threshold_db=-18, ratio=1.6, attack_ms=30, release_ms=250), Limiter(threshold_db=-1.0, release_ms=150)])(st, SR)
# fades
fade = np.ones(N); fade[: int(.05 * SR)] = np.linspace(0, 1, int(.05 * SR)); fade[-int(2.5 * SR):] *= np.linspace(1, 0, int(2.5 * SR)) ** 1.5
st = st * fade
peak = np.abs(st).max(); st = st / peak * 0.89
rms = np.sqrt((st ** 2).mean())
print("peak", round(float(np.abs(st).max()), 3), "rms dBFS", round(float(20 * np.log10(rms)), 1))
wavfile.write("music.wav", SR, (st.T * 32767).astype(np.int16))
