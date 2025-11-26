#!/usr/bin/env python3
"""
dopamine_rl.py

Simple Q-learning simulation illustrating reward prediction error (TD error) dynamics
as a computational proxy for dopaminergic reward signaling (Schultz et al., 1997).

Outputs:
- q_values.npy        : learned Q-values
- qlearning_reward.png: moving-average episode reward plot
- qlearning_td_error.png: moving-average mean absolute TD error per episode
- results.csv         : episode, reward, mean_td_error
"""
import numpy as np
import matplotlib.pyplot as plt
import csv

# -------------------------
# Environment & parameters
# -------------------------
np.random.seed(1)

n_states = 5           # states 0..4, terminal state = 4
n_actions = 2          # actions: 0=left, 1=right
gamma = 0.9            # discount factor
alpha = 0.1            # learning rate
epsilon = 0.1          # exploration probability (epsilon-greedy)
n_episodes = 500

def step(state, action):
    """Stochastic chain: action 1 tends to move right, action 0 tends to move left.
       Reward=1 when agent reaches terminal state (n_states-1)."""
    prob = np.random.rand()
    if action == 1:
        ns = state + 1 if prob < 0.9 else state - 1
    else:
        ns = state - 1 if prob < 0.9 else state + 1
    ns = max(0, min(n_states-1, ns))
    reward = 1.0 if ns == n_states-1 else 0.0
    done = (ns == n_states-1)
    return ns, reward, done

# -------------------------
# Q-learning
# -------------------------
Q = np.zeros((n_states, n_actions))
episode_rewards = []
td_errors_all = []

for ep in range(n_episodes):
    state = 0
    total_reward = 0.0
    td_errors = []
    while True:
        # epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = np.random.randint(n_actions)
        else:
            action = int(np.argmax(Q[state]))
        ns, r, done = step(state, action)
        total_reward += r

        # Q update and TD error (delta)
        best_next = np.max(Q[ns])
        td_error = r + gamma * best_next - Q[state, action]
        Q[state, action] += alpha * td_error

        td_errors.append(abs(td_error))
        state = ns
        if done:
            break

    episode_rewards.append(total_reward)
    td_errors_all.append(np.mean(td_errors))

# -------------------------
# Save outputs and plots
# -------------------------
np.save("q_values.npy", Q)

# Save CSV results
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["episode", "reward", "mean_td_error"])
    for i, (r, td) in enumerate(zip(episode_rewards, td_errors_all), start=1):
        writer.writerow([i, r, td])

# Plot episode reward (10-episode moving average)
window = 10
if len(episode_rewards) >= window:
    ma_reward = np.convolve(episode_rewards, np.ones(window)/window, mode='valid')
else:
    ma_reward = episode_rewards

plt.figure(figsize=(7,4))
plt.plot(ma_reward)
plt.title("Q-learning: Episode Reward ({}-episode MA)".format(window))
plt.xlabel("Episode")
plt.ylabel("Reward (moving average)")
plt.tight_layout()
plt.savefig("qlearning_reward.png")
plt.close()

# Plot mean TD error per episode (10-episode moving average)
if len(td_errors_all) >= window:
    ma_td = np.convolve(td_errors_all, np.ones(window)/window, mode='valid')
else:
    ma_td = td_errors_all

plt.figure(figsize=(7,4))
plt.plot(ma_td)
plt.title("Q-learning: Mean |TD error| per Episode ({}-episode MA)".format(window))
plt.xlabel("Episode")
plt.ylabel("Mean |TD error|")
plt.tight_layout()
plt.savefig("qlearning_td_error.png")
plt.close()

print("Done. Saved: q_values.npy, results.csv, qlearning_reward.png, qlearning_td_error.png")
