# Chapter 5: Supervised Learning & Decision Trees – Study Notes

*(Key Concepts, Quick Formula Previews, and Exercises with Solutions)*

---

## 1. Introduction to Machine Learning

- **Deduction:** Drawing certain conclusions from known facts.
- **Induction:** Making generalizations from examples—uncertain but backed by data.

**Main goal:** Learn from experience/data to improve performance automatically.

---

## 2. Types of Machine Learning

- **Supervised Learning:** Learn using labeled examples (input-output pairs)  
  *Examples: regression, classification*
- **Unsupervised Learning:** Find structure in unlabeled data  
  *Examples: clustering, dimensionality reduction*
- **Reinforcement Learning:** Learn to act so as to maximize long-term reward  
  *Examples: MDPs, Q-learning*

---

## 3. Supervised Learning Overview

A typical **labeled dataset** includes:
- **Features** (predictors): Input variables
- **Target** (label): Output to be predicted

**Tasks:**
- **Classification:** Target is discrete (e.g., spam vs not spam)
- **Regression:** Target is continuous (e.g., temperature)

**Example dataset:**

| SubAllCap | TrustSend | InvRet | ... | Spam |
|-----------|-----------|--------|-----|------|
| y         | n         | n      | ... | y    |
| n         | n         | n      | ... | n    |
| ...       | ...       | ...    | ... | ...  |

- **Training Set:** Used to learn the model
- **Test Set:** Used to evaluate its performance

---

## 4. Ingredients of a Learning Method

- **Hypothesis Space:** All possible models (e.g., all trees, all lines)
- **Parameters:** Model-specific values learned from data
- **Hyperparameters:** User-set values, not learned automatically
- **Evaluation Measure:** Score function (e.g., squared error, accuracy)
- **Search/Optimization:** The process or algorithm for finding the best hypothesis

---

## 5. Regression

Used to predict a **continuous** quantity.

### Key Preview

$$
\textbf{Linear Regression:}\\
\hat{y} = w_0 + w_1x_1 + w_2x_2 + \ldots + w_nx_n
$$

**Error Functions:**

$$
\begin{align*}
\text{Sum of Squared Errors (SSE):}\qquad & SSE = \sum_e (Y(e) - \hat{Y}(e))^2 \\
\text{Sum of Absolute Errors (SAE):}\qquad & SAE = \sum_e |Y(e) - \hat{Y}(e)| \\
\text{0/1 Error:} \qquad & \text{(Count of mispredictions)} \\
\text{Worst-case Error:} \qquad & \max\,|Y - \hat{Y}| \\
\end{align*}
$$

---

## 6. Decision Trees

**Structure:**
- **Internal nodes:** Feature tests (e.g., "color=red?")
- **Branches:** Outcomes of those tests
- **Leaves:** Class label or prediction value

**Hypothesis space:** Every possible tree given available features. For $n$ binary features, possible unique trees = $2^{2^n}$.

**Preview Example Table:**

| Ex. | Author  | Thread    | Length | WhereRead | UserAction |
|-----|---------|-----------|--------|-----------|------------|
| e1  | known   | new       | long   | home      | skips      |
| e2  | unknown | new       | short  | work      | reads      |
| ... | ...     | ...       | ...    | ...       | ...        |

> **Goal:** Predict `UserAction` for a new book/email

---

## 7. Learning Decision Trees – ID3 Algorithm

**Process:** Top-down, recursively select the best feature for splitting.

**Preview (Pseudocode):**

```
DecisionTreeLearner(X, Y, E):
    if stopping_criterion(E): return majority_class(E)
    pick feature Xi with highest IG
    for v in values(Xi):
        Ev = subset of E with Xi = v
        child[v] = DecisionTreeLearner(X \ {Xi}, Y, Ev)
    return tree node (Xi, children)
```

---

## 8. Choosing the Best Feature – Information Gain

### Formula Preview

**Entropy** (for binary classes with $p$ and $1-p$):

$$
H(p) = -p \log_2 p - (1-p) \log_2 (1-p)
$$

**Expected entropy after split:**

$$
H(Y|X) = \sum_v \frac{|E_v|}{|E|} H(Y|X=v)
$$

