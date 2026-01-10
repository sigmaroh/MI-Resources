# 📋 MI Quick Reference Guide - Exam Cheat Sheet

> **Last-minute revision** - All formulas and key concepts at a glance

---

## 🔢 Essential Formulas

### Machine Learning

**Mean Squared Error (MSE)**
```
MSE = (1/n) × Σ(yᵢ - ŷᵢ)²
```

**Linear Regression**
```
ŷ = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ
```

**Euclidean Distance**
```
d = √[(x₁-x₂)² + (y₁-y₂)²]
```

**Manhattan Distance**
```
d = |x₁-x₂| + |y₁-y₂|
```

---

### Probability

**Independence**
```
P(X,Y) = P(X) × P(Y)  [for all values]
```

**Conditional Probability**
```
P(A|B) = P(A,B) / P(B)
```

**Bayes' Theorem**
```
P(A|B) = [P(B|A) × P(A)] / P(B)
```

**Marginalization**
```
P(X) = Σy P(X, Y=y)
```

**Chain Rule**
```
P(A,B,C) = P(A) × P(B|A) × P(C|A,B)
```

---

### Reinforcement Learning

**Bellman Equation (Value Iteration)**
```
V(s) = max_a [R(s,a) + γ Σs' P(s'|s,a)V(s')]
```

**Q-Learning Update**
```
Q(s,a) ← Q(s,a) + α[R + γ max_a' Q(s',a') - Q(s,a)]
```

**Policy Extraction**
```
π(s) = argmax_a Q(s,a)
```

**State Value from Q-values**
```
V(s) = max_a Q(s,a)
```

---

## ⚡ Quick Facts

### Learning Types

| Type | Labels? | Goal |
|------|---------|------|
| **Supervised** | ✅ Yes | Learn input→output mapping |
| **Unsupervised** | ❌ No | Find patterns/structure |
| **Reinforcement** | Rewards | Maximize cumulative reward |

---

### Overfitting vs Underfitting

| | Train Error | Test Error |
|---|-------------|------------|
| **Overfitting** | LOW ⬇️ | HIGH ⬆️ |
| **Underfitting** | HIGH ⬆️ | HIGH ⬆️ |
| **Good Fit** | LOW ⬇️ | LOW ⬇️ |

---

### K-NN

- **Smaller K** → More overfitting, complex boundaries
- **Larger K** → Less overfitting, smoother boundaries
- **K=1** → Most prone to overfitting

**Process:**
1. Calculate distances
2. Find K nearest neighbors
3. Majority vote (classification) or average (regression)

---

### Neural Networks

**Weight Update Depends On:**
- ✅ Error term of OUTPUT neuron
- ✅ Input through THAT link
- ✅ Activation function type
- ❌ NOT error of INPUT neuron
- ❌ NOT overall network error directly

**Learning Rate Effects:**
- **Too small α** → Slow convergence ⏱️
- **Too large α** → Overshooting 🎯❌
- **Just right α** → Fast, stable convergence ✅

**Which use Gradient Descent?**
- ✅ Linear Regression
- ✅ Neural Networks (backpropagation)
- ❌ Decision Trees
- ❌ K-NN
- ❌ K-means (standard version)

---

### CSP (Constraint Satisfaction)

**GAC Algorithm:**
1. Create arc pairs from constraints
2. For each arc (X,Y), check if every value in X has support in Y
3. Remove unsupported values
4. Repeat until no changes

**Variable Elimination:**
- Create table per CONSTRAINT
- Remove VARIABLE by combining its constraints

---

### Bayesian Networks

**CPT Size Formula:**
```
Size = |Domain(X)| × ∏(parent) |Domain(parent)|
```

**Example:**
- Node B with parents Q(5 values), S(3 values), C(4 values)
- Domain(B) = 2
- CPT size = 2 × 5 × 3 × 4 = **120 entries**

**Joint Probability:**
```
P(vars) = ∏(each node) P(node | parents)
```

---

### Game Trees (Minimax)

**Rules:**
- **MAX level**: Choose MAXIMUM child value
- **MIN level**: Choose MINIMUM child value

**Alpha-Beta Pruning:**
- α = best for MAX so far
- β = best for MIN so far
- **Prune when**: α ≥ β

