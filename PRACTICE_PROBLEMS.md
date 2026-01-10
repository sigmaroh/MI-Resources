# 🎯 MI Practice Problems & Solutions

> **Practice makes perfect** - Work through these problems to master each topic

---

## 📑 Contents by Topic

1. [Machine Learning Fundamentals](#1-machine-learning-fundamentals)
2. [K-Nearest Neighbors](#2-k-nearest-neighbors)
3. [Linear Regression](#3-linear-regression)
4. [Neural Networks](#4-neural-networks)
5. [Constraint Satisfaction Problems](#5-constraint-satisfaction-problems)
6. [Probability & Statistics](#6-probability--statistics)
7. [Bayesian Networks](#7-bayesian-networks)
8. [Search Algorithms](#8-search-algorithms)
9. [Game Theory & Minimax](#9-game-theory--minimax)
10. [Markov Decision Processes](#10-markov-decision-processes)
11. [Reinforcement Learning](#11-reinforcement-learning)

---

## 1. Machine Learning Fundamentals

### Problem 1.1: Learning Types

**Question:** Classify each scenario as supervised, unsupervised, or reinforcement learning:

a) Training a spam filter using 10,000 labeled emails  
b) Grouping customers by purchasing behavior (no labels)  
c) Teaching a robot to walk using trial and error  
d) Predicting house prices from historical sales data  
e) Finding topics in a collection of documents (no labels)

**Solution:**
- a) **Supervised** - labeled data (spam/not spam)
- b) **Unsupervised** - no labels, finding groups
- c) **Reinforcement** - trial and error with rewards
- d) **Supervised** - labeled historical data
- e) **Unsupervised** - no labels, finding patterns

---

### Problem 1.2: Overfitting Identification

**Question:** You train a neural network and get these results:

| Model | Train Accuracy | Test Accuracy |
|-------|----------------|---------------|
| A     | 99%            | 60%           |
| B     | 75%            | 73%           |
| C     | 65%            | 64%           |

Which model is:
- Overfitting?
- Underfitting?
- Best generalization?

**Solution:**
- **Overfitting:** Model A (high train, low test - memorizing)
- **Underfitting:** Model C (both low - too simple)
- **Best:** Model B (close train/test scores, highest test)

---

### Problem 1.3: Model Selection

**Question:** You're building a medical diagnosis system. Which metric is most important if:
a) Missing a disease is very costly (false negative is bad)  
b) False alarms are very costly (false positive is bad)  
c) You need balance between both

**Solution:**
- a) **Recall** - want to catch all diseases (minimize false negatives)
- b) **Precision** - want to avoid false alarms (minimize false positives)
- c) **F1-Score** - balances precision and recall

---

## 2. K-Nearest Neighbors

### Problem 2.1: Basic K-NN

**Question:** Given training data:

| Point | x | y | Class |
|-------|---|---|-------|
| A     | 1 | 2 | Red   |
| B     | 2 | 3 | Red   |
| C     | 3 | 1 | Blue  |
| D     | 5 | 4 | Blue  |
| E     | 6 | 2 | Blue  |

Classify new point P(3, 3) using K=3 and Euclidean distance.

**Solution:**

**Step 1: Calculate distances**
- A to P: √[(3-1)² + (3-2)²] = √(4+1) = √5 ≈ 2.24
- B to P: √[(3-2)² + (3-3)²] = √(1+0) = 1.00
- C to P: √[(3-3)² + (3-1)²] = √(0+4) = 2.00
- D to P: √[(5-3)² + (4-3)²] = √(4+1) = √5 ≈ 2.24
- E to P: √[(6-3)² + (2-3)²] = √(9+1) = √10 ≈ 3.16

**Step 2: Sort by distance**
1. B (1.00) - Red
2. C (2.00) - Blue
3. A (2.24) - Red
4. D (2.24) - Blue
5. E (3.16) - Blue

**Step 3: K=3 nearest**
B (Red), C (Blue), A (Red)

**Step 4: Vote**
Red: 2, Blue: 1

**Answer: Red**

---

### Problem 2.2: K-NN with Categorical Features

**Question:** 
Feature 1: Categorical with distance table:
|   | A | B | C |
|---|---|---|---|
| A | 0 | 10| 20|
| B | 10| 0 | 15|
| C | 20| 15| 0 |

