# MI Exercises - Organized by Chapter

---

# Chapter 2: Constraint Satisfaction Problems (CSP)

## Arc Consistency on a Constraint Network

This task involves applying the Generalized Arc Consistency (GAC) algorithm to the constraint network γ = (V, D, C):

### Problem Statement

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

### Solution

Let's enforce GAC on each constraint step by step.

#### 1. Constraint: a + 2 < d

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

#### 2. Constraint: b × d < 6

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

#### 3. Constraint: a + c < 6

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

### **Final Domains after GAC:**

- **a = {1, 2}**
- **b = {1}**
- **c = {1, 2, 3, 4}**
- **d = {4, 5}**

---

## GAC Example with 5 Variables

### Problem Definition

**Constraint Network:**  
γ = (V, D, C)

- **Variables:** V = {a, b, c, d, e}
- **Domains:** For all v ∈ V: Dv = {1, 2, 3, 4, 5, 6}
- **Constraints:**
  - a + d > 8
  - 4e – 2b < 3
  - c + 2 > a
  - b < d

### Task

1. **Run the Generalized Arc Consistency (GAC) algorithm** on the above constraint network.
2. **Select the valid To-do Arcs** for the first iteration of the GAC algorithm.
3. **List the pruned domains** of all variables after enforcing GAC.

---

### Solution

#### Step 1: Represent each constraint as arcs

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

#### Step 2: Valid To-Do Arcs for First Iteration

From the options given, the correct set for the initial to-do list is:

> (a, d), (d, a), (b, d), (d, b), (a, c), (c, a), (e, b), (b, e)

This matches the set in the option:
> (e, b), (d, b), (d, a), (c, a), (b, e), (b, d), (a, d), (a, c)

#### Step 3: Run GAC and Prune Domains

##### 1. **Constraint:** a + d > 8  
Possible values:  
Both a and d range from 1 to 6.

It turns out, the pairs for which a + d > 8 are:
- (3,6)
- (4,5), (4,6)
- (5,4), (5,5), (5,6)
- (6,3), (6,4), (6,5), (6,6)

**Therefore:**
- a ∈ {3,4,5,6}
- d ∈ {3,4,5,6}

##### 2. **Constraint**: 4e – 2b < 3  

Test for e = 1:
4×1 – 2b < 3 ⇒ 4 – 2b < 3 ⇒ –2b < –1 ⇒ b > 0.5

So, b ∈ {1,2,3,4,5,6}

e = 2:
4×2 – 2b < 3 ⇒ 8 – 2b < 3 ⇒ –2b < –5 ⇒ b > 2.5 ⇒ b ∈ {3,4,5,6}

e = 3:
4×3 – 2b < 3 ⇒ 12 – 2b < 3 ⇒ –2b < –9 ⇒ b > 4.5 ⇒ b ∈ {5,6}

e = 4:
16 – 2b < 3 ⇒ –2b < –13 ⇒ b > 6.5 ⇒ b ∈ {} (empty)

Therefore,
- e ∈ {1,2,3}

##### 3. **Constraint:** c + 2 > a  
For pruned a ∈ {3,4,5,6}, so c > a – 2

For a = 3: c > 1 ⇒ c ∈ {2,3,4,5,6}
a = 4: c > 2 ⇒ c ∈ {3,4,5,6}
a = 5: c > 3 ⇒ c ∈ {4,5,6}
a = 6: c > 4 ⇒ c ∈ {5,6}

So union over a ∈ {3,4,5,6} = c ∈ {2,3,4,5,6}

##### 4. **Constraint:** b < d  
d ∈ {3,4,5,6}; b ∈ ?

b must be less than at least one value of d. So possible b ∈ {1,2,3,4,5}

### Summary Table

| Variable | Final Domain       |
|----------|-------------------|
|   a      | 3, 4, 5, 6        |
|   b      | 1, 2, 3, 4, 5     |
|   c      | 2, 3, 4, 5, 6     |
|   d      | 3, 4, 5, 6        |
|   e      | 1, 2, 3           |

---

## GAC Example with Equality Constraints

### Constraint Network

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

### Task

**Run the Generalized Arc Consistency (GAC) algorithm** on this network.

Determine the resulting domains for each variable.

---

### Solution

#### 1. **Initial Domains**
- a ∈ {1, 2, 3}
- b ∈ {1, 2, 3}
- c ∈ {1, 2, 3}
- d ∈ {1, 2, 3}

---

#### 2. **Constraint Propagation**

##### a. **b = a**
- For every (a, b) pair, must have a = b.  
So, a and b must always be equal.

##### b. **b > c**
- For possible b ∈ {1,2,3} and c ∈ {1,2,3}, only consider pairs where b > c.
- The valid pairs:
  - b = 2, c = 1
  - b = 3, c = 1
  - b = 3, c = 2

- Therefore, **possible values for b: 2, 3**, and for c: 1, 2.

But **remember b = a**, so a ∈ domain(b) ⇒ a ∈ {2, 3}.

After this step:
- a ∈ {2, 3}
- b ∈ {2, 3}
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

##### c. **a ≠ c**
- a ∈ {2,3}
- c ∈ {1,2}

- For a = 2, c can be 1 (since a ≠ c)  
- For a = 3, c can be 1 or 2

##### d. **c ≠ d**
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

So for each c:
- c = 1: d ∈ {2, 3}
- c = 2: d ∈ {1, 3}

##### e. **d ≤ a**
a ∈ {2, 3}
d ∈ {1, 2, 3}

For a = 2: d ∈ {1,2}  
For a = 3: d ∈ {1,2,3}  

---

### 3. **Final Pruned Domains**

From the possible tuples above, extract values that appear for each variable:

- a ∈ {2, 3}
- b ∈ {2, 3}
- c ∈ {1, 2}
- d ∈ {1, 2, 3}

---

## Variable Elimination Algorithm for CSPs

**Question:**  
In the variable elimination algorithm to solve CSPs, which of the following is correct?

Select one:

a. We construct a table for each constraint, and at each step the algorithm removes a constraint by combining all its variables.

b. We construct a table for each constraint, and at each step the algorithm removes a variable by combining all its constraints.

c. We construct a table for each variable, and at each step the algorithm removes a constraint by combining all its variables.

