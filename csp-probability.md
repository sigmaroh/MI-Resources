# Arc Consistency on a Constraint Network
This task involves applying the Generalized Arc Consistency (GAC) algorithm to the constraint network γ = (V, D, C):

## Problem Statement

- **Variables**:  
  V = {a, b, c, d}
- **Domains**:  
  For all v ∈ V: Dv = {1, 2, 3, 4, 5}
- **Constraints**:  
  - a + 2 < d  
  - b × d < 6  
  - a + c < 6

Your task: **Run the Generalized Arc Consistency algorithm** on this constraint network. After enforcing GAC, what are the possible values (domains) for each variable?

---

## Solution

Let's enforce GAC on each constraint step by step.

### 1. Constraint: a + 2 < d

For each possible a ∈ {1,2,3,4,5}, determine possible d ∈ {1,2,3,4,5} such that a + 2 < d.
- a = 1 ⇒ 1+2=3<d ⇒ d∈{4,5}
- a = 2 ⇒ 2+2=4<d ⇒ d=5
- a = 3 ⇒ 3+2=5<d ⇒ d>5 ⇒ d=∅ (no solution)
- a = 4 ⇒ 4+2=6<d ⇒ d>6 ⇒ d=∅
- a = 5 ⇒ 5+2=7<d ⇒ d>7 ⇒ d=∅

So **a ∈ {1,2}**. Corresponding feasible d (due to this constraint):
- For a=1 ⇒ d∈{4,5}
- For a=2 ⇒ d=5

Therefore, for this constraint, **d∈{4,5}**.

### 2. Constraint: b × d < 6

Original: b, d ∈ {1,2,3,4,5}. Update d to {4,5} (from above):

Check for each b ∈ {1,2,3,4,5} and d∈{4,5}:
- d=4:
  - b=1: 1×4=4<6 ✔️
  - b=2: 2×4=8 ✗
  - b=3: 3×4=12 ✗
  - b=4: 4×4=16 ✗
  - b=5: 5×4=20 ✗
- d=5:
  - b=1: 1×5=5<6 ✔️
  - b=2: 2×5=10 ✗
  - b=3: 3×5=15 ✗
  - b=4: 4×5=20 ✗
  - b=5: 5×5=25 ✗

So, for both d=4 and d=5, only **b=1** is possible.  
Thus, **b = {1}**

### 3. Constraint: a + c < 6

Recall a = {1,2}

- For a=1:
  - 1+c<6 ⇒ c<5 ⇒ c∈{1,2,3,4}
- For a=2:
  - 2+c<6 ⇒ c<4 ⇒ c∈{1,2,3}

So, possible c are those that work for at least one a:
- For a=1: c∈{1,2,3,4}
- For a=2: c∈{1,2,3}

But GAC means for every remaining c, there must exist a compatible a as well.
- c=1: (a=1 or a=2)
- c=2: (a=1 or a=2)
- c=3: (a=1 or a=2)
- c=4: (only a=1)

So c∈{1,2,3,4}

But let's check reversibility: for every a, there must be a c:
- a=1: c∈{1,2,3,4} (all fine)
- a=2: c∈{1,2,3} (4 does not work)

So, update:  
- a=1: compatible with c∈{1,2,3,4}
- a=2: compatible with c∈{1,2,3}
But c=4 is only valid if a=1, and since a=1 is still in the domain, that's acceptable.

So final domains:
- a∈{1,2}
- b∈{1}
- c∈{1,2,3,4}
- d∈{4,5}

---

## **Final Domains after GAC:**

- **a = {1, 2}**
- **b = {1}**
- **c = {1, 2, 3, 4}**
- **d = {4, 5}**


# README: Generalized Arc Consistency Example

This document presents a constraint satisfaction problem and guides you through running the Generalized Arc Consistency (GAC) algorithm to prune variable domains. At the end, both the to-do list for arcs and the pruned domains are provided.

---

## Problem Definition

**Constraint Network:**  
γ = (V, D, C)

- **Variables:** V = {a, b, c, d, e}
- **Domains:** For all v ∈ V: Dv = {1, 2, 3, 4, 5, 6}
- **Constraints:**
  - a + d > 8
  - 4e – 2b < 3
  - c + 2 > a
  - b < d

