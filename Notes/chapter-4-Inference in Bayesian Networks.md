# Chapter 4: Inference in Bayesian Networks - Study Notes

_(Includes Key Concepts, Examples, Exercises & Solutions)_

---

## 1. Introduction to Probabilistic Inference

- **Goal:** Compute the posterior distribution of query variables given evidence variables.
- **Hidden variables:** Variables not in query or evidence.

### Task

$$P(X \mid e)$$

- **X:** Query variables  
- **e:** Observed evidence

**Example:**

$$P(\text{Burglary} \mid \text{johncalls}, \text{marycalls})$$

Query: `Burglary`  
Evidence: `JohnCalls`, `MaryCalls`

---

## 2. Normalization and Marginalization

### Normalization

$$P(X \mid e) = \alpha P(X, e)$$

where

$$\alpha = \frac{1}{\sum_x P(X=x, e)}$$

($\alpha$ ensures probabilities sum to 1.)

### Marginalization

Sum over hidden variables $Y$:

$$P(X, e) = \sum_y P(X, e, y)$$

### Combined

$$P(X \mid e) = \alpha \sum_y P(X, e, y)$$

**Example:**

Given:

$$
\begin{align*}
P(\text{cavity} \wedge \text{toothache}) &= 0.12\\
P(\neg\text{cavity} \wedge \text{toothache}) &= 0.08
\end{align*}
$$

Find $P(\text{cavity} \mid \text{toothache})$:

$$
\begin{align*}
P(\text{cavity} \mid \text{toothache}) &= \alpha (0.12, 0.08)\\
\alpha &= \frac{1}{0.12 + 0.08} = 5\\
P(\text{cavity} \mid \text{toothache}) &= 0.12 \times 5 = 0.6
\end{align*}
$$

---

## 3. Inference by Enumeration

**Steps:**

- **Normalization and Marginalization:**

  $$P(X \mid e) = \alpha \sum_y P(X, e, y)$$

- **Chain Rule:**

  $$P(X_1, ..., X_n) = \prod_i P(X_i \mid \text{Parents}(X_i))$$

- **Exploit conditional independence to simplify**

### Example (Alarm Bayesian Network)

Compute $P(\text{Burglary} \mid j, m)$:

$$P(B \mid j, m) = \alpha \sum_E \sum_A P(B)P(E)P(A \mid B, E)P(j \mid A)P(m \mid A)$$

- **Complexity:** Exponential in number of hidden variables.

---

## 4. D-Separation

Determines conditional independence in a Bayesian Network given evidence.

**Three connection types:**

- **Serial** ($A \rightarrow B \rightarrow C$): Evidence at $B$ blocks transmission.
- **Diverging** ($A \leftarrow B \rightarrow C$): Evidence at $B$ blocks transmission.
- **Converging** ($A \rightarrow B \leftarrow C$): Evidence at $B$ or its descendants enables transmission.

**Algorithm:**

1. Take ancestors of $A, B, E$.
2. Moralize (add edges between co-parents).
3. Remove evidence nodes.
4. If no path between $A$ and $B$, they are d-separated.

**Theorem:**

If $C$ d-separates $A$ from $B$, then

$$P(A \mid B, C) = P(A \mid C)$$

---

## 5. Approximate Inference by Sampling

Used when exact inference is too costly.

### Rejection Sampling

- Generate samples from BN.
- Reject samples not matching evidence.
- Estimate $P(X \mid e)$ from accepted samples.
- Inefficient if $P(e)$ is small.

### Likelihood Weighting

- Fix evidence variables to observed values.
- Sample other variables.
- Weight each sample by:

  $$\prod_{E \in e} P(E \mid \text{parents}(E))$$

- Estimate:

  $$\hat{P}(X \mid e) = \frac{\sum_{\text{samples}: X=x} w}{\sum_{\text{all}} w}$$

### Hoeffding Bound

$$P(|s - p| > \epsilon) \leq 2e^{-2n\epsilon^2}$$

To guarantee error $< \epsilon$ with probability $> 1 - \delta$:

$$n > \frac{-\ln(\delta/2)}{2\epsilon^2}$$

---

## 6. Variable Elimination (Exact Inference)

- **Goal:** Avoid repeated and irrelevant computations.
- **Factors:** Functions mapping variable assignments to numbers (like CPTs).

**Operations:**

- **Restriction:** Fix variable to value.
- **Multiplication:** Combine factors.
- **Marginalization:** Sum out a variable.

**Algorithm:**

1. Start with CPTs as factors.
2. Restrict evidence variables.
3. Eliminate hidden variables in order:
    - Multiply factors involving the variable
    - Marginalize it out.
4. Repeat until only query variables remain.

**Complexity:** Depends on elimination order.

- Polytree (singly connected): Linear time.
- General: #P-hard (worst-case exponential).

---

## 7. Exercises & Solutions

### **Exercise 1: Normalization**

**Given:**

- $P(\text{dog}) = 0.4$
- $P(\text{loudnoise} \mid \text{dog}) = 0.7$
- $P(\text{loudnoise} \mid \text{cat}) = 0.2$
- $P(\text{loudnoise} \mid \text{other}) = 0.01$
- $P(\text{cat}) = 0.4$
- $P(\text{other}) = 0.2$

**Find** $P(\text{dog} \mid \text{loudnoise})$:

**Solution:**

$$
\begin{align*}
P(d \mid ln) &= \alpha P(ln \mid d) P(d) = \alpha (0.7 \times 0.4) = \alpha \cdot 0.28 \\
P(c \mid ln) &= \alpha (0.2 \times 0.4) = \alpha \cdot 0.08 \\
P(o \mid ln) &= \alpha (0.01 \times 0.2) = \alpha \cdot 0.002 \\
\alpha &= \frac{1}{0.28 + 0.08 + 0.002} \approx 2.77 \\
P(d \mid ln) &\approx 0.28 \times 2.77 \approx 0.776
\end{align*}
$$

---

### **Exercise 2: D-Separation**

**Given BN:**

$$\text{Rain} \rightarrow \text{WetGrass} \leftarrow \text{Sprinkler}$$

**Question:** Are Rain and Sprinkler independent given WetGrass?

**Solution:**

- Connection type: **Converging** at WetGrass.
- Evidence at WetGrass **enables** transmission.
- **No**, they are *not* conditionally independent given WetGrass.

---

### **Exercise 3: Variable Elimination**

**Given CPTs:**

- $P(B) = 0.5$
- $P(A|B)$:
    - If $B=t$: $[t: 0.7, f: 0.3]$
    - If $B=f$: $[t: 0.1, f: 0.9]$
- $P(C|B)$:
    - If $B=t$: $[t: 0.7, f: 0.3]$
    - If $B=f$: $[t: 0.2, f: 0.8]$
- $P(D|A, C)$:
    - Example: If $A=t, C=t$: $[t: 0.9, f: 0.1]$, etc.

**Compute** $P(A \mid D = f)$:

**Solution (sketch):**

- **Restrict:** Set $D = f$
- **Eliminate $C$:**

  $$F_1(B, A) = \sum_c P(C|B) P(D=f|A, C)$$

- **Eliminate $B$:**

  $$F_2(A) = \sum_b P(B) P(A|B) F_1(B, A)$$

- **Normalize:**

  $$P(A \mid D=f) = \alpha F_2(A)$$