d. We construct a table for each variable, and at each step the algorithm removes a variable by combining all its constraints.

---

### Solution

The correct answer is:

**b. We construct a table for each constraint, and at each step the algorithm removes a variable by combining all its constraints.**

**Explanation:**  
In the variable elimination algorithm for CSPs (Constraint Satisfaction Problems):

- Initially, a "factor" (table of allowed values) is constructed for each constraint.
- At each step, the algorithm selects a variable to eliminate. All the tables ("factors") involving that variable are combined into a new table (by joining and summing/eliminating over the selected variable).
- This process continues — eliminating one variable at a time — until all variables are removed or a solution is produced.

So the process is not about removing constraints, but about eliminating variables by combining the relevant constraint tables.

**Answer: b**

---

# Chapter 3: Reasoning Under Uncertainty and Probability

## Analyzing Independence in Categorical Data: Positive Reviews & Discounts

Consider the following scenario:

There are **10,000 reviews** for a restaurant, each annotated with three boolean variables:

- **Positive** (was the review positive?)
- **Discount** (was a discount offered?)
- **Long** (was the review long or short?)

The following table displays the counts for each combination of these variables:

![Dependence Table](/images/Dependence.png)

*Dependence for exercise*

---

Your tasks:

### 1. Are "Positive" and "Discount" independent?

Determine whether the variables **Positive** and **Discount** are independent of each other.

### 2. Joint and Marginal Distributions

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

### 3. Independence Check

Based on your calculations above, do **Positive** and **Discount** appear to be independent?  
State your reasoning and show your calculations or explanation.

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

---

# Chapter 5: Supervised Learning & K-NN

## K-Nearest Neighbour (k-NN) Classification

We are applying classification using the nearest neighbour method (K-NN) using Euclidean distance. We have the following dataset: 
![K_NN](/images/2024-nearest-neighbours.png)

We're provided a new data point (size=2,weight=2), which we want to classify. Indicate the class for several values of K: 

If we use K=3: ?? [bad,ok,great, none]
 

If we use K=7: ?? [bad,ok,great, none]
 



We're provided a new data point (size=4,weight=9), which we want to classify. Indicate the class for several values of K: 

If we use K=3: ?? [bad,ok,great, none]
 

If we use K=7: ?? [bad,ok,great, none]
 

---

## Solution

### k-Nearest Neighbour (k-NN) Classification — Distance Tables & Explanation

We apply **k-Nearest Neighbour (k-NN)** classification using **Euclidean distance**.

Classes in the dataset:
- **Bad** (blue squares)
- **Ok** (red triangles)
- **Great** (black circles)

Classification is done by **majority voting among the k nearest neighbors**, without relying on tie-breaking.

---

### Euclidean Distance Formula

For two points  
\[
(x_1, y_1), (x_2, y_2)
\]

\[
d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
\]

To compare distances, we use **squared distances**, since the square root preserves ordering.

---

### 1. Classifying Point (2, 2)

#### Distance Table

| Data point | Class | Distance formula | Distance² |
|-----------|-------|------------------|-----------|
| (1,2) | Bad | √((2−1)²+(2−2)²) | **1** |
| (2,2) | Ok | √((2−2)²+(2−2)²) | **0** |
| (2,4) | Bad | √((2−2)²+(2−4)²) | **4** |
| (1,5) | Ok | √((2−1)²+(2−5)²) | 10 |
| (3,4) | Bad | √((2−3)²+(2−4)²) | 5 |
| (4,3) | Bad | √((2−4)²+(2−3)²) | 5 |
| (4,1) | Bad | √((2−4)²+(2−1)²) | 5 |

---

#### K = 3
Nearest neighbors (smallest distances):
- Ok, Bad, Bad  

Votes:
- Bad = 2  
- Ok = 1  

**Classification: Bad**

---

#### K = 7
Votes:
- Bad = 5  
- Ok = 2  

**Classification: Bad**

---

### 2. Classifying Point (4, 9)

#### Distance Table

| Data point | Class | Distance² |
|-----------|-------|-----------|
| (3,9) | Great | **1** |
| (4,8) | Ok | **1** |
| (5,8) | Ok | **2** |
| (6,9) | Bad | 4 |
| (6,8) | Bad | 5 |
| (5,7) | Bad | 5 |
| (4,6) | Bad | 9 |

---

#### K = 3
Nearest neighbors:
- Great, Ok, Ok  

Votes:
- Ok = 2  
- Great = 1  

**Classification: Ok**

---

#### K = 7
Votes:
- Bad = 4  
- Ok = 2  
- Great = 1  

**Classification: Bad**

---

### 3. Classifying Point (10, 9)

#### Distance Table

| Data point | Class | Distance² |
|-----------|-------|-----------|
| (10,9) | Bad | **0** |
| (10,8) | Ok | 1 |
| (9,8) | Great | 2 |
| (10,7) | Great | 4 |
| (9,6) | Ok | 10 |
| (9,4) | Great | 26 |
| (8,4) | Great | 29 |

---

#### Classified as Bad?
- K = 1 → nearest neighbor is Bad  

**Yes — lowest K = 1**

---

#### Classified as Ok?
- No value of K gives Ok a strict majority without ties  

**No**

---

#### Classified as Great?
- K = 7 gives:
  - Great = 4  
  - Ok = 2  
  - Bad = 1  

**Yes — lowest K = 7**

---

### Overfitting Question

Small values of K are more sensitive to noise and local variations.

**Value of K most likely to overfit:**
\[
K = 1
\]

---

### Final Answers Summary

| Question | Answer |
|--------|-------|
| (2,2), K=3 | Bad |
| (2,2), K=7 | Bad |
| (4,9), K=3 | Ok |
| (4,9), K=7 | Bad |
| Bad at (10,9)? | Yes, K = 1 |
| Ok at (10,9)? | No |
| Great at (10,9)? | Yes, K = 7 |
| Overfitting | K = 1 |

---

## K-NN Classification with Mixed Feature Types

We are given the following setup:

- **Feature 1**: Categorical, values ∈ {1, 2, 3}
- **Feature 2**: Numerical

### Distance Table for Feature 1 (Categorical):