## Task

1. **Run the Generalized Arc Consistency (GAC) algorithm** on the above constraint network.
2. **Select the valid To-do Arcs** for the first iteration of the GAC algorithm.
3. **List the pruned domains** of all variables after enforcing GAC.

---

# Solution

## Step 1: Represent each constraint as arcs

The binary constraints induce the following arcs (in both directions for a binary constraint):

- a + d > 8 ⇒ (a, d), (d, a)
- b < d     ⇒ (b, d), (d, b)
- c + 2 > a ⇒ (c, a), (a, c)
- 4e – 2b < 3 ⇒ (e, b), (b, e)

Thus, the initial To-Do list of arcs (all arcs affected by some constraint):

- (a, d), (d, a)
- (b, d), (d, b)
- (c, a), (a, c)
- (e, b), (b, e)

## Step 2: Valid To-Do Arcs for First Iteration

From the options given, the correct set for the initial to-do list is:

> (a, d), (d, a), (b, d), (d, b), (a, c), (c, a), (e, b), (b, e)

This matches the set in the option:
> (e, b), (d, b), (d, a), (c, a), (b, e), (b, d), (a, d), (a, c)

## Step 3: Run GAC and Prune Domains

### 1. **Constraint:** a + d > 8  
Possible values:  
Both a and d range from 1 to 6.
- For a = 3, d must be > 5 ⇒ impossible, since max d = 6.
- Let's brute-force all possibilities:

| a | d | a+d | a+d>8? |
|---|---|-----|--------|
| 3 | 6 |   9 | YES    |
| 4 | 5 |   9 | YES    |
| 4 | 6 |  10 | YES    |
| 5 | 4 |   9 | YES    |
| 5 | 5 |  10 | YES    |
| 5 | 6 |  11 | YES    |
| 6 | 3 |   9 | YES    |
| 6 | ... | ...| YES if d ≥ 3 |

It turns out, the pairs for which a + d > 8 are:
- (3,6)
- (4,5), (4,6)
- (5,4), (5,5), (5,6)
- (6,3), (6,4), (6,5), (6,6)

So possible a values: 3,4,5,6  
Possible d values: 3,4,5,6

**But wait: let's check which values of a and d actually occur in the allowed pairs.**

Set of possible a:  
- a = 3 occurs with d = 6  
- a = 4 with d = 5,6  
- a = 5 with d = 4,5,6  
- a = 6 with d = 3,4,5,6  

Set of possible d:  
- d=3 with a=6  
- d=4 with a=5,6  
- d=5 with a=4,5,6  
- d=6 with a=3,4,5,6  

**Therefore:**
- a ∈ {3,4,5,6}
- d ∈ {3,4,5,6}

### 2. **Constraint**: 4e – 2b < 3  
That is, 4e – 2b < 3 ⇒ 2e – b < 1.5  
Let’s just test all values for e and b from 1 to 6.

Try e = 1:
- b = any ⇒ 4×1 – 2b < 3 ⇒ 4 – 2b < 3 ⇒ –2b < –1 ⇒ b > 0.5 ⇒ b ∈ {1,2,3,4,5,6}
But let's check further since b is integer.

Test for e = 1:
4×1 – 2b < 3 ⇒ 4 – 2b < 3 ⇒ –2b < –1 ⇒ b > 0.5

So, b ∈ {1,2,3,4,5,6}

e = 2:
4×2 – 2b < 3 ⇒ 8 – 2b < 3 ⇒ –2b < –5 ⇒ b > 2.5 ⇒ b ∈ {3,4,5,6}

e = 3:
4×3 – 2b < 3 ⇒ 12 – 2b < 3 ⇒ –2b < –9 ⇒ b > 4.5 ⇒ b ∈ {5,6}

e = 4:
16 – 2b < 3 ⇒ –2b < –13 ⇒ b > 6.5 ⇒ b ∈ {} (empty)

e = 5:
20 – 2b < 3 ⇒ –2b < –17 ⇒ b > 8.5 ⇒ b ∈ {}

