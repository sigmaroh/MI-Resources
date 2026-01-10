# 📊 Machine Intelligence - Complete Course Summary

> **At-a-Glance** - All 13 topics organized for comprehensive review

---

## 📚 Course Structure Overview

The MI course covers 13 main topics organized into 4 major themes:

### 🎯 Theme 1: Problem Solving & Search
1. **Agents** - Rational agents, environments, agent types
2. **Search** - Uninformed & informed search algorithms
3. **CSP** - Constraint satisfaction, arc consistency
4. **Planning** - STRIPS, planning graphs, heuristics

### 🎮 Theme 2: Adversarial & Sequential Decisions
5. **Multi-Agent** - Game theory, minimax, alpha-beta pruning
6. **MDPs** - Markov decision processes, value iteration
7. **Reinforcement Learning** - Q-learning, exploration/exploitation

### 📊 Theme 3: Uncertainty & Reasoning
8. **Uncertainty** - Probability basics, independence
9. **Bayesian Networks** - Structure, CPTs, inference
10. **BN Inference** - Variable elimination, sampling

### 🤖 Theme 4: Machine Learning
11. **Supervised Learning** - Regression, classification, K-NN
12. **Neural Networks** - Backpropagation, gradient descent
13. **Learning Evaluation** - Cross-validation, metrics, overfitting
14. **Clustering** - K-means, hierarchical clustering

---

## 1️⃣ AGENTS

### Key Concepts
- **Agent:** Entity that perceives and acts in an environment
- **Rational Agent:** Maximizes expected performance measure
- **PEAS:** Performance, Environment, Actuators, Sensors

### Agent Types
| Type | Description | Example |
|------|-------------|---------|
| **Simple Reflex** | Current percept only | Thermostat |
| **Model-Based** | Maintains internal state | Robot with map |
| **Goal-Based** | Plans to achieve goals | GPS navigation |
| **Utility-Based** | Maximizes utility function | Trading bot |
| **Learning** | Improves with experience | All modern AI |

### Environment Properties
- **Observable:** Full vs Partial
- **Deterministic:** vs Stochastic
- **Episodic:** vs Sequential
- **Static:** vs Dynamic
- **Discrete:** vs Continuous
- **Single-agent:** vs Multi-agent

### Exam Tips
- ✅ Know PEAS for different agent types
- ✅ Classify environments by properties
- ✅ Match agent type to environment

---

## 2️⃣ SEARCH ALGORITHMS

### Uninformed Search

| Algorithm | Complete | Optimal | Time | Space | Notes |
|-----------|----------|---------|------|-------|-------|
| **BFS** | Yes | Yes* | O(b^d) | O(b^d) | *If uniform cost |
| **DFS** | No** | No | O(b^m) | O(bm) | **Infinite spaces |
| **UCS** | Yes | Yes | O(b^C) | O(b^C) | C = cost of solution |
| **DLS** | No | No | O(b^l) | O(bl) | l = depth limit |
| **IDS** | Yes | Yes* | O(b^d) | O(bd) | Best of BFS+DFS |

Where: b=branching factor, d=depth of solution, m=max depth

### Informed Search

**A* Algorithm:**
```
f(n) = g(n) + h(n)
```
- g(n) = cost from start to n
- h(n) = heuristic estimate from n to goal
- f(n) = estimated total cost

**Properties:**
- **Complete:** Yes (with admissible h)
- **Optimal:** Yes (with admissible + consistent h)

**Heuristic Properties:**
- **Admissible:** h(n) ≤ h*(n) (never overestimates)
- **Consistent:** h(n) ≤ cost(n,n') + h(n') (triangle inequality)

### Common Heuristics

**8-Puzzle:**
- Misplaced tiles: admissible
- Manhattan distance: admissible, more informed

**Navigation:**
- Straight-line distance: admissible if no obstacles

