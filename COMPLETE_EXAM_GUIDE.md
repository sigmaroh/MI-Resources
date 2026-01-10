# 📚 Machine Intelligence - Complete Examination Guide

> **All-in-One Study Resource** - Theory, Examples, Formulas, and Quick Reference

---

## 📖 Table of Contents

### Part I: Core Topics (Detailed Coverage)
1. [Agents](#1-agents)
2. [Search Algorithms](#2-search-algorithms)
3. [Constraint Satisfaction Problems](#3-constraint-satisfaction-problems)
4. [Planning](#4-planning)
5. [Game Trees & Minimax](#5-game-trees--minimax)
6. [Probability & Independence](#6-probability--independence)
7. [Bayesian Networks](#7-bayesian-networks)
8. [Bayesian Network Inference](#8-bayesian-network-inference)
9. [Machine Learning Basics](#9-machine-learning-basics)
10. [K-Nearest Neighbors](#10-k-nearest-neighbors)
11. [Linear Regression & MSE](#11-linear-regression--mse)
12. [Neural Networks](#12-neural-networks)
13. [Learning Evaluation](#13-learning-evaluation)
14. [Clustering](#14-clustering)
15. [Markov Decision Processes](#15-markov-decision-processes)
16. [Reinforcement Learning](#16-reinforcement-learning)

### Part II: Quick Reference
- [Formula Sheet](#formula-sheet)
- [Problem-Solving Templates](#problem-solving-templates)
- [Common Mistakes](#common-mistakes)
- [Exam Checklist](#exam-checklist)

---

# Part I: Core Topics

## 1. Agents

**Agent:** Entity that perceives environment through sensors and acts through actuators.

**Rational Agent:** Selects actions that maximize expected performance measure.

### PEAS Framework

To design an agent, specify:
- **P**erformance: How we evaluate success
- **E**nvironment: What agent operates in
- **A**ctuators: How agent acts
- **S**ensors: How agent perceives

**Example - Self-Driving Car:**
- P: Safety, speed, legality, comfort, profit
- E: Roads, traffic, pedestrians, weather
- A: Steering, accelerator, brake, horn
- S: Cameras, sonar, GPS, speedometer

### Agent Types

| Type | Chooses Action Based On | Example |
|------|------------------------|---------|
| **Simple Reflex** | Current percept only | Thermostat |
| **Model-Based** | Current percept + internal state | Robot with map |
| **Goal-Based** | Goals + how world evolves | GPS navigation |
| **Utility-Based** | Expected utility of outcomes | Trading bot |
| **Learning** | All above + learning | Modern AI |

### Environment Properties

| Property | Options | Example |
|----------|---------|---------|
| **Observable** | Fully / Partially | Chess (fully) vs Poker (partially) |
| **Deterministic** | vs Stochastic | Chess vs Dice game |
| **Episodic** | vs Sequential | Image classification vs Chess |
| **Static** | vs Dynamic | Crossword vs Self-driving |
| **Discrete** | vs Continuous | Chess vs Taxi driving |
| **Single-agent** | vs Multi-agent | Puzzle vs Soccer |

**Hardest environment:** Partially observable, stochastic, sequential, dynamic, continuous, multi-agent

---

## 2. Search Algorithms

### Uninformed Search

| Algorithm | Complete | Optimal | Time | Space | Notes |
|-----------|----------|---------|------|-------|-------|
| **BFS** | Yes | Yes* | O(b^d) | O(b^d) | *If uniform cost |
| **DFS** | No** | No | O(b^m) | O(bd) | **Finite spaces only |
| **UCS** | Yes | Yes | O(b^d) | O(b^d) | Uniform Cost Search |
| **IDS** | Yes | Yes* | O(b^d) | O(bd) | Best of BFS+DFS |

Where: b=branching factor, d=depth of solution, m=max depth

### Informed Search: A*

**Formula:** $f(n) = g(n) + h(n)$

- $g(n)$ = actual cost from start to n
- $h(n)$ = heuristic estimate from n to goal
- $f(n)$ = estimated total cost

**Properties:**
- **Complete:** Yes (with admissible h)
- **Optimal:** Yes (with admissible + consistent h)

**Heuristic Properties:**
- **Admissible:** $h(n) \leq h^*(n)$ (never overestimates)
- **Consistent:** $h(n) \leq cost(n,n') + h(n')$ (triangle inequality)

**Common Heuristics:**
- 8-Puzzle: Misplaced tiles, Manhattan distance (both admissible)
- Navigation: Straight-line distance (admissible if no obstacles)

---

## 3. Constraint Satisfaction Problems

**Components:** CSP = (Variables, Domains, Constraints)

### Generalized Arc Consistency (GAC)

**Algorithm:**
1. Create arc pairs for each constraint
2. For each arc (X,Y): Remove values from $D_X$ with no support in $D_Y$
3. If $D_X$ changed, add all arcs (Z,X) to queue
4. Repeat until no changes

**Example 1:**
```
Variables: {a,b,c,d} ∈ {1,2,3,4,5}
Constraints: a+2<d; b×d<6; a+c<6

After GAC:
a ∈ {1,2}, b ∈ {1}, c ∈ {1,2,3,4}, d ∈ {4,5}
```

**Example 2:**
```
Variables: {a,b,c,d} ∈ {1,2,3}
Constraints: b=a; b>c; a≠c; c≠d; d≤a

After GAC:
a ∈ {2,3}, b ∈ {2,3}, c ∈ {1,2}, d ∈ {1,2,3}
```

### Variable Elimination

**Process:**
1. Create factor (table) for each constraint
2. Select variable to eliminate
3. Join all factors containing that variable
4. Project out (eliminate) that variable
5. Repeat

> **Key:** Table per CONSTRAINT, eliminate VARIABLE

---

## 4. Planning

**Goal:** Find sequence of actions from initial state to goal state.

### STRIPS Representation

- **State:** Conjunction of facts (ground atoms)
- **Goal:** Conjunction of literals
- **Action:** (preconditions, effects)

**Example Action:** Fly(p, from, to)
- Precondition: At(p,from), Plane(p), Airport(from), Airport(to)
- Effect: ¬At(p,from), At(p,to)

### Search Approaches

**Forward (Progression):**
- Start from initial state
- Apply applicable actions
- Branching factor: All applicable actions

**Backward (Regression):**
- Start from goal
- Find actions that achieve goal
- Branching factor: Actions relevant to goal

### Planning Graphs

**Structure:** S₀ → A₀ → S₁ → A₁ → S₂ ...

**Mutexes (Mutual Exclusions):**
- **Inconsistent effects:** One negates other
- **Interference:** Effect deletes precondition
- **Competing needs:** Preconditions are mutex

**Heuristics:**
- **Level cost:** First level with all goals
- **Max-level:** Max of individual goal appearances
- **Set-level:** First level with goals non-mutex

**GraphPlan Algorithm:**
1. Expand until all goals appear non-mutex
2. Try to extract solution (backward search)
3. If fails, expand further
4. Repeat until solution found

---

## 5. Game Trees & Minimax

### Minimax Algorithm

**Rules:**
- MAX player: Choose maximum child value
- MIN player: Choose minimum child value

**Pseudocode:**
```python
def minimax(node, depth, isMax):
    if depth == 0 or terminal:
        return evaluate(node)
    
    if isMax:
        return max(minimax(child, depth-1, False) 
                   for child in children)
    else:
        return min(minimax(child, depth-1, True)
                   for child in children)
```

### Alpha-Beta Pruning

**Variables:**
- $\alpha$ = best value for MAX so far
- $\beta$ = best value for MIN so far

**Prune when:** $\alpha \geq \beta$

**Benefits:**
- Same result as minimax
- Fewer nodes: Best case O(b^(d/2)) vs O(b^d)
- Move ordering matters

### Expectimax

For stochastic games with chance nodes:
- MAX nodes: take maximum
- CHANCE nodes: take expected value
- MIN nodes: take minimum

---

## 6. Probability & Independence

### Fundamental Rules

**Joint Probability:** $P(A,B) = P(A|B) \cdot P(B)$

**Chain Rule:** $P(A,B,C) = P(A) P(B|A) P(C|A,B)$

**Bayes' Theorem:** $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$

**Marginalization:** $P(X) = \sum_y P(X,Y=y)$

### Independence

**Definition:** X and Y are independent if:
$$P(X,Y) = P(X) \times P(Y) \text{ for ALL values}$$

**Equivalent conditions:**
- $P(X|Y) = P(X)$
- $P(Y|X) = P(Y)$
- Knowing Y doesn't change belief about X

### Example: Independence Check

| | Disc=yes | Disc=no | P(Pos) |
|---|----------|---------|--------|
| Pos=Y | 0.03 | 0.27 | 0.30 |
| Pos=N | 0.07 | 0.63 | 0.70 |
| P(Disc) | 0.10 | 0.90 | |

Check: $0.03 = 0.30 \times 0.10$ ✓, $0.27 = 0.30 \times 0.90$ ✓, etc.
→ Positive ⊥ Discount (Independent)

### Conditional Independence

**X ⊥ Y | Z** means:
$$P(X,Y|Z) = P(X|Z) \times P(Y|Z)$$

Given Z, X and Y are independent.

---

## 7. Bayesian Networks

**Structure:** Directed Acyclic Graph (DAG) + Conditional Probability Tables (CPTs)

### CPT Size Calculation

**Formula:**
$$\text{CPT size} = |Domain(X)| \times \prod_{\text{parent}} |Domain(\text{parent})|$$

**Example Network:**
- Q → S, Q → P, Q → B
- C → S, C → B
- S → P, S → B
- P → B

| Var | Parents | CPT | #Entries |
|-----|---------|-----|----------|
| Q | none | P(Q) | 5 |
| C | none | P(C) | 4 |
| S | Q, C | P(S\|Q,C) | 3×5×4 = 60 |
| P | Q, S | P(P\|Q,S) | 3×5×3 = 45 |
| B | Q,S,C,P | P(B\|Q,S,C,P) | 2×5×3×4×3 = 360 |

### Joint Probability Factorization

**Chain Rule for BNs:**
$$P(X_1,...,X_n) = \prod_i P(X_i | Parents(X_i))$$

**Example:** A → B → C
$$P(A,B,C) = P(A) \times P(B|A) \times P(C|B)$$

### D-Separation (Conditional Independence)

1. **Chain (A → B → C):** A ⊥ C | B (B blocks)
2. **Common Cause (A ← B → C):** A ⊥ C | B (B blocks)
3. **V-structure (A → C ← B):** A ⊥ B (not blocked); A ⊥̸ B | C (C opens!)

---

## 8. Bayesian Network Inference

### Exact Inference: Variable Elimination

**Goal:** Compute P(X|e) for query variable X given evidence e

**Algorithm:**
1. Start with factors: One for each CPT
2. Join factors: Multiply factors sharing variables
3. Eliminate hidden variables:
   - Join all factors containing it
   - Sum over variable's values
4. Normalize: Get final probability

**Example:** P(B|j,m) in Burglary network

```
Factors: P(B), P(E), P(A|B,E), P(J|A), P(M|A)
Evidence: J=true, M=true

1. Eliminate E:
   f₁(B,A) = Σₑ P(E=e) P(A|B,e)

2. Eliminate A:
   f₂(B) = Σₐ f₁(B,a) P(j|a) P(m|a)

3. Normalize over B
```

**Complexity:** O(n × d^(w+1)) where w = treewidth

### Approximate Inference: Sampling

**Direct Sampling:**
- Sample in topological order using CPTs
- Count samples matching query

**Rejection Sampling:**
- Generate samples, reject inconsistent with evidence
- Inefficient if evidence is rare

**Likelihood Weighting:**
- Fix evidence variables
- Sample non-evidence variables
- Weight by P(evidence | parents)

**Gibbs Sampling (MCMC):**
- Start with random assignment
- Sample each non-evidence variable given others
- After burn-in, collect samples
- Efficient for rare evidence

---

## 9. Machine Learning Basics

### Learning Types

| Type | Training Data | Goal | Examples |
|------|---------------|------|----------|
| **Supervised** | Labeled | Learn input→output | Classification, Regression |
| **Unsupervised** | Unlabeled | Find structure | Clustering, PCA |
| **Reinforcement** | Rewards | Maximize reward | Game AI, Robotics |

### Overfitting vs. Underfitting

| | Train Error | Test Error | Issue |
|---|-------------|------------|-------|
| **Overfitting** | Low ⬇️ | High ⬆️ | Memorizes, can't generalize |
| **Underfitting** | High ⬆️ | High ⬆️ | Too simple, misses patterns |
| **Good Fit** | Low ⬇️ | Low ⬇️ | Generalizes well |

> **Key:** Overfitting = Low train error + High test error

### Model Selection Metrics

**Choose based on application:**
- **Accuracy:** (TP+TN)/Total - overall correctness
- **Precision:** TP/(TP+FP) - of predicted +, how many correct?
- **Recall:** TP/(TP+FN) - of actual +, how many found?
- **F1-Score:** 2PR/(P+R) - harmonic mean

---

## 10. K-Nearest Neighbors

### Algorithm

1. Compute distances to all training points
2. Select K closest neighbors
3. **Classification:** Majority vote
4. **Regression:** Average value

### Distance Metrics

**Euclidean:**
$$d = \sqrt{\sum_i (x_i - y_i)^2}$$

**Manhattan:**
$$d = \sum_i |x_i - y_i|$$

**Mixed (categorical + numerical):**
$$d_{\text{Manhattan}} = \text{CatDist}(f_1) + |f_2^{\text{new}} - f_2^i|$$
$$d_{\text{Euclidean}} = \sqrt{\text{CatDist}(f_1)^2 + (f_2^{\text{new}} - f_2^i)^2}$$

### Example with Mixed Features

**Categorical Distance Table (Feature 1):**

| | 1 | 2 | 3 |
|---|---|---|---|
| 1 | 0 | 20 | 60 |
| 2 | 20 | 0 | 35 |
| 3 | 60 | 35 | 0 |

**Dataset:**

| ID | F1 | F2 | Class |
|----|----|----|-------|
| 1 | 2 | 88 | A |
| 2 | 2 | 80 | A |
| 3 | 3 | 110 | A |
| 4 | 1 | 69 | B |
| 5 | 2 | 77 | B |

**Query:** F1=2, F2=67

**Manhattan Distances:**
- ID5: 0 + |67-77| = 10 (B)
- ID2: 0 + |67-80| = 13 (A)
- ID1: 0 + |67-88| = 21 (A)
- ID4: 20 + |67-69| = 22 (B)
- ID3: 35 + |67-110| = 78 (A)

**Results:**
- 1-NN: **B** (ID5)
- 3-NN: B,A,A → **A** (majority)

### K Selection and Overfitting

- **Small K (K=1):** Complex boundaries, **overfits to noise**
- **Large K:** Smooth boundaries, **less overfitting**
- **Rule of thumb:** K = √n or use cross-validation

---

## 11. Linear Regression & MSE

### Model

$$\hat{y} = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n$$

### Mean Squared Error

$$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

**Properties:**
- Always ≥ 0
- Penalizes large errors more (squared)
- Lower MSE = better model

### Example Calculation

**Given:** $w_0=1$, $w_1=2$, $w_2=-1$

| x₁ | x₂ | y | ŷ | Error | Error² |
|----|----|---|-------|-------|--------|
| 3 | 2 | 4 | 5 | -1 | 1 |
| 1 | 4 | 2 | -1 | 3 | 9 |
| 2 | 0 | 1 | 5 | -4 | 16 |
| 1 | 1 | 3 | 2 | 1 | 1 |
| 0 | 4 | -1 | -3 | 2 | 4 |

**MSE** = (1+9+16+1+4)/5 = 31/5 = **6.2**

---

## 12. Neural Networks

### Architecture

**Structure:** Input Layer → Hidden Layers → Output Layer

**Neuron:** output = activation(Σᵢ wᵢxᵢ + bias)

### Activation Functions

| Function | Formula | Range | Use |
|----------|---------|-------|-----|
| Sigmoid | 1/(1+e⁻ˣ) | (0,1) | Output probabilities |
| Tanh | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | (-1,1) | Hidden layers |
| ReLU | max(0,x) | [0,∞) | Hidden (most common) |
| Softmax | eˣⁱ/Σeˣʲ | (0,1), sum=1 | Multi-class output |

### Backpropagation

**Weight Update:**
$$w_{ij} \leftarrow w_{ij} - \alpha \frac{\partial Loss}{\partial w_{ij}}$$

**What affects weight from A to B:**
- ✅ Error term at neuron B
- ✅ Input through that link
- ✅ Activation function
- ❌ NOT error at neuron A

### Learning Rate Effects

| α Value | Effect | Problem |
|---------|--------|---------|
| Too small | Slow convergence | Many iterations |
| Optimal | Fast, stable | Best performance |
| Too large | Oscillation | Overshoots minimum |

### Gradient Descent Variants

**Batch:** Use all data per update  
**Stochastic (SGD):** Use one example per update  
**Mini-batch:** Use batch of examples per update

**Which methods use gradient descent:**
- ✅ Linear Regression
- ✅ Neural Networks
- ❌ Decision Trees
- ❌ K-NN
- ❌ K-means (standard)

---

## 13. Learning Evaluation

### Data Split

- **Training (60-70%):** Learn parameters
- **Validation (15-20%):** Tune hyperparameters
- **Test (15-20%):** Final evaluation (use ONCE!)

**Golden Rule:** NEVER use test data for training/model selection

### Cross-Validation

**K-Fold:**
1. Split data into K folds
2. For each fold: Train on K-1, test on 1
3. Average results

**Leave-One-Out (LOO):** K = n (expensive but low bias)  
**Stratified K-Fold:** Preserves class distribution

### Confusion Matrix

```
              Predicted
            Pos    Neg
Actual Pos   TP     FN
       Neg   FP     TN
```

**Metrics:**

| Metric | Formula | When to Use |
|--------|---------|-------------|
| Accuracy | (TP+TN)/Total | Balanced classes |
| Precision | TP/(TP+FP) | Minimize false positives |
| Recall | TP/(TP+FN) | Minimize false negatives |
| Specificity | TN/(TN+FP) | True negative rate |
| F1-Score | 2PR/(P+R) | Balance precision & recall |

**Example:**
```
             Predicted
           Cancer  Healthy
Actual Can   90      10     (100)
       Hea   20     880     (900)

Accuracy = 970/1000 = 0.97
Precision = 90/110 = 0.818
Recall = 90/100 = 0.90
F1 = 2×0.818×0.90/(0.818+0.90) = 0.857
```

### ROC Curve & AUC

**ROC:** Plot TPR (Recall) vs FPR at different thresholds  
**AUC:** Area under ROC curve
- AUC = 1.0: Perfect
- AUC = 0.5: Random
- AUC > 0.8: Good

**Benefits:**
- Threshold-independent
- Works for imbalanced data

### Bias-Variance Tradeoff

**Bias:** Error from wrong assumptions (high = underfitting)  
**Variance:** Error from data sensitivity (high = overfitting)

**Total Error = Bias² + Variance + Irreducible Error**

**Goal:** Low bias AND low variance

---

## 14. Clustering

### K-Means Algorithm

```
1. Initialize K cluster centers (randomly or K-means++)
2. Repeat until convergence:
   a. Assignment: Assign each point to nearest center
   b. Update: Move centers to mean of assigned points
3. Stop when centers don't change
```

**Distance:** Usually Euclidean: $d(x,y) = \sqrt{\sum_i (x_i-y_i)^2}$

**Objective (WCSS):**
$$WCSS = \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2$$

K-means minimizes WCSS

### Choosing K

**Elbow Method:**
- Plot WCSS vs K
- Look for "elbow" where improvement slows

**Silhouette Score:**
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
- a(i) = avg distance within cluster
- b(i) = avg distance to nearest other cluster
- s(i) ∈ [-1,1], higher is better

### K-Means Properties

**Advantages:**
- Simple, fast, scalable
- Works well for spherical clusters

**Disadvantages:**
- Must specify K
- Sensitive to initialization
- Assumes spherical, similar-sized clusters
- Affected by outliers

**Time Complexity:** O(n × K × d × iterations)

### Hierarchical Clustering

**Agglomerative (Bottom-Up):**
1. Start: Each point is cluster
2. Repeatedly merge closest clusters
3. Stop: Desired number reached

**Linkage Methods:**

| Method | Distance | Property |
|--------|----------|----------|
| Single | min(d(a,b)) | Long chains |
| Complete | max(d(a,b)) | Compact clusters |
| Average | avg(d(a,b)) | Compromise |
| Ward | Minimizes variance | Best for spherical |

**Output:** Dendrogram (tree)

**Advantages:** No K needed, produces hierarchy  
**Disadvantages:** Slow O(n²logn), can't undo merges

### Distance Metrics

**Euclidean:** Most common, sensitive to scale  
**Manhattan:** Less sensitive to outliers  
**Cosine:** Good for high-dimensional sparse data  
**Jaccard:** For binary/categorical data

---

## 15. Markov Decision Processes

### Components

**MDP = (S, A, T, R, γ)**

- **S:** States
- **A:** Actions
- **T:** Transitions P(s'|s,a)
- **R:** Rewards R(s,a)
- **γ:** Discount factor [0,1]

### Bellman Equation

**Value of state:**
$$V^*(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s') \right]$$

**Optimal policy:**
$$\pi^*(s) = \arg\max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s') \right]$$

### Value Iteration

**Algorithm:**
```
1. Initialize V₀(s) for all s
2. Repeat until convergence:
     For each state s:
       V_{k+1}(s) = max_a [R(s,a) + γ Σ P(s'|s,a)V_k(s')]
3. Extract policy:
     π(s) = argmax_a [R(s,a) + γ Σ P(s'|s,a)V(s')]
```

**Convergence:** When max_s |V_{k+1}(s) - V_k(s)| < ε

### Policy Iteration

**Algorithm:**
```
1. Initialize policy π₀
2. Repeat:
     Policy Evaluation: Compute V^π
     Policy Improvement: π' = argmax_a [...]
   Until policy stable
```

Usually faster than value iteration.

### Discount Factor Effects

| γ Value | Effect | Interpretation |
|---------|--------|----------------|
| γ → 0 | Myopic | Values immediate rewards |
| γ → 1 | Far-sighted | Values future rewards |
| γ = 0.9 | Typical | Balances immediate/future |

**Important:** γ affects reward valuation, NOT exploration!

---

## 16. Reinforcement Learning

### Q-Learning

**Q-value:** Expected cumulative reward from (s,a) following optimal policy

**Update Rule:**
$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]$$

**Components:**
- **α:** Learning rate [0,1] - update magnitude
- **R:** Immediate reward
- **γ:** Discount factor [0,1] - future weight
- **s':** Next state
- **max Q(s',a'):** Best future value

### Key Properties

**Model-free:** Doesn't need P(s'|s,a) or R(s,a)

**Off-policy:** Learns optimal while following exploratory policy

**Convergence:** To Q* if:
- All (s,a) visited infinitely often
- Learning rate: Σα=∞, Σα²<∞

### Policy Extraction

**Greedy policy:** $\pi(s) = \arg\max_a Q(s,a)$

**State value:** $V(s) = \max_a Q(s,a)$

### Exploration vs. Exploitation

**ε-Greedy Strategy:**
```
With probability ε: random action (explore)
With probability 1-ε: best action (exploit)
```

**Strategies:**
- High ε early: Discover strategies
- Low ε later: Use known good strategies
- ε-decay: Gradually reduce ε

### Parameter Summary

| Parameter | Symbol | Controls | Typical |
|-----------|--------|----------|---------|
| Learning rate | α | Update magnitude | 0.01-0.1 |
| Discount | γ | Future weight | 0.9-0.99 |
| Exploration | ε | Random action prob | 0.1-0.3 |

**Critical Distinctions:**
- **α:** How MUCH to update (magnitude)
- **γ:** How much to VALUE future (NOT exploration!)
- **ε:** How much to EXPLORE (random vs greedy)

### Q-Learning Update Example

**Given:**
- Q(s,a) = 10
- Take action a, get R=5
- Land in s' where max Q(s',a')=8
- α=0.1, γ=0.9

**Update:**
```
Q(s,a) ← 10 + 0.1[5 + 0.9×8 - 10]
       = 10 + 0.1[5 + 7.2 - 10]
       = 10 + 0.1[2.2]
       = 10.22
```

**Key:** Only Q(s,a) changes! All others unchanged.

### SARSA (On-Policy Alternative)

**Update:**
$$Q(s,a) \leftarrow Q(s,a) + \alpha[R + \gamma Q(s',a') - Q(s,a)]$$

**Difference:** Uses actual next action a', not max

---

# Part II: Quick Reference

## Formula Sheet

### Probability Essentials
```
P(A|B) = P(A,B) / P(B)
P(A|B) = [P(B|A) × P(A)] / P(B)           [Bayes]
P(X) = Σy P(X,Y=y)                        [Marginalization]
P(X,Y) = P(X) × P(Y)                      [Independence]
P(A,B,C) = P(A) × P(B|A) × P(C|A,B)      [Chain Rule]
```

### Machine Learning
```
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
ŷ = w₀ + Σᵢ wᵢxᵢ
Accuracy = (TP+TN) / Total
Precision = TP / (TP+FP)
Recall = TP / (TP+FN)
F1 = 2PR / (P+R)
```

### Reinforcement Learning
```
V(s) = max_a [R(s,a) + γ Σ P(s'|s,a)V(s')]    [Bellman]
Q(s,a) ← Q(s,a) + α[R + γ max Q(s',a') - Q(s,a)]  [Q-Learning]
π(s) = argmax_a Q(s,a)                         [Policy]
V(s) = max_a Q(s,a)                            [State Value]
```

### Bayesian Networks
```
CPT_size = |Domain(X)| × ∏parent |Domain(parent)|
P(X₁,...,Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))          [Chain Rule]
```

---

## Problem-Solving Templates

### MSE Calculation
```
1. Calculate predictions: ŷ = w₀ + w₁x₁ + ...
2. Find errors: e = y - ŷ
3. Square errors: e²
4. Sum: Σe²
5. Divide by n: MSE = Σe²/n
```

### K-NN Classification
```
1. Calculate ALL distances
2. Sort by distance
3. Take K smallest
4. Count votes per class
5. Majority wins
```

### GAC Algorithm
```
1. List all constraints
2. Create arc pairs
3. For each arc, check values have support
4. Remove unsupported values
5. Repeat until stable
```

### Independence Check
```
1. Calculate joint P(X,Y) for all combinations
2. Calculate marginals P(X), P(Y)
3. For EACH combo: verify P(X,Y) = P(X)×P(Y)
4. ALL must match for independence
```

### CPT Size
```
1. Identify parents of node
2. Count domain size of node
3. Count domain size of each parent
4. Multiply: |D(X)| × ∏|D(parent)|
```

### Minimax
```
1. Start from leaves (bottom-up)
2. Work up level by level
3. MIN level: take minimum of children
4. MAX level: take maximum of children
5. Root = best achievable value
```

### Value Iteration
```
1. For each state, try each action
2. For each action: R + γ Σ P(s'|s,a)V(s')
3. Take maximum over actions
4. Update V(s)
5. Repeat until convergence
```

### Q-Learning Update
```
1. Identify (s, a, R, s') from transition
2. Find max_a' Q(s',a')
3. Calculate: α[R + γ max Q(s',a') - Q(s,a)]
4. Add to Q(s,a)
5. ONLY Q(s,a) changes!
```

---

## Common Mistakes

### ❌ WRONG → ✅ RIGHT

**Learning Rate:**
- ❌ Affects number of updates
- ✅ Affects magnitude of updates

**K-NN:**
- ❌ Smaller K reduces overfitting
- ✅ Larger K reduces overfitting (K=1 overfits most)

**Overfitting:**
- ❌ High train + high test error
- ✅ Low train + high test error

**Unsupervised Learning:**
- ❌ Training labeled, testing unlabeled
- ✅ Training data has NO labels

**Q-Learning:**
- ❌ Update all Q-values
- ✅ Update ONLY Q(s,a) taken

**Independence:**
- ❌ Check one combination
- ✅ Check ALL combinations

**Discount Factor:**
- ❌ Affects exploration
- ✅ Affects future valuation (ε affects exploration)

**CPT Size:**
- ❌ Multiply only parent domains
- ✅ Multiply node × all parent domains

**Backpropagation:**
- ❌ Update based on input neuron error
- ✅ Update based on output neuron error

---
## Quick Examples

### Example 1: MSE
```
Data: [(1,3), (2,5), (3,7)]
Model: ŷ = 2x

Predictions: [2, 4, 6]
Errors: [1, 1, 1]
MSE = 3/3 = 1.0
```

### Example 2: Independence
```
P(A=1,B=1) = 0.15
P(A=1) = 0.30, P(B=1) = 0.50

Check: 0.30 × 0.50 = 0.15 ✓
Must check all combinations!
```

### Example 3: Q-Learning
```
Q(s1,a2) = 10
Take a2, get R=5, land in s2
Q(s2) values: [8, 12]
α=0.1, γ=0.9

Update = 0.1[5 + 0.9×12 - 10]
       = 0.1[5.8] = 0.58
New Q(s1,a2) = 10.58
```

### Example 4: CPT Size
```
Node B: Domain {yes,no} = 2
Parents: A(3 values), C(4 values)
CPT = 2 × 3 × 4 = 24 entries
```

---