e = 6:
24 – 2b < 3 ⇒ –2b < –21 ⇒ b > 10.5 ⇒ b ∈ {}

Therefore,
- e ∈ {1,2,3}
- For e = 1 ⇒ b ∈ {1,2,3,4,5,6}
- For e = 2 ⇒ b ∈ {3,4,5,6}
- For e = 3 ⇒ b ∈ {5,6}

But if e is restricted, the possible domains are:
- e ∈ {1,2,3}
- b ∈ {1,2,3,4,5,6}
Now, considering only possible e’s, must prune b further.

From the above:
- b ∈ {1,2,3,4,5,6}: compatible with e=1
- b ∈ {3,4,5,6}: compatible with e=2
- b ∈ {5,6}: compatible with e=3

All this will be further pruned by other constraints (see next).

### 3. **Constraint:** c + 2 > a  
For pruned a ∈ {3,4,5,6}, so c > a – 2

Let’s see for what values of c (1,2,3,4,5,6) and a ∈ {3,4,5,6}, c + 2 > a ⇒ c > a – 2

For a = 3: c > 1 ⇒ c ∈ {2,3,4,5,6}
a = 4: c > 2 ⇒ c ∈ {3,4,5,6}
a = 5: c > 3 ⇒ c ∈ {4,5,6}
a = 6: c > 4 ⇒ c ∈ {5,6}

So union over a ∈ {3,4,5,6} = c ∈ {2,3,4,5,6}

**But**, for a particular value of c, are there any compatible a values left with all the constraints? Let’s keep c ∈ {2,3,4,5,6} for now.

### 4. **Constraint:** b < d  
d ∈ {3,4,5,6}; b ∈ ?

Let’s consider all candidate b's from earlier ({1,2,3,4,5,6}). For d values {3,4,5,6}, b can be at most 5.

But with previous constraints (like 4e – 2b < 3) and domain restrictions, finally feasible values are:

- b must be less than at least one value of d. So possible b ∈ {1,2,3,4,5}

But factoring in all constraints, and cross-referencing with e domain:

From 4e – 2b < 3, we had 
- If e = 1 → b ∈ {1,2,3,4,5,6}
- If e = 2 → b ∈ {3,4,5,6}
- If e = 3 → b ∈ {5,6}

But b cannot be above 5, since d ∈ {3,4,5,6} ⇒ b < d ⇒ b ∈ {1,2,3,4,5}

For b = 6 to be valid, need d = 6+something ⇒ d=6 but b<6 fails for b=6. So b=6 excluded.

So finally b ∈ {1,2,3,4,5}

e=1 is compatible with b ∈ {1,2,3,4,5}, e=2 with b ∈ {3,4,5}, e=3 with b ∈ {5}, else e out of domain.

So, all considered, final feasible values:

- a ∈ {3,4,5,6}
- b ∈ {1,2,3,4,5}
- c ∈ {2,3,4,5,6}
- d ∈ {3,4,5,6}
- e ∈ {1,2,3}

---

## Summary Table

| Variable | Final Domain       |
|----------|-------------------|
|   a      | 3, 4, 5, 6        |
|   b      | 1, 2, 3, 4, 5     |
|   c      | 2, 3, 4, 5, 6     |
|   d      | 3, 4, 5, 6        |
|   e      | 1, 2, 3           |

---

## Answers

**1. Valid To-Do Arcs for the first iteration of GAC:**

`(e, b), (d, b), (d, a), (c, a), (b, e), (b, d), (a, d), (a, c)`

**2. Domains after GAC:**

- a ∈ {3,4,5,6}
- b ∈ {1,2,3,4,5}
- c ∈ {2,3,4,5,6}
- d ∈ {3,4,5,6}
- e ∈ {1,2,3}

# Generalized Arc Consistency Example: README and Solution

## Constraint Network

**Variables:**  
V = {a, b, c, d}

**Domains:**  
D_v = {1, 2, 3} for all v in V

**Constraints:**  
- b = a  
- b > c  
- a ≠ c  
- c ≠ d  
- d ≤ a  

---

## Task

**Run the Generalized Arc Consistency (GAC) algorithm** on this network.