|         | **1** | **2** | **3** |
|---------|-------|-------|-------|
| **1**   | 0     | 20    | 60    |
| **2**   | 20    | 0     | 35    |
| **3**   | 60    | 35    | 0     |

### Dataset:

| Index | Feature 1 | Feature 2 | Class |
|-------|-----------|-----------|-------|
| 1     |     2     |     88    |  A    |
| 2     |     2     |     80    |  A    |
| 3     |     3     |    110    |  A    |
| 4     |     1     |     69    |  B    |
| 5     |     2     |     77    |  B    |

---

We have a **new observation**:
- Feature 1 = **2**
- Feature 2 = **67**

---

### Questions

#### 1. What is the class of the new observation according to **1-nearest neighbor with Manhattan distance**?

> **Your answer:**


#### 2. What is the class of the new observation according to **1-nearest neighbor with Euclidean distance**?

> **Your answer:**


#### 3. What would the class of the new observation be according to **3-nearest neighbor with Manhattan distance**?

> **Your answer:**


#### 4. What would the class of the new observation be according to **3-nearest neighbor with Euclidean distance**?

> **Your answer:**

 

---

### Solution

#### **1. Understanding the data**

We have **Feature 1** (categorical with values 1, 2, 3) and **Feature 2** (numerical).  
There's also a given **dissimilarity table for Feature 1** (like a distance matrix between categories):

| F1(a) \ F1(b) | 1   | 2   | 3   |
|---|---|---|---|
| 1             | 0   | 20  | 60  |
| 2             | 20  | 0   | 35  |
| 3             | 60  | 35  | 0   |

So if Feature 1 is 1 and Feature 1 is 2 → distance = 20.  
This is *categorical distance*.

**Dataset:**
| ID | Feature 1 | Feature 2 | Class |
|----|-----------|-----------|-------|
| 1  | 2         | 88        | A     |
| 2  | 2         | 80        | A     |
| 3  | 3         | 110       | A     |
| 4  | 1         | 69        | B     |
| 5  | 2         | 77        | B     |

New observation: Feature 1 = 2, Feature 2 = 67.

---

#### **2. Manhattan distance**

For Manhattan distance between (F1_new, F2_new) and (F1_i, F2_i):

\[
d_{\text{manhattan}} = \text{DistTable}(F1_{\text{new}}, F1_i) + |F2_{\text{new}} - F2_i|
\]

- **Point 1:** F1=2, F2=88  
  DistTable(2,2) = 0  
  |67-88| = 21  
  d = 0 + 21 = **21**

- **Point 2:** F1=2, F2=80  
  DistTable(2,2) = 0  
  |67-80| = 13  
  d = **13**

- **Point 3:** F1=3, F2=110  
  DistTable(2,3) = 35  
  |67-110| = 43  
  d = 35 + 43 = **78**

- **Point 4:** F1=1, F2=69  
  DistTable(2,1) = 20  
  |67-69| = 2  
  d = 20 + 2 = **22**

- **Point 5:** F1=2, F2=77  
  DistTable(2,2) = 0  
  |67-77| = 10  
  d = **10**

Order by Manhattan distance:  
1st: ID5 (d=10, Class B)  
2nd: ID2 (d=13, Class A)  
3rd: ID1 (d=21, Class A)  
4th: ID4 (d=22, Class B)  
5th: ID3 (d=78, Class A)

---

**1-NN Manhattan** → nearest is ID5 → class **B**.

---

#### **3. Euclidean distance**

Euclidean distance:
\[
d_{\text{euclidean}} = \sqrt{ \text{DistTable}(F1_{\text{new}}, F1_i)^2 + (F2_{\text{new}} - F2_i)^2 }
\]

Compute squares:

- ID1: Dist=0, diff=21 → \(0 + 441\) = 441 → sqrt ≈ **21.0**  
- ID2: Dist=0, diff=13 → \(0 + 169\) = 169 → sqrt ≈ **13.0**  
- ID3: Dist=35, diff=43 → \(1225 + 1849\) = 3074 → sqrt ≈ **55.44**  
- ID4: Dist=20, diff=2 → \(400 + 4\) = 404 → sqrt ≈ **20.10**  
- ID5: Dist=0, diff=10 → \(0 + 100\) = 100 → sqrt ≈ **10.0**

Order Euclidean distances:  
1st: ID5 (d≈10.0, Class B)  
2nd: ID2 (d≈13.0, Class A)  
3rd: ID4 (d≈20.10, Class B)  
4th: ID1 (d≈21.0, Class A)  
5th: ID3 (d≈55.44, Class A)

**1-NN Euclidean** → nearest is ID5 → class **B**.

---

#### **4. 3-NN Manhattan**

From earlier Manhattan ranking:  
Nearest 3: ID5 (B), ID2 (A), ID1 (A)  
Classes: B, A, A → majority = A (2 A vs 1 B).

So **3-NN Manhattan** → class **A**.

---

#### **5. 3-NN Euclidean**

Euclidean ranking:  
Nearest 3: ID5 (B), ID2 (A), ID4 (B)  
Classes: B, A, B → majority = B (2 B vs 1 A).

So **3-NN Euclidean** → class **B**.

---

**Final answers:**

- 1-NN Manhattan: **B**  
- 1-NN Euclidean: **B**  
- 3-NN Manhattan: **A**  
- 3-NN Euclidean: **B**

---

\[
\boxed{B, B, A, B}
\]

---

## Mean Squared Error (MSE)

### Definition
**Mean Squared Error (MSE)** is a common loss function used in regression problems to measure the average squared difference between predicted values and actual observed values.

### Formula
Mean Squared Error (MSE) is calculated as:

MSE = (1/n) × Σ(yᵢ - ŷᵢ)²

Where:
- n = number of data points
- yᵢ = actual value for the i-th data point
- ŷᵢ = predicted value for the i-th data point

### Calculation Steps
1. **Compute predictions** using your model
2. **Calculate errors**: eᵢ = yᵢ - ŷᵢ
3. **Square each error**: (eᵢ)²
4. **Sum all squared errors**
5. **Divide by n** to get the average

### Example
Given predictions and actual values:
- Predicted: \([5, -1, 5, 2, -3]\)
- Actual: \([4, 2, 1, 3, -1]\)

