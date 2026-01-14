# Constraint Satisfaction Problems (CSP) – Exam Study Notes

## Table of Contents

1. [Basic Concepts](#basic-concepts)
2. [CSP Formal Definition](#csp-formal-definition)
3. [Solving Methods](#solving-methods)
4. [Exercises with Solutions](#exercises-with-solutions)
5. [Common Exam Questions](#common-exam-questions)
6. [Important Theorems & Properties](#important-theorems--properties)
7. [Practice Problems](#practice-problems)
8. [Memory Aid](#memory-aid)

---

## 1. Basic Concepts

### Key Definitions

- **Variable (V):** A feature of the problem that can take different values.
- **Domain (D):** The set of possible values for a variable.
- **Constraint (C):** A restriction on allowed combinations of variable values.
- **Assignment:** A mapping of variables to values from their domains.
- **Solution:** A complete assignment satisfying all constraints.

### CSP Components

A CSP can be described as:

$$
\text{CSP} = (V, D, C)
$$

Where:
- $V = \{v_1, v_2, ..., v_n\}$ (variables)
- $D = \{D_1, D_2, ..., D_n\}$ (domains for each variable)
- $C =$ set of constraints

---

## 2. CSP Formal Definition

### Binary CSP

**Formal representation:**
```python
# CSP as a tuple:
γ = (V, D, C)
# V: Finite set of variables {v₁, v₂, ..., vₙ}
# D: Set of domains {D₁, D₂, ..., Dₙ} where Dᵢ is finite
# C: Set of constraints (typically binary: Cᵢⱼ ⊆ Dᵢ × Dⱼ)
```

#### Example: Map Coloring

- **Variables:** {WA, NT, SA, Q, NSW, V, T}
- **Domains:** All {red, green, blue}
- **Constraints:** For all adjacent $(u, v): C_{uv} = \{(d, d') | d \neq d'\}$

---

## 3. Solving Methods

### 3.1 Backtracking Search

```python
def backtracking(a, γ):
    if is_inconsistent(a):
        return None
    if is_complete(a):
        return a
    
    v = select_unassigned_variable(a, γ)
    for d in order_domain_values(v, γ):
        a_prime = a ∪ {v = d}
        result = backtracking(a_prime, γ)
        if result is not None:
            return result
    return None
```
**Properties:**
- **Complete:** Will find a solution if one exists.
- **Exponential worst-case complexity:** $O(d^n)$, where $d$ = domain size, $n$ = #variables.
- Better than full enumeration but can still be inefficient.

---

### 3.2 Arc Consistency (AC-3 Algorithm)

```python
def AC3(γ):
    queue = all arcs in γ
    while queue not empty:
        (Xi, Cij) = queue.pop()
        if revise(γ, Xi, Cij):
            if Di is empty: return False
            for each Xk where Cki exists and k ≠ j:
                queue.add( (Xk, Cki) )
    return True

def revise(γ, Xi, Cij):
    revised = False
    for x in Di:
        if no y in Dj with (x, y) ∈ Cij:
            remove x from Di
            revised = True
    return revised
```
- **Runtime:** $O(ed^3)$, where $e$ = number of constraints, $d$ = domain size.

---

### 3.3 Variable Elimination

**Steps:**
1. Pick a variable $X$ to eliminate.
2. **Join:** Combine all constraints involving $X$.
3. **Project:** Project result onto remaining variables.
4. Add new constraint to the set.
5. Repeat until one constraint remains.

**Operations:**
- **Join $(\Join)$:** Combine constraints (like relational join).
- **Projection $(\pi)$:** Remove columns, eliminate duplicates.

---

## 4. Exercises with Solutions

### Exercise 1: Basic CSP Formulation

**Problem:** Model the 4-Queens problem as a CSP.

**Solution:**
```python
# Variables: Q₁, Q₂, Q₃, Q₄ (queen in each column)
# Domains: {1,2,3,4} (row positions)
# Constraints:
# 1. No two queens in same row: Qᵢ ≠ Qⱼ for all i ≠ j
# 2. No two queens on same diagonal: |i - j| ≠ |Qᵢ - Qⱼ|
```

---

### Exercise 2: Map Coloring Consistency

**Problem:**  
Given Australian map coloring with:  
- WA = red, NT = green, SA = ?  
- Domains: {red, green, blue}  
- Constraint: Adjacent regions must have different colors.

Is the partial assignment {WA=red, NT=green} consistent? Can it be extended?

**Solution:**
- **Check consistency:** WA ≠ NT: red ≠ green ✓ (consistent so far)
- **Check extensibility:** SA ≠ WA (red) and ≠ NT (green) ⇒ only option: SA=blue  
- Continue checking other regions as needed.  
**Conclusion:** Yes, extensible to a full solution.

---

### Exercise 3: Arc Consistency Application

**Problem:**  
Apply arc consistency to:  
- Variables: $X, Y, Z$
- Domains: $D_x = D_y = D_z = \{1,2,3\}$
- Constraints: $X < Y,\ Y < Z$

**Solution Steps:**
1. **Revise(X, X<Y):**
    - X=1: Y in {2,3} ✓
    - X=2: Y in {3} ✓
    - X=3: no $Y>3$ ✗ → remove 3 from $D_x \rightarrow D_x = \{1,2\}$
2. **Revise(Y, X<Y):**
    - Y=1: no $X<1$ ✗ → remove 1 from $D_y$
    - Y=2: X in {1} ✓
    - Y=3: X in {1,2} ✓
    - $D_y = \{2,3\}$
3. **Revise(Y, Y<Z):**
    - Y=2: Z in {3} ✓
    - Y=3: no $Z>3$ ✗ → remove 3 from $D_y \rightarrow D_y = \{2\}$
4. **Revise(Z, Y<Z):**
    - Z=1,2: no $Y<z$ ✗ → remove 1,2 from $D_z$
    - Z=3: Y in {2} ✓
    - $D_z = \{3\}$
5. **Revise(X, X<Y) again:**
    - X=1: Y=2 ✓
    - X=2: Y=2 ✗ → remove 2 from $D_x \rightarrow D_x = \{1\}$

**Final domains:** $D_x = \{1\}$, $D_y = \{2\}$, $D_z = \{3\}$

---

### Exercise 4: Variable Elimination

**Problem:** Eliminate variable $B$ from:
- Constraints:  
    $C_1$: $A ≠ B = \{(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)\}$  
    $C_2$: $B < C = \{(1,2), (1,3), (2,3)\}$  
    Domains: $A,B,C \in \{1,2,3\}$

**Solution:**
1. **Join $C_1$ and $C_2$ on $B$:**
    - $Join = \{(A,B,C) | (A,B) \in C_1, (B,C) \in C_2\}$
    - E.g., $(A=1, B=2, C=3)$, etc.
2. **Project onto $A$ and $C$:**
    - $\pi(A,C) = \{(1,3), (2,2), (2,3), (3,2), (3,3)\}$
3. **New constraint:** $C' = \{(1,3), (2,2), (2,3), (3,2), (3,3)\}$

---

## 5. Common Exam Questions

### Question Type 1: Modeling

> **Q:** Model the following as a CSP: “Schedule 3 courses (A,B,C) in 2 time slots (1,2) with constraints: A and B cannot be together, C must be in slot 2.”

**Answer:**
- **Variables:** $A, B, C$
- **Domains:** $\{1,2\}$ for all
- **Constraints:**
    1. $A \neq B$
    2. $C = 2$

---

### Question Type 2: Consistency Checking

> **Q:** Given CSP with $X,Y\in\{0,1\}$, constraint $X \neq Y$, and partial assignment $\{X=0\}$. Is this consistent? Extensible?

**Answer:**
- **Consistent:** No constraint violation yet.
- **Extensible:** Yes, set $Y=1$ gives a solution.

---

### Question Type 3: Algorithm Analysis

> **Q:** What is time complexity of AC-3 algorithm?

**Answer:**
- $O(ed^3)$ where:
    - $e$ = number of arcs/constraints
    - $d$ = maximum domain size

---

### Question Type 4: Constraint Graph Properties

> **Q:** A CSP has constraint graph that is a tree. What is complexity of solving it?

**Answer:**
- $O(nd^2)$ using directed arc consistency + backtracking.
- Polynomial time solvable.

---

## 6. Important Theorems & Properties

- **Theorem 1: Disconnected Components**  
  If constraint graph has disconnected components, they can be solved independently.

- **Theorem 2: Acyclic Constraint Graphs**  
  A CSP with acyclic constraint graph can be solved in $O(nd^2 + n^2 d)$ time.

- **Theorem 3: Arc Consistency ≠ Solution Existence**  
  A CSP can be arc consistent but have no solution.

  **Example:**  
  - Variables: $A, B, C$ with domains $\{0,1\}$
  - Constraints: $A \neq B$, $B \neq C$, $A \neq C$
  - Arc consistent, but no solution for 3 variables with 2 colors.

- **Theorem 4: Cutset Conditioning**  
  By instantiating a cutset of variables to make graph acyclic, we can solve remaining CSP efficiently.

---

## 7. Practice Problems

### Problem 1: Sudoku CSP

**Formulate a $4 \times 4$ Sudoku as CSP. How many variables? Constraints?**

**Solution Template:**
- **Variables:** $v_{ij}$ for $i,j \in \{1,2,3,4\}$
- **Domains:** $\{1,2,3,4\}$
- **Constraints:**
    1. Row: $v_{ij} \neq v_{ik}$ for $j \neq k$
    2. Column: $v_{ij} \neq v_{kj}$ for $i \neq k$
    3. Block: $2\times2$ blocks must all differ

---

### Problem 2: N-Queens Complexity

For $N$-Queens problem with $N=8$:
- **How many variables?** 8 (one per column)
- **Domains?** $\{1,\dots,8\}$ (row positions)
- **How many binary constraints?** Approximately $O(N^2)$ pairwise constraints

---

### Problem 3: Map Coloring

Color this map with 3 colors:
```
  A -- B -- C
  |    |
  D -- E
```
**Find all solutions:**
- Try $A = $red, $B =$ green
- $C \neq B \to C \in \{$red, blue$\}$
- $D \neq A \to D \in \{$green, blue$\}$
- $E \neq B$ and $E \neq D \to$ determine $E$
- **Backtrack if needed**

---

## 8. Memory Aid

**CSP Mnemonic:** *"Very Delicious Cookies"*
- Variables
- Domains
- Constraints

### Algorithm Summary

- **Backtracking:** Try & backtrack
- **AC-3:** Make arcs consistent
- **VE:** Eliminate variables
- **Local Search:** Hill climb with restarts

### Common Pitfalls

- Confusing consistency with extensibility
- Forgetting to propagate after domain reduction
- Missing constraints when modeling
- Assuming arc consistency means solution exists