### Exam Tips
- ✅ Know time/space complexity
- ✅ Recognize admissible heuristics
- ✅ Apply A* search step-by-step

---

## 3️⃣ CONSTRAINT SATISFACTION PROBLEMS

### Components
```
CSP = (Variables, Domains, Constraints)
```

### Arc Consistency (AC-3 / GAC)

**Algorithm:**
1. Add all arcs to queue
2. For each arc (X, Y):
   - Remove values from D_X with no support in D_Y
   - If D_X changed, add all arcs (Z, X) to queue
3. Repeat until queue empty

**Node Consistency:** Each variable satisfies unary constraints

**Arc Consistency:** For arc (X,Y), every value in D_X has support in D_Y

**Path Consistency:** Stronger than arc consistency

### Variable Elimination

**Process:**
1. Create factor (table) for each constraint
2. Select variable to eliminate
3. Join all factors containing that variable
4. Project out (sum over) that variable
5. Repeat

**Correct statement:** 
> "We construct a table for each constraint, and at each step remove a variable by combining all its constraints"

### Example Workflow

**Problem:**
```
Variables: {A, B, C} ∈ {1,2,3}
Constraints: A < B, B = C
```

**After GAC:**
```
A ∈ {1, 2}  (can't be 3, no valid B)
B ∈ {2, 3}  (must be > A and = C)
C ∈ {2, 3}  (must equal B)
```

### Exam Tips
- ✅ Apply GAC systematically
- ✅ Check all arcs, iterate until stable
- ✅ Remember: factor per CONSTRAINT, eliminate VARIABLE

---

## 4️⃣ UNCERTAINTY & PROBABILITY

### Fundamental Rules

**Joint Probability:**
```
P(A, B) = P(A|B) × P(B) = P(B|A) × P(A)
```

**Chain Rule:**
```
P(A, B, C) = P(A) × P(B|A) × P(C|A,B)
```

**Marginalization:**
```
P(X) = Σ_y P(X, Y=y)
```

**Bayes' Theorem:**
```
P(A|B) = [P(B|A) × P(A)] / P(B)
```

### Independence

**Definition:** X and Y are independent if:
```
P(X, Y) = P(X) × P(Y)  [for ALL values]
```

**Equivalent conditions:**
- P(X|Y) = P(X)
- P(Y|X) = P(Y)
- Knowing Y doesn't change belief about X

### Conditional Independence

**X ⊥ Y | Z** means:
```
P(X, Y | Z) = P(X | Z) × P(Y | Z)
```

Given Z, X and Y are independent.

### Example: Medical Test

**Given:**
- P(Disease) = 0.01
- P(+|Disease) = 0.95 (sensitivity)
- P(+|Healthy) = 0.05 (false positive)

**Find:** P(Disease|+)

**Solution:**
```
P(+) = 0.95×0.01 + 0.05×0.99 = 0.059
P(Disease|+) = (0.95×0.01) / 0.059 = 0.161
```

Only 16% despite positive test!

### Exam Tips
- ✅ Check independence for ALL value combinations
- ✅ Use Bayes' when seeing P(A|B) but given P(B|A)
- ✅ Marginalize by summing over unwanted variables

---

## 5️⃣ BAYESIAN NETWORKS

### Structure

**Bayesian Network = (DAG, CPTs)**
- **DAG:** Directed Acyclic Graph of variables
- **CPTs:** Conditional Probability Tables

**Each node stores:** P(Node | Parents)

### CPT Size Calculation

```
CPT_size = |Domain(X)| × ∏_{parent} |Domain(parent)|
```

**Example:**
```
Node B with parents A (3 values), C (4 values)
Domain(B) = 2 values
CPT size = 2 × 3 × 4 = 24 entries
```

### Joint Probability Factorization

