# Chapter 5: Supervised Learning & Decision Trees – Study Notes

*(Includes Key Concepts, Examples, Exercises & Solutions)*

---

## 1. Introduction to Machine Learning

**Deduction vs. Induction:**
- **Deduction:** Derive conclusions from known facts (certain).
- **Induction:** Generalize from examples (probable).

**Goal of ML:** Automatically improve performance from experience.

---

## 2. Types of Learning

| Type         | Description                                   | Examples                           |
|--------------|-----------------------------------------------|------------------------------------|
| Supervised   | Learn from labeled examples (input-output pairs)| Regression, Classification         |
| Unsupervised | Find patterns in unlabeled data                | Clustering, Dimensionality reduction|
| Reinforcement| Learn actions to maximize cumulative reward    | MDPs, Q-learning                   |

---

## 3. Supervised Learning

- **Labeled dataset:** Table with:
    - **Features (predictors):** Input attributes.
    - **Target (label):** Output to predict.

**Tasks:**
- **Classification:** Target is discrete (e.g., spam/not spam)
- **Regression:** Target is continuous (e.g., temperature)

**Example Dataset (Spam filter):**

| SubAllCap | TrustSend | InvRet | ... | Spam |
|-----------|-----------|--------|-----|------|
| y         | n         | n      | ... | y    |
| n         | n         | n      | ... | n    |
| ...       | ...       | ...    | ... | ...  |

- **Training set:** Used to learn model.
- **Test set:** Used to evaluate model.

---

## 4. Ingredients of a Learning Method

- **Hypothesis Space:** Set of possible models.
- **Parameters:** Chosen by algorithm.
- **Hyperparameters:** Chosen by user.
- **Evaluation Measure:** Error function.
- **Search/Optimization:** Find best model.

---

## 5. Regression

- **Predicts continuous target.**

**Linear Regression:**

\[
\hat{y} = w_0 + \sum_{i=1}^n w_i x_i
\]

**Error Functions:**

- **Sum Squared Error (SSE):**
    \[
    SSE = \sum_e (Y(e) - \hat{Y}(e))^2
    \]
- **Sum Absolute Error (SAE):**
    \[
    SAE = \sum_e |Y(e) - \hat{Y}(e)|
    \]
- **0/1 Error:** Count of mispredictions.
- **Worst-case Error:** Max absolute error.

---

## 6. Decision Trees

**Structure:**
- Internal nodes: Test on attribute.
- Branches: Outcome of test.
- Leaves: Class label (or probability).

- **Hypothesis Space:** All possible trees over features.

For \( n \) binary features: \( 2^{2^n} \) possible trees.

**Example: Book Recommendation**

| Example | Author  | Thread    | Length | WhereRead | UserAction |
|---------|---------|-----------|--------|-----------|------------|
| e1      | known   | new       | long   | home      | skips      |
| e2      | unknown | new       | short  | work      | reads      |
| ...     | ...     | ...       | ...    | ...       | ...        |

- **Goal:** Predict UserAction for new examples.

---

## 7. Learning Decision Trees – ID3 Algorithm

Top-down recursive splitting:

```plaintext
DecisionTreeLearner(X, Y, E):
  if stopping_criterion:
    return leaf with majority class in E
  else:
    choose best feature Xi (max information gain)
    for each value v of Xi:
      Ev = {e in E: Xi(e) = v}
      child = DecisionTreeLearner(X \ {Xi}, Y, Ev)
    return node(Xi, children)
```

---

## 8. Choosing the Best Feature – Information Gain

**Entropy** (impurity measure):

For binary class with probabilities \( (p, 1-p) \):
\[
H(p) = -p \log_2 p - (1-p)\log_2(1-p)
\]

**Expected entropy after split on feature \( X \):**

\[
H(Y|X) = \sum_v \frac{|E_v|}{|E|} \cdot H(Y|X=v)
\]

**Information Gain:**

\[
IG(X) = H(Y) - H(Y|X)
\]

Choose feature with highest IG.

---

## 9. Example Calculation – Book Recommendation

