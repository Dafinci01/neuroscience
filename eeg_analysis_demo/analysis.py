#!/usr/bin/env python3
"""
EEG Analysis Demo (synthetic data)

This script:
- generates synthetic EEG-like signals with event markers
- applies a bandpass filter (1-40 Hz)
- epochs around events (-0.2s to +0.6s)
- computes the average ERP for channel 0
- saves figures: raw_eeg_channel0.png, spectrogram_channel0.png, erp_channel0.png

To run with real data:
- replace data generation block with code to load your real EEG (n_channels x n_samples)
- create an `events.npy` file with event sample indices (integers, samples)
"""

import os
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

out_dir = "outputs"
os.makedirs(out_dir, exist_ok=True)

# Sampling frequency and time
sf = 256  # Hz
duration_s = 60  # seconds
t = np.arange(0, duration_s, 1/sf)
n_chan = 4

# RNG
rng = np.random.default_rng(42)

# Function to create pink-ish noise (approx)
def pink_noise(length, rng):
    x = rng.standard_normal(length)
    b, a = sig.butter(1, 0.1, btype='low', fs=sf)
    return sig.lfilter(b, a, x)

# Generate synthetic data: baseline + alpha oscillation + transient ERP component
data = np.array([0.5*pink_noise(len(t), rng) + 0.05*rng.standard_normal(len(t)) for _ in range(n_chan)])
for ch in range(n_chan):
    data[ch] += 0.5*np.sin(2*np.pi*10*t + rng.random()*2*np.pi) * (0.5 + 0.5*rng.random())

# Make event times (seconds) and samples
n_events = 30
event_times = np.sort(rng.choice(np.arange(2, duration_s-2), size=n_events, replace=False))
event_samples = (event_times * sf).astype(int)

# Add a small ERP-like transient to channels 0 and 1 at ~200 ms post-event
erp_len = int(0.6*sf)
erp = np.zeros(erp_len)
erp_peak = int(0.2*sf)
erp[erp_peak:erp_peak+20] = np.hanning(20)*2.0
for s in event_samples:
    for ch in [0,1]:
        if s + erp_len < data.shape[1]:
            data[ch, s:s+erp_len] += erp * (0.8 + 0.4*rng.random())

# Save a raw signal plot (first 10 seconds of channel 0)
plt.figure(figsize=(10,4))
plt.plot(t[0:sf*10], data[0,0:sf*10])
plt.title("Synthetic EEG channel 0 (first 10 s)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (a.u.)")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "raw_eeg_channel0.png"))
plt.close()

# Bandpass filter 1-40 Hz
bp_b, bp_a = sig.butter(4, [1, 40], btype='band', fs=sf)
fdata = sig.filtfilt(bp_b, bp_a, data, axis=1)

# Epoching: -0.2s to +0.6s around events
pre = int(0.2*sf); post = int(0.6*sf)
epochs = []
valid_events = []
for s in event_samples:
    if s-pre >= 0 and s+post < fdata.shape[1]:
        epochs.append(fdata[:, s-pre:s+post])
        valid_events.append(s)
epochs = np.stack(epochs, axis=0)  # shape: (n_epochs, n_chan, samples)
times = np.linspace(-0.2, 0.6, pre+post)

# Compute ERP for channel 0
erp_avg = epochs.mean(axis=0)[0]

plt.figure(figsize=(6,4))
plt.plot(times, erp_avg)
plt.axvline(0, color='k', linestyle='--', linewidth=0.7)
plt.title("ERP (channel 0) - average across epochs")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (a.u.)")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "erp_channel0.png"))
plt.close()

# Spectrogram for channel 0 (first 10 s)
f, tt, Sxx = sig.spectrogram(data[0,0:sf*10], fs=sf, nperseg=256, noverlap=128)
plt.figure(figsize=(6,4))
plt.pcolormesh(tt, f, Sxx, shading='gouraud')
plt.title("Spectrogram (channel 0, first 10 s)")
plt.ylabel("Frequency [Hz]")
plt.xlabel("Time [sec]")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "spectrogram_channel0.png"))
plt.close()

# Save numpy arrays for reproducibility
np.save(os.path.join(out_dir, "data.npy"), data)
np.save(os.path.join(out_dir, "events.npy"), np.array(valid_events))

print("Done. Output files are in the 'outputs' folder:")
print(sorted(os.listdir(out_dir)))
