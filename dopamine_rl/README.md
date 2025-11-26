# Dopamine RL Model Demo

Educational Q-learning demo that illustrates how temporal-difference (TD) errors evolve during learning.
TD error is used as a computational proxy for dopamine reward prediction error signals (Schultz et al., 1997).

## Contents
- `dopamine_rl.py` : Python script implementing the Q-learning demo.
- `q_values.npy` : saved Q-values after running the script.
- `results.csv` : episode-level reward and mean TD error.
- `qlearning_reward.png` : learning curve (moving average of episode reward).
- `qlearning_td_error.png` : mean absolute TD error per episode (moving average).

## Run
```bash
pip install numpy matplotlib
python3 dopamine_rl.py