Determine the resulting domains for each variable.

---

## Solution

Let's apply GAC step by step:

### 1. **Initial Domains**
- a ∈ {1, 2, 3}
- b ∈ {1, 2, 3}
- c ∈ {1, 2, 3}
- d ∈ {1, 2, 3}

---

### 2. **Constraint Propagation**

Let's propagate each constraint in turn, applying pruning as needed.

#### a. **b = a**
- For every (a, b) pair, must have a = b.  
So, a and b must always be equal.

Therefore, after this constraint:
- a, b domains must be equal at each pruning step.

#### b. **b > c**
- For possible b ∈ {1,2,3} and c ∈ {1,2,3}, only consider pairs where b > c.
- The valid pairs:
  - b = 2, c = 1
  - b = 3, c = 1
  - b = 3, c = 2

- Therefore, **possible values for b: 2, 3** (since no b = 1 > c for c ∈ {1,2,3}), and for c: 1, 2 (since only c = 1 or 2 can appear in {b > c}).

But **remember b = a**, so a ∈ domain(b) ⇒ a ∈ {2, 3}.

After this step:
- a ∈ {2, 3}
- b ∈ {2, 3}
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

#### c. **a ≠ c**
- a ∈ {2,3}
- c ∈ {1,2}

- For a = 2, c can be 1 (since a ≠ c)  
- For a = 3, c can be 1 or 2 (since a ≠ c always holds: 3 ≠ 1, 3 ≠ 2)

So,
- For c = 2: only compatible with a = 3

#### d. **c ≠ d**
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

So for each c:
- c = 1: d ∈ {2, 3}
- c = 2: d ∈ {1, 3}

#### e. **d ≤ a**
a ∈ {2, 3}
d ∈ {1, 2, 3}

For a = 2: d ∈ {1,2}  
For a = 3: d ∈ {1,2,3}  

---

#### Now, let's express all possible consistent tuples and prune incompatible values.

Let's enumerate all possible values for (a, b, c, d) consistent with all constraints.

**Remember:**
- b = a
- b > c
- a ≠ c
- c ≠ d
- d ≤ a

Loop over a ∈ {2,3}, b = a, c ∈ {1,2}, d ∈ possible values.

##### a = 2, b = 2:
- c ∈ {1}
  - b > c → 2 > 1 ✓
  - a ≠ c: 2 ≠ 1 ✓
  - c ≠ d → d ≠ 1
  - d ≤ a → d ∈ {1,2}
  - So: d = 2 (since d ≠ 1 by c ≠ d).
  - So possible tuple: (a=2, b=2, c=1, d=2)
- c = 2:
  - b > c → 2 > 2 ✗ (no, must be b>c)
  - skip

##### a = 3, b = 3:
- c = 1:
  - b > c → 3 > 1 ✓
  - a ≠ c: 3 ≠ 1 ✓
  - c ≠ d: d ≠ 1
  - d ≤ a → d ∈ {1,2,3}
  - d ∈ {2,3}
  - So, possible tuples:
    - (a=3, b=3, c=1, d=2)
    - (a=3, b=3, c=1, d=3)
- c = 2:
  - b > c → 3 > 2 ✓
  - a ≠ c: 3 ≠ 2 ✓
  - c ≠ d → d ≠ 2
  - d ≤ a → d ∈ {1,2,3}
  - d ∈ {1,3}
  - So, possible tuples:
    - (a=3, b=3, c=2, d=1)
    - (a=3, b=3, c=2, d=3)

---

### 3. **Final Pruned Domains**

From the possible tuples above, extract values that appear for each variable:

- a: appears as 2, 3
- b: equal to a ⇒ {2, 3}
- c: 1, 2
- d: 1, 2, 3 (let's see which d's occur: 2, 2, 3, 1, 3 → so 1, 2, 3; but check which values for which a)

Mapping:
- (a=2, b=2, c=1, d=2)
- (a=3, b=3, c=1, d=2)
- (a=3, b=3, c=1, d=3)
- (a=3, b=3, c=2, d=1)
- (a=3, b=3, c=2, d=3)