```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

**Example:** A → B → C
```
P(A, B, C) = P(A) × P(B|A) × P(C|B)
```

### Conditional Independence in BNs

**D-Separation Rules:**

1. **Chain:** A → B → C
   - A ⊥ C | B (B blocks)

2. **Common Cause:** A ← B → C  
   - A ⊥ C | B (B blocks)

3. **Common Effect (V-structure):** A → C ← B
   - A ⊥ B (not blocked)
   - A ⊥̸ B | C (C opens path!)

### Inference Types

| Query Type | Question | Example |
|------------|----------|---------|
| **Prior** | P(X) | P(Cancer) |
| **Posterior** | P(X\|e) | P(Cancer\|Symptom) |
| **MPE** | argmax P(X\|e) | Most likely diagnosis |

### Variable Elimination

**Algorithm:**
1. Write factors for each CPT
2. Choose elimination order
3. For each variable to eliminate:
   - Join factors containing it
   - Sum out that variable
4. Normalize result

**Complexity:** O(exp(treewidth))

### Exam Tips
- ✅ CPT size = node domain × product of parent domains
- ✅ Joint = product of all CPTs
- ✅ Remember V-structures open paths when conditioned

---

## 6️⃣ GAME THEORY & MINIMAX

### Minimax Algorithm

**Assumption:** Both players play optimally

**Rules:**
- **MAX player:** Choose move with highest value
- **MIN player:** Choose move with lowest value

**Pseudocode:**
```python
def minimax(node, depth, isMax):
    if terminal or depth == 0:
        return evaluate(node)
    
    if isMax:
        return max(minimax(child, depth-1, False) 
                   for child in children)
    else:
        return min(minimax(child, depth-1, True)
                   for child in children)