Feature 2: Numerical

Training data:
| ID | F1 | F2 | Class |
|----|----|----|-------|
| 1  | A  | 5  | +     |
| 2  | B  | 8  | +     |
| 3  | C  | 3  | -     |
| 4  | B  | 2  | -     |

Classify (F1=B, F2=6) using K=3 with Manhattan distance.

**Solution:**

**Manhattan distances:**
- ID1: d(B,A) + |6-5| = 10 + 1 = 11
- ID2: d(B,B) + |6-8| = 0 + 2 = 2
- ID3: d(B,C) + |6-3| = 15 + 3 = 18
- ID4: d(B,B) + |6-2| = 0 + 4 = 4

**3 nearest:**
1. ID2 (2) - Class +
2. ID4 (4) - Class -
3. ID1 (11) - Class +

**Vote:** +: 2, -: 1

**Answer: Class +**

---

### Problem 2.3: K Selection

**Question:** What happens to K-NN classifier as K increases from 1 to N (total training examples)?

**Solution:**
- **K=1:** Most complex, prone to overfitting, very flexible boundaries
- **K increasing:** Smoother boundaries, less overfitting
- **K=N:** Predicts majority class for all points, maximally simple
- **Sweet spot:** Usually odd number (avoid ties), often √N or cross-validated

---

## 3. Linear Regression

### Problem 3.1: Prediction

**Question:** Given model: ŷ = 3 + 2x₁ - x₂

Predict for:
a) x₁=5, x₂=2  
b) x₁=0, x₂=10  
c) x₁=3, x₂=3

**Solution:**
- a) ŷ = 3 + 2(5) - 2 = 3 + 10 - 2 = **11**
- b) ŷ = 3 + 2(0) - 10 = 3 - 10 = **-7**
- c) ŷ = 3 + 2(3) - 3 = 3 + 6 - 3 = **6**

---

### Problem 3.2: MSE Calculation

**Question:** Calculate MSE for predictions:

| Actual | Predicted |
|--------|-----------|
| 10     | 12        |
| 15     | 13        |
| 8      | 8         |
| 20     | 18        |

**Solution:**

| y | ŷ | Error | Squared Error |
|---|---|-------|---------------|
| 10| 12| -2    | 4             |
| 15| 13| 2     | 4             |
| 8 | 8 | 0     | 0             |
| 20| 18| 2     | 4             |

MSE = (4 + 4 + 0 + 4) / 4 = 12 / 4 = **3.0**

---

### Problem 3.3: MSE Comparison

**Question:** Which model is better?

**Model A:** MSE = 15.3  
**Model B:** MSE = 8.7

**Solution:**
**Model B** is better (lower MSE = smaller average squared error)

---

## 4. Neural Networks

### Problem 4.1: Backpropagation Concepts

**Question:** True or False:

a) Weight from A to B is updated based on error at B  
b) Weight from A to B is updated based on error at A  
c) Learning rate determines how many times we update  
d) Learning rate determines how much we update  
e) Activation function type affects gradients

**Solution:**
- a) **TRUE** - error backpropagates from output
- b) **FALSE** - uses error at receiving neuron (B)
- c) **FALSE** - doesn't determine number of updates
- d) **TRUE** - controls magnitude of updates
- e) **TRUE** - affects gradient computation

---

### Problem 4.2: Learning Rate Effects

**Question:** Match the learning rate with the outcome:

Learning rates: 0.0001, 0.1, 10.0

Outcomes:
- A) Overshoots, unstable, diverges
- B) Very slow convergence, many iterations
- C) Reasonable convergence speed

**Solution:**
- 0.0001 → **B** (too small, slow)
- 0.1 → **C** (reasonable)
- 10.0 → **A** (too large, overshoots)

---

### Problem 4.3: Gradient Descent Methods

**Question:** Which methods can use gradient descent?

a) Linear Regression  
b) Decision Trees  
c) K-NN  
d) Neural Networks  
e) K-means clustering  

**Solution:**
- a) **YES** - can optimize weights via gradient descent
- b) **NO** - uses splitting criteria (greedy algorithm)
- c) **NO** - no training phase, just stores data
- d) **YES** - backpropagation uses gradient descent
- e) **NO** - uses EM algorithm (though gradient-based variants exist)

---

## 5. Constraint Satisfaction Problems