So the final domains are:
- a ∈ {2, 3}
- b ∈ {2, 3}
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

---

## **Summary Table**

| Variable | Domain        |
|----------|--------------|
|   a      | {2, 3}       |
|   b      | {2, 3}       |
|   c      | {1, 2}       |
|   d      | {1, 2, 3}    |

---

```md
# Generalized Arc Consistency (GAC) – Step-by-Step Execution

## Constraint Network γ = (V, D, C)

### Variables
V = {a, b, c, d}

### Domains (initial)
Da = Db = Dc = Dd = {1,2,3,4,5,6,7,8,9,10}

### Constraints
- c1: 2|a − c| > 3
- c2: b² − 3d < 9
- c3: b + 3 < c

---

## Initial To-do-arcs (lexicographic, FIFO)

To-do-arcs₀ =
[(a,c1), (c,c1), (b,c2), (d,c2), (b,c3), (c,c3)]

---

## GAC Execution

### Iteration 1
**To-do-arcs**:  
[(a,c1), (c,c1), (b,c2), (d,c2), (b,c3), (c,c3)]

**Removed**: (a,c1)

**Revise result**:  
Da = {1,2,3,4,5,6,7,8,9,10}

**Added to M**: ∅

---

### Iteration 2
**Removed**: (c,c1)

**Revise result**:  
Dc = {1,2,3,4,5,6,7,8,9,10}

**Added to M**: ∅

---

### Iteration 3
**Removed**: (b,c2)

Constraint: b² − 3d < 9

**Revise result**:  
Db = {1,2,3,4,5,6}

**Added to M**:  
(d,c2)

---

### Iteration 4
**Removed**: (d,c2)

Constraint: b² − 3d < 9, with Db = {1,…,6}

**Revise result**:  
Dd = {10}

**Added to M**:  
(b,c2)

---

### Iteration 5
**Removed**: (b,c3)

Constraint: b + 3 < c

**Revise result**:  
Db = {1,2,3,4,5,6}

**Added to M**: ∅

---

### Iteration 6
**Removed**: (c,c3)

Constraint: b + 3 < c, with Db = {1,…,6}

**Revise result**:  
Dc = {5,6,7,8,9,10}

**Added to M**:  
(b,c3)

---

### Iteration 7
**Removed**: (d,c2)

**Revise result**:  
Dd = {10}

**Added to M**: ∅

---

### Iteration 8
**Removed**: (b,c2)

**Revise result**:  
Db = {1,2,3,4,5,6}

**Added to M**: ∅

---

### Iteration 9
**Removed**: (b,c3)

**Revise result**:  
Db = {1,2,3,4,5,6}

**Added to M**: ∅

---

## Final GAC Domains

- Da = {1,2,3,4,5,6,7,8,9,10}
- Db = {1,2,3,4,5,6}
- Dc = {5,6,7,8,9,10}
- Dd = {10}

---

**GAC reached**: To-do-arcs is empty.
```

## Generalized Arc Consistency (GAC) on a Simple CSP

**Constraint network:**  
Let $\gamma = (V, D, C)$, where:

- **Variables:** $V = \{a, b, c, d\}$
- **Domains:** For all $v \in V$, $D_v = \{1, 2, 3, 4, 5\}$
- **Constraints:**
    - $a + 2 < d$
    - $b \cdot d < 6$
    - $a + c < 6$

---

### Task

**Run the Generalized Arc Consistency algorithm on this constraint network.  
What are the domains of the variables after enforcing GAC?**

---

### **Final GAC Domains**

- **$D_a =$** $\{1,2\}$
- **$D_b =$** $\{1\}$
- **$D_c =$** $\{1,2,3,4\}$
- **$D_d =$** $\{4,5\}$
	​

---

**Explanation:**

- $a + 2 < d$ restricts $a$ to $\{1,2,3\}$ and $d$ to $\{4,5\}$.
- $a + c < 6$ limits $c$ to at most $4$.
- $b \cdot d < 6$ with $d \in \{4,5\}$ allows all $b$, since $b \leq 1$ for $d=5$ and $b\leq 1$ for $d=4$, but $b$ can be $1$ for both.