```

### Alpha-Beta Pruning

**Optimization:** Prune branches that can't affect decision

**Variables:**
- α = best value for MAX so far (lower bound)
- β = best value for MIN so far (upper bound)

**Pruning condition:** α ≥ β

**Benefits:**
- Same result as minimax
- Fewer nodes explored
- Best case: O(b^(d/2)) vs O(b^d)
- Worst case: still O(b^d)

**Move ordering matters:** Best first gives most pruning

### Expectimax

**For stochastic games (chance nodes):**
- MAX nodes: take maximum
- CHANCE nodes: take expected value
- MIN nodes: take minimum (if opponent exists)

### Game Properties

| Property | Description |
|----------|-------------|
| **Zero-sum** | One player's gain = other's loss |
| **Perfect information** | All info visible (chess) |
| **Imperfect information** | Hidden info (poker) |
| **Deterministic** | No randomness |
| **Stochastic** | Includes chance (backgammon) |

### Exam Tips
- ✅ Work bottom-up in minimax
- ✅ MAX maximizes, MIN minimizes
- ✅ Depth-limited uses heuristics at cutoff
- ✅ Alpha-beta gives same result as minimax

---

## 7️⃣ MARKOV DECISION PROCESSES

### Components

```
MDP = (S, A, T, R, γ)
```

- **S:** Set of states
- **A:** Set of actions
- **T:** Transition function P(s'|s,a)
- **R:** Reward function R(s,a,s')
- **γ:** Discount factor [0, 1]

### Bellman Equation

**Value of state:**
```
V*(s) = max_a [R(s,a) + γ Σ_{s'} P(s'|s,a) V*(s')]
```

**Optimal policy:**
```
π*(s) = argmax_a [R(s,a) + γ Σ_{s'} P(s'|s,a) V*(s')]
```

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

**Usually faster** than value iteration in practice.

### Discount Factor Effects

| γ Value | Effect | Use Case |
|---------|--------|----------|
| **γ → 0** | Myopic (immediate rewards) | Short-term optimization |
| **γ → 1** | Far-sighted (future rewards) | Long-term planning |
| **γ = 0** | Only immediate reward | One-step problems |
| **γ = 1** | All rewards equal | Infinite horizon |

**Important:** γ affects reward valuation, NOT exploration!

### Exam Tips
- ✅ Bellman equation is the core
- ✅ Higher γ = values future more
- ✅ Policy = action selection, Value = expected reward
- ✅ Show calculations step by step

---

## 8️⃣ REINFORCEMENT LEARNING

### Q-Learning

**Q-value:** Expected cumulative reward from (s,a) following optimal policy

**Update Rule:**
```
Q(s,a) ← Q(s,a) + α[R + γ max_{a'} Q(s',a') - Q(s,a)]
```

**Components:**
- **α:** Learning rate [0,1]
- **R:** Immediate reward
- **γ:** Discount factor [0,1]
- **s':** Next state
- **max Q(s',a'):** Best future value

### Key Properties

**Model-free:** Doesn't need P(s'|s,a) or R(s,a)

**Off-policy:** Learns optimal policy while following exploratory policy

**Convergence:** Converges to Q* under conditions:
- All (s,a) pairs visited infinitely often
- Learning rate satisfies Σα=∞, Σα²<∞

### Policy from Q-values

**Greedy policy:**
```
π(s) = argmax_a Q(s,a)
```

**State value:**
```
V(s) = max_a Q(s,a)
```

### Exploration vs Exploitation

**ε-Greedy Policy:**
```
With probability ε: random action (explore)
With probability 1-ε: best action (exploit)
```

**Strategies:**
- **High ε early:** Explore to find good strategies
- **Low ε later:** Exploit known good strategies
- **ε-decay:** Gradually reduce ε over time

### SARSA

**On-policy alternative to Q-learning:**
```
Q(s,a) ← Q(s,a) + α[R + γ Q(s',a') - Q(s,a)]
```

**Difference:** Uses actual next action a', not max

### Parameters Summary

| Parameter | Symbol | Controls | Typical Value |
|-----------|--------|----------|---------------|
| **Learning rate** | α | Update magnitude | 0.01 - 0.1 |
| **Discount** | γ | Future weight | 0.9 - 0.99 |
| **Exploration** | ε | Random action prob | 0.1 - 0.3 |

**Important distinctions:**
- **α:** How much to update (magnitude)
- **γ:** How much to value future (NOT exploration!)
- **ε:** How much to explore (random vs greedy)

### Q-Learning Update Example

**Given:**
- Q(s,a) = 10
- Take action a, get reward R=5
- Land in s' where max Q(s',a')=8
- α=0.1, γ=0.9

**Update:**
```
Q(s,a) ← 10 + 0.1[5 + 0.9×8 - 10]
       = 10 + 0.1[5 + 7.2 - 10]
       = 10 + 0.1[2.2]
       = 10 + 0.22
       = 10.22
```

**Key:** Only Q(s,a) changes! All other entries unchanged.

### Exam Tips
- ✅ Only update Q(s,a) for action taken
- ✅ ε controls exploration, γ controls future valuation
- ✅ Show all steps in update calculation
- ✅ Know difference between Q-learning and SARSA

---

## 9️⃣ SUPERVISED LEARNING

### Learning Types

| Type | Training Data | Goal | Examples |
|------|---------------|------|----------|
| **Supervised** | Labeled | Learn mapping | Classification, Regression |
| **Unsupervised** | Unlabeled | Find structure | Clustering, PCA |
| **Reinforcement** | Rewards | Maximize reward | Game playing, Robotics |

### Regression vs Classification

**Regression:**
- **Output:** Continuous value
- **Examples:** House price, temperature
- **Metrics:** MSE, MAE, R²

**Classification:**
- **Output:** Discrete category
- **Examples:** Spam/not spam, digit recognition
- **Metrics:** Accuracy, Precision, Recall, F1

### K-Nearest Neighbors

**Algorithm:**
1. Calculate distance to all training points
2. Select K nearest neighbors
3. Classification: majority vote
4. Regression: average value

**Distance Metrics:**

**Euclidean:**
```
d = √[Σᵢ (xᵢ - yᵢ)²]
```

**Manhattan:**
```
d = Σᵢ |xᵢ - yᵢ|
```

**Mixed (categorical + numerical):**
```
d = CatDist(f₁) + |f₂_new - f₂_i|  (Manhattan)
d = √[CatDist(f₁)² + (f₂_new - f₂_i)²]  (Euclidean)
```

**K Selection:**
- **Small K (K=1):** Complex, overfits, sensitive to noise
- **Large K:** Smooth boundaries, less overfitting
- **Rule of thumb:** K = √n or use cross-validation

### Linear Regression

**Model:**
```
ŷ = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ
```

**Loss Function (MSE):**
```
MSE = (1/n) Σᵢ (yᵢ - ŷᵢ)²
```

**Training:** Minimize MSE using gradient descent or closed-form solution

**Closed-form solution:**
```
w = (XᵀX)⁻¹Xᵀy
```

### Evaluation Metrics

**Classification:**

| Metric | Formula | When to Use |
|--------|---------|-------------|
| **Accuracy** | (TP+TN)/Total | Balanced classes |
| **Precision** | TP/(TP+FP) | False positives costly |
| **Recall** | TP/(TP+FN) | False negatives costly |
| **F1-Score** | 2PR/(P+R) | Balance P and R |

**Regression:**
- **MSE:** Mean squared error
- **RMSE:** √MSE (same units as target)
- **MAE:** Mean absolute error
- **R²:** Coefficient of determination (0-1)

### Overfitting Solutions

1. **More data:** Best solution if possible
2. **Regularization:** L1 (Lasso), L2 (Ridge)
3. **Feature selection:** Remove irrelevant features
4. **Cross-validation:** Tune hyperparameters
5. **Ensemble methods:** Combine multiple models
6. **Early stopping:** Stop before overfitting (neural nets)

### Exam Tips
- ✅ K-NN: smaller K → more overfitting
- ✅ MSE calculation: predict, error, square, sum, divide
- ✅ Overfitting = low train error, high test error
- ✅ Choice of metric depends on application

---

## 🔟 NEURAL NETWORKS

### Architecture

**Basic Structure:**
```
Input Layer → Hidden Layers → Output Layer
```

**Neuron:**
```
output = activation(Σᵢ wᵢxᵢ + bias)
```

### Activation Functions

| Function | Formula | Range | Use |
|----------|---------|-------|-----|
| **Sigmoid** | 1/(1+e⁻ˣ) | (0,1) | Output probabilities |
| **Tanh** | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | (-1,1) | Hidden layers |
| **ReLU** | max(0,x) | [0,∞) | Hidden layers (most common) |
| **Softmax** | eˣⁱ/Σeˣʲ | (0,1), sum=1 | Multi-class output |

### Backpropagation

**Purpose:** Calculate gradients for weight updates

**Weight Update Rule:**
```
wᵢⱼ ← wᵢⱼ - α × ∂Loss/∂wᵢⱼ
```

**What affects weight update from A to B:**
- ✅ Error term at neuron B
- ✅ Input to B through that link
- ✅ Activation function (affects gradient)
- ❌ NOT error at neuron A
- ❌ NOT inputs through other links

### Gradient Descent

**Batch Gradient Descent:**
```
For each epoch:
    Calculate gradient over ALL training data
    Update weights
```

**Stochastic Gradient Descent (SGD):**
```
For each training example:
    Calculate gradient for that example
    Update weights
```

**Mini-batch Gradient Descent:**
```
For each mini-batch:
    Calculate gradient over batch
    Update weights
```

### Learning Rate Effects

| α Value | Effect | Problem |
|---------|--------|---------|
| **Too small** | Slow convergence | Many iterations needed |
| **Optimal** | Fast, stable convergence | Best performance |
| **Too large** | Oscillation, divergence | Overshoots minimum |

**Learning rate schedules:**
- Constant: α fixed
- Step decay: Reduce α every N epochs
- Exponential decay: α = α₀ × e^(-kt)
- Adaptive: Adam, RMSprop, Adagrad

### Regularization

**L2 Regularization (Weight Decay):**
```
Loss = MSE + λ Σᵢ wᵢ²
```

**L1 Regularization (Lasso):**
```
Loss = MSE + λ Σᵢ |wᵢ|
```

**Dropout:**
- Randomly drop neurons during training
- Prevents co-adaptation
- Typical rate: 0.2-0.5

### Training Process

1. **Initialize** weights (small random values)
2. **Forward pass:** Calculate outputs
3. **Calculate loss:** Compare to targets
4. **Backward pass:** Compute gradients
5. **Update weights:** w ← w - α∇Loss
6. **Repeat** until convergence

### Common Issues

| Problem | Symptom | Solution |
|---------|---------|----------|
| **Vanishing gradients** | Learning stops | ReLU, skip connections |
| **Exploding gradients** | NaN values | Gradient clipping |
| **Overfitting** | High test error | Regularization, dropout |
| **Slow convergence** | Many epochs | Adjust α, better initialization |

### Exam Tips
- ✅ Weight update depends on error at OUTPUT neuron
- ✅ Learning rate affects magnitude, not number of updates
- ✅ Gradient descent works for neural nets and linear regression
- ✅ ReLU most common for hidden layers

---

## 1️⃣1️⃣ LEARNING EVALUATION & CLUSTERING

### Cross-Validation

**K-Fold Cross-Validation:**
1. Split data into K folds
2. For each fold:
   - Train on K-1 folds
   - Test on remaining fold
3. Average results

**Stratified K-Fold:** Preserves class distribution

**Leave-One-Out (LOOCV):** K = n (all data points)

### Confusion Matrix

```
              Predicted
            Positive  Negative
Actual Pos    TP        FN
       Neg    FP        TN
```

**From this calculate:**
- Accuracy = (TP+TN) / Total
- Precision = TP / (TP+FP)
- Recall = TP / (TP+FN)
- F1 = 2 × P×R / (P+R)

### K-Means Clustering

**Algorithm:**
1. Initialize K centroids randomly
2. Repeat until convergence:
   - Assign each point to nearest centroid
   - Update centroids to mean of assigned points
3. Stop when centroids stop moving

**Distance:** Usually Euclidean

**Choosing K:**
- Elbow method (plot within-cluster variance)
- Silhouette score
- Domain knowledge

**Limitations:**
- Assumes spherical clusters
- Sensitive to initialization
- Must specify K

### Hierarchical Clustering

**Agglomerative (bottom-up):**
1. Start with each point as cluster
2. Repeatedly merge closest clusters
3. Stop at desired number or threshold

**Linkage methods:**
- **Single:** Minimum distance between clusters
- **Complete:** Maximum distance
- **Average:** Average distance
- **Ward:** Minimize variance

### Exam Tips
- ✅ Cross-validation for hyperparameter tuning
- ✅ Test set NEVER used for training
- ✅ K-means iterates: assign, update, repeat
- ✅ Choose metric based on problem (accuracy vs F1)

---

## 🔑 Quick Reference Tables

### Algorithm Complexity Comparison

| Algorithm | Time (train) | Time (test) | Space |
|-----------|--------------|-------------|-------|
| **K-NN** | O(1) | O(nd) | O(nd) |
| **Linear Regression** | O(nd²+d³) | O(d) | O(d) |
| **Neural Network** | O(iterations×n×edges) | O(edges) | O(edges) |
| **Decision Tree** | O(n log n × d) | O(depth) | O(nodes) |

### When to Use What

| Problem | Algorithm | Why |
|---------|-----------|-----|
| Small data, simple | K-NN | No training, interpretable |
| Linear relationship | Linear Regression | Fast, interpretable |
| Complex patterns | Neural Network | Most flexible |
| Need interpretability | Decision Tree | Clear rules |
| Unlabeled data | K-means | Find groups |
| Sequential decisions | Q-Learning | Learn from interaction |

### Common Mistakes & Corrections

| ❌ Wrong | ✅ Right |
|----------|----------|
| Learning rate determines # of updates | Learning rate determines magnitude |
| Smaller K in K-NN reduces overfitting | Larger K reduces overfitting |
| Overfitting = high train & test error | Overfitting = low train, high test |
| Unsupervised = test data unlabeled | Unsupervised = training data unlabeled |
| Update all Q-values in Q-learning | Update only Q(s,a) for action taken |
| γ affects exploration | γ affects future valuation, ε affects exploration |
| Independence: check one combination | Independence: check ALL combinations |

---

## 📝 Formula Sheet

### Probability
```
P(A|B) = P(A,B) / P(B)
P(A|B) = P(B|A)P(A) / P(B)  [Bayes]
P(X) = Σy P(X,Y=y)          [Marginalization]
P(X,Y) = P(X)P(Y)           [Independence]
```

### Machine Learning
```
MSE = (1/n) Σ(y - ŷ)²
ŷ = w₀ + Σᵢ wᵢxᵢ
Accuracy = (TP + TN) / Total
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1 = 2PR / (P + R)
```

### Reinforcement Learning
```
V(s) = max_a [R(s,a) + γ Σ P(s'|s,a)V(s')]  [Bellman]
Q(s,a) ← Q(s,a) + α[R + γ max Q(s',a') - Q(s,a)]  [Q-Learning]
π(s) = argmax_a Q(s,a)  [Policy]
V(s) = max_a Q(s,a)     [State Value]
```

### Bayesian Networks
```
CPT_size = |D(X)| × ∏parent |D(parent)|
P(X₁,...,Xₙ) = ∏ᵢ P(Xᵢ | Parents(Xᵢ))
```

---

## ✅ Pre-Exam Checklist

### Concepts to Know Cold
- [ ] Supervised vs Unsupervised vs Reinforcement Learning
- [ ] Overfitting definition (low train, high test error)
- [ ] K-NN algorithm (distance, select K, vote)
- [ ] MSE calculation steps
- [ ] Neural network weight update factors
- [ ] Learning rate effects (small=slow, large=overshoot)
- [ ] GAC algorithm for CSP
- [ ] Independence test (P(X,Y) = P(X)P(Y) for ALL)
- [ ] CPT size = node domain × parent domains
- [ ] Minimax (MAX max, MIN min)
- [ ] Bellman equation for MDPs
- [ ] Q-learning update (only Q(s,a) taken!)
- [ ] α vs γ vs ε distinctions

### Calculations to Practice
- [ ] MSE from predictions
- [ ] K-NN with mixed features
- [ ] Probability (independence, Bayes)
- [ ] CPT sizes for Bayesian Network
- [ ] Minimax tree evaluation
- [ ] Value iteration step
- [ ] Q-table update

### Common Traps to Avoid
- [ ] Read "NOT" in questions carefully
- [ ] Check independence for ALL combinations
- [ ] Remember: only update Q(s,a) taken
- [ ] CPT includes node's own domain
- [ ] γ affects future, NOT exploration
- [ ] Smaller K overfits in K-NN

---

## 🎯 Final Study Strategy

### 3 Days Before
- Review all formula sheets
- Do 5-10 practice problems per topic
- Focus on weak areas

### 2 Days Before
- Complete full practice exams
- Review mistakes thoroughly
- Make final formula summary

### 1 Day Before
- Light review of key concepts
- Skim through this summary
- Get good sleep!

### Day Of
- Quick formula review
- Stay calm
- Read questions twice
- Show all work

---

**You're ready for this! Trust your preparation and good luck! 🌟**

