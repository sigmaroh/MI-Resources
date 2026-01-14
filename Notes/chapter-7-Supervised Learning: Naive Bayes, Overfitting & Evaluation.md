# Supervised Learning: Naive Bayes, Overfitting & Evaluation - Exam Study Notes

## Table of Contents

1. [Naive Bayes Classifier](#1-naive-bayes-classifier)
2. [Case-Based Reasoning & k-NN](#2-case-based-reasoning--k-nn)
3. [Overfitting & Generalization](#3-overfitting--generalization)
4. [Model Evaluation Metrics](#4-model-evaluation-metrics)
5. [Exercises with Solutions](#5-exercises-with-solutions)
6. [Exam Tips](#6-exam-tips)

---

## 1. Naive Bayes Classifier

### Core Concept

- **Bayesian approach** to classification
- Uses probability theory to predict class labels.
- **Based on Bayes' Theorem:**

  $$
  P(\text{Class}|\text{Features}) = \frac{P(\text{Features}|\text{Class}) \times P(\text{Class})}{P(\text{Features})}
  $$

#### The "Naive" Assumption

- All input features are conditionally independent given the class.

  $$
  P(A_1, A_2, ..., A_n|C) = P(A_1|C) \times P(A_2|C) \times ... \times P(A_n|C)
  $$

#### Training Phase

- Estimate prior probabilities: $P(C)$ for each class.
- Estimate conditional probabilities: $P(A_i|C)$ for each feature given a class.
- Use empirical frequencies from training data.

**Example Calculation:**
```python
P(reads) = #reads / total_examples = 9/18 = 0.5
P(known|reads) = #(known ∧ reads) / #reads = 6/9 ≈ 0.667
```

#### Prediction Phase

For new instance $x = [a_1, a_2, ..., a_n]$:

$$
P(C|a_1,...,a_n) \propto P(C) \times \prod P(a_i|C)
$$

Choose class with highest probability.

**Example:**
```
P(skips|unknown,followUp,short,home) 
  ∝ P(skips) × P(unknown|skips) × P(followUp|skips) 
    × P(short|skips) × P(home|skips)
```

#### Handling Zero Probabilities

- **Problem:** If $P(a_i|C)=0$, whole product becomes $0$.
- **Solution:** Laplace smoothing / Pseudo-counts.

  $$
  P(A=a|C=c) = \frac{\text{count}(a,c) + m \times p}{\text{count}(c) + m}
  $$
  - $m$ = virtual sample size (weight of prior)
  - $p$ = prior estimate (often uniform: $1/k$ for $k$ values)

**Example:**
```
P(known|reads) = (2 + 0.5×4) / (3 + 4) = 4/7 ≈ 0.571
```

#### Limitations

- Cannot learn XOR (like linear classifiers)
- Redundant features cause double-counting
- Independence assumption rarely holds in practice
- **Paradox**: Despite unrealistic assumptions, Naive Bayes often works well!
  - Needs correct **decision boundaries**, not exact probabilities

---

## 2. Case-Based Reasoning & k-NN

### Core Idea

- **Lazy learning:** No explicit model built during training
- Store all training examples
- At prediction time: Find similar examples and use their labels

### Distance Metrics

#### Numeric Features
- **Euclidean:** $d(x,x') = \sqrt{\sum (x_i - x'_i)^2}$
- **Manhattan:** $d(x,x') = \sum|x_i - x'_i|$

#### Discrete Features
- **Zero-One:** $d(x_i,x_j) = 0$ (same), $1$ (different)
- **Custom matrix:** Define distances between values

#### Mixed Features
- **Weighted sum:** $d(x,x') = \sum w_i \times d_i(x_i, x'_i)$

### k-Nearest Neighbors (k-NN) Algorithm

**Algorithm:**
1. For new instance $x$:
   - Find $k$ training examples closest to $x$
   - Predict most frequent class among these $k$ neighbors

**Choosing $k$:**
- $k=1:$ Highly sensitive to noise (overfit)
- Large $k:$ Smoother boundaries (may underfit)
- **Rule of thumb:** $k = \sqrt{n}$ where $n = \text{training examples}$

**Example: 3-NN Classification**

Training: `[(1,2):A, (2,1):A, (3,3):B, (4,2):B]`  
New point: `(2.5, 2)`  
```
Distances:
  d((2.5,2), (1,2)) = 1.5
  d((2.5,2), (2,1)) = 1.12
  d((2.5,2), (3,3)) = 1.12
  d((2.5,2), (4,2)) = 1.5

3 nearest: (2,1):A, (3,3):B, (1,2):A
Prediction: A (2 votes vs 1)
```

---

## 3. Overfitting & Generalization

### Key Definitions

- **Overfitting:** Model fits training data too closely (captures noise)
- **Generalization:** Model performs well on unseen data

**Formal Definition:**  
Hypothesis $h$ overfits if $\exists h'$ such that:
- $h$ has lower error than $h'$ on training data
- $h'$ has lower error than $h$ on entire distribution

### The Big ML Assumption

> **Training data and future data come from the same distribution.**  
> Training examples must be representative.

- Violations cause poor generalization (e.g., train on children, test on adults)

### Overfitting Examples

- **Decision Trees:** Deep trees memorize training examples  
  *Solution:* Pruning, limit depth, min samples per leaf
- **Neural Networks:** Too many neurons/layers capture noise  
  *Solution:* Early stopping, regularization, dropout
- **k-NN:** $k=1$ creates complex boundaries around outliers  
  *Solution:* Increase $k$
- **Naive Bayes:** Zero probabilities from small samples  
  *Solution:* Laplace smoothing

### The Bias-Variance Tradeoff

$$
\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
$$

- **Bias:** Error from overly simple assumptions
- **Variance:** Error from sensitivity to training data noise
- **Overfitting:** Low bias, high variance
- **Underfitting:** High bias, low variance

### Avoiding Overfitting

1. **Simpler Models**  
   - Limit hypothesis space (e.g., tree depth, $k$ value)
   - Regularization: Add penalty for complexity  
     $$
     \text{Loss} = \text{Training Error} + \lambda \times \text{Complexity}
     $$
2. **Data Splitting**

```
        ┌─────────────┐
        │  All Data   │
        └─────┬───────┘
              │ Split
     ┌────────┴────────┐
     ▼                 ▼
 ┌─────────┐      ┌─────────┐
 │ Training│      │  Test   │
 │(60-80%) │      │(20-40%) │
 └────┬────┘      └─────────┘
      │
 ┌────┴────┐
 │Validation│
 │ (from    │
 │  train)  │
 └─────────┘
```

3. **Cross-Validation**  
   - k-fold CV: Split into $k$ equal folds  
     For $i=1..k$:
     - Train on $k$–1 folds
     - Validate on fold $i$
     - Average results

   - **Benefits:**  
     - All data used for training/validation  
     - Less variance in performance estimates

4. **Early Stopping**  
   - Monitor validation error during training  
   - Stop when validation error starts increasing

---

## 4. Model Evaluation Metrics

### Confusion Matrix

|          | Predicted No | Predicted Yes |
|----------|--------------|--------------|
| Actual No| TN           | FP           |
| Actual Yes| FN          | TP           |

### Key Metrics

- **Accuracy:**  
  $$
  \text{Accuracy} = \frac{TP + TN}{\text{Total}}
  $$
  *Misleading for imbalanced datasets*

- **Precision (Positive Predictive Value):**  
  $$
  \text{Precision} = \frac{TP}{TP + FP}
  $$
  When model predicts "yes", how often is it correct?  
  $P(\text{Actual=Yes} | \text{Predicted=Yes})$

- **Recall (Sensitivity, True Positive Rate):**  
  $$
  \text{Recall} = \frac{TP}{TP + FN}
  $$
  Of actual "yes", how many caught?  
  $P(\text{Predicted=Yes} | \text{Actual=Yes})$

- **Specificity (True Negative Rate):**  
  $$
  \text{Specificity} = \frac{TN}{TN + FP}
  $$
  Of actual "no", how many correctly rejected?

- **F1-Score (Harmonic Mean):**  
  $$
  \text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  $$
  Balances precision and recall. Range: [0, 1] (1 = perfect)

#### Example Calculation

**Given:**

|          | Predicted No | Predicted Yes |
|----------|--------------|--------------|
| Actual No| 50           | 10           |
| Actual Yes| 5           | 100          |
|          | 55           | 110 (165 total) |

- $\text{Accuracy} = (50+100)/165 = 150/165 \approx 90.9\%$
- $\text{Precision} = 100/110 \approx 90.9\%$
- $\text{Recall} = 100/105 \approx 95.2\%$
- $\text{Specificity} = 50/60 \approx 83.3\%$
- $\text{F1} = 2 \times (0.909 \times 0.952) / (0.909+0.952) \approx 93.0\%$

#### Multi-Class Evaluation

For each class $C_i$:
- $TP_i$: Correctly predicted as $C_i$
- $FP_i$: Others predicted as $C_i$
- $FN_i$: $C_i$ predicted as other classes

- **Macro-average:** Average metrics across classes
- **Micro-average:** Aggregate all predictions then compute

---

## 5. Exercises with Solutions

### Exercise 1: Naive Bayes Probability Calculation

**Problem:**  
Train Naive Bayes on:

| Day | Outlook   | Temp | Play |
|-----|-----------|------|------|
| 1   | Sunny     | Hot  | No   |
| 2   | Sunny     | Mild | Yes  |
| 3   | Overcast  | Hot  | Yes  |
| 4   | Rainy     | Mild | Yes  |

Predict: Outlook=Sunny, Temp=Mild

**Solution:**

- **Priors:**  
  $P(\text{Yes}) = 3/4 = 0.75$  
  $P(\text{No}) = 1/4 = 0.25$

- **Conditionals:**  
  $P(\text{Sunny}|\text{Yes}) = 1/3 \approx 0.333$  
  $P(\text{Mild}|\text{Yes}) = 2/3 \approx 0.667$  
  $P(\text{Sunny}|\text{No}) = 1/1 = 1.0$  
  $P(\text{Mild}|\text{No}) = 0/1 = 0.0$

- **Apply Laplace smoothing** (m=1, p=0.5):  
  $P(\text{Sunny}|\text{Yes}) = (1+0.5)/(3+1) = 0.375$  
  $P(\text{Mild}|\text{Yes}) = (2+0.5)/(3+1) = 0.625$  
  $P(\text{Sunny}|\text{No}) = (1+0.5)/(1+1) = 0.75$  
  $P(\text{Mild}|\text{No}) = (0+0.5)/(1+1) = 0.25$

- **Predictions:**  
  $P(\text{Yes}|\text{Sunny,Mild}) \propto 0.75 \times 0.375 \times 0.625 = 0.1758$  
  $P(\text{No}|\text{Sunny,Mild}) \propto 0.25 \times 0.75 \times 0.25 = 0.0469$

  **Normalize:**  
  $P(\text{Yes}) = 0.1758/(0.1758+0.0469) \approx 0.789$  
  $P(\text{No}) = 0.0469/(0.1758+0.0469) \approx 0.211$

- **Prediction:** Yes (higher probability)

---

### Exercise 2: k-NN Classification

**Problem:** Points: A(1,1), B(2,2), C(3,3) are Class X; D(5,5), E(6,6) are Class Y.  
Use Euclidean distance, $k=3$. Classify point (4,4).

**Solution:**
- $d(A) = \sqrt{(4-1)^2 + (4-1)^2} = \sqrt{18} \approx 4.24$
- $d(B) = \sqrt{(4-2)^2 + (4-2)^2} = \sqrt{8} \approx 2.83$
- $d(C) = \sqrt{(4-3)^2 + (4-3)^2} = \sqrt{2} \approx 1.41$
- $d(D) = \sqrt{(4-5)^2 + (4-5)^2} = \sqrt{2} \approx 1.41$
- $d(E) = \sqrt{(4-6)^2 + (4-6)^2} = \sqrt{8} \approx 2.83$

3 nearest: C (1.41), D (1.41), B (2.83)  
Classes: C=X, D=Y, B=X  
Votes: X=2, Y=1  
**Prediction:** Class X

---

### Exercise 3: Confusion Matrix Analysis

**Problem:** Given:

|         | Predicted Cat | Predicted Dog | Predicted Bird |
|---------|---------------|--------------|---------------|
| Actual Cat |  30        | 5            | 5             |
| Actual Dog |  4         | 35           | 1             |
| Actual Bird| 2          | 3            | 45            |

Calculate precision, recall, F1 for "Cat" class.

**Solution:**

- $TP = 30$ (Cat predicted as Cat)
- $FP = 4 + 2 = 6$ (Dog, Bird predicted as Cat)
- $FN = 5 + 5 = 10$ (Cat predicted as Dog or Bird)

- **Precision:** $30/(30+6) = 30/36 \approx 0.833$
- **Recall:** $30/(30+10) = 30/40 = 0.75$
- **F1:** $2\times(0.833\times0.75)/(0.833+0.75) = 2\times0.625/1.583 \approx 0.789$

---

### Exercise 4: Overfitting Diagnosis

**Problem:**  
Model has:
- Training accuracy: 99.8%
- Validation accuracy: 72.3%
- Test accuracy: 71.9%

**Diagnose the issue and suggest solutions.**

**Solution:**

**Diagnosis:** Severe overfitting  
Evidence:
- Very high training accuracy (≈100%)
- Much lower validation/test accuracy
- Gap: $99.8\% - 72.3\% = 27.5\%$

**Possible causes:**
1. Model too complex (e.g., deep tree, many neurons)
2. Training on noise/outliers
3. Insufficient training data

**Solutions:**
- Simplify model (reduce depth, fewer neurons)
- Increase training data
- Add regularization
- Use early stopping
- Apply data augmentation

---

### Exercise 5: Data Splitting Strategy

**Problem:**  
You have 10,000 labeled examples. Design a strategy for:
- Hyperparameter tuning  
- Final model evaluation  
- Avoiding overfitting

**Solution:**

**Strategy:** 3-way split with cross-validation

**Step 1:** Initial split  
- Training+Validation: 8,000 (80%)  
- Test: 2,000 (20%) — Lock away for final evaluation

**Step 2:** Hyperparameter tuning on 8,000  
**Option A:** Hold-out validation  
- Train: 6,400 (80% of 8,000)
- Validation: 1,600 (20% of 8,000)
- Tune hyperparameters on validation set

**Option B:** k-fold cross-validation (**better**)  
- Use 5-fold CV on 8,000 examples
- Each fold: 6,400 train, 1,600 validation
- Average results across folds

**Step 3:** Final training  
- Use best hyperparameters
- Train on all 8,000
- Evaluate on locked test set (2,000)

**Step 4:** Report final performance  
- Test accuracy: performance on 2,000 test examples
- **Never tune based on test performance!**

---

## 6. Exam Tips

### Key Concepts to Memorize

- Naive Bayes independence assumption
- Laplace smoothing formula
- Confusion matrix components (TP, FP, TN, FN)
- Precision, recall, specificity, F1 formulas
- Overfitting definition and symptoms
- k-fold cross-validation procedure

### Common Calculations

- Naive Bayes probabilities (with/without smoothing)
- k-NN distances and classification
- Evaluation metrics from confusion matrix
- Data splitting percentages

### Important Distinctions

- **Training vs Validation vs Test sets**: Different purposes
- **Precision vs Recall**: Trade-off (high precision → low recall, and vice versa)
- **Overfitting vs Underfitting**: High variance vs high bias
- **Naive Bayes vs k-NN**: Eager vs lazy learning

### Exam Question Types

- Calculation questions: Compute probabilities, distances, metrics
- Diagnosis questions: Identify overfitting from performance metrics
- Design questions: Propose evaluation strategy
- Comparison questions: Contrast different algorithms
- Interpretation questions: Explain what metrics mean in context

### Problem-Solving Framework

**For evaluation problems:**
1. Construct confusion matrix if needed
2. Identify TP, FP, TN, FN
3. Apply correct formula
4. Interpret result in context

**For overfitting problems:**
1. Compare training vs validation performance
2. Identify gap (>5–10% suggests overfitting)
3. Propose appropriate remedies

**For algorithm selection:**
1. Consider data type (numeric/categorical)
2. Consider dataset size
3. Consider need for interpretability
4. Consider computational constraints

### Common Pitfalls

- Naive Bayes zero probabilities: Forgetting Laplace smoothing
- k-NN distance metric: Using wrong formula
- Data leakage: Using test data for tuning
- Imbalanced data: Relying only on accuracy
- Overfitting remedies: Applying wrong solution

### Memory Aids

**Confusion Matrix:**
```
        Predicted
        -     +
Actual - TN   FP
       + FN   TP
```

**Metrics:**
- Precision: "How precise are our positive predictions?"
- Recall: "How many positives did we recall/catch?"
- Specificity: "How specific are our negative predictions?"

**Overfitting Signs:**
- Training accuracy ≫ Validation accuracy
- Complex model + Small dataset
- Performance suddenly drops on new data