- **Root entropy:**  
  Class distribution: (skips=9, reads=9) → \( H=1 \).

| Feature   | Values     | Counts (skips, reads) | Entropy per branch | Weighted entropy                |
|-----------|------------|----------------------|--------------------|---------------------------------|
| Length    | long       | (7, 0) → H=0         | 7/18·0 + 11/18·H(2/11,9/11) ≈ 0.582 |
|           | short      | (2, 9) → H≈0.684     |                                 |
| Thread    | new        | (6, 2) → H≈0.811     | 8/18·0.811 + 10/18·H(3/10,7/10) ≈ 0.85 |
|           | follow-up  | (3, 7) → H≈0.881     |                                 |
| Author    | known      | (6, 6) → H=1         | 12/18·1 + 6/18·1 = 1            |
|           | unknown    | (3, 3) → H=1         |                                 |
| WhereRead | home       | (4, 4) → H=1         | 8/18·1 + 10/18·1 = 1            |
|           | work       | (5, 5) → H=1         |                                 |

- \( IG(\text{Length}) = 1 - 0.582 = 0.418 \) (highest → choose Length first).

---

## 10. Handling Many-valued & Continuous Attributes

- Many-valued attributes (e.g., Date) can artificially increase IG.

**Solution: Use Gain Ratio:**

\[
\text{GainRatio}(X) = \frac{IG(X)}{\text{SplitInfo}(X)}
\]

where

\[
\text{SplitInfo}(X) = -\sum_v \frac{|E_v|}{|E|} \log_2 \frac{|E_v|}{|E|}
\]

- **Continuous attributes:** Discretize by testing thresholds (e.g., midpoint between adjacent values), pick threshold with highest IG.

---

## 11. Stopping Criteria

- All examples in node belong to same class.
- No features left.
- Information gain below threshold.
- Tree depth limit reached.

---

## 12. Exercises & Solutions

### Exercise 1: Entropy Calculation

**Given class distribution:** (yes=5, no=3)

**Calculate entropy:**

\[
p_{yes} = 5/8 = 0.625, \quad p_{no} = 3/8 = 0.375
\]
\[
H = -0.625\log_2 0.625 - 0.375\log_2 0.375 \approx 0.954
\]

---

### Exercise 2: Information Gain

**Dataset:**

| Outlook   | Play? |
|-----------|-------|
| Sunny     | No    |
| Sunny     | No    |
| Overcast  | Yes   |
| Rainy     | Yes   |
| Rainy     | Yes   |

**Calculate:** \( IG(\text{Outlook}) \)

**Solution:**

- Root entropy: (Yes=3, No=2) → \( H = 0.971 \)
- Outlook splits:
    - Sunny: (Yes=0, No=2) → H=0
    - Overcast: (Yes=1, No=0) → H=0
    - Rainy: (Yes=2, No=0) → H=0

\[
H(Y|\text{Outlook}) = (2/5)\cdot0 + (1/5)\cdot0 + (2/5)\cdot0 = 0
\]
\[
IG = 0.971 - 0 = 0.971
\]

---

### Exercise 3: Continuous Attribute Discretization

**Temperatures:** [40, 48, 60, 72, 80, 90]  
**Labels:** [Yes, Yes, No, No, No, Yes]  
**Find best binary split.**

**Solution:**

1. Sort: (40Y, 48Y, 60N, 72N, 80N, 90Y)
2. Candidate thresholds: midpoints between differing labels:
    - \( (48+60)/2 = 54 \)
    - \( (80+90)/2 = 85 \)
3. Test threshold = 54:
    - \( \leq 54: \) (40Y,48Y) → (Yes=2, No=0) \( H=0 \)
    - \( >54: \) (60N,72N,80N,90Y) → (Yes=1, No=3) \( H=0.811 \)
    - Weighted \( H = (2/6)\cdot 0 + (4/6)\cdot 0.811 \approx 0.541 \)
    - \( IG = H_{root} - 0.541 \)
4. Test threshold = 85 similarly, pick higher IG.

---