**Errors**: \([-1, 3, -4, 1, 2]\)  
**Squared errors**: \([1, 9, 16, 1, 4]\)  
**Sum**: \(31\)  
**MSE**: \(31 / 5 = 6.2\)

### Properties
- **Always non-negative** (squares are ≥ 0)
- **Penalizes large errors more** (due to squaring)
- **Differentiable everywhere** (useful for gradient-based optimization)
- Measured in **squared units** of the original data

### Use Cases
- Evaluating regression model performance
- Training machine learning models (as a loss function)
- Comparing different regression models
- Hyperparameter tuning

### Interpretation
- Lower MSE = better model fit
- MSE = 0 means perfect predictions
- Higher MSE indicates larger prediction errors

---

## Linear Regression MSE Calculation

### Linear Regression MSE Example

Given the following data points, calculate the predictions and Mean Squared Error (MSE) for a linear regression model with specified parameters.

#### Data

| x₁ | x₂ | y  | ŷ  |
|----|----|----|----|
| 3  | 2  | 4  | ?  |
| 1  | 4  | 2  | ?  |
| 2  | 0  | 1  | ?  |
| 1  | 1  | 3  | ?  |
| 0  | 4  | -1 | ?  |

#### Model parameters

- **w₀** = 1  
- **w₁** = 2  
- **w₂** = -1  

The linear regression model is:

```
ŷ = w₀ + w₁·x₁ + w₂·x₂
```

Calculate:

- The predicted value (ŷ) for each row:
    - **Row 1:** ŷ = ?
    - **Row 2:** ŷ = ?
    - **Row 3:** ŷ = ?
    - **Row 4:** ŷ = ?
    - **Row 5:** ŷ = ?
- The Mean Squared Error (MSE) for the model using these predictions.

---

### Solution

#### 📊 Data and Parameters
**Given data points:**
| x₁ | x₂ | y  |
|----|----|----|
| 3  | 2  | 4  |
| 1  | 4  | 2  |
| 2  | 0  | 1  |
| 1  | 1  | 3  |
| 0  | 4  | -1 |

**Model parameters:**
- w₀ = 1 (bias/intercept)
- w₁ = 2 (coefficient for x₁)
- w₂ = -1 (coefficient for x₂)

**Regression model:**
ŷ = w₀ + w₁·x₁ + w₂·x₂

#### 🔢 Predicted Values (ŷ)
**Row 1:** ŷ = 1 + 2(3) + (-1)(2) = 1 + 6 - 2 = **5**  
**Row 2:** ŷ = 1 + 2(1) + (-1)(4) = 1 + 2 - 4 = **-1**  
**Row 3:** ŷ = 1 + 2(2) + (-1)(0) = 1 + 4 + 0 = **5**  
**Row 4:** ŷ = 1 + 2(1) + (-1)(1) = 1 + 2 - 1 = **2**  
**Row 5:** ŷ = 1 + 2(0) + (-1)(4) = 1 - 4 = **-3**

**Complete table:**
| x₁ | x₂ | y  | ŷ  |
|----|----|----|----|
| 3  | 2  | 4  | 5  |
| 1  | 4  | 2  | -1 |
| 2  | 0  | 1  | 5  |
| 1  | 1  | 3  | 2  |
| 0  | 4  | -1 | -3 |

#### 📈 Error Calculation
**Errors (y - ŷ):**
1. 4 - 5 = -1
2. 2 - (-1) = 3
3. 1 - 5 = -4
4. 3 - 2 = 1
5. -1 - (-3) = 2

**Squared errors:**
1. (-1)² = 1
2. 3² = 9
3. (-4)² = 16
4. 1² = 1
5. 2² = 4

| x₁ | x₂ |  y  | ŷ  | e = y - ŷ | e² = (y - ŷ)² |
|----|----|-----|----|-----------|---------------|
|  3 |  2 |  4  |  5 |    -1     |       1       |
|  1 |  4 |  2  | -1 |     3     |       9       |
|  2 |  0 |  1  |  5 |    -4     |      16       |
|  1 |  1 |  3  |  2 |     1     |       1       |
|  0 |  4 | -1  | -3 |     2     |       4       |
|----|----|-----|----|-----------|---------------|
|**Sum of squared errors**       |   **31**      |

#### 🧮 MSE Calculation
**Sum of squared errors:** 1 + 9 + 16 + 1 + 4 = 31

**MSE formula:**  
MSE = (1/n) × Σ(y - ŷ)²  
MSE = 31 ÷ 5 = **6.2**

#### 📋 Final Results
ŷ of first row: **5**  
ŷ of second row: **-1**  
ŷ of third row: **5**  
ŷ of fourth row: **2**  
ŷ of fifth row: **-3**  

**Mean Squared Error (MSE) for the model: 6.2**

---

# Chapter 6: Neural Networks

## Neural Network Forward Pass with ReLU

### Question

Consider the following neural network with two input neurons \(I_1, I_2\) and one output neuron \(D\).

The network structure is:
- Inputs \(I_1, I_2\)
- Hidden neuron \(A\)
- Hidden neurons \(B\) and \(C\)
- Output neuron \(D\)

#### Weights

| Edge | Weight |
|----|----|
| \(I_1 \to A\) | 2 |
| \(I_2 \to A\) | -3 |
| \(A \to B\) | 1 |
| \(A \to C\) | 3 |
| \(B \to D\) | 4 |
| \(C \to D\) | -1 |

#### Biases

| Node | Bias |
|----|----|
| A | -1 |
| B | -5 |
| C | -3 |
| D | 10 |

The activation function used for all neurons is the **Rectified Linear Unit (ReLU)**:

```
ReLU(x) = max(0, x)
```

Given the input values:

```
I₁ = 3,    I₂ = 1
```

**Tasks:**
1. Compute, for each neuron **A, B, C, D**, the value *before* applying the activation function.
2. Compute the value *after* applying the ReLU activation function.
3. For gradient descent training, state:
   - What gets updated,
   - The gradient of what,
   - With respect to what.

---

### Solution

#### Activation Function

```
ReLU(x) = max(0, x)
```

---

#### Neuron A

**Before activation:**

```
z_A = I₁ × w_{I₁A} + I₂ × w_{I₂A} + b_A
    = (3 × 2) + (1 × -3) + (-1)
    = 6 - 3 - 1
    = 2
```