### Problem 5.1: Domain Reduction

**Question:** Apply GAC to:

Variables: {X, Y, Z}  
Domains: X ∈ {1,2,3}, Y ∈ {1,2,3}, Z ∈ {1,2,3}  
Constraints:
- X < Y
- Y < Z
- X + Z ≤ 4

**Solution:**

**Step 1: X < Y**
- X can be 1,2 (not 3, as Y would have no valid value > 3)
- Y can be 2,3 (not 1, as no X < 1)

**Step 2: Y < Z**
- Y can be 1,2 (not 3, as Z would have no valid value > 3)
- Combined with previous: Y ∈ {2}
- Z ∈ {3} (must be > Y=2)

**Step 3: X + Z ≤ 4**
- Z = 3, so X ≤ 1
- Combined with X ∈ {1,2}: X = 1

**Final domains:**
- **X = {1}**
- **Y = {2}**
- **Z = {3}**

**Valid solution:** (1, 2, 3)

---

### Problem 5.2: Arc Consistency

**Question:** Given constraint X + Y = 5 with:
- X ∈ {1, 2, 3, 4}
- Y ∈ {1, 2, 3, 4}

What are domains after arc consistency?

**Solution:**

**For arc (X, Y):** For each X, must have Y = 5-X
- X=1 → Y=4 ✓
- X=2 → Y=3 ✓
- X=3 → Y=2 ✓
- X=4 → Y=1 ✓

**For arc (Y, X):** Same analysis

**Final domains:**
- **X ∈ {1, 2, 3, 4}** (all have support)
- **Y ∈ {1, 2, 3, 4}** (all have support)

No pruning needed - all values have support.

---

### Problem 5.3: Multiple Constraints

**Question:** Variables A, B ∈ {1,2,3,4,5}

Constraints:
- A > B
- A + B > 7

After GAC, what are valid domains?

**Solution:**

**Analyze A + B > 7:**
Valid pairs: (3,5), (4,4), (4,5), (5,3), (5,4), (5,5) and more...

**Add constraint A > B:**
Must have A > B AND A + B > 7:
- (4,4): 4>4? NO
- (5,3): 5>3? YES, 5+3=8>7? YES ✓
- (5,4): 5>4? YES, 5+4=9>7? YES ✓
- (4,5): 4>5? NO
- etc.

Valid pairs: (5,3), (5,4), (4,3), etc.

**Final domains:**
- **A ∈ {4, 5}**
- **B ∈ {1, 2, 3, 4}**

(More specific: A=4→B∈{1,2,3}, A=5→B∈{1,2,3,4})

---

## 6. Probability & Statistics

### Problem 6.1: Independence Check

**Question:** Given joint distribution:

| P(X,Y) | Y=0 | Y=1 |
|--------|-----|-----|
| X=0    | 0.2 | 0.3 |
| X=1    | 0.1 | 0.4 |

Are X and Y independent?

**Solution:**

**Marginals:**
- P(X=0) = 0.2 + 0.3 = 0.5
- P(X=1) = 0.1 + 0.4 = 0.5
- P(Y=0) = 0.2 + 0.1 = 0.3
- P(Y=1) = 0.3 + 0.4 = 0.7

**Check independence:**
- P(X=0,Y=0) = 0.2, P(X=0)×P(Y=0) = 0.5×0.3 = 0.15 ❌
- 0.2 ≠ 0.15

**Answer: NOT independent** (first check fails)

---

### Problem 6.2: Conditional Probability

**Question:** 
- P(A) = 0.3
- P(B) = 0.4
- P(A,B) = 0.15

Calculate:
a) P(A|B)  
b) P(B|A)  
c) Are A and B independent?

**Solution:**

a) P(A|B) = P(A,B) / P(B) = 0.15 / 0.4 = **0.375**

b) P(B|A) = P(A,B) / P(A) = 0.15 / 0.3 = **0.5**

c) Independent? P(A)×P(B) = 0.3×0.4 = 0.12  
   P(A,B) = 0.15  
   0.12 ≠ 0.15, so **NOT independent**

---

### Problem 6.3: Bayes' Theorem

**Question:** 
Disease test:
- P(Disease) = 0.01 (1% of population)
- P(Positive|Disease) = 0.95 (95% sensitivity)
- P(Positive|No Disease) = 0.05 (5% false positive)

