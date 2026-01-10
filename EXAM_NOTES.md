# 📚 Machine Intelligence (MI) - Comprehensive Examination Notes

> **Complete Study Guide** covering all topics from Agents to Reinforcement Learning

---

## 📖 Table of Contents

1. [Machine Learning Basics](#1-machine-learning-basics)
2. [K-Nearest Neighbors (K-NN)](#2-k-nearest-neighbors-k-nn)
3. [Linear Regression & MSE](#3-linear-regression--mse)
4. [Neural Networks](#4-neural-networks)
5. [Constraint Satisfaction Problems (CSP)](#5-constraint-satisfaction-problems-csp)
6. [Probability & Independence](#6-probability--independence)
7. [Bayesian Networks](#7-bayesian-networks)
8. [Search Algorithms](#8-search-algorithms)
9. [Game Trees & Minimax](#9-game-trees--minimax)
10. [Markov Decision Processes (MDPs)](#10-markov-decision-processes-mdps)
11. [Reinforcement Learning & Q-Learning](#11-reinforcement-learning--q-learning)
12. [Key Exam Concepts](#12-key-exam-concepts)

---

## 1. Machine Learning Basics

### Types of Learning

#### **Supervised Learning**
- Training dataset **is labeled** with target features
- Goal: Learn mapping from inputs to outputs
- Examples: Classification, Regression

#### **Unsupervised Learning**
- Training dataset is **NOT labeled** with target features
- Goal: Find patterns, structures, groupings in data
- Examples: Clustering, Dimensionality Reduction

#### **Reinforcement Learning**
- Agent learns through interaction with environment
- Receives rewards/penalties for actions
- Goal: Maximize cumulative reward over time

---

### Overfitting vs. Underfitting

| Condition | Train Error | Test Error | Interpretation |
|-----------|-------------|------------|----------------|
| **Overfitting** | Low | High | Model memorizes training data, doesn't generalize |
| **Underfitting** | High | High | Model too simple, can't capture patterns |
| **Good Fit** | Low | Low | Model generalizes well |

**Key Point:** Overfitting = **Train error is low but test error is high**

---

### Model Selection

**Q: How to choose the best model for classification?**
- **Answer:** Depends on the application
- Different metrics for different goals:
  - **Accuracy**: Overall correctness
  - **Precision**: Of predicted positives, how many are correct?
  - **Recall**: Of actual positives, how many were found?
  - **F1-Score**: Harmonic mean of precision and recall

---

## 2. K-Nearest Neighbors (K-NN)

### Algorithm Overview
1. Calculate distance from new point to all training points
2. Select K nearest neighbors
3. Classify based on majority vote (classification) or average (regression)

### Distance Metrics

#### **Euclidean Distance**
For mixed features (categorical + numerical):

\[
d_{euclidean} = \sqrt{\text{CategoricalDist}^2 + (f_2^{new} - f_2^i)^2}
\]

#### **Manhattan Distance**
For mixed features:

\[
d_{manhattan} = \text{CategoricalDist}(F1) + |F2_{new} - F2_i|
\]

### Example with Mixed Features

**Setup:**
- Feature 1: Categorical {1, 2, 3} with distance table
- Feature 2: Numerical

**Distance Table for Feature 1:**

|     | 1  | 2  | 3  |
|-----|----|----|----| 
| 1   | 0  | 20 | 60 |
| 2   | 20 | 0  | 35 |
| 3   | 60 | 35 | 0  |

**Dataset:**

| ID | F1 | F2  | Class |
|----|----| ----|-------|
| 1  | 2  | 88  | A     |
| 2  | 2  | 80  | A     |
| 3  | 3  | 110 | A     |
| 4  | 1  | 69  | B     |
| 5  | 2  | 77  | B     |

**New observation:** F1=2, F2=67

**Manhattan Distances:**
- ID5: 0 + |67-77| = **10** (Class B)
- ID2: 0 + |67-80| = **13** (Class A)
- ID1: 0 + |67-88| = **21** (Class A)
- ID4: 20 + |67-69| = **22** (Class B)
- ID3: 35 + |67-110| = **78** (Class A)

**Results:**
- **1-NN Manhattan:** Class **B** (ID5)
- **3-NN Manhattan:** B, A, A → Class **A** (majority)

**Euclidean Distances:**
- ID5: √(0² + 10²) = **10.0** (Class B)
- ID2: √(0² + 13²) = **13.0** (Class A)
- ID4: √(20² + 2²) = **20.10** (Class B)
- ID1: √(0² + 21²) = **21.0** (Class A)
- ID3: √(35² + 43²) = **55.44** (Class A)

**Results:**
- **1-NN Euclidean:** Class **B** (ID5)
- **3-NN Euclidean:** B, A, B → Class **B** (majority)

---

### K-NN and Overfitting

**Q: Which value of K is more likely to lead to overfitting?**
- **Answer:** **K=1** (smaller K values)
- Smaller K → More sensitive to noise → Overfitting
- Larger K → Smoother decision boundaries → Less overfitting

---

## 3. Linear Regression & MSE

### Linear Regression Model

\[
\hat{y} = w_0 + w_1 x_1 + w_2 x_2 + ... + w_n x_n
\]

Where:
- \( \hat{y} \) = predicted value
- \( w_0 \) = bias/intercept
- \( w_i \) = coefficient for feature \( x_i \)

### Mean Squared Error (MSE)

\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

**Properties:**
- Always non-negative
- Penalizes large errors more (due to squaring)
- Lower MSE = better model
- MSE = 0 means perfect predictions

### Example Calculation

**Given:**
- w₀ = 1, w₁ = 2, w₂ = -1

| x₁ | x₂ | y  | ŷ | Error | Squared Error |
|----|----|----|----|-------|---------------|
| 3  | 2  | 4  | 5  | -1    | 1             |
| 1  | 4  | 2  | -1 | 3     | 9             |
| 2  | 0  | 1  | 5  | -4    | 16            |
| 1  | 1  | 3  | 2  | 1     | 1             |
| 0  | 4  | -1 | -3 | 2     | 4             |

**Predictions:**
- Row 1: ŷ = 1 + 2(3) + (-1)(2) = 5
- Row 2: ŷ = 1 + 2(1) + (-1)(4) = -1
- Row 3: ŷ = 1 + 2(2) + (-1)(0) = 5
- Row 4: ŷ = 1 + 2(1) + (-1)(1) = 2
- Row 5: ŷ = 1 + 2(0) + (-1)(4) = -3

**MSE = (1 + 9 + 16 + 1 + 4) / 5 = 31 / 5 = 6.2**

---

## 4. Neural Networks

### Backpropagation

**Q: What affects weight update from neuron A to neuron B?**

Correct factors:
- ✅ **a. The error term for neuron B**
- ✅ **d. The input through that link during forward propagation**
- ✅ **f. The type of activation function**

**Weight Update Rule:**

\[
\Delta w_{AB} = \alpha \cdot \text{input}_A \cdot \text{error}_B \cdot \text{activation}'
\]

---

### Learning Rate (α)

**Q: Which statement is true about learning rate α in gradient descent?**

✅ **Correct:** If the learning rate is very small, gradient descent can be slow to converge. If too large, gradient descent will overshoot.

**Learning Rate Effects:**
- **Too small α:** Slow convergence, many iterations needed
- **Too large α:** Overshooting, unstable, may diverge
- **Optimal α:** Fast, stable convergence

---

### Gradient Descent Applicability

**Which ML methods can use gradient descent?**
- ✅ **Linear Regression**
- ❌ Decision Trees (use splitting criteria)
- ❌ K-means (uses expectation-maximization)
- ❌ K-nearest neighbors (no training phase)
- ✅ **Neural Networks** (backpropagation)

---

### Key Neural Network Concepts

**Learning Rate:**
- ✅ Determines **how much** we update each weight
- ❌ Does NOT determine how many times we update
- ❌ Does NOT determine batch size
- ❌ Does NOT control which weights to update

---

## 5. Constraint Satisfaction Problems (CSP)

### Components
- **Variables:** V = {a, b, c, d, ...}
- **Domains:** D_v = possible values for each variable
- **Constraints:** Rules that must be satisfied

### Generalized Arc Consistency (GAC) Algorithm

**Goal:** Prune domains by removing values that cannot participate in any solution

**Process:**
1. Create arc pairs for each constraint
2. For each arc (X, Y), ensure every value in D_X has a compatible value in D_Y
3. Remove values that have no support
4. Repeat until no more changes

---

### Example 1: Simple CSP

**Variables:** V = {a, b, c, d}  
**Domains:** All variables ∈ {1, 2, 3, 4, 5}  
**Constraints:**
- a + 2 < d
- b × d < 6
- a + c < 6

**After GAC:**
- **a ∈ {1, 2}**
- **b ∈ {1}**
- **c ∈ {1, 2, 3, 4}**
- **d ∈ {4, 5}**

**Reasoning:**
1. a + 2 < d → a ∈ {1,2}, d ∈ {4,5}
2. b × d < 6 with d ∈ {4,5} → only b=1 works
3. a + c < 6 with a ∈ {1,2} → c ∈ {1,2,3,4}

---

### Example 2: Equality and Inequality Constraints

**Variables:** V = {a, b, c, d}  
**Domains:** All ∈ {1, 2, 3}  
**Constraints:**
- b = a
- b > c
- a ≠ c
- c ≠ d
- d ≤ a

**After GAC:**
- **a ∈ {2, 3}**
- **b ∈ {2, 3}**
- **c ∈ {1, 2}**
- **d ∈ {1, 2, 3}**

**Valid Tuples:**
- (2, 2, 1, 2)
- (3, 3, 1, 2)
- (3, 3, 1, 3)
- (3, 3, 2, 1)
- (3, 3, 2, 3)

---

### Variable Elimination Algorithm

**Q: In variable elimination for CSPs, which is correct?**

✅ **Correct:** We construct a table for each constraint, and at each step the algorithm removes a variable by combining all its constraints.

**Process:**
1. Start with one factor (table) per constraint
2. Choose a variable to eliminate
3. Join all factors involving that variable
4. Project out (eliminate) that variable
5. Repeat until all variables eliminated or solution found

---

## 6. Probability & Independence

### Independence Test

Two variables X and Y are **independent** if:

\[
P(X, Y) = P(X) \times P(Y)
\]

For all values of X and Y.

---

### Example: Restaurant Reviews

**Data:** 10,000 reviews with:
- Positive (yes/no)
- Discount (yes/no)
- Long (yes/no)

**Joint Distribution after marginalizing Long:**

| P(Positive, Discount) | Discount=yes | Discount=no | P(Positive) |
|-----------------------|--------------|-------------|-------------|
| Positive = yes        | 0.03         | 0.27        | **0.30**    |
| Positive = no         | 0.07         | 0.63        | **0.70**    |
| **P(Discount)**       | **0.10**     | **0.90**    |             |

**Independence Check:**
- P(yes, yes) = 0.03 = 0.30 × 0.10 ✓
- P(yes, no) = 0.27 = 0.30 × 0.90 ✓
- P(no, yes) = 0.07 = 0.70 × 0.10 ✓
- P(no, no) = 0.63 = 0.70 × 0.90 ✓

**Conclusion:** Positive and Discount are **INDEPENDENT**

---

### Probability Rules

**Joint Probability:**
\[
P(A, B) = P(A|B) \times P(B) = P(B|A) \times P(A)
\]

**Chain Rule:**
\[
P(A, B, C) = P(A) \times P(B|A) \times P(C|A,B)
\]

**Bayes' Theorem:**
\[
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
\]

**Marginalization:**
\[
P(X) = \sum_{y} P(X, Y=y)
\]

---

## 7. Bayesian Networks

### Definition
A Bayesian Network is:
- **Directed Acyclic Graph (DAG)** representing variables
- **Conditional Probability Tables (CPTs)** for each node
- Encodes conditional independence assumptions

### Structure

**Example Network:**
- Q → S, Q → P, Q → B
- C → S, C → B
- S → P, S → B
- P → B

**Variables:**
- Q: Quality {very poor, poor, average, good, very good} (5 values)
- S: Size {small, medium, big} (3 values)
- C: Color {red, blue, green, yellow} (4 values)
- P: Price {cheap, expensive, luxury} (3 values)
- B: Buy {yes, no} (2 values)

---

### CPT Size Calculation

**Formula:** 
\[
\text{CPT size} = |Domain(X)| \times \prod_{\text{parent } Y} |Domain(Y)|
\]

**For This Network:**

| Variable | Parents      | CPT          | # Entries              |
|----------|-------------|--------------|------------------------|
| Q        | none        | P(Q)         | 5                      |
| C        | none        | P(C)         | 4                      |
| S        | Q, C        | P(S\|Q,C)    | 3 × 5 × 4 = **60**     |
| P        | Q, S        | P(P\|Q,S)    | 3 × 5 × 3 = **45**     |
| B        | Q, S, C, P  | P(B\|Q,S,C,P)| 2 × 5 × 3 × 4 × 3 = **360** |

---

### Joint Probability Factorization

**Chain Rule for Bayesian Networks:**

\[
P(Q, C, S, P, B) = P(Q) \times P(C) \times P(S|Q,C) \times P(P|Q,S) \times P(B|Q,S,C,P)
\]

**Example:**
\[
P(\text{good, red, small, cheap, yes}) = 
\]
\[
P(\text{good}) \times P(\text{red}) \times P(\text{small}|\text{good, red}) \times
\]
\[
P(\text{cheap}|\text{good, small}) \times P(\text{yes}|\text{good, small, red, cheap})
\]

---

### Inference in Bayesian Networks

**Types of Queries:**
1. **Prior Marginal:** P(X)
2. **Posterior Marginal:** P(X | evidence)
3. **Most Probable Explanation (MPE):** argmax P(X | evidence)

**Methods:**
- **Exact:** Variable elimination, junction tree
- **Approximate:** Monte Carlo sampling, Markov Chain Monte Carlo

---

## 8. Search Algorithms

### Uninformed Search

| Algorithm | Complete? | Optimal? | Space | Time |
|-----------|-----------|----------|-------|------|
| BFS       | Yes       | Yes*     | O(b^d)| O(b^d)|
| DFS       | No**      | No       | O(bd) | O(b^m)|
| UCS       | Yes       | Yes      | O(b^d)| O(b^d)|

*If step costs are uniform  
**Complete in finite spaces

### Informed Search

**A* Search:**
\[
f(n) = g(n) + h(n)
\]

Where:
- g(n) = cost from start to node n
- h(n) = heuristic estimate from n to goal
- f(n) = estimated total cost

**Properties:**
- **Complete:** Yes (with admissible heuristic)
- **Optimal:** Yes (with admissible + consistent heuristic)

**Admissible Heuristic:** Never overestimates true cost (h(n) ≤ h*(n))

**Consistent Heuristic:** h(n) ≤ cost(n, n') + h(n')

---

## 9. Game Trees & Minimax

### Minimax Algorithm

**Goal:** Find optimal move assuming opponent plays optimally

**Rules:**
- **MAX player:** Choose move with highest value
- **MIN player:** Choose move with lowest value

**Pseudocode:**
```
function MINIMAX(node, depth, maximizingPlayer):
    if depth == 0 or node is terminal:
        return evaluation(node)
    
    if maximizingPlayer:
        value = -∞
        for each child of node:
            value = max(value, MINIMAX(child, depth-1, false))
        return value
    else:
        value = +∞
        for each child of node:
            value = min(value, MINIMAX(child, depth-1, true))
        return value
```

---

### Example: Minimax Tree

**Given values:**
- Leaves: I=-3, J=-9, K=4, L=-3, M=3, N=10, D=-7
- Non-terminal heuristics: e=-6, f=3, g=-8, h=-7

**Full-Depth Minimax:**
1. e = max(I, J) = max(-3, -9) = **-3**
2. f = max(I, J) = **-3**
3. g = max(K, L) = max(4, -3) = **4**
4. h = max(M, N) = max(3, 10) = **10**
5. B = min(e, f) = min(-3, -3) = **-3**
6. C = min(g, h) = min(4, 10) = **4**
7. A = max(B, C, D) = max(-3, 4, -7) = **4**

**Best move:** Choose **C** (value 4)

---

**Depth-Limited Minimax (depth=2):**
Use heuristic values at depth 2:
1. B = min(-6, 3) = **-6**
2. C = min(-8, -7) = **-8**
3. A = max(-6, -8, -7) = **-6**

**Best move:** Choose **B** (value -6)

**Note:** Best move changes with depth-limited search!

---

### Alpha-Beta Pruning

**Optimization:** Prune branches that cannot affect final decision

\[
\alpha = \text{best value for MAX so far}
\]
\[
\beta = \text{best value for MIN so far}
\]

**Prune when:** α ≥ β

**Benefits:**
- Same result as minimax
- Fewer nodes evaluated
- Best case: O(b^(d/2)) vs O(b^d)

---

## 10. Markov Decision Processes (MDPs)

### MDP Components

1. **States:** S = {s₁, s₂, ..., sₙ}
2. **Actions:** A = {a₁, a₂, ..., aₘ}
3. **Transition Model:** P(s'|s, a)
4. **Reward Function:** R(s, a) or R(s, a, s')
5. **Discount Factor:** γ ∈ [0, 1]

---

### Value Iteration

**Bellman Update:**

\[
V_{k+1}(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V_k(s') \right]
\]

**Algorithm:**
1. Initialize V₀(s) for all states
2. Repeat until convergence:
   - For each state s:
     - Update V(s) using Bellman equation
3. Extract policy: π(s) = argmax_a [R(s,a) + γ Σ P(s'|s,a) V(s')]

---

### MDP Example: Student & Solutions

**Setup:**
- 3×3 grid
- Student at various positions
- Goal: Get solutions (+5)
- Avoid teacher at (3,2) (-10)
- Movement cost: -0.3

**Transition Model:**
- 50% intended direction
- 30% stay in place
- 20% move right (relative to intended)

**Discount factor:** γ = 0.6

---

**Initial Values V₀:**
```
(1,3)=-2   (2,3)=3    (3,3)=6
(1,2)=6    (2,2)=-4   (3,2)=-12
(1,1)=3    (2,1)=1    (3,1)=0
```

**After 1 iteration V₁:**
- (3,2) = **-10.0** (terminal)
- (1,3) = **1.0**
- (3,3) = **5.0** (terminal)

**After 2 iterations V₂:**
- (2,3) = **1.618**
- (3,2) = **-10.000**
- (2,2) = **0.812**

---

### Discount Factor Effects

**High discount factor (γ → 1):**
- ✅ Values future rewards more
- ✅ Encourages long-term planning
- Makes agent "patient"

**Low discount factor (γ → 0):**
- ✅ Values immediate rewards more
- ✅ Discourages long-term planning
- Makes agent "myopic"

**Note:** Discount factor is NOT related to exploration/exploitation

---

## 11. Reinforcement Learning & Q-Learning

### Q-Learning Algorithm

**Q-value:** Expected cumulative reward from state s, taking action a, then following optimal policy

\[
Q(s, a) = \text{Expected total reward starting from } s, \text{ doing } a
\]

---

### Q-Learning Update Rule

\[
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]
\]

Where:
- α = learning rate (0 to 1)
- R = immediate reward
- γ = discount factor
- s' = next state after taking action a in state s

**Key Point:** Only update Q(s,a) for the actual (state, action) pair taken

---

### Q-Table Example 1

**Given Q-values:**

| State | a1  | a2  | a3  |
|-------|-----|-----|-----|
| S     | 13  | 8   | 5   |
| W     | 12  | 0   | 6   |
| L     | 0   | 2   | 5   |

**Questions:**

1. **Value of each state:**
   - V(S) = max(13, 8, 5) = **13**
   - V(W) = max(12, 0, 6) = **12**
   - V(L) = max(0, 2, 5) = **5**

2. **Best action in each state:**
   - S: **a1** (Q=13)
   - W: **a1** (Q=12)
   - L: **a3** (Q=5)

---

### Q-Table Example 2

**Given Q-values:**

| State | a1  | a2  | a3  |
|-------|-----|-----|-----|
| s1    | 8   | 10  | 15  |
| s2    | -20 | 7   | 13  |

**Questions:**

1. **Currently at s1, what action to maximize expected reward?**
   - **Answer: a3** (Q=15)

2. **At s1, expected cumulative reward with best policy?**
   - **Answer: 15** (= V(s1) = max Q(s1, a))

3. **Currently at s2, what action?**
   - **Answer: a3** (Q=13)

4. **At s2, expected reward?**
   - **Answer: 13**

---

### Q-Learning Table Update Example

**Scenario:**
- Current state: s1
- Take action: a1
- Receive reward: R = 100
- New state: s2
- Q(s2, a1) = -20, Q(s2, a2) = 7, Q(s2, a3) = 13

**Which Q-values update?**
- **Only Q(s1, a1)** updates
- All other entries remain unchanged

**Update (assuming α=1, γ=1):**
\[
Q(s1, a1) = R + \gamma \max_{a'} Q(s2, a') = 100 + 1 \times 13 = 113
\]

**Updated Table:**

| State | a1  | a2  | a3  |
|-------|-----|-----|-----|
| s1    | 113 | 10  | 15  |
| s2    | -20 | 7   | 13  |

---

### Exploration vs. Exploitation

**Epsilon-Greedy Strategy:**
- With probability ε: **Explore** (random action)
- With probability 1-ε: **Exploit** (best known action)

**Effects of ε:**
- **Higher ε:** More exploration, discover new strategies
- **Lower ε:** More exploitation, use known good strategies

**Important:**
- ε controls exploration/exploitation balance
- Discount factor γ controls future reward valuation
- Learning rate α controls update magnitude

**Relationships:**
- ✅ Higher ε → more exploration
- ✅ Higher γ → values long-term rewards more
- ❌ Discount factor NOT related to exploration/exploitation

---

## 12. Key Exam Concepts

### Decision Making Summary

| Algorithm/Method | Best Action | Based On |
|------------------|-------------|----------|
| **Minimax** | Best move | Recursive min/max of child values |
| **MDP Value Iteration** | Best action | argmax [R + γ Σ P(s'\|s,a)V(s')] |
| **Q-Learning** | Best action | argmax Q(s, a) |

---

### Training & Testing

**Supervised Learning Process:**
1. **Training Phase:** Learn parameters from labeled data
2. **Validation Phase:** Tune hyperparameters
3. **Testing Phase:** Evaluate on unseen data

**Key Metrics:**
- **Accuracy:** (TP + TN) / Total
- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **F1:** 2 × (Precision × Recall) / (Precision + Recall)

---

### Common Pitfalls

❌ **Wrong:** Thinking learning rate affects number of updates  
✅ **Right:** Learning rate affects magnitude of weight updates

❌ **Wrong:** Discount factor affects exploration  
✅ **Right:** Epsilon (ε) affects exploration

❌ **Wrong:** Smaller K in K-NN reduces overfitting  
✅ **Right:** Larger K reduces overfitting

❌ **Wrong:** In Q-learning, update all Q-values  
✅ **Right:** Only update Q(s,a) for the action taken

❌ **Wrong:** Overfitting means high train and test error  
✅ **Right:** Overfitting means low train, high test error

---

### Formula Quick Reference

**MSE:**
\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

**Bellman Equation (MDP):**
\[
V(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s') \right]
\]

**Q-Learning Update:**
\[
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]
\]

**Bayes' Theorem:**
\[
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
\]

**Independence:**
\[
P(X,Y) = P(X) P(Y)
\]

---

## 📝 Exam Preparation Checklist

### Must Know Cold:
- ✅ Difference between supervised and unsupervised learning
- ✅ What overfitting looks like (low train, high test error)
- ✅ How K-NN classifies (distance + voting)
- ✅ MSE calculation steps
- ✅ What affects neural network weight updates
- ✅ Learning rate effects (too small = slow, too large = overshoot)
- ✅ GAC algorithm for CSPs
- ✅ Independence test: P(X,Y) = P(X)P(Y)
- ✅ CPT size calculation for Bayesian Networks
- ✅ Minimax algorithm (max for MAX, min for MIN)
- ✅ MDP Value Iteration Bellman equation
- ✅ Q-Learning update rule (only update Q(s,a) taken)
- ✅ Discount factor vs learning rate vs epsilon

### Practice Problems:
1. Calculate distances for K-NN with mixed features
2. Compute MSE given model predictions
3. Apply GAC to constrained CSP
4. Check independence from data table
5. Calculate CPT sizes for Bayesian Network
6. Perform minimax on game tree
7. Execute one iteration of Value Iteration
8. Update Q-table given transition
9. Identify which ML methods use gradient descent

---

## 🎯 Final Tips

1. **Read questions carefully** - "NOT" questions are common
2. **Show your work** - partial credit on calculations
3. **Check units** - probabilities sum to 1, errors can be negative
4. **Draw diagrams** - for Bayesian Networks and game trees
5. **Verify independence** - check ALL combinations
6. **Count carefully** - CPT sizes, domain products
7. **Remember edge cases** - terminal states, boundary conditions
8. **Practice time management** - don't get stuck on one problem

---

**Good luck with your examination! 🎓**

*This study guide consolidates all key concepts from the MI course. Review each section, practice the examples, and test yourself with the exercises.*

