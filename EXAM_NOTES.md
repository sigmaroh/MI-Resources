# 📚 Machine Intelligence (MI) - Comprehensive Examination Notes

> **Complete Study Guide** covering all topics from Agents to Reinforcement Learning

---

## 📖 Table of Contents

1. [Agents](#1-agents)
2. [Search Algorithms](#2-search-algorithms)
3. [Constraint Satisfaction Problems (CSP)](#3-constraint-satisfaction-problems-csp)
4. [Planning](#4-planning)
5. [Game Trees & Minimax](#5-game-trees--minimax)
6. [Probability & Independence](#6-probability--independence)
7. [Bayesian Networks](#7-bayesian-networks)
8. [Bayesian Network Inference](#8-bayesian-network-inference)
9. [Machine Learning Basics](#9-machine-learning-basics)
10. [K-Nearest Neighbors (K-NN)](#10-k-nearest-neighbors-k-nn)
11. [Linear Regression & MSE](#11-linear-regression--mse)
12. [Neural Networks](#12-neural-networks)
13. [Learning Evaluation](#13-learning-evaluation)
14. [Clustering](#14-clustering)
15. [Markov Decision Processes (MDPs)](#15-markov-decision-processes-mdps)
16. [Reinforcement Learning & Q-Learning](#16-reinforcement-learning--q-learning)
17. [Key Exam Concepts](#17-key-exam-concepts)

---

## 1. Agents

**Agent:** An entity that perceives its environment through sensors and acts upon it through actuators.

**Rational Agent:** Selects actions that maximize expected performance measure given percept sequence and built-in knowledge.

### PEAS Framework

To design an agent, specify:
- **P**erformance measure: How we evaluate success
- **E**nvironment: What the agent operates in  
- **A**ctuators: How agent acts on environment
- **S**ensors: How agent perceives environment

**Example - Self-Driving Car:**
- P: Safety, speed, legality, comfort, profit
- E: Roads, traffic, pedestrians, weather
- A: Steering, accelerator, brake, horn, display
- S: Cameras, sonar, GPS, speedometer, engine sensors

### Agent Types

| Type | Description | Chooses Action Based On |
|------|-------------|------------------------|
| **Simple Reflex** | Condition-action rules | Current percept only |
| **Model-Based** | Maintains internal state | Current percept + internal model |
| **Goal-Based** | Plans to reach goals | Goals + how world evolves |
| **Utility-Based** | Maximizes utility function | Expected utility of outcomes |
| **Learning** | Improves over time | All above + learning element |

### Environment Properties

| Property | Options | Example |
|----------|---------|---------|
| **Observable** | Fully / Partially | Chess (fully) vs Poker (partially) |
| **Deterministic** | vs Stochastic | Chess (deterministic) vs Dice game (stochastic) |
| **Episodic** | vs Sequential | Image classification vs Chess |
| **Static** | vs Dynamic | Crossword (static) vs Self-driving (dynamic) |
| **Discrete** | vs Continuous | Chess (discrete) vs Taxi driving (continuous) |
| **Single-agent** | vs Multi-agent | Puzzle (single) vs Soccer (multi) |

**Hardest environment:** Partially observable, stochastic, sequential, dynamic, continuous, multi-agent

---

## 2. Search Algorithms

**Uninformed:**

| Alg | Complete | Optimal | Space     | Time      |
|-----|----------|---------|-----------|-----------|
| BFS | Yes      | Yes*    | O(b^d)    | O(b^d)    |
| DFS | No**     | No      | O(bd)     | O(b^m)    |
| UCS | Yes      | Yes     | O(b^d)    | O(b^d)    |

*If step costs same.  
**Complete if finite search space.

**Informed:**

- **A\***: $f(n)=g(n)+h(n)$  
    - $g(n)$ = cost so far  
    - $h(n)$ = heuristic  
    - Admissible $h$ = never overestimates
    - Consistent $h$: $h(n) \leq cost(n,n') + h(n')$

---

## 3. Constraint Satisfaction Problems (CSP)

**Key Concepts:**
- *Variables*: $V=\{a, b, c, d, ...\}$
- *Domains*: possible values for each variable
- *Constraints*: rules that limit combinations

**GAC (Generalized Arc Consistency):**
- For every variable's value, there must be some compatible value in other variables (as per constraints)
- Prune by removing unsupported values
- Repeat until "stuck"

**Examples:**

***Simple CSP:***
- $V = \{a, b, c, d\}, D = \{1,2,3,4,5\}$
- a + 2 < d; b × d < 6; a + c < 6  
After GAC:
- a ∈ {1,2}
- b ∈ {1}
- c ∈ {1,2,3,4}
- d ∈ {4,5}

***Equality/Inequality constraints:***
- $V = \{a,b,c,d\}$, $D = \{1,2,3\}$
- b = a, b > c, a ≠ c, c ≠ d, d ≤ a  
After GAC:
- a ∈ {2,3}
- b ∈ {2,3}
- c ∈ {1,2}
- d ∈ {1,2,3}

**Variable Elimination:**  
- Construct tables per constraint
- At each step, combine tables and eliminate a variable

---

## 4. Planning

**Planning Problem:** Find sequence of actions to reach goal state from initial state.

### STRIPS Representation

**State:** Conjunction of facts (ground atoms)  
**Goal:** Conjunction of literals  
**Action:** (preconditions, effects)

**Example Action:** *Fly(p, from, to)*
- **Precondition:** At(p, from), Plane(p), Airport(from), Airport(to)
- **Effect:** ¬At(p, from), At(p, to)

### Forward (Progression) Search
- Start from initial state
- Apply applicable actions
- Check if goal reached
- **Branching factor:** All applicable actions in current state

### Backward (Regression) Search  
- Start from goal
- Find actions that achieve goal
- Regress to find what must be true before
- **Branching factor:** Actions relevant to current goal

### Planning Graphs

**Structure:**
- Alternating state levels and action levels
- S₀ → A₀ → S₁ → A₁ → S₂ ...

**Mutexes (Mutual Exclusions):**
- **Inconsistent effects:** One action negates effect of another
- **Interference:** Effect of one deletes precondition of other
- **Competing needs:** Preconditions are mutex

**Heuristics from Planning Graph:**
- **Level cost:** First level where all goal literals appear
- **Max-level:** Max of individual goal literal first appearances
- **Set-level:** First level where all goals appear non-mutex

### GraphPlan Algorithm
1. Expand planning graph until all goals appear non-mutex
2. Try to extract solution (backward search in graph)
3. If extraction fails, expand graph further
4. Repeat until solution found or proven impossible

---

## 5. Game Trees & Minimax

**Minimax:**
- Max nodes pick max of children
- Min nodes pick min

Pseudocode:
```pseudo
function MINIMAX(node, depth, maximizingPlayer):
    if depth == 0 or node is terminal:
        return evaluation(node)
    if maximizingPlayer:
        value = -∞
        for each child:
            value = max(value, MINIMAX(child, depth-1, false))
        return value
    else:
        value = +∞
        for each child:
            value = min(value, MINIMAX(child, depth-1, true))
        return value
```

**Alpha-beta pruning:**  
Keep track of best value for max ($\alpha$), min ($\beta$). Prune when $\alpha \geq \beta$.

- Alpha-beta gives same answer as minimax, but fewer nodes.
- Best case: O(b^(d/2))

---

## 6. Probability & Independence

**Definition of Independence:**  
$P(X,Y) = P(X)P(Y)$ (for all values of X & Y)

**Example Table:**

|        | Disc=yes | Disc=no | P(Pos) |
|--------|----------|---------|--------|
| Pos=Y  | 0.03     | 0.27    | 0.30   |
| Pos=N  | 0.07     | 0.63    | 0.70   |
| P(Disc)| 0.10     | 0.90    |        |

All combinations match:  
e.g., $0.03 = 0.30×0.10$, $0.27 = 0.30×0.90$... so Positive ⟂ Discount

**Useful Probability Rules:**
- $P(A,B) = P(A|B) \cdot P(B)$
- Chain: $P(A,B,C) = P(A)P(B|A)P(C|A,B)$
- Bayes: $P(A|B) = P(B|A)P(A)/P(B)$
- Marginal: $P(X) = \sum_y P(X,Y=y)$

---

## 7. Bayesian Networks

- **Bayesian Network**: DAG with CPTs at each node
- Encodes conditional independencies.

**Example Structure:**
- Q → S, Q → P, Q → B
- C → S, C → B
- S → P, S → B
- P → B

**CPT Size:**
- General: $|Dom(X)| \times$ (product of parent sizes)
- Table:

| Var | Parents    | CPT            | #Entries      |
|-----|------------|----------------|--------------|
| Q   | none       | P(Q)           | 5            |
| C   | none       | P(C)           | 4            |
| S   | Q, C       | P(S|Q,C)       | 3×5×4 = 60   |
| P   | Q, S       | P(P|Q,S)       | 3×5×3 = 45   |
| B   | Q,S,C,P    | P(B|Q,S,C,P)   | 2×5×3×4×3=360|

**Chain Rule:**  
$P(Q,C,S,P,B) = P(Q)P(C)P(S|Q,C)P(P|Q,S)P(B|Q,S,C,P)$

---

## 8. Bayesian Network Inference

### Exact Inference: Variable Elimination

**Goal:** Compute P(X|e) for query variable X given evidence e

**Algorithm:**
1. **Start with factors:** One for each CPT
2. **Join factors:** Multiply factors that share variables
3. **Eliminate (sum out):** For each hidden variable:
   - Join all factors containing it
   - Sum over that variable's values
4. **Normalize:** Final factor gives unnormalized P(X, e)

**Example:** P(B|j,m) in Burglary network

```
Factors: P(B), P(E), P(A|B,E), P(J|A), P(M|A)
Evidence: J=true, M=true

1. Eliminate E:
   - Join P(E), P(A|B,E) → f₁(B,A)
   - Sum over E: f₁(B,A) = Σₑ P(E=e) P(A|B,e)

2. Eliminate A:  
   - Join f₁(B,A), P(J|A), P(M|A) → f₂(B)
   - Sum over A: f₂(B) = Σₐ f₁(B,a) P(j|a) P(m|a)

3. Final:
   - Multiply by P(B), normalize
```

**Complexity:** O(n × d^(w+1)) where w = induced width (treewidth)

### Approximate Inference: Sampling

**Direct Sampling:**
1. Sample variables in topological order
2. Use CPTs to determine probabilities
3. Count samples matching query

**Rejection Sampling:**
- Generate samples, reject those inconsistent with evidence
- Very inefficient if evidence is rare

**Likelihood Weighting:**
- Fix evidence variables
- Sample only non-evidence variables
- Weight each sample by P(evidence | parents)

**Gibbs Sampling (MCMC):**
- Start with random assignment
- Sample each non-evidence variable given others
- After burn-in, collect samples
- More efficient for rare evidence

---

## 9. Machine Learning Basics

### Types of Learning

**Supervised Learning**
- Training data is **labeled**
- Learn a mapping from inputs to outputs
- Examples: Classification, Regression

**Unsupervised Learning**
- Training data is **not labeled**
- Find patterns, structure, or groups in the data
- Examples: Clustering, Dimensionality Reduction

**Reinforcement Learning**
- Agent interacts with environment; receives rewards/penalties
- Goal: Maximize total reward over time

---

### Overfitting vs. Underfitting

| Condition     | Train Error | Test Error | Interpretation                              |
|---------------|-------------|------------|----------------------------------------------|
| Overfitting   | Low         | High       | Memorizes training data, can't generalize    |
| Underfitting  | High        | High       | Too simple, misses patterns                  |
| Good Fit      | Low         | Low        | Generalizes well                             |

> **Key:** Overfitting = Low train error, high test error

---

### Model Selection

How do you choose the best model for classification?
- It **depends on the metric that's most important** for your application:
    - **Accuracy:** % predicted correctly overall
    - **Precision:** Of predicted positives, what percent were correct?
    - **Recall:** Of actual positives, what percent did we find?
    - **F1-Score:** Harmonic mean of precision & recall

---

## 10. K-Nearest Neighbors (K-NN)

**Supervised Learning**
- Training data is **labeled**
- Learn a mapping from inputs to outputs
- Examples: Classification, Regression

**Unsupervised Learning**
- Training data is **not labeled**
- Find patterns, structure, or groups in the data
- Examples: Clustering, Dimensionality Reduction

**Reinforcement Learning**
- Agent interacts with environment; receives rewards/penalties
- Goal: Maximize total reward over time

---

### Overfitting vs. Underfitting

| Condition     | Train Error | Test Error | Interpretation                              |
|---------------|-------------|------------|----------------------------------------------|
| Overfitting   | Low         | High       | Memorizes training data, can't generalize    |
| Underfitting  | High        | High       | Too simple, misses patterns                  |
| Good Fit      | Low         | Low        | Generalizes well                             |

> **Key:** Overfitting = Low train error, high test error

---

### Model Selection

How do you choose the best model for classification?
- It **depends on the metric that's most important** for your application:
    - **Accuracy:** % predicted correctly overall
    - **Precision:** Of predicted positives, what percent were correct?
    - **Recall:** Of actual positives, what percent did we find?
    - **F1-Score:** Harmonic mean of precision & recall

---

## 2. K-Nearest Neighbors (K-NN)

**Algorithm Steps**
1. Compute distances to all training points
2. Select K closest neighbors
3. For classification: **vote** among labels; for regression: **average**

**Distance Metrics:**
- **Euclidean:** For continuous/mixed features  
  $$d = \sqrt{(\text{CategoricalDist})^2 + (f_2^\text{new} - f_2^i)^2}$$
- **Manhattan:**  
  $$d = \text{CategoricalDist}(F1) + |F2_\text{new} - F2_i|$$

**Example with Categorical + Numerical Features**

Distance table (Feature 1: Categorical):

|     | 1  | 2  | 3  |
|-----|----|----|----|
| 1   | 0  | 20 | 60 |
| 2   | 20 | 0  | 35 |
| 3   | 60 | 35 | 0  |

Dataset:

| ID | F1 | F2  | Class |
|----|----|-----|-------|
| 1  | 2  | 88  | A     |
| 2  | 2  | 80  | A     |
| 3  | 3  | 110 | A     |
| 4  | 1  | 69  | B     |
| 5  | 2  | 77  | B     |

**Query:** F1=2, F2=67

Manhattan Distances (|67-F2| plus categorical):

- 5: 0 + |67-77| = **10** (B)
- 2: 0 + |67-80| = **13** (A)
- 1: 0 + |67-88| = **21** (A)
- 4: 20 + |67-69| = **22** (B)
- 3: 35 + |67-110| = **78** (A)

Results:
- 1-NN: **B** (ID5)
- 3-NN: B, A, A → **A** (majority)

Euclidean Distances:

- 5: √(0² + 10²) = **10.0** (B)
- 2: √(0² + 13²) = **13.0** (A)
- 4: √(20² + 2²) ≈ **20.10** (B)
- 1: √(0² + 21²) = **21.0** (A)
- 3: √(35² + 43²) ≈ **55.44** (A)

Results:
- 1-NN: **B** (ID5)
- 3-NN: B, A, B → **B**

**Overfitting:**  
Low K (e.g. K=1) makes K-NN easily overfit to noise.  
High K = more smoothing, less overfitting.

---

## 3. Linear Regression & MSE

**Model:**
$$\hat{y} = w_0 + w_1x_1 + ... + w_nx_n$$

**MSE (Mean Squared Error):**

$$
MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

Properties:
- Always ≥ 0
- Bigger errors penalized extra
- Lower MSE = better model

**Example:**  
Given weights $w_0=1$, $w_1=2$, $w_2=-1$

| x₁ | x₂ | y | ŷ | Error | Error² |
|----|----|---|----|-------|--------|
| 3  | 2  | 4 |  5 |   -1  |   1    |
| 1  | 4  | 2 | -1 |    3  |   9    |
| 2  | 0  | 1 |  5 |   -4  |  16    |
| 1  | 1  | 3 |  2 |    1  |   1    |
| 0  | 4  | -1| -3 |    2  |   4    |

MSE $=(1+9+16+1+4)/5 = 6.2$

---

## 4. Neural Networks

**Backpropagation:**  
Weight update from neuron A to B depends on:
- Error at neuron B
- Input activation from A
- Activation function

Update rule:  
$$
\Delta w_{AB} = \alpha \cdot \text{input}_A \cdot \text{error}_B \cdot \text{activation}'
$$

**Learning Rate ($\alpha$):**
- Too small: slow learning
- Too big: may not converge
- Just right: fast, stable learning

Gradient descent used for:  
- Linear regression ✅  
- Neural networks ✅  
- NOT for: decision trees, k-NN, k-means

**Learning rate controls:**  
- how much you update weights

---

## 13. Learning Evaluation

### Train / Validation / Test Split

**Standard Practice:**
- **Training Set** (60-70%): Learn model parameters
- **Validation Set** (15-20%): Tune hyperparameters
- **Test Set** (15-20%): Final evaluation (use ONCE!)

**Golden Rule:** NEVER use test data for training or model selection

### Cross-Validation

**K-Fold Cross-Validation:**
1. Split data into K equal folds
2. For each fold i:
   - Train on all folds except i
   - Test on fold i
3. Average performance across all K runs

**Benefits:**
- Better use of limited data
- More reliable performance estimate
- Reduces variance in evaluation

**Leave-One-Out (LOO):** K = n (number of examples)
- Maximum data for training
- Computationally expensive
- Low bias, high variance

**Stratified K-Fold:** Preserves class distribution in each fold

### Confusion Matrix

For binary classification:

```
              Predicted
            Positive  Negative
Actual Pos    TP        FN
       Neg    FP        TN
```

**Metrics:**

| Metric | Formula | Meaning |
|--------|---------|---------|
| **Accuracy** | (TP+TN)/Total | Overall correctness |
| **Precision** | TP/(TP+FP) | Of predicted +, how many correct? |
| **Recall (Sensitivity)** | TP/(TP+FN) | Of actual +, how many found? |
| **Specificity** | TN/(TN+FP) | Of actual -, how many correct? |
| **F1-Score** | 2×P×R/(P+R) | Harmonic mean of P and R |

**Example:**

```
             Predicted
           Cancer  Healthy
Actual Can   90      10     (100 total)
       Hea   20     880     (900 total)
```

- Accuracy = (90+880)/1000 = 0.97
- Precision = 90/(90+20) = 0.818
- Recall = 90/(90+10) = 0.90
- F1 = 2×0.818×0.90/(0.818+0.90) = 0.857

### When to Use Which Metric?

| Scenario | Metric | Why |
|----------|--------|-----|
| Balanced classes | Accuracy | Treats all errors equally |
| False positives costly | Precision | Minimize FP (e.g., spam filter) |
| False negatives costly | Recall | Minimize FN (e.g., disease detection) |
| Need balance | F1-Score | Balances precision and recall |
| Imbalanced classes | F1, Precision, Recall | Accuracy can be misleading |

### ROC Curve & AUC

**ROC (Receiver Operating Characteristic):**
- Plot: True Positive Rate (Recall) vs False Positive Rate
- TPR = TP/(TP+FN)
- FPR = FP/(FP+TN)
- Each point = different classification threshold

**AUC (Area Under Curve):**
- AUC = 1.0: Perfect classifier
- AUC = 0.5: Random classifier
- AUC > 0.8: Good classifier

**Benefits:**
- Threshold-independent evaluation
- Works well for imbalanced data
- Compares classifiers easily

### Bias-Variance Tradeoff

**Bias:** Error from wrong assumptions
- High bias → underfitting
- Simple models have high bias

**Variance:** Error from sensitivity to training data
- High variance → overfitting
- Complex models have high variance

**Total Error = Bias² + Variance + Irreducible Error**

**Goal:** Find sweet spot with low bias AND low variance

---

## 14. Clustering

### K-Means Clustering

**Algorithm:**
```
1. Initialize K cluster centers (randomly or K-means++)
2. Repeat until convergence:
   a. Assignment step: Assign each point to nearest center
   b. Update step: Move centers to mean of assigned points
3. Stop when centers don't change (or change < threshold)
```

**Distance:** Usually Euclidean: $d(x,y) = \sqrt{\sum_i (x_i - y_i)^2}$

**Example:**

```
Data: (1,1), (2,1), (4,3), (5,4)
K = 2

Initial centers: c₁=(1,1), c₂=(2,1)

Iteration 1:
- Assign: {(1,1), (2,1)} → c₁; {(4,3), (5,4)} → c₂
- Update: c₁=(1.5,1), c₂=(4.5,3.5)

Iteration 2:
- Assign: {(1,1), (2,1)} → c₁; {(4,3), (5,4)} → c₂
- Update: c₁=(1.5,1), c₂=(4.5,3.5)
- No change → Stop
```

**Objective Function (Within-Cluster Sum of Squares):**
$$
WCSS = \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2
$$

K-means minimizes WCSS

### Choosing K

**Elbow Method:**
- Plot WCSS vs K
- Look for "elbow" where improvement slows
- Diminishing returns after optimal K

**Silhouette Score:**
$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$
- a(i) = avg distance to points in same cluster
- b(i) = avg distance to points in nearest other cluster
- s(i) ∈ [-1, 1], higher is better
- Average over all points to get overall score

### K-Means Properties

**Advantages:**
- Simple, fast, scalable
- Works well for spherical clusters
- Easy to implement

**Disadvantages:**
- Must specify K in advance
- Sensitive to initialization (use K-means++)
- Assumes spherical clusters of similar size
- Affected by outliers

**Time Complexity:** O(n × K × d × iterations)
- n = number of points
- K = number of clusters
- d = number of dimensions

### Hierarchical Clustering

**Agglomerative (Bottom-Up):**
```
1. Start: Each point is its own cluster
2. Repeat:
   - Find two closest clusters
   - Merge them
3. Stop: When desired # clusters reached (or all merged)
```

**Linkage Methods:**

| Method | Distance Between Clusters | Property |
|--------|---------------------------|----------|
| **Single** | min(d(a,b)) | Forms long chains |
| **Complete** | max(d(a,b)) | Compact clusters |
| **Average** | avg(d(a,b)) | Compromise |
| **Centroid** | d(μ_A, μ_B) | Similar to K-means |
| **Ward** | Minimizes variance | Best for spherical clusters |

**Output:** Dendrogram (tree showing merges)

**Advantages:**
- No need to specify K upfront
- Produces hierarchy of clusters
- Works with any distance metric

**Disadvantages:**
- Slow: O(n³) naive, O(n² log n) optimized
- Can't undo merges (greedy)
- Sensitive to noise and outliers

### Distance Metrics

**Euclidean:** $d(x,y) = \sqrt{\sum_i (x_i-y_i)^2}$
- Most common
- Sensitive to scale

**Manhattan:** $d(x,y) = \sum_i |x_i-y_i|$
- Less sensitive to outliers
- Good for grid-like data

**Cosine Similarity:** $sim(x,y) = \frac{x \cdot y}{||x|| \times ||y||}$
- Good for high-dimensional sparse data
- Used in text/document clustering
- Range: [-1, 1], higher = more similar

**Jaccard (for sets):** $J(A,B) = \frac{|A \cap B|}{|A \cup B|}$
- For binary/categorical data

---

## 15. Constraint Satisfaction Problems (CSP)

**Key Concepts:**
- *Variables*: $V=\{a, b, c, d, ...\}$
- *Domains*: possible values for each variable
- *Constraints*: rules that limit combinations

**GAC (Generalized Arc Consistency):**
- For every variable's value, there must be some compatible value in other variables (as per constraints)
- Prune by removing unsupported values
- Repeat until "stuck"

**Examples:**

***Simple CSP:***
- $V = \{a, b, c, d\}, D = \{1,2,3,4,5\}$
- a + 2 < d; b × d < 6; a + c < 6  
After GAC:
- a ∈ {1,2}
- b ∈ {1}
- c ∈ {1,2,3,4}
- d ∈ {4,5}

***Equality/Inequality constraints:***
- $V = \{a,b,c,d\}$, $D = \{1,2,3\}$
- b = a, b > c, a ≠ c, c ≠ d, d ≤ a  
After GAC:
- a ∈ {2,3}
- b ∈ {2,3}
- c ∈ {1,2}
- d ∈ {1,2,3}

**Variable Elimination:**  
- Construct tables per constraint
- At each step, combine tables and eliminate a variable

---

## 6. Probability & Independence

**Definition of Independence:**  
$P(X,Y) = P(X)P(Y)$ (for all values of X & Y)

**Example Table:**

|        | Disc=yes | Disc=no | P(Pos) |
|--------|----------|---------|--------|
| Pos=Y  | 0.03     | 0.27    | 0.30   |
| Pos=N  | 0.07     | 0.63    | 0.70   |
| P(Disc)| 0.10     | 0.90    |        |

All combinations match:  
e.g., $0.03 = 0.30×0.10$, $0.27 = 0.30×0.90$... so Positive ⟂ Discount

**Useful Probability Rules:**
- $P(A,B) = P(A|B) \cdot P(B)$
- Chain: $P(A,B,C) = P(A)P(B|A)P(C|A,B)$
- Bayes: $P(A|B) = P(B|A)P(A)/P(B)$
- Marginal: $P(X) = \sum_y P(X,Y=y)$

---

## 7. Bayesian Networks

- **Bayesian Network**: DAG with CPTs at each node
- Encodes conditional independencies.

**Example Structure:**
- Q → S, Q → P, Q → B
- C → S, C → B
- S → P, S → B
- P → B

**CPT Size:**
- General: $|Dom(X)| \times$ (product of parent sizes)
- Table:

| Var | Parents    | CPT            | #Entries      |
|-----|------------|----------------|--------------|
| Q   | none       | P(Q)           | 5            |
| C   | none       | P(C)           | 4            |
| S   | Q, C       | P(S|Q,C)       | 3×5×4 = 60   |
| P   | Q, S       | P(P|Q,S)       | 3×5×3 = 45   |
| B   | Q,S,C,P    | P(B|Q,S,C,P)   | 2×5×3×4×3=360|

**Chain Rule:**  
$P(Q,C,S,P,B) = P(Q)P(C)P(S|Q,C)P(P|Q,S)P(B|Q,S,C,P)$

---

## 8. Search Algorithms

**Uninformed:**

| Alg | Complete | Optimal | Space     | Time      |
|-----|----------|---------|-----------|-----------|
| BFS | Yes      | Yes*    | O(b^d)    | O(b^d)    |
| DFS | No**     | No      | O(bd)     | O(b^m)    |
| UCS | Yes      | Yes     | O(b^d)    | O(b^d)    |

*If step costs same.  
**Complete if finite search space.

**Informed:**

- **A\***: $f(n)=g(n)+h(n)$  
    - $g(n)$ = cost so far  
    - $h(n)$ = heuristic  
    - Admissible $h$ = never overestimates
    - Consistent $h$: $h(n) \leq cost(n,n') + h(n')$

---

## 9. Game Trees & Minimax

**Minimax:**
- Max nodes pick max of children
- Min nodes pick min

Pseudocode:
```pseudo
function MINIMAX(node, depth, maximizingPlayer):
    if depth == 0 or node is terminal:
        return evaluation(node)
    if maximizingPlayer:
        value = -∞
        for each child:
            value = max(value, MINIMAX(child, depth-1, false))
        return value
    else:
        value = +∞
        for each child:
            value = min(value, MINIMAX(child, depth-1, true))
        return value
```

**Alpha-beta pruning:**  
Keep track of best value for max ($\alpha$), min ($\beta$). Prune when $\alpha \geq \beta$.

- Alpha-beta gives same answer as minimax, but fewer nodes.
- Best case: O(b^(d/2))

---

## 15. Markov Decision Processes (MDPs)

**Key elements:**
- States: $S$
- Actions: $A$
- Transitions: $P(s'|s,a)$
- Rewards: $R(s,a)$
- Discount: $\gamma$

**Value Iteration:** (Bellman Equation)

$$
V_{k+1}(s) = \max_a \left( R(s,a) + \gamma \sum_{s'} P(s'|s,a) V_k(s') \right)
$$

**Steps:**
1. Start with $V_0$ for all states
2. Update using Bellman until converge
3. Policy $\pi(s) = \arg\max_a [R(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s')]$

**Discount factor $\gamma$:**
- High $\gamma$: long-term reward
- Low $\gamma$: immediate reward

---

## 16. Reinforcement Learning & Q-Learning

**Q-Learning core idea:**  
Learn $Q(s,a)$ = expected cumulative reward from (s,a) onward.

**Q-Learning update:**

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R + \gamma \max_{a'}Q(s', a') - Q(s,a)\right]
$$

Only update $Q(s,a)$ for action actually taken.

**Epsilon-Greedy:**  
- With probability $\epsilon$: random action (explore)
- With $1-\epsilon$: best action (exploit)

**Parameters:**
- $\alpha =$ learning rate (how big is update)
- $\gamma =$ discount factor (future value weight)
- $\epsilon =$ exploration rate

---

## 17. Key Exam Concepts

**Summary Table:**

| Method         | Picks Best Action By:                        |
|----------------|---------------------------------------------|
| Minimax        | Recursively computing min/max                |
| Value Iteration| $\arg\max$ of Bellman update                 |
| Q-learning     | $\arg\max Q(s, a)$                           |

**Supervised Learning Process:**
1. Train on labeled data
2. Validate (tune hyperparameters)
3. Test on unseen data

**Key Metrics:**
- Accuracy: (TP+TN)/Total
- Precision: TP/(TP+FP)
- Recall: TP/(TP+FN)
- F1: $2 \times$ (Precision × Recall) / (Precision + Recall)

**Common Pitfalls:**
- Learning rate does **not** affect # updates, only size
- Discount factor does **not** affect exploration, $\epsilon$ does
- Small K in K-NN = overfitting
- Only update $Q(s,a)$ for actual (s,a)
- Overfitting = low train error + high test error

**Formula Quick Reference:**

- MSE: $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$
- Bellman: $V(s) = \max_a [R(s,a) + \gamma \sum_{s'} P(s'|s,a)V(s')]$
- Q-learning: $Q(s,a) \leftarrow Q(s,a) + \alpha [R + \gamma \max_{a'} Q(s',a') - Q(s,a)]$
- Bayes: $P(A|B) = P(B|A)P(A)/P(B)$
- Independence: $P(X,Y) = P(X)P(Y)$

---

## 📝 Exam Preparation Checklist

**Must Know Cold**
- **Agents:** PEAS framework, agent types, environment properties
- **Search:** BFS/DFS/A*, admissible heuristics
- **CSP:** GAC algorithm, variable elimination
- **Planning:** STRIPS, forward/backward search, planning graphs
- **Game Theory:** Minimax, alpha-beta pruning
- **Probability:** Independence test ($P(X,Y)=P(X)P(Y)$), Bayes' theorem
- **Bayesian Networks:** CPT sizes, chain rule factorization
- **BN Inference:** Variable elimination steps
- **ML Basics:** Supervised vs. Unsupervised vs. RL
- **K-NN:** Distance calculations, voting, overfitting with small K
- **Linear Regression:** MSE calculation steps
- **Neural Networks:** Backpropagation, learning rate effects
- **Evaluation:** Confusion matrix metrics, cross-validation
- **Clustering:** K-means algorithm, choosing K
- **MDPs:** Bellman equation, value iteration
- **Q-Learning:** Update rule (only update taken $(s,a)$)
- **Parameters:** Distinguish $\gamma$, $\alpha$, $\epsilon$ effects

**Practice Problems:**
1. Design PEAS for an agent
2. Apply A* search with heuristic
3. GAC on constraint problem
4. STRIPS action representation
5. Minimax tree evaluation
6. Independence check from data table
7. Calculate CPT sizes for BN
8. Variable elimination inference
9. K-NN with mixed features
10. Calculate MSE
11. Backpropagation weight update
12. Confusion matrix metrics
13. K-means clustering iteration
14. MDP value iteration step
15. Q-table update

---

## 🎯 Final Tips

1. **Read the questions closely:** look for "NOT"
2. **Show your work:** partial credit!
3. **Check units:** probs sum to 1, squared errors can be big
4. **Draw diagrams!** (BNs, game trees)
5. **Check independence for all combos**
6. **Count CPTs carefully**
7. **Think through edge/terminal states**
8. **Manage your time** – don't get stuck

---

**Good luck with your examination! 🎓**

*This study guide covers all essential MI concepts. Review, practice, and succeed!*

