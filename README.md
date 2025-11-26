

# 🧠 Neurocomputational & Electrophysiology Portfolio

*A collection of reproducible neuroscience mini-projects built using public datasets, computational models, and literature-driven analysis.*

---

## 📌 Overview

This repository contains three research-oriented projects demonstrating core competencies in **computational neuroscience**, **electrophysiology**, and **mechanistic neurobiology**.
All analyses are fully reproducible, use publicly available datasets, and are grounded in peer-reviewed literature.

These projects were built to strengthen my applied neuroscience skills in preparation for graduate-level study.

---

## 📁 Repository Structure

```
📦 neuroscience-portfolio
│
├── eeg-analysis/
│   ├── data/                     # Public EEG samples (links + instructions)
│   ├── scripts/                  # Preprocessing & ERP extraction
│   ├── results/                  # ERPs, PSD plots, artifacts removed
│   └── README.md
│
├── dopamine-rl-model/
│   ├── model.py                  # Temporal Difference learning implementation
│   ├── plots/                    # Dopamine RPE curves, value updates, policy heatmaps
│   └── README.md
│
├── neuroinflammation-review/
│   ├── review.pdf                # My synthesized mini-review
│   ├── references.bib            # All citations
│   └── notes/                    # Annotated papers
│
└── main README.md                # (This file)
```

---

## 🔬 1. EEG Signal Analysis (MNE-Python)

**Goal:**
Extract event-related potentials (ERPs) and spectral features from public EEG datasets.

**Key Skills Demonstrated:**

* EEG preprocessing (band-pass filter, ICA artifact removal)
* ERP extraction (N100, P300)
* Time-frequency (Morlet wavelets)
* Signal visualization with MNE-Python

**Dataset Sources (Public):**

* **PhysioNet EEG Motor Movement/Imagery Dataset**
* **BNCI Horizon 2020**

**Outputs included:**

* Cleaned EEG epochs
* ERP plots
* Power spectral density (PSD) graphs
* Notebook explaining methodology

---

## 🧮 2. Dopamine Reward Prediction Model (RL-based)

**Goal:**
Simulate dopamine-like reward prediction errors using classical reinforcement learning (Schultz et al., 1997).

**Key Skills Demonstrated:**

* Implementing Temporal Difference (TD) learning
* Simulating trial-by-trial RPE dynamics
* Visualizing positive and negative prediction errors
* Connecting RL theory to basal ganglia physiology

**Outputs included:**

* Learning curves
* RPE plots across trials
* Policy/value evolution
* Annotated Python code

---

## 📖 3. Mini-Review on Neuroinflammation & Synaptic Plasticity

**Goal:**
Summarize mechanistic links between neuroinflammation, microglial activation, and synaptic remodeling in CNS disorders.

**Components:**

* 15+ peer-reviewed papers synthesized
* Molecular pathways: TNF-α, IL-1β, NF-κB, complement signaling
* Functional consequences on LTP/LTD
* Implications for Alzheimer’s, depression, Parkinson’s

**Outputs included:**

* PDF review
* Structured notes folder
* Citations & bibliography

---

## 🧰 Tools & Libraries Used

* **Python:** NumPy, Pandas, Matplotlib, MNE-Python
* **ML/RL:** Basic TD Learning, Q-Learning
* **Documentation:** Markdown, LaTeX, BibTeX

---

## 📎 How to Reproduce the Projects

### Clone the repository

```bash
git clone https://github.com/<your-username>/neuroscience-portfolio.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Each subfolder also contains a **local README** with detailed reproduction instructions.

---

## 📬 Contact

If you'd like to collaborate on computational neuroscience or electrophysiology projects:

**Email:** odelanadavidp20@gmail.com
**GitHub:**https://github.com/Dafinci01/
**LinkedIn:** (optional)

---

## 🧩 License

MIT License — free to use, modify, and cite.