If test is positive, what's P(Disease|Positive)?

**Solution:**

**Need P(Positive) first:**
P(Positive) = P(Positive|Disease)×P(Disease) + P(Positive|No Disease)×P(No Disease)
= 0.95×0.01 + 0.05×0.99
= 0.0095 + 0.0495
= 0.059

**Bayes' Theorem:**
P(Disease|Positive) = P(Positive|Disease)×P(Disease) / P(Positive)
= (0.95 × 0.01) / 0.059
= 0.0095 / 0.059
≈ **0.161 or 16.1%**

(Surprisingly low despite positive test!)

---

## 7. Bayesian Networks

### Problem 7.1: CPT Size Calculation

**Question:** Calculate CPT sizes:

Network:
- A (no parents), Domain: {a1, a2, a3}
- B (parent: A), Domain: {b1, b2}
- C (parents: A, B), Domain: {c1, c2, c3, c4}
- D (parent: C), Domain: {d1, d2}

**Solution:**

| Node | Parents | Calculation | CPT Size |
|------|---------|-------------|----------|
| A    | none    | 3           | **3**    |
| B    | A       | 2 × 3       | **6**    |
| C    | A, B    | 4 × 3 × 2   | **24**   |
| D    | C       | 2 × 4       | **8**    |

**Total parameters:** 3 + 6 + 24 + 8 = 41

---

### Problem 7.2: Joint Probability

**Question:** Given network A → B → C with:
- P(A=1) = 0.6
- P(B=1|A=1) = 0.8
- P(C=1|B=1) = 0.7

Calculate P(A=1, B=1, C=1).

**Solution:**

P(A=1, B=1, C=1) = P(A=1) × P(B=1|A=1) × P(C=1|B=1)
= 0.6 × 0.8 × 0.7
= **0.336**

---

### Problem 7.3: D-Separation

**Question:** In network A → B → C ← D:

Are A and D independent given:
a) No evidence?  
b) Evidence on C?  
c) Evidence on B?

**Solution:**

a) **YES** - A and D are d-separated (no active path)
b) **NO** - Observing C (collider) opens the path A → B → C ← D
c) **YES** - Observing B blocks the path at B

---

## 8. Search Algorithms

### Problem 8.1: Algorithm Properties

**Question:** Fill in the table:

| Algorithm | Complete? | Optimal? | Space Complexity |
|-----------|-----------|----------|------------------|
| DFS       | ?         | ?        | ?                |
| BFS       | ?         | ?        | ?                |
| A*        | ?         | ?        | ?                |

**Solution:**

| Algorithm | Complete? | Optimal? | Space Complexity |
|-----------|-----------|----------|------------------|
| DFS       | No*       | No       | O(bm)            |
| BFS       | Yes       | Yes**    | O(b^d)           |
| A*        | Yes***    | Yes***   | O(b^d)           |

*Complete in finite spaces  
**If step costs equal  
***With admissible heuristic

---

### Problem 8.2: A* Search

**Question:** Which heuristic is admissible for 8-puzzle?

a) Number of misplaced tiles  
b) Manhattan distance  
c) Number of tiles × 100  
d) Random number

**Solution:**
- a) **Admissible** - never overestimates (each tile needs ≥1 move)
- b) **Admissible** - sum of Manhattan distances ≤ actual moves
- c) **NOT admissible** - overestimates wildly
- d) **NOT admissible** - no guarantee

**Answer: a and b**

---

## 9. Game Theory & Minimax

### Problem 9.1: Simple Minimax

**Question:** Evaluate this tree (MAX plays first):

```
        MAX
       /   \
      A     B
     / \   / \
    3   5 2   6
```

**Solution:**

**MIN layer:**
- A = min(3, 5) = 3
- B = min(2, 6) = 2

**MAX layer:**
- Root = max(3, 2) = 3

**Best move: Choose A** (value 3)

---

### Problem 9.2: Three-Level Minimax

**Question:**

```
           MAX
        /   |   \
       A    B    C
      /|\  /|\  /|\
     MIN  MIN  MIN
    /|\ /|\ /|\
    235 461 789
```

Calculate root value and best move.

**Solution:**

**MIN layer:**
- Under A: min(2,3,5) = 2
- Under B: min(4,6,1) = 1
- Under C: min(7,8,9) = 7