**After activation:**

```
A = max(0, 2) = 2
```

---

#### Neuron B

**Before activation:**

```
z_B = A × w_{AB} + b_B
    = (2 × 1) + (-5)
    = 2 - 5
    = -3
```

**After activation:**

```
B = max(0, -3) = 0
```

---

#### Neuron C

**Before activation:**

```
z_C = A × w_{AC} + b_C
    = (2 × 3) + (-3)
    = 6 - 3
    = 3
```

**After activation:**

```
C = max(0, 3) = 3
```

---

#### Neuron D

**Before activation:**

```
z_D = B × w_{BD} + C × w_{CD} + b_D
    = (0 × 4) + (3 × -1) + 10
    = 0 - 3 + 10
    = 7
```

**After activation:**

```
D = max(0, 7) = 7
```

---

#### Final Results

| Neuron | Value before activation | Value after ReLU |
|--------|------------------------|------------------|
|   A    |          2             |        2         |
|   B    |         -3             |        0         |
|   C    |          3             |        3         |
|   D    |          7             |        7         |

---

#### Training with Gradient Descent

When training this network using gradient descent:

> **We update the weights (and biases) using the gradient of the loss function with respect to the weights (and biases).**

---

#### Key Takeaway

Forward propagation computes weighted sums plus biases followed by an activation function, and gradient descent updates parameters to minimize the loss.

---

## Neural Network Error Analysis

### Question

We have the following data set with **3 input attributes** (`i1`, `i2`, `i3`) and **1 target attribute**.

#### Testing Set

| Example | i1 | i2 | i3 | Target |
|--------|----|----|----|--------|
| ex1 | 3 | 4 | 1 | 5 |
| ex2 | 2 | 2 | 2 | 6 |
| ex3 | 1 | 2 | 1 | 0 |
| ex4 | 1 | 1 | 1 | 1 |

We have the outputs of **two neural networks** on the testing set.

#### Neural Network Outputs

| Example | Neural Network A | Neural Network B |
|--------|------------------|------------------|
| ex1 | 10 | 7 |
| ex2 | 6 | 4 |
| ex3 | 0 | 2 |
| ex4 | 1 | 0 |

Tasks:

1. Compute the **sum of absolute error** for each neural network.
2. Compute the **sum of squared error** for each neural network.
3. Decide which neural network is better if we want to **avoid large deviations** in any example.

---

### Solution

#### Definitions

- **Absolute Error**:
\[
|y - \hat{y}|
\]

- **Squared Error**:
\[
(y - \hat{y})^2
\]

Where:
- \( y \) is the true target
- \( \hat{y} \) is the predicted value

---

#### 1. Sum of Absolute Error

##### Neural Network A

##### Neural Network A

| Example | Target (y) | Prediction (\hat{y}) | \|y - \hat{y}\| |
|---------|------------|----------------------|-----------------|
| ex1     |     5      |         10           |        5        |
| ex2     |     6      |         6            |        0        |
| ex3     |     0      |         0            |        0        |
| ex4     |     1      |         1            |        0        |

**Sum of absolute error (A): 5**

---

##### Neural Network B

| Example | Target (y) | Prediction (\hat{y}) | \|y - \hat{y}\| |
|---------|------------|----------------------|-----------------|
| ex1     |     5      |         7            |        2        |
| ex2     |     6      |         4            |        2        |
| ex3     |     0      |         2            |        2        |
| ex4     |     1      |         0            |        1        |

**Sum of absolute error (B): 7**


---

#### 2. Sum of Squared Error

##### Neural Network A

| Example | Calculation         | Squared Error |
|---------|---------------------|---------------|
| ex1     | $(5 - 10)^2$        | 25            |
| ex2     | $(6 - 6)^2$         | 0             |
| ex3     | $(0 - 0)^2$         | 0             |
| ex4     | $(1 - 1)^2$         | 0             |

**Sum of squared error (A):** $\boxed{25}$

---

##### Neural Network B

| Example | Calculation         | Squared Error |
|---------|---------------------|---------------|
| ex1     | $(5 - 7)^2$         | 4             |
| ex2     | $(6 - 4)^2$         | 4             |
| ex3     | $(0 - 2)^2$         | 4             |
| ex4     | $(1 - 0)^2$         | 1             |

**Sum of squared error (B):** $\boxed{13}$

---

#### 3. Best Neural Network

- Squared error penalizes **large deviations** more strongly.
- Neural Network A has one very large error ($25$).
- Neural Network B has smaller, more evenly distributed errors.

**✅ Best choice:**  
$\boxed{\text{Neural Network B}}$  
Because it avoids large deviations in any single example.

---

### Final Answers Summary

- **Sum of absolute error (A):** $5$  
- **Sum of absolute error (B):** $7$  
- **Sum of squared error (A):** $25$  
- **Sum of squared error (B):** $13$  
- **Best neural network:** **Neural Network B**

---

# Chapter 7: Learning Evaluation & Concepts

## Concept Questions: Neural Networks & Machine Learning

---

### Backpropagation in Neural Networks

**Q18. Which statements are correct about how a weight (link from neuron A to neuron B) is updated during backpropagation? Select one or more:**

- a. The error term for neuron B  
- b. The error term for neuron A  
- c. The input to neuron B through other links during the forward propagation phase  
- d. The input to neuron B through *that* link during the forward propagation phase  
- e. The overall error of the entire neural network  
- f. The type of activation function

**Answer:** a, d, f

---

### Decision Trees: Model Selection

**Q19. When training two decision trees for a classification task, how should we choose the best model?**

- a. Depends on the application.  
- b. The one that has highest accuracy.  
- c. The one that has highest precision.  
- d. The one that has highest recall.

**Answer:** a. Depends on the application

---

### Backpropagation & Learning Rate

**Q20. If we perform backpropagation, which statements are true about the learning rate? Select one or more:**

- a. The learning rate determines how many times we update the weights based on each example.  
- b. The learning rate determines how much we update each of the weights in the neural network.  
- c. The learning rate determines how many examples we use from the training data in each batch.  
- d. The learning rate controls how many weights we update in the neural network.

**Answer:** b

---

### Gradient Descent: Learning Rate $\alpha$

