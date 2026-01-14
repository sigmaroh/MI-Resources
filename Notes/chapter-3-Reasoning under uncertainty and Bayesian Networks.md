# Chapter 3: Reasoning under uncertainty and Bayesian Networks — Study Notes

*Includes Key Concepts, Examples, Exercises & Solutions*

---

## 1. Introduction

Reasoning under uncertainty deals with making decisions in situations of incomplete knowledge.

**Logic alone is insufficient for reasoning under uncertainty because:**
- It cannot weigh alternatives.
- It cannot handle incomplete or probabilistic knowledge.

---

## 2. Probability Basics

- **Probability:** Degree of belief given current knowledge.
- **Random Variable (RV):** Variable that defines possible worlds.
- **Distribution:** For a random variable $A$, $P(A)$ maps each value $a$ of $A$ to a probability.
- **Joint Distribution:** $P(A_1, \ldots, A_k)$ assigns probabilities to tuples of RV values.
- **Atomic Event:** Complete assignment to all RVs.

**Example:**
- $P(\text{Headache}) = \langle \text{True}: 0.9, \text{False}: 0.1 \rangle$
- $P(\text{Weather}) = \langle \text{sunny}: 0.7, \text{rain}: 0.2, \text{cloudy}: 0.08, \text{snow}: 0.02 \rangle$

---

## 3. Conditional Probability

The conditional probability of $p$ given $e$ is:

$$
P(p \mid e) = \frac{P(p \wedge e)}{P(e)} \quad \text{(for } P(e) \neq 0\text{)}
$$

Posterior probability of $p$ given evidence $e$.

**Interpretation:** Updates belief when new evidence is obtained.

**Example:**  
Given:
- $P(\text{toothache}) = 0.2$
- $P(\text{cavity}) = 0.2$
- $P(\text{toothache} \wedge \text{cavity}) = 0.12$

Then:

$$
P(\text{cavity} \mid \text{toothache}) = \frac{P(\text{toothache} \wedge \text{cavity})}{P(\text{toothache})} = \frac{0.12}{0.2} = 0.6
$$

---

## 4. Bayes’ Rule

$$
P(a \mid b) = \frac{P(b \mid a) \cdot P(a)}{P(b)}
$$

Bayes’ Rule is used to invert conditional probabilities.

- _Causal probabilities_ (e.g., $P(\text{symptom} \mid \text{cause})$) are often easier to assess than _diagnostic probabilities_ (e.g., $P(\text{cause} \mid \text{symptom})$).

**Example:**  
Given:
- $P(\text{toothache} \mid \text{cavity}) = 0.6$
- $P(\text{cavity}) = 0.2$
- $P(\text{toothache}) = 0.2$

Then,

$$
P(\text{cavity} \mid \text{toothache}) = \frac{P(\text{toothache} \mid \text{cavity}) \cdot P(\text{cavity})}{P(\text{toothache})} = \frac{0.6 \times 0.2}{0.2} = 0.6
$$

---

## 5. Independence & Conditional Independence

- **Independence:**  
  $P(a \wedge b) = P(a) \cdot P(b)$

- **Conditional Independence:**  
  $$
  P(Z_1, Z_2 \mid Z) = P(Z_1 \mid Z) \cdot P(Z_2 \mid Z)
  $$

**Example:**
Hair length and height are not independent, but they are conditionally independent given sex.

---

## 6. Bayesian Networks (BNs)

A **Bayesian Network** is a directed acyclic graph (DAG) where:
- **Nodes:** Random Variables (RVs)
- **Edges:** Conditional dependencies
- **Each node:** Conditional Probability Table (CPT), $P(X_i \mid \operatorname{Parents}(X_i))$

**Example BN: Alarm System**  
Random Variables: Burglary, Earthquake, Alarm, JohnCalls, MaryCalls

**CPTs encode:**
- $P(\text{Alarm} \mid \text{Burglary}, \text{Earthquake})$
- $P(\text{JohnCalls} \mid \text{Alarm})$
- $P(\text{MaryCalls} \mid \text{Alarm})$

**Joint distribution factorization:**

$$
P(B, E, A, J, M) = P(B) \cdot P(E) \cdot P(A \mid B, E) \cdot P(J \mid A) \cdot P(M \mid A)
$$

---

## 7. Constructing BNs

Guidelines:
- Order variables: causes before effects.
- Choose minimal parent set for each node to satisfy conditional independence.
- Network size depends on variable ordering.

**Size of BN:**

$$
\text{size(BN)} = \sum_i |D_i| \cdot \prod_{X_j \in \text{Parents}(X_i)} |D_j|
$$

This is much smaller than the full joint distribution if each node has few parents.

---

## 8. Inference in BNs

To recover the full joint from a BN, use the chain rule:

$$
P(X_1, \ldots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))
$$

Compute probabilities of queries given evidence.

---

## 9. Exercises & Solutions

---

### Exercise 1: Conditional Probability

**Given:**
- $P(A) = 0.3$
- $P(B) = 0.4$
- $P(A \wedge B) = 0.1$

Find $P(A \mid B)$ and $P(B \mid A)$.

**Solution:**

$$
P(A \mid B) = \frac{P(A \wedge B)}{P(B)} = \frac{0.1}{0.4} = 0.25
$$

$$
P(B \mid A) = \frac{P(A \wedge B)}{P(A)} = \frac{0.1}{0.3} \approx 0.333
$$

---

### Exercise 2: Bayes’ Rule

**Problem:**  
A disease affects 1% of the population. A test is 95% accurate for diseased people and 90% accurate for healthy people.  
If a person tests positive, what is the probability they actually have the disease?

**Solution:**

Let $D$ = disease, $T^+$ = positive test.

Given:
- $P(D) = 0.01$
- $P(T^+ \mid D) = 0.95$
- $P(T^+ \mid \neg D) = 0.1$

Compute $P(D \mid T^+)$.

First, calculate $P(T^+)$:

$$
P(T^+) = P(T^+ \mid D)P(D) + P(T^+ \mid \neg D)P(\neg D) = 0.95 \times 0.01 + 0.1 \times 0.99 = 0.0095 + 0.099 = 0.1085
$$

Now, apply Bayes’ Rule:

$$
P(D \mid T^+) = \frac{P(T^+ \mid D)P(D)}{P(T^+)} = \frac{0.95 \times 0.01}{0.1085} \approx 0.0876 \ (\text{or } 8.76\%)
$$

---

### Exercise 3: BN Construction

**Given random variables:** Rain, Sprinkler, WetGrass.

- WetGrass is true if either Rain or Sprinkler is true.
- Rain and Sprinkler are independent.

**Draw the BN and write the CPTs.**

**Solution:**

- **Nodes:** Rain (R), Sprinkler (S), WetGrass (W)
- **Edges:** $R \rightarrow W$, $S \rightarrow W$

**CPT for $W$:**

| $R$     | $S$     | $P(W = \text{true} \mid R, S)$ |
|---------|---------|----------------------------|
| true    | true    | 1                          |
| true    | false   | 1                          |
| false   | true    | 1                          |
| false   | false   | 0                          |

---
