# EEG Analysis Demo (Synthetic Data)

This demo repo shows a minimal EEG preprocessing and ERP pipeline using **synthetic** EEG-like data.
It is provided to produce reproducible figures for CV/research-evidence purposes. Replace the synthetic data with real datasets from PhysioNet (links below) to perform an actual analysis.

## What this repo contains
- `analysis.py` : script that generates synthetic EEG, preprocesses (1-40 Hz bandpass), epochs (-0.2 s to +0.6 s), computes ERP for channel 0, and saves figures.
- `requirements.txt` : required Python packages.
- `outputs/` : directory created when script runs; contains PNG figures and `data.npy`, `events.npy`.

## Recommended real datasets
- PhysioNet EEG Motor Movement/Imagery Dataset: https://physionet.org/content/eegmmidb/1.0.0/
- BNCI Horizon 2020 datasets: http://bnci-horizon-2020.eu/database/data-sets
# EEG Signal Analysis Demo

This project demonstrates EEG preprocessing, visualization, and event-related potential (ERP) extraction using Python.

### What this repo contains
- Synthetic EEG dataset (data.npy)
- Event markers (events.npy)
- Analysis script (analysis.py)
- Output figures:
  - ERP
  - Raw EEG trace
  - Spectrogram

### Skills demonstrated
- Signal processing (filtering, segmentation)
- Event-related potential extraction
- Time-frequency analysis
- Python (NumPy, SciPy, Matplotlib)

### Reproducibility
Run:
    python3 analysis.py
Outputs will appear in /outputs.

Suitable for neuroscience applications, research positions, and computational analysis portfolios.

## How to run
1. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