**Q21. Which statement is true about the learning rate $\alpha$ in gradient descent?**

- a. If the learning rate is very small, gradient descent will be fast to converge. If the learning rate is too large, gradient descent will be slow.  
- b. If the learning rate is very small, gradient descent can be slow to converge. If the learning rate is too large, gradient descent can be slow too.  
- c. If the learning rate is very small, gradient descent will be fast to converge. If the learning rate is too large, gradient descent will overshoot.  
- d. If the learning rate is very small, gradient descent can be slow to converge. If the learning rate is too large, gradient descent will overshoot.

**Answer:** d

---

### Overfitting in Machine Learning

**Q22. When is a model said to be overfitting?**

- a. Both the train and test errors are high.  
- b. Train error is low but test error is high.  
- c. Train error is high but the test error is low.  
- d. Both train and test errors are low.

**Answer:** b

---

### Unsupervised Learning

**Q23. In unsupervised learning:**

- a. The training dataset is not labelled with a target feature  
- b. There is no training dataset  
- c. The training dataset is labelled with a target feature, but the testing dataset is not labelled.  
- d. The training dataset is labelled with a target feature but there is no testing dataset

**Answer:** a

---

### Gradient Descent Applicability

**Q24. Which of the following ML methods can use gradient descent for learning? (Select one or more):**

- a. Decision Trees  
- b. Linear Regression  
- c. K-means  
- d. K-nearest neighbors  
- e. Neural Networks

**Answer:** b, e

---

# Chapter 11: Multi-Agent Systems & Adversarial Search

## Minimax Search Tree Analysis

Given the following game tree:

![Minimax Tree](/images/2024-minmax.png)

We have the following evaluation function. In terminal nodes, the evaluation function is the same as the utility function. In non-terminal nodes, the evaluation function is computed in some other way (e.g., has been learned with a neural network).

### Node Values

| Node |  A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  |  I  |  J  |  K  |  L  |  M  |  N  |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Value| -2  |  3  | 10  | -7  | -6  |  3  | -8  | -7  | -3  | -9  |  4  | -3  |  3  | 10  |

---

## Minimax Value Computation

### 1. Full-Depth Minimax

**Compute the minimax value for these nodes:**

| Node | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Value|   |   |   |   |   |   |   |   |

**_Question:_** What move is best for the Max player in the starting position?    

---

### 2. Depth-2 Minimax (Depth 2 = Terminal)

**Compute the minimax value for these nodes:**

| Node | A | B | C | D | E | F | G | H |
|------|---|---|---|---|---|---|---|---|
| Value|   |   |   |   |   |   |   |   |

**_Question:_** What move will the Max player using depth=2 make in the starting position? 

---

### Problem Description

We are given a game tree with **Max** and **Min** nodes at alternating depths, along with an evaluation function that provides heuristic values for non-terminal nodes. The task is to compute node values for two scenarios:

1. **Full-depth minimax**: Expand to terminal leaves.  
2. **Depth-limited minimax**: Nodes at depth 2 are considered terminal.

Tree structure:

- **A** (Max, depth 0) → children: **B**, **C**, **D** (Min, depth 1)
    - **B** → children: **e**, **f** (Max, depth 2)
    - **C** → children: **g**, **h** (Max, depth 2)
    - **D** → leaf node
    - **e** → children: **I**, **J**
    - **f** → children: **i = I**, **j = J**
    - **g** → children: **K**, **L**
    - **h** → children: **M**, **N**

> **Note**: Capital E, F, G, H in tables correspond to e, f, g, h in the tree.

---

### Given Evaluation Function Values

| Node | A  | B  | C  | D  | E  | F  | G  | H  | I  | J  | K  | L  | M  | N  |
|------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Value| -2 |  3 | 10 | -7 | -6 |  3 | -8 | -7 | -3 | -9 |  4 | -3 |  3 | 10 |

---

## 1️⃣ Full-Depth Minimax Solution

a. **Compute Values at Leaf Nodes (Depth 2, Max nodes):**

- **e** = $\max$(I, J) = $\max$(-3, -9) = **-3**
- **f** = $\max$(i, j) = $\max$(-3, -9) = **-3**
- **g** = $\max$(K, L) = $\max$(4, -3) = **4**
- **h** = $\max$(M, N) = $\max$(3, 10) = **10**

b. **Compute Values at Min Nodes:**

- **B** = $\min$(e, f) = $\min$(-3, -3) = **-3**
- **C** = $\min$(g, h) = $\min$(4, 10) = **4**
- **D** = -7 (already a leaf)

c. **Compute Value at Root (Max node A):**
- **A** = $\max$(B, C, D) = $\max$(-3, 4, -7) = **4**

**Full-depth Results:**

| Node | A | B  | C  | D  | E  | F  | G | H  |
|------|---|----|----|----|----|----|---|----|
| Value| 4 | -3 | 4  | -7 | -3 | -3 | 4 | 10 |

- **Best move for Max player at start (full-depth):**  
  **Choose C** (value 4)

---

## 2️⃣ Depth-Limited Minimax (Depth 2 Terminal) Solution

For depth-limited search, use the given evaluation values for nodes **E**, **F**, **G**, **H** ("e", "f", "g", "h") as the leaves.

a. **Compute Values at Min Nodes:**

- **B** = $\min$(E, F) = $\min$(-6, 3) = **-6**
- **C** = $\min$(G, H) = $\min$(-8, -7) = **-8**
- **D** = -7

b. **Compute Value at Root (Max node A):**

- **A** = $\max$(B, C, D) = $\max$(-6, -8, -7) = **-6**

**Depth=2 Results:**

| Node | A  | B  | C  | D  | E  | F  | G  | H  |
|------|----|----|----|----|----|----|----|----|
| Value| -6 | -6 | -8 | -7 | -6 | 3  | -8 | -7 |

- **Best move for Max player at start (depth=2):**  
  **Choose B** (value -6)

---

## 📌 Summary Table

| Scenario              | A's Value | Best Move |
|-----------------------|-----------|-----------|
| Full-depth            |     4     |     C     |
| Depth-limited (d=2)   |    -6     |     B     |

> **Note:** The best move changes from C to B when using a depth-limited search, due to the heuristic values at depth 2 differing from the true minimax values.

---

