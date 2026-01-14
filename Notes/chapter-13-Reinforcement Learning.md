# Reinforcement Learning – Exam Notes

---

## 1. Introduction to Reinforcement Learning

**RL vs. Supervised/Unsupervised Learning:**

- **Supervised**: Learn from labeled examples.
- **Unsupervised**: Find patterns in data (clustering).
- **Reinforcement**: Learn by interacting with an environment to maximize cumulative reward.

**Agent-Environment Interaction:**

- At time step *t*, agent observes state $s_t$, chooses action $a_t$, receives reward $r_{t+1}$ and moves to new state $s_{t+1}$.

**Goal:** Learn a policy that maximizes total reward.

---

## 2. MDP Recap

An MDP is defined as $\Theta = (S, A, r, P, I, S_T)$:

- $S$: states
- $A$: actions
- $r$: reward function
- $P$: transition probabilities
- $I$: initial state
- $S_T$: terminal states

- **Probabilistic Planning:** MDP known → compute optimal policy.
- **Reinforcement Learning:** MDP unknown → learn from interaction.

---

## 3. Model-Free vs Model-Based RL

- **Model-Free:** Learn policy/value function directly (e.g., Q-learning).
- **Model-Based:** Learn transition/reward model, then plan.

---

## 4. Q-Learning

- **Q-Value Definition:**
  - $Q^*(s, a)$: expected utility starting in state $s$, taking action $a$, then acting optimally.
- **Temporal Difference (TD) Update Rule:**
  - $$
  Q(s, a) \leftarrow (1-\alpha) Q(s, a) + \alpha \Big[r + \gamma \max_{a'} Q(s', a')\Big]
  $$

  where:
  - $\alpha$: learning rate
  - $\gamma$: discount factor
  - $r$: observed reward
  - $s'$: observed next state

- **TD Error:**
  - $$
  \text{TD error} = r + \gamma \max_{a'} Q(s', a') - Q(s, a)
  $$

---

## 5. Tabular Q-Learning Algorithm

```text
Initialize Q(s, a) arbitrarily
s ← initial state
repeat:
    a ← choose action (e.g., ε-greedy)
    execute a, observe r, s'
    Q(s, a) ← Q(s, a) + α [r + γ max_{a'} Q(s', a') - Q(s, a)]
    s ← s'
    if s is terminal: reset to initial state
until convergence
```

---

## 6. Exploration vs Exploitation

- **Exploitation:** Choose best-known action.
- **Exploration:** Try new actions to improve knowledge.

**$\epsilon$-greedy Policy:**

- With probability $1-\epsilon$: choose $\arg\max_a Q(s, a)$
- With probability $\epsilon$: choose random action

_Typically, start with high $\epsilon$, and decrease over time._

---

## 7. Convergence Conditions

Q-learning converges to optimal $Q^*$ if:

1. All state-action pairs are visited infinitely often.
2. Learning rate $\alpha_t$ satisfies:
   - $\sum_{t=1}^{\infty} \alpha_t = \infty$
   - $\sum_{t=1}^{\infty} \alpha_t^2 < \infty$

Example: $\alpha_t = 1/t$

---

## 8. Deep Q-Learning (DQN)

**Idea:**  
Use a neural network $Q(s, a; W)$ to approximate Q-values.

**Loss Function:**
$$
L(W) = \big[r + \gamma\max_{a'} Q(s', a'; W) - Q(s, a; W)\big]^2
$$

Update weights $W$ via gradient descent.

**Experience Replay:**  
- Store experiences $(s, a, r, s')$ in a replay buffer.
- Train on random mini-batches to break correlation in data.

**Architecture Example (Atari):**
- Input: $84 \times 84 \times 4$ (stack of 4 frames)
- Convolutional layers → fully connected layers → output Q-values for each action

---

## 9. Model-Based RL

- Learn $P(s' | s, a)$ and $r(s, a)$ from experience.
- Use learned model to plan (e.g., via value iteration).

---

## 10. Evaluation of RL Agents

- **Learning Curve:** Average return per episode over time.
- **Final Policy Performance:** Evaluate greedy policy after training.

---

## 11. Exercises with Solutions

### Exercise 1: Q-learning Update

**Given:**
- $Q(s_1, a_1) = 2.0$
- Take action $a_1$ in $s_1$, receive $r = 5$, go to $s_2$
- $Q(s_2, a_1) = 3.0$, $Q(s_2, a_2) = 1.0$
- $\alpha = 0.1$, $\gamma = 0.9$

**Compute new $Q(s_1,a_1)$:**  
- $\text{target} = r + \gamma \max_{a'} Q(s_2, a') = 5 + 0.9 \times 3.0 = 7.7$
- $Q_\text{new}(s_1,a_1) = (1-0.1) \times 2.0 + 0.1 \times 7.7 = 1.8 + 0.77 = 2.57$

---

### Exercise 2: $\epsilon$-greedy Action Selection

**Given:**
- $Q(s, [a_1, a_2, a_3]) = [4.0, 5.0, 3.0]$
- $\epsilon = 0.2$

**Probability of choosing each action:**
- Greedy action: $a_2$ (max Q = 5.0)
- With probability $1-\epsilon = 0.8$: choose $a_2$
- With probability $\epsilon = 0.2$: choose randomly among $\{a_1, a_2, a_3\}$

Final probabilities:
- $P(a_1) = 0.2/3 \approx 0.067$
- $P(a_2) = 0.8 + 0.2/3 \approx 0.867$
- $P(a_3) = 0.2/3 \approx 0.067$

---

### Exercise 3: TD Error Calculation

**Given:**
- $Q(s, a) = 10$
- After taking $a$: $r = 2$, new state $s'$ where $\max Q = 12$
- $\gamma = 0.9$

**TD error:**  
$\text{TD error} = r + \gamma \max Q(s') - Q(s,a) = 2 + 0.9 \times 12 - 10 = 2 + 10.8 - 10 = 2.8$

---

### Exercise 4: Convergence Conditions

**Which learning rate schedules satisfy convergence conditions?**

a) $\alpha_t = 0.1$ (constant)  
b) $\alpha_t = 1/t$  
c) $\alpha_t = 1/t^2$

**Solution:**

- a) **No**: $\sum \alpha_t = \infty$ but $\sum \alpha_t^2 = \infty$ (violates 2nd condition)
- b) **Yes**: $\sum 1/t = \infty$, $\sum 1/t^2 < \infty$
- c) **No**: $\sum 1/t^2 < \infty$ (fails 1st condition)

---

### Exercise 5: DQN Loss

**Given:**
- $Q(s, a; W) = 7$
- $r = 1$, $s'$ where $\max Q = 8$
- $\gamma=0.9$

**Compute loss $L(W)$:**  
- $\text{target} = 1 + 0.9 \times 8 = 8.2$
- $L(W) = (8.2 - 7)^2 = 1.44$

---

## 12. Key Points for Exam

- **Q-learning:** Model-free, TD updates, $\epsilon$-greedy exploration.
- **Convergence:** Requires infinite visits and decreasing $\alpha$.
- **Deep Q-Networks:** NN approximation, experience replay.
- **Model-based RL:** Learn transition model, then plan.
- **Evaluation:** Learning curves and final policy performance.
