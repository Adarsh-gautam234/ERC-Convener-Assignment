import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt
import os

# Create plots folder
os.makedirs("plots", exist_ok=True)

# =========================
# LOAD AUDIO
# =========================
signal, sr = sf.read("Signals/corrupted.wav")

# Convert to mono if stereo
if len(signal.shape) > 1:
    signal = signal.mean(axis=1)

t = np.arange(len(signal)) / sr

print("Sample Rate:", sr)

# =========================
# STAGE 1 — TIME DOMAIN
# =========================
plt.figure()
plt.plot(signal)
plt.title("Stage 1: Corrupted Signal")
plt.savefig("plots/stage1_time.png")
plt.show()

# =========================
# STAGE 1 — FFT
# =========================
N = len(signal)
yf = fft(signal)
xf = fftfreq(N, 1/sr)

plt.figure()
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Stage 1: FFT")
plt.savefig("plots/stage1_fft.png")
plt.show()

# =========================
# STAGE 2 — DEMODULATION
# =========================
f_shift = 5000  # try 4000–6000 if needed

demodulated = signal * np.cos(2 * np.pi * f_shift * t)

plt.figure()
plt.plot(demodulated)
plt.title("Stage 2: After Frequency Shift")
plt.savefig("plots/stage2_time.png")
plt.show()

# FFT after demodulation
yf2 = fft(demodulated)

plt.figure()
plt.plot(xf[:N//2], np.abs(yf2[:N//2]))
plt.title("Stage 2: FFT")
plt.savefig("plots/stage2_fft.png")
plt.show()

# =========================
# STAGE 4 — ENVELOPE DETECTION
# =========================
# Rectification
envelope = np.abs(demodulated)

# Low-pass filter
def lowpass(data, cutoff, sr):
    nyq = 0.5 * sr
    b, a = butter(5, cutoff/nyq, btype='low')
    return filtfilt(b, a, data)

envelope = lowpass(envelope, 4000, sr)

plt.figure()
plt.plot(envelope)
plt.title("Stage 4: Envelope Recovered")
plt.savefig("plots/stage4_time.png")
plt.show()

# FFT after envelope
yf3 = fft(envelope)

plt.figure()
plt.plot(xf[:N//2], np.abs(yf3[:N//2]))
plt.title("Stage 4: FFT")
plt.savefig("plots/stage4_fft.png")
plt.show()

# =========================
# FINAL CLEANUP FILTER
# =========================
def bandpass_filter(data, lowcut, highcut, sr, order=6):
    nyq = 0.5 * sr
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

# Strong speech isolation
cleaned = bandpass_filter(envelope, 500, 2500, sr)

# Extra smoothing
cleaned = lowpass(cleaned, 2000, sr)

# Normalize
final_signal = cleaned / np.max(np.abs(cleaned))

# =========================
# SAVE OUTPUT
# =========================
sf.write("recovered.wav", final_signal, sr)

print("✅ Final recovered audio saved as recovered.wav")
print("✅ All plots saved in 'plots' folder")