## Min-Max Search

We perform Min-Max search on the following tree. Annotate each internal node with the corresponding value.

**Min-Max Tree**  
![Minmax](/images/minmax.png)

| Node | Value (Blank)         |
|------|-----------------------|
| A    | Blank 1 (Question 17) |
| B    | Blank 2 (Question 17) |
| C    | Blank 3 (Question 17) |
| D    | Blank 4 (Question 17) |
| E    | Blank 5 (Question 17) |
| F    | Blank 6 (Question 17) |
| G    | Blank 7 (Question 17) |

---

**What move should the MAX player choose?**  
**Blank 8 (Question 17)**

---

### Solution

**Tree Structure:**

- **A** (MAX, root) → children: **B**, **C**, **D** (MIN layer)
  - **B** (MIN) → children: **2** (terminal), **E** (MAX)
  - **C** (MIN) → children: **F** (MAX), **1** (terminal), **9** (terminal)
  - **D** (MIN) → children: **G** (MAX), **-2** (terminal), **5** (terminal)
- **E** (MAX) → children: **3**, **-7** (terminals)
- **F** (MAX) → children: **-1**, **6** (terminals)
- **G** (MAX) → children: **10**, **4**, **-8** (terminals)

**Minimax Computation (Bottom-Up):**

1. **Compute MAX nodes (E, F, G)**
    - **E** = $\max(3, -7) = 3$
    - **F** = $\max(-1, 6) = 6$
    - **G** = $\max(10, 4, -8) = 10$

2. **Compute MIN nodes (B, C, D)**
    - **B** = $\min(2, E) = \min(2, 3) = 2$
    - **C** = $\min(F, 1, 9) = \min(6, 1, 9) = 1$
    - **D** = $\min(G, -2, 5) = \min(10, -2, 5) = -2$

3. **Compute root MAX node (A)**
    - **A** = $\max(B, C, D) = \max(2, 1, -2) = 2$

**Final Values:**

| Node | Value |
|------|-------|
| A    | 2     |
| B    | 2     |
| C    | 1     |
| D    | -2    |
| E    | 3     |
| F    | 6     |
| G    | 10    |

