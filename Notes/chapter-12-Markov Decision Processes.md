# Markov Decision Processes – Exam Notes

## 1. Introduction to MDPs

MDPs (Markov Decision Processes) model sequential decision-making under uncertainty.

**Key differences from classical planning:**

- Non-deterministic outcomes
- Reward-oriented (not only goal-oriented)
- Unbounded time horizon (possibly infinite steps)
- Fully observable, discrete, single-agent

---

## 2. Formal Definition of an MDP

An MDP is a 6-tuple $\Theta = (S, A, r, P, I, S_T)$:

- **$S$**: finite set of states
- **$A$**: finite set of actions
- **$r: S \times A \times S \rightarrow \mathbb{R}$** : reward function
- **$P: S \times A \times S \rightarrow [0,1]$** : transition probability function
- **$I \in S$**: initial state
- **$S_T \subseteq S$**: set of terminal states (can be empty)

**Markov Assumption:** The future depends only on the present state and action (not on the full history).

---

## 3. Policies in MDPs

A **policy** $\pi: S \rightarrow A$ maps states to actions.

- **Pure policy**: deterministic mapping.
- **Optimal policy**: maximizes expected cumulative reward.
- **Implication of Markov property**: policies do not depend on history.

---

## 4. Evaluating Policies: Expected Utility

**Problem:** Infinite horizon $\rightarrow$ cumulative reward may be infinite.

**Solutions:**
- *Finite Horizon:* Consider only first $k$ steps (may ignore long-term effects).
- *Discounted Rewards:* Weigh future rewards less.

The **discounted utility** is:
$$ U = r_0 + \gamma r_1 + \gamma^2 r_2 + \ldots $$
where $0 \leq \gamma < 1$.

- Ensures the sum is finite
- Typically, $\gamma \approx 1$, e.g., $0.99$, to balance short- and long-term rewards.

---

## 5. Value Functions

- **State-Value Function:** $V_\pi(s)$
    - Expected cumulative discounted reward starting from $s$ and following $\pi$.
- **Optimal Value Function:** $V^*(s)$
    $$
    V^*(s) = \max_\pi V_\pi(s)
    $$