**Information Gain:**

$$
IG(X) = H(Y) - H(Y|X)
$$

> *Always pick feature with largest $IG$ at each split!*

---

## 9. Example Calculation – Book Recommendation

Suppose at the root:
- $(skips=9, reads=9) \implies H=1$

| Feature   | Values     | (skips, reads) | Branch Entropy | Weighted Total                |
|-----------|------------|----------------|----------------|-------------------------------|
| Length    | long       | (7, 0)         | H=0            |                               |
|           | short      | (2, 9)         | H ≈ 0.684      | $7/18 \cdot 0 + 11/18 \cdot 0.684 \approx 0.418$ |
| Thread    | new        | (6, 2)         | H ≈ 0.811      |                               |
|           | follow-up  | (3, 7)         | H ≈ 0.881      | $8/18 \cdot 0.811 + 10/18 \cdot 0.881 \approx 0.85$ |
| Author    | known      | (6, 6)         | H=1            |                               |
|           | unknown    | (3, 3)         | H=1            | $12/18 \cdot 1 + 6/18 \cdot 1 = 1$        |
| WhereRead | home       | (4, 4)         | H=1            |                               |
|           | work       | (5, 5)         | H=1            | $8/18 \cdot 1 + 10/18 \cdot 1 = 1$        |

Thus,  

$$
\text{Information Gain for Length} = 1 - 0.582 = 0.418 \;\; (\text{highest!})
$$

So the root splits on **Length**.

---

## 10. Handling Many-valued & Continuous Attributes

- Features with many possible values (like Date) can distort IG.

**Gain Ratio:**

$$
\text{Gain Ratio}(X) = \frac{IG(X)}{\text{SplitInfo}(X)}
$$

$$
\text{SplitInfo}(X) = -\sum_v \frac{|E_v|}{|E|} \log_2 \frac{|E_v|}{|E|}
$$

- **Continuous features:** Try splitting at "between values with different labels" and pick the threshold with the highest IG.

---

## 11. Stopping Criteria

- All examples in node are same class
- No features left
- Information gain below threshold
- Tree depth limit reached

---

## 12. Exercises & Solutions

---

### Exercise 1: Entropy Calculation

**Given:** (yes=5, no=3)  
So $p_{yes} = 0.625$, $p_{no} = 0.375$

Preview:

$$
H = -0.625 \log_2 0.625 - 0.375 \log_2 0.375 \approx 0.954
$$

---

### Exercise 2: Information Gain

**Toy data:**

| Outlook   | Play? |
|-----------|-------|
| Sunny     | No    |
| Sunny     | No    |
| Overcast  | Yes   |
| Rainy     | Yes   |
| Rainy     | Yes   |

$$
\begin{align*}
\text{Root:}\;\; & (\text{Yes}=3, \text{No}=2): \\
  & H = -\frac{3}{5}\log_2\frac{3}{5} - \frac{2}{5}\log_2\frac{2}{5} \approx 0.971 \\
\text{Split Entropies:} \quad & H=0 \text{ for each branch (Sunny/Overcast/Rainy)} \\
\text{Weighted Entropy after split: } & 0 \\
IG = 0.971 - 0 = 0.971
\end{align*}
$$

---

### Exercise 3: Continuous Attribute Discretization

**Data:**  
Temps: 40, 48, 60, 72, 80, 90  
Labels: Yes, Yes, No, No, No, Yes

- Sort: 40Y, 48Y, 60N, 72N, 80N, 90Y
- Try splits: (48+60)/2 = 54 and (80+90)/2 = 85

Threshold $\leq 54$:

$$
\begin{align*}
&(40Y, 48Y):\;\;\; \text{Yes}=2, \text{No}=0 \implies H=0 \\
&(60N, 72N, 80N, 90Y):\; \text{Yes}=1, \text{No}=3 \\
&H = -0.25\log_2 0.25 - 0.75\log_2 0.75 \approx 0.811 \\
\text{Weighted entropy: } & \frac{2}{6} \times 0 + \frac{4}{6} \times 0.811 \approx 0.541 \\
\end{align*}
$$

Compute $IG =$ (root entropy) $-$ (weighted entropy). Try all thresholds, pick largest IG.

---