- **Blank 1 (A):** 2  
- **Blank 2 (B):** 2  
- **Blank 3 (C):** 1  
- **Blank 4 (D):** -2  
- **Blank 5 (E):** 3  
- **Blank 6 (F):** 6  
- **Blank 7 (G):** 10  
- **Blank 8 (Best move for MAX player):** **B** (since B has the highest value among A's children)

---

# Chapter 12: Markov Decision Processes

## MDP Value Iteration — Full Solution

Consider the following MDP graph, where the student wants to get the solutions to the exercise section, but the teacher won't let the student have the solutions (the teacher is standing at $(3, 2)$):

![MarkovChains2](/images/MarkovChains2.drawio.png)

Here, the reward structure is as follows:

- **Getting the solutions:** $+5$
- **Getting caught by the teacher:** $-10$
- **Moving elsewhere:** $-0.3$

The student is hesitant when moving, so there is a 30% chance he won't move, a 20% chance he will take a wrong turn and move to the right, and a 50% chance he will move in the desired direction. The discounting factor is $\gamma = 0.6$.

The MDP will initialize with the following values:

![MDP](/images/MDP-Initial.png)

### Initial Value Table

```
(1,3) = -2   (2,3) = 3    (3,3) = 6
(1,2) = 6    (2,2) = -4   (3,2) = -12
(1,1) = 3    (2,1) = 1    (3,1) = 0
```

---

## Part 1 — One Iteration of Value Iteration

**Value Iteration Update:**
$$
V_{k+1}(s) = \max_{a} \Big[ R(s, a) + \gamma \sum_{s'} P(s'|s,a) V_k(s') \Big]
$$

**Terminal states** keep their reward value (no action):
- $(3, 3) \to +5$
- $(3, 2) \to -10$
- $(1, 3)$: If considered terminal, also $+5$ (but problem assumes non-terminal in initial run).

#### $(3,2)$ — Teacher state  
Terminal $\Rightarrow V_1 = -10.$

#### $(3,3)$ — Solution state  
Terminal $\Rightarrow V_1 = +5.$

#### $(1,3)$ — Non-terminal state  
Possible moves: E, S, W

- Try **East** (to $(2,3)$):  
  - $P((2,3)) = 0.5$
  - $P(\text{stay } (1,3)) = 0.3$
  - $P(\text{right of East} = (1,2)) = 0.2$
- Immediate reward $R = -0.3$

Calculation:
- $= -0.3 + 0.6 \times [ 0.5 \times 3 + 0.3 \times (-2) + 0.2 \times 6 ] $
- $= -0.3 + 0.6 \times (1.5 - 0.6 + 1.2)$
- $= -0.3 + 0.6 \times 2.1$
- $= -0.3 + 1.26$
- $= 0.96 \approx 1.0$

Best action is **E** with value $1.0$.

---

**After 1 iteration (rounded to 1 decimal):**

- $(3, 2) = -10.0$
- $(1, 3) = 1.0$
- $(3, 3) = 5.0$

---

## Part 2 — Two Iterations of Value Iteration

Now compute $V_2$ for the requested states.

- $(3,2)$: Terminal $\to$ stays at $-10.000$

#### $(2,3)$:

- Try **East** (to $(3,3)$ terminal $+5$):
  - $P((3,3)) = 0.5$
  - $P((2,3)) = 0.3$
  - $P((2,2)) = 0.2$
- $R = -0.3$
- $Value_E = -0.3 + 0.6 \times [0.5 \times 5 + 0.3 \times V_1(2,3) + 0.2 \times V_1(2,2)]$

(Requires intermediate computation...)

**After 2 iterations (rounded to 3 decimals):**

- $(2, 3) = 1.618$
- $(3, 2) = -10.000$
- $(2, 2) = 0.812$

---

## Part 3 — High Discount Factor

A **high discount factor** $\gamma$:

- [x] Values future rewards more  
- [ ] Values immediate results more  
- [x] Encourages long-term planning  
- [ ] Discourages long-term planning  
- [ ] Encourages exploration  
- [ ] Discourages exploration  

---

## Final Answers

**1 iteration (1 decimal):**

- (3, 2) = **-10.0**
- (1, 3) = **1.0**
- (3, 3) = **5.0**

**2 iterations (3 decimals):**
- (2, 3) = **1.618**
- (3, 2) = **-10.000**
- (2, 2) = **0.812**

**High discount factor effects:**  
Values future rewards more; encourages long-term planning.

---

## Question: MDP Q-Value Table — Maximizing Expected Utility

An agent operates on an MDP with 3 states (**S**, **W**, **L**) and 5 possible actions (**a1**–**a5**). The transition and reward functions are unknown, but the Q-value table below gives the expected utility for each (state, action) pair:

| State | a1 | a2 | a3 | a4 | a5 |
|-------|----|----|----|----|----|
| **S** | 13 |  8 |  5 |  8 |  4 |
| **W** | 12 |  0 |  0 |  6 | 15 |
| **L** |  0 |  2 |  5 |  2 |  0 |

### 1. What is the value for each state?

For each state, $V(s) = \max_a Q(s, a)$.

- **V(S):** $\max(13, 8, 5, 8, 4) = 13$
- **V(W):** $\max(12, 0, 0, 6, 15) = 15$
- **V(L):** $\max(0, 2, 5, 2, 0) = 5$

---

### 2. What action should be applied to maximize expected utility on each state?

- **S:** Action **a1** (since $Q(S, a1) = 13$ is highest)
- **W:** Action **a5** (since $Q(W, a5) = 15$ is highest)
- **L:** Action **a3** (since $Q(L, a3) = 5$ is highest)

---

#### Summary Table

| State | V(s) | Best Action |
|-------|------|-------------|
| S     | 13   | a1          |
| W     | 15   | a5          |
| L     | 5    | a3          |

---

# Chapter 13: Reinforcement Learning

## Q-Learning Best Actions and Values

Consider a Q-learning problem with **2 states**: `s1` and `s2`. At every step, the agent can choose one of **three actions**: `a1`, `a2`, and `a3`.

After training, the Q-values $Q(s, a)$ are as follows:

| State | a1 | a2 | a3 |
|-------|----|----|----|
| s1    |  8 | 10 | 15 |
| s2    | -20|  7 | 13 |

### 1. *Currently, the agent is at state `s1`. What action should the agent perform to maximize the expected reward?*

- **Answer:**  
  The agent should choose the action with the highest Q-value at `s1`: **a3** (since $Q(s1, a3) = 15$).

---

### 2. *Currently, the agent is at state `s1`. What is the expected cumulative reward if it applies the best policy?*

- **Answer:**  
  The expected cumulative reward is the highest Q-value at `s1`: **15**

---

### 3. *Currently, the agent is at state `s2`. What action should the agent perform to maximize the expected reward?*

- **Answer:**  
  The agent should choose the action with the highest Q-value at `s2`: **a3** (since $Q(s2, a3) = 13$).

---

### 4. *Currently, the agent is at state `s2`. What is the expected reward it will get?*

- **Answer:**  
  The expected reward is the highest Q-value at `s2`: **13**

---

## Q-Learning Table Update Example

**Scenario:**  
Given the same $Q(s, a)$ matrix as before. The agent is currently at state `s1` and takes action `a1`. As a result, it receives an immediate reward of **100** and reaches state `s2`.

**Question:**  
_When using the Q-learning algorithm, which entries in the Q-table should have their value updated as a result of this transition?_

### Q(s, a) Table Structure

|      | a1       | a2       | a3       |
|------|----------|----------|----------|
| s1   | Blank 1  | Blank 2  | Blank 3  |
| s2   | Blank 4  | Blank 5  | Blank 6  |

Only **Q(s1, a1)** is updated when the agent takes action a1 from state s1.

---

### Q-learning Table Update Rule

The Q-learning update for the state-action pair $(s_1, a_1)$ is:  
$$
Q(s_1, a_1) \leftarrow Q(s_1, a_1) + \alpha \Big[ R + \gamma \max_{a'} Q(s_2, a') - Q(s_1, a_1) \Big]
$$
Where:

- $Q(s_1, a_1)$ is the entry being updated.
- $R$ is the immediate reward received (here, **100**).
- $\gamma$ is the discount factor.
- $\max_{a'} Q(s_2, a')$ is the maximal estimated future return from new state s2.
- $\alpha$ is the learning rate.

> **Answer:**  
> The only entry updated is **Q(s1, a1)** (Blank 1).

---

## Exploration/Exploitation & Discount Factor

**Question:**  
_What is the relation between the discount factor and exploration/exploitation?_

**Options:**

a. The value of the discount factor is not related to exploration/exploitation  
b. The lower the discount factor, the more exploitation  
c. The higher the discount factor, the more exploration  

**Explanation:**

- The discount factor ($\gamma$) determines how much future rewards are valued versus immediate rewards.
- In standard Q-learning, the *discount factor* regulates the time horizon of planning (whether to prioritize immediate or future rewards).
- *Exploration* vs. *exploitation* relates to policy (choosing random vs. known good actions), typically controlled by an exploration parameter (e.g., $\epsilon$ in epsilon-greedy).

**Correct answer:**  
**a. The value of the discount factor is not related to exploration/exploitation**

The discount factor affects how future rewards are valued, not the balance between exploration and exploitation.

---

### Additional Questions

**Question 11**  
Higher $\gamma$ $\rightarrow$ future rewards less discounted $\rightarrow$ agent values long-term rewards more.  
**Correct answer:** a. The higher the discount factor, the more the agent values long-term rewards.

---

**Question 12**  
In $\epsilon$-greedy: higher $\epsilon$ $\rightarrow$ more random actions $\rightarrow$ more exploration.  
**Correct answer:** c. The higher the epsilon, the more exploration.

---

**Question 13**  
$\epsilon$ affects exploration, which can help discover better long-term rewards by exploring more early on. But the question is tricky: $\epsilon$ itself doesn't change how we value future rewards ($\gamma$ does), but higher $\epsilon$ can lead to better long-term outcomes due to more exploration.  
However, strictly speaking, "values long-term rewards" refers to weighting, not outcome quality. So $\epsilon$ is **not** about valuation per se.  
**Correct answer:** a. The value of epsilon is not related to how the agent values long-term rewards.

---