**Bellman Equation (for $V^*$):**
$$
V^*(s) = R(s) + \max_{a \in A} \gamma \sum_{s'} P(s'|s, a)V^*(s')
$$

**Bellman Operator ($B$):**
$$
BV(s) = R(s) + \max_{a \in A} \gamma \sum_{s'} P(s'|s, a) V(s')
$$
- Repeated application of $B$ converges to $V^*$.

---

## 6. Value Iteration Algorithm

**Steps:**
1. **Initialize:** $V_0(s) = R(s)$ (or 0)
2. **Repeat until convergence:**  
   $$
   V_{i+1}(s) = R(s) + \max_{a \in A} \gamma \sum_{s'} P(s'|s, a)V_i(s')
   $$
   - Stop when $\max_s |V_{i+1}(s) - V_i(s)| < \epsilon$

3. **Extract optimal policy:**
   $$
   \pi^*(s) = \arg\max_{a \in A} \sum_{s'} P(s'|s, a)V^*(s')
   $$

**Convergence:** Guaranteed for $\gamma < 1$.

**Error bound after $m$ iterations:**
$$
m = \frac{\log(\epsilon (1-\gamma) / 2R_{max})}{\log(\gamma)}
$$

---

## 7. Policy Iteration Algorithm

**Steps:**
1. **Start** with random policy $\pi_0$
2. **Policy Evaluation:** Solve for $U_{\pi_i}$, where
   $$
   U_{\pi_i}(s) = R(s) + \gamma \sum_{s'} P(s' | s, \pi_i(s)) U_{\pi_i}(s')
   $$
   - This is a system of linear equations.

3. **Policy Improvement:**  
   $$
   \pi_{i+1}(s) = \arg\max_{a \in A} \sum_{s'} P(s' | s, a) U_{\pi_i}(s')
   $$

4. **Repeat** until policy unchanged.

---

## 8. Example: Grid World MDP

- **Setup:** $3 \times 3$ grid
    - Start: (1,1)
    - Gold: (3,1)
    - Snake: (2,3)
- **Actions:** {north, east, south, west}
- **Move succeeds:** $p=0.8$, otherwise moves right
- **Rewards:**
    - Gold: $+10$
    - Snake: $-5$
    - Move: $-0.1$

**Value Iteration Example ($\gamma=0.9$):**
- **Iteration 0:** All states = immediate reward
- **Iteration 1:**  
  $$
  V_1(1,2) = -0.1 + 0.9 \cdot \max(\text{expected future})
  $$
- **After convergence:** Optimal policy avoids snake, heads for gold.

---

## 9. Exercises with Solutions

### Exercise 1: Bellman Update

**Given:**

- $S = \{ s_1, s_2 \}$
- $A = \{ a_1, a_2 \}$

Transitions:

- $P(s_1|s_1, a_1) = 0.7$, $P(s_2|s_1, a_1) = 0.3$
- $P(s_1|s_1, a_2) = 0.2$, $P(s_2|s_1, a_2) = 0.8$

Rewards:

- $r(s_1, a_1, s_1) = 5$, $r(s_1, a_1, s_2) = -1$
- $r(s_1, a_2, s_1) = 2$, $r(s_1, a_2, s_2) = 1$

Values:  
$V(s_1)=10$, $V(s_2)=4$, $\gamma=0.9$, $R(s_1)=0$

**Compute new $V(s_1)$ using Bellman update:**

- $Q(s_1, a_1) = 0.7 \times (5 + 0.9 \times 10) + 0.3 \times (-1 + 0.9 \times 4) = 0.7 \times 14 + 0.3 \times 2.6 = 9.8 + 0.78 = 10.58$
- $Q(s_1, a_2) = 0.2 \times (2 + 0.9 \times 10) + 0.8 \times (1 + 0.9 \times 4) = 0.2 \times 11 + 0.8 \times 4.6 = 2.2 + 3.68 = 5.88$
- $V_\text{new}(s_1) = 0 + \max(10.58, 5.88) = 10.58$

---

### Exercise 2: Optimal Policy Extraction

**Given $V^*$:**
- $V^*(s_1)=20$, $V^*(s_2)=10$, $V^*(s_3)=5$

**Transitions from $s_1$:**
- $a_1$: $s_2$ with $p=0.6$, $s_3$ with $p=0.4$
- $a_2$: $s_1$ with $p=1.0$
- $\gamma=0.9$

**Compute $\pi^*(s_1)$:**

- $Q(s_1, a_1) = 0.6 \cdot 0.9 \cdot 10 + 0.4 \cdot 0.9 \cdot 5 = 5.4 + 1.8 = 7.2$
- $Q(s_1, a_2) = 1.0 \cdot 0.9 \cdot 20 = 18$
- $\pi^*(s_1) = a_2$ (since $18 > 7.2$)

---

### Exercise 3: Discount Factor Impact

**Question:** Why use $\gamma < 1$ in practice?

**Solution:**
- Ensures finite cumulative reward
- Models preference for immediate rewards
- Can represent probability of process ending
- Typical values: $\gamma = 0.9$ or $0.99$

---

### Exercise 4: Policy Evaluation

**Given:**  
Policy $\pi$: always choose $a_1$ from $s_1$

Transitions from $s_1$:
- $a_1 \rightarrow s_2$ (prob $0.8$, reward $1$)
- $a_1 \rightarrow s_1$ (prob $0.2$, reward $0$)

$\gamma = 0.9$, $R(s_1)=0$, $R(s_2)=0$

**Set up equation for** $U_\pi(s_1)$:

- $U_\pi(s_1) = 0 + 0.9[0.8 \times (1 + U_\pi(s_2)) + 0.2 \times (0 + U_\pi(s_1))]$
- $U_\pi(s_2) = 0$ (terminal)

Expand:
- $U_\pi(s_1) = 0.9 [0.8 \cdot 1 + 0.2 \cdot U_\pi(s_1)]$
- $U_\pi(s_1) = 0.72 + 0.18 U_\pi(s_1)$
- $0.82 U_\pi(s_1) = 0.72$
- $U_\pi(s_1) \approx 0.878$

---

## 10. Key Points for Exam

- **MDP components:** states, actions, rewards, transitions
- **Policies** map states to actions
- **Value functions:** quantify expected return
- **Bellman equation**: fundamental relationship
- **Solution methods:** Value Iteration and Policy Iteration
- **Discount factor $\gamma$:** ensures convergence and models time preference
- **Markov property:** future is independent of past given present