---

| Variable | Domain after GAC        |
|----------|------------------------|
| $a$      | $\{1,2\}$            |
| $b$      | $\{1\}$        |
| $c$      | $\{1,2,3,4\}$          |
| $d$      | $\{4,5\}$              |


# Generalized Arc Consistency (GAC)

## Problem

Consider the constraint network  
\[
\gamma = (V, D, C)
\]

### Variables
\[
V = \{a, b, c, d\}
\]

### Domains
For all \( v \in V \):
\[
D_v = \{1, 2, 3, 4, 5\}
\]

### Constraints
1. \( a + 2 < d \)
2. \( b \times d < 6 \)
3. \( a + c < 6 \)

Run the **Generalized Arc Consistency (GAC)** algorithm and determine the final domain of each variable.

---

## Constraint Analysis

### Constraint 1: \( a + 2 < d \)

Valid pairs \((a,d)\):

- If \(a=1\), then \(d \ge 4\)
- If \(a=2\), then \(d \ge 5\)
- If \(a \ge 3\), then \(d > 5\) (impossible)

✅ Valid values:
- \(a \in \{1,2\}\)
- \(d \in \{4,5\}\)

---

### Constraint 2: \( b \times d < 6 \)

With \(d \in \{4,5\}\):

- If \(d=4\): \(b=1\) (since \(2\times4=8>6\))
- If \(d=5\): \(b=1\) (since \(2\times5=10>6\))

✅ Valid values:
- \(b \in \{1\}\)
- \(d \in \{4,5\}\) (still valid)

---

### Constraint 3: \( a + c < 6 \)

With \(a \in \{1,2\}\):

- If \(a=1\): \(c \le 4\)
- If \(a=2\): \(c \le 3\)

Union of supported values:
- \(c \in \{1,2,3,4\}\)

---

## Final Domains After GAC

### Variable Domains

- **a** = {1, 2}
- **b** = {1}
- **c** = {1, 2, 3, 4}
- **d** = {4, 5}

---

## Final Answer (Selection Format)

### a =
- ✅ 1  
- ✅ 2  
- ⛔ 3  
- ⛔ 4  
- ⛔ 5  

### b =
- ✅ 1  
- ⛔ 2  
- ⛔ 3  
- ⛔ 4  
- ⛔ 5  

### c =
- ✅ 1  
- ✅ 2  
- ✅ 3  
- ✅ 4  
- ⛔ 5  

### d =
- ⛔ 1  
- ⛔ 2  
- ⛔ 3  
- ✅ 4  
- ✅ 5  




# README: Variable Elimination Algorithm for CSPs

**Question:**  
In the variable elimination algorithm to solve CSPs, which of the following is correct?

Select one:

a.  
We construct a table for each constraint, and at each step the algorithm removes a constraint by combining all its variables.

b.  
We construct a table for each constraint, and at each step the algorithm removes a variable by combining all its constraints.

c.  
We construct a table for each variable, and at each step the algorithm removes a constraint by combining all its variables.

d.  
We construct a table for each variable, and at each step the algorithm removes a variable by combining all its constraints.

---

## Solution

The correct answer is:

**b. We construct a table for each constraint, and at each step the algorithm removes a variable by combining all its constraints.**

**Explanation:**  
In the variable elimination algorithm for CSPs (Constraint Satisfaction Problems):

- Initially, a "factor" (table of allowed values) is constructed for each constraint.
- At each step, the algorithm selects a variable to eliminate. All the tables ("factors") involving that variable are combined into a new table (by joining and summing/eliminating over the selected variable).
- This process continues — eliminating one variable at a time — until all variables are removed or a solution is produced.

So the process is not about removing constraints, but about eliminating variables by combining the relevant constraint tables.

**Answer: b**








# Analyzing Independence in Categorical Data: Positive Reviews & Discounts

Consider the following scenario:

There are **10,000 reviews** for a restaurant, each annotated with three boolean variables:

- **Positive** (was the review positive?)
- **Discount** (was a discount offered?)
- **Long** (was the review long or short?)

The following table (see image below) displays the counts for each combination of these variables:

![Dependence Table](/images/Dependence.png)