**MAX layer:**
- Root: max(2, 1, 7) = 7

**Best move: Choose C** (value 7)

---

### Problem 9.3: Alpha-Beta Pruning

**Question:** How many nodes can we prune in Problem 9.2 using alpha-beta?

**Solution:**

**Left-to-right evaluation:**
1. Explore A: value 2, α=2
2. Explore B:
   - First child: 4 ≥ α (continue)
   - Second child: 6 ≥ α (continue)
   - Third child: 1 < α (B value = 1)
3. Update α=2 (max so far is A)
4. Explore C:
   - First child: 7 ≥ α (C will be ≤7)
   - Since 7 > 2, must explore all

**Minimal pruning in this case** (might prune 1-2 nodes depending on order)

---

## 10. Markov Decision Processes

### Problem 10.1: Value Iteration Step

**Question:** State s with:
- V(s) = 5 (current value)
- Two actions:
  - a1: R=2, with prob 0.5 → s1 (V=10), prob 0.5 → s2 (V=4)
  - a2: R=8, with prob 1.0 → s3 (V=3)
- γ = 0.9

Calculate new V(s).

**Solution:**

**Action a1:**
Value = 2 + 0.9 × [0.5×10 + 0.5×4]
= 2 + 0.9 × [5 + 2]
= 2 + 0.9 × 7
= 2 + 6.3
= 8.3

**Action a2:**
Value = 8 + 0.9 × [1.0×3]
= 8 + 2.7
= 10.7

**New V(s) = max(8.3, 10.7) = 10.7**

**Best action: a2**

---

### Problem 10.2: Discount Factor

**Question:** Agent in state with two choices:
- A: Immediate reward 10
- B: Immediate reward 5, then guaranteed reward 10 next step

Which is better for:
a) γ = 0.9  
b) γ = 0.1

**Solution:**

**a) γ = 0.9:**
- A: 10
- B: 5 + 0.9×10 = 5 + 9 = 14
- **Choose B** (values future)

**b) γ = 0.1:**
- A: 10
- B: 5 + 0.1×10 = 5 + 1 = 6
- **Choose A** (prioritizes immediate)

---

### Problem 10.3: Policy Extraction

**Question:** Given values:
- V(s1) = 10, V(s2) = 15, V(s3) = 8

From state s, actions lead:
- a1: deterministically to s1, R=1
- a2: deterministically to s2, R=0
- a3: deterministically to s3, R=5

γ = 1.0

What's the optimal action?

**Solution:**

**Expected values:**
- a1: 1 + 1.0×10 = 11
- a2: 0 + 1.0×15 = 15
- a3: 5 + 1.0×8 = 13

**Optimal action: a2** (value 15)

---

## 11. Reinforcement Learning

### Problem 11.1: Q-Table Interpretation

**Question:** Given Q-table:

| State | Left | Right | Up |
|-------|------|-------|----|
| s1    | 5    | 12    | 8  |
| s2    | -3   | 2     | 10 |
| s3    | 7    | 7     | 4  |

For each state, what action should agent take?

**Solution:**
- **s1: Right** (Q=12, highest)
- **s2: Up** (Q=10, highest)
- **s3: Left or Right** (Q=7, tied)

---

### Problem 11.2: Q-Learning Update

**Question:** 
Current Q(s,a) = 20

Agent takes action a from state s:
- Receives reward R = 10
- Transitions to s'
- max Q(s',a') = 30

Update with α=0.2, γ=0.8

**Solution:**

Q(s,a) ← Q(s,a) + α[R + γ max Q(s',a') - Q(s,a)]
= 20 + 0.2[10 + 0.8×30 - 20]
= 20 + 0.2[10 + 24 - 20]
= 20 + 0.2[14]
= 20 + 2.8
= **22.8**

---

### Problem 11.3: Exploration vs Exploitation

**Question:** Agent uses ε-greedy with ε=0.2.

Q-values in current state: {a1: 10, a2: 5, a3: 3}

What's probability of choosing each action?

**Solution:**

**Best action:** a1 (Q=10)

**Probabilities:**
- Exploit (1-ε = 0.8): Choose best (a1)
- Explore (ε = 0.2): Choose random (1/3 each)

**Final probabilities:**
- P(a1) = 0.8 + 0.2/3 = 0.8 + 0.0667 = **0.8667**
- P(a2) = 0 + 0.2/3 = **0.0667**
- P(a3) = 0 + 0.2/3 = **0.0667**