---

### MDP Components

1. **States (S)** - All possible situations
2. **Actions (A)** - What agent can do
3. **Transitions P(s'|s,a)** - State change probabilities
4. **Rewards R(s,a)** - Immediate payoff
5. **Discount γ ∈ [0,1]** - Future reward weight

**Value Iteration:**
- Start with V₀(s) for all states
- Update: V_{k+1}(s) = max_a [R(s,a) + γ Σ P(s'|s,a)V_k(s')]
- Repeat until convergence

---

### Reinforcement Learning

**Q-Learning Key Points:**
- Only update **Q(s,a)** for action actually taken
- All other Q-values remain unchanged
- Best action: argmax_a Q(s,a)
- Expected reward: max_a Q(s,a)

**Exploration vs Exploitation:**
- **ε (epsilon)** controls exploration/exploitation
- **Higher ε** → more exploration (random actions)
- **Lower ε** → more exploitation (best known actions)

**Discount Factor:**
- **Higher γ** → values future rewards more
- **Lower γ** → values immediate rewards more
- **γ NOT related to exploration!**

---

## 🎯 Common Exam Mistakes

### ❌ WRONG → ✅ RIGHT

**Learning:**
- ❌ Learning rate affects NUMBER of updates
- ✅ Learning rate affects MAGNITUDE of updates

**K-NN:**
- ❌ Smaller K reduces overfitting
- ✅ Larger K reduces overfitting (K=1 overfits most)

**Overfitting:**
- ❌ High train + high test error
- ✅ Low train + high test error

**Unsupervised:**
- ❌ Training labeled, testing unlabeled
- ✅ Training data has NO labels for target

**Q-Learning:**
- ❌ Update all Q-values after action
- ✅ Update ONLY Q(s,a) for action taken

**Independence:**
- ❌ Check just one combination
- ✅ Must verify P(X,Y) = P(X)P(Y) for ALL combinations

**Discount Factor:**
- ❌ Affects exploration/exploitation
- ✅ Affects future reward valuation (NOT exploration)

**CPT Calculation:**
- ❌ Multiply only parent domains
- ✅ Multiply (node domain) × (all parent domains)

---

## 📊 Decision Flow Charts

### Choosing ML Algorithm

```
Labeled data?
├─ YES → Supervised Learning
│  ├─ Continuous output? → Regression (Linear, Neural Net)
│  └─ Discrete output? → Classification (K-NN, Decision Tree, Neural Net)
└─ NO → Unsupervised Learning
   ├─ Find groups? → Clustering (K-means)
   └─ Reduce dimensions? → PCA, etc.
```

### MDP vs Q-Learning

```
Know transition model P(s'|s,a)?
├─ YES → Use MDP (Value Iteration, Policy Iteration)
└─ NO → Use Q-Learning (model-free)
```

---

## 🔑 Key Values to Remember

### Typical Hyperparameters

| Parameter | Symbol | Typical Range | Effect |
|-----------|--------|---------------|--------|
| Learning rate | α | 0.001 - 0.1 | Update step size |
| Discount factor | γ | 0.8 - 0.99 | Future reward weight |
| Epsilon | ε | 0.1 - 0.3 | Exploration rate |
| K (in K-NN) | K | 3, 5, 7, 9 | # neighbors |

---

## 💡 Problem-Solving Strategies

### K-NN Problems
1. ✓ Calculate ALL distances first
2. ✓ Sort by distance
3. ✓ Take K smallest
4. ✓ Count votes per class
5. ✓ Majority wins

### MSE Problems
1. ✓ Calculate predictions: ŷ = w₀ + w₁x₁ + ...
2. ✓ Find errors: e = y - ŷ
3. ✓ Square each error: e²
4. ✓ Sum all squared errors
5. ✓ Divide by n

### GAC Problems
1. ✓ List all constraints
2. ✓ Create arc pairs
3. ✓ Check each variable's values for support
4. ✓ Remove unsupported values
5. ✓ Repeat until stable

### Independence Check
1. ✓ Calculate joint probabilities P(X,Y)
2. ✓ Calculate marginals P(X), P(Y)
3. ✓ For EACH combination: check if P(X,Y) = P(X)×P(Y)
4. ✓ ALL must match for independence

### CPT Size
1. ✓ Identify parents of node
2. ✓ Count domain size of node
3. ✓ Count domain size of each parent
4. ✓ Multiply: node_domain × ∏(parent_domains)

### Minimax
1. ✓ Start from leaves (bottom)
2. ✓ Work up level by level
3. ✓ MIN level: take minimum of children
4. ✓ MAX level: take maximum of children
5. ✓ Root value = best achievable outcome

### Value Iteration
1. ✓ For each state, try each action
2. ✓ For each action, calculate: R + γ Σ P(s'|s,a)V(s')
3. ✓ Take maximum over actions
4. ✓ Update V(s)

### Q-Learning Update
1. ✓ Identify (s, a, R, s') from transition
2. ✓ Find max_a' Q(s', a')
3. ✓ Calculate: α[R + γ max Q(s',a') - Q(s,a)]
4. ✓ Add to Q(s,a)
5. ✓ Only Q(s,a) changes!

---

## 🧮 Calculation Examples

### Example 1: MSE
```
Data: [(x=1,y=3), (x=2,y=5), (x=3,y=7)]
Model: ŷ = 2x + 0

Predictions: [2, 4, 6]
Errors: [1, 1, 1]
Squared: [1, 1, 1]
MSE = 3/3 = 1.0
```

### Example 2: Independence
```
P(A=1, B=1) = 0.15
P(A=1) = 0.30
P(B=1) = 0.50

Check: 0.30 × 0.50 = 0.15 ✓
(Need to check all combinations)
```

### Example 3: Q-Learning Update
```
Current: Q(s1,a2) = 10
Take action a2 from s1
Get reward R = 5
End in s2 where Q(s2,a1)=8, Q(s2,a2)=12

α=0.1, γ=0.9

Update = 0.1[5 + 0.9×12 - 10]
       = 0.1[5 + 10.8 - 10]
       = 0.1[5.8]
       = 0.58

New Q(s1,a2) = 10 + 0.58 = 10.58
```

### Example 4: CPT Size
```
Node: B
Domain: {yes, no} → 2 values
Parents: A (3 values), C (4 values)

CPT Size = 2 × 3 × 4 = 24 entries
```

---

## 📚 Topic Coverage Checklist

### Before Exam:
- [ ] Can calculate MSE from scratch
- [ ] Know K-NN with mixed features (categorical + numerical)
- [ ] Understand what causes overfitting
- [ ] Can apply GAC algorithm
- [ ] Can check independence from data
- [ ] Can calculate CPT sizes
- [ ] Can do minimax on game tree
- [ ] Can perform Value Iteration step
- [ ] Can update Q-table
- [ ] Know difference between α, γ, ε
- [ ] Know which ML methods use gradient descent
- [ ] Understand supervised vs unsupervised
- [ ] Can extract policy from Q-values

---

## ⏰ Time Management

**Typical Exam (90 minutes, 10 questions):**
- Quick read-through: **5 min**
- Per question: **8 min average**
- Review: **5 min**

**Strategy:**
1. Answer easy questions first (build confidence)
2. Skip and mark hard questions (come back later)
3. Show work for partial credit
4. Check arithmetic twice
5. Verify independence for ALL cases
6. Double-check which Q-values update

---

## 🎓 Last-Minute Tips

### The Night Before:
- ✅ Review formulas
- ✅ Practice 2-3 problems per topic
- ✅ Get good sleep (seriously!)
- ✅ Prepare materials (calculator, pens)

### During Exam:
- ✅ Read ALL instructions
- ✅ Budget time per question
- ✅ Show your work
- ✅ Check units (probabilities sum to 1)
- ✅ Verify arithmetic
- ✅ Answer every question (no blank answers)

### Common Traps:
- ⚠️ NOT questions (read carefully!)
- ⚠️ "Select all that apply" vs "Select one"
- ⚠️ Independence requires checking ALL combinations
- ⚠️ Q-learning only updates ONE entry
- ⚠️ CPT size includes node's own domain
- ⚠️ Minimax: MAX takes max, MIN takes min (don't mix up!)

---

**Print this page and keep it handy for quick reference!**

**Good luck! 🍀**