*Dependence for exercise*

---

Your tasks:

## 1. Are “Positive” and “Discount” independent?

Determine whether the variables **Positive** and **Discount** are independent of each other.

## 2. Joint and Marginal Distributions

Fill in the joint probabilities for the following outcomes (all as probabilities, not counts):

- **P(Positive=Yes, Discount=Yes):**  
- **P(Positive=Yes, Discount=No):**  
- **P(Positive=No, Discount=Yes):**  
- **P(Positive=No, Discount=No):**  

Also, compute the marginal probabilities:

- **P(Positive=Yes):**
- **P(Positive=No):**
- **P(Discount=Yes):**
- **P(Discount=No):**

---

## 3. Independence Check

Based on your calculations above, do **Positive** and **Discount** appear to be independent?  
State your reasoning and show your calculations or explanation.


Here is the answer formatted for a README file:

---

## Restaurant Review Independence Analysis

### 📊 Data Summary  
From a dataset of **10,000 restaurant reviews**, we have three boolean variables:  

| Variable  | Description                          |
|-----------|--------------------------------------|
| `Positive`| Whether the review is positive       |
| `Discount`| Whether a discount was mentioned     |
| `Long`    | Whether the review is long           |

**Data Table:**  

|            | Discount = yes       | Discount = no        |
|------------|----------------------|----------------------|
|            | Long = yes | Long = no | Long = yes | Long = no |
| **Positive = yes** | 130        | 170       | 1000       | 1700      |
| **Positive = no**  | 500        | 200       | 4000       | 2300      |

---

### 🔍 Step 1 – Marginalize over `Long`  
We sum over `Long` to get joint counts of `(Positive, Discount)`.

- **Positive = yes, Discount = yes**  
  \( 130 + 170 = 300 \)

- **Positive = yes, Discount = no**  
  \( 1000 + 1700 = 2700 \)

- **Positive = no, Discount = yes**  
  \( 500 + 200 = 700 \)

- **Positive = no, Discount = no**  
  \( 4000 + 2300 = 6300 \)

**Check total:**  
\( 300 + 2700 + 700 + 6300 = 10000 \) ✓

---

### 📈 Step 2 – Joint & Marginal Probabilities  

**Joint distribution \(P(Positive, Discount)\)** (divide by 10000):

| \(P\)           | Discount = yes | Discount = no | **Marginal \(P(Positive)\)** |
|-----------------|----------------|---------------|------------------------------|
| Positive = yes  | 0.0300         | 0.2700        | **0.3000**                   |
| Positive = no   | 0.0700         | 0.6300        | **0.7000**                   |
| **Marginal \(P(Discount)\)** | **0.1000**     | **0.9000**    |                              |

---

### ✅ Step 3 – Test for Independence  
Two variables are independent if:  
\[
P(Positive, Discount) = P(Positive) \times P(Discount)
\]

- \(P(Positive=yes) \times P(Discount=yes) = 0.3 \times 0.1 = 0.03\)  
  → Matches joint \(0.03\) ✓

- \(P(Positive=yes) \times P(Discount=no) = 0.3 \times 0.9 = 0.27\)  
  → Matches joint \(0.27\) ✓

- \(P(Positive=no) \times P(Discount=yes) = 0.7 \times 0.1 = 0.07\)  
  → Matches joint \(0.07\) ✓

- \(P(Positive=no) \times P(Discount=no) = 0.7 \times 0.9 = 0.63\)  
  → Matches joint \(0.63\) ✓

All match exactly.

---

### 🧮 Conclusion  
**Positive and Discount are independent** in this dataset.

---

### 📌 Summary Table (Joint Distribution)

| \(P(Positive, Discount)\) | Discount = yes | Discount = no |
|---------------------------|----------------|---------------|
| **Positive = yes**        | 0.0300         | 0.2700        |
| **Positive = no**         | 0.0700         | 0.6300        |

Marginals:  
- \(P(Positive=yes) = 0.3000\)  
- \(P(Positive=no) = 0.7000\)  
- \(P(Discount=yes) = 0.1000\)  
- \(P(Discount=no) = 0.9000\)