---

### Problem 11.4: Q-Learning Convergence

**Question:** True or False:

a) Q-learning requires knowing transition probabilities  
b) Q-learning converges to optimal policy  
c) Higher learning rate always better  
d) Q-learning is model-free

**Solution:**
- a) **FALSE** - model-free, doesn't need P(s'|s,a)
- b) **TRUE** - converges under certain conditions
- c) **FALSE** - too high can cause instability
- d) **TRUE** - learns from experience, no model needed

---

## 🎯 Mixed Practice Problems

### Mixed 1: Complete Scenario

**Scenario:** Medical diagnosis AI

**Data:** 1000 patients, features {age, symptoms}, label {disease: yes/no}

**Questions:**
a) What type of learning?  
b) If you use K-NN with K=1, what's the risk?  
c) If train accuracy is 99% but test is 60%, what's wrong?  
d) How to fix it?

**Solution:**
a) **Supervised learning** (labeled data)  
b) **Overfitting** (K=1 memorizes training data)  
c) **Overfitting** (low train, high test error)  
d) **Solutions:** Increase K, use regularization, get more data, feature selection

---

### Mixed 2: Probability + Bayesian Network

**Network:** Smoking → Cancer → XRay

**Given:**
- P(Smoking) = 0.3
- P(Cancer|Smoking) = 0.1
- P(Cancer|¬Smoking) = 0.01
- P(XRay|Cancer) = 0.9
- P(XRay|¬Cancer) = 0.2

**Questions:**
a) How many CPT entries total?  
b) Calculate P(Smoking, Cancer, XRay)  
c) What's P(Cancer)?

**Solution:**

a) **CPT entries:**
- Smoking: 2 (yes/no)
- Cancer: 2×2 = 4 (for each smoking value)
- XRay: 2×2 = 4 (for each cancer value)
- **Total: 10**

b) P(S=yes, C=yes, X=yes) = P(S) × P(C|S) × P(X|C)
= 0.3 × 0.1 × 0.9 = **0.027**

c) P(Cancer) = P(C|S)P(S) + P(C|¬S)P(¬S)
= 0.1×0.3 + 0.01×0.7
= 0.03 + 0.007
= **0.037**

---

### Mixed 3: MDP + Q-Learning

**Question:** Same MDP solved two ways:

Method A: Value Iteration (knows transition model)  
Method B: Q-Learning (learns from experience)

Which statement is true?
a) A converges faster  
b) B works without knowing transitions  
c) A requires more memory  
d) B always finds better policy

**Solution:**
- a) **TRUE** - Value iteration can be more sample-efficient
- b) **TRUE** - Q-learning is model-free
- c) **Depends** - Q-learning needs Q(s,a), VI needs V(s)
- d) **FALSE** - Both converge to optimal (in limit)

---

## ✅ Self-Check Questions

Before exam, ensure you can:

- [ ] Calculate MSE from scratch
- [ ] Apply K-NN with mixed features
- [ ] Explain overfitting vs underfitting
- [ ] List what affects neural network weight updates
- [ ] Apply GAC to CSP
- [ ] Check independence from data table
- [ ] Calculate CPT sizes for Bayesian Network
- [ ] Perform minimax on game tree
- [ ] Execute Value Iteration step
- [ ] Update Q-table correctly
- [ ] Distinguish α, γ, ε and their effects
- [ ] Identify supervised vs unsupervised learning
- [ ] Extract policy from Q-values or V-values

---

## 🎓 Study Recommendations

### Week Before Exam:
- **Day 1-2:** Fundamentals + K-NN (Sections 1-2)
- **Day 3:** Regression + Neural Networks (Sections 3-4)
- **Day 4:** CSP + Probability (Sections 5-6)
- **Day 5:** Bayesian Networks + Search (Sections 7-8)
- **Day 6:** Game Theory + MDPs + RL (Sections 9-11)
- **Day 7:** Review all, do mixed problems

### Day Before:
- Quick review of formulas
- Redo 2-3 problems from each section
- Get good sleep!

### Day Of:
- Light review of formula sheet
- Stay calm and confident
- Read questions carefully

---

**You've got this! 🌟**

*Practice these problems multiple times until you can solve them without looking at solutions.*

