# Bayesian Network Exercise – Complete Solution

## Problem Statement

We are given a Bayesian Network that predicts whether a user will buy a product, based on several product characteristics.

### Variables and their Domains

| Variable | Values (Domain)                   | Meaning                           |
|----------|----------------------------------|-----------------------------------|
| Q        | very poor, poor, average, good, very good | Quality of the product         |
| S        | small, medium, big               | Size of the product                |
| C        | red, blue, green, yellow         | Color of the product               |
| P        | cheap, expensive, luxury         | Price of the product               |
| B        | yes, no                          | Whether the user will buy the product |

### Network Structure

![Bayesian Network Diagram](/images/2024-bn.png)

- Q → S, Q → P, Q → B
- S → P, S → B
- C → S, C → B
- P → B

---

## Question 1: CPT (Conditional Probability Table) Specifications

For each node in the Bayesian Network, specify:
1. The probability table it must store (its meaning)
2. The number of entries in its table

**Note:** Use the format like `P(X|Y,Z)` (no spaces).  
Count *all* rows (even if some can be derived from others).

---

### Solution

#### Step 1: Identify Parents for Each Node

- **Q**: no parents (root)
- **C**: no parents (root)
- **S**: parents = Q, C
- **P**: parents = Q, S
- **B**: parents = Q, S, C, P

#### Step 2: Calculate Table Size for Each Node

- **Q:**  
  - Table:  P(Q)  
  - Domain(Q) = 5  
  - Number of entries = 5

- **C:**  
  - Table:  P(C)  
  - Domain(C) = 4  
  - Number of entries = 4

- **S:**  
  - Table:  P(S|Q,C)  
  - Parents: Q (5), C (4) → 5×4 = 20 conditionings  
  - Domain(S) = 3  
  - Number of entries = 3 × 20 = 60

- **P:**  
  - Table:  P(P|Q,S)  
  - Parents: Q (5), S (3) → 5×3 = 15  
  - Domain(P) = 3  
  - Number of entries = 3 × 15 = 45

- **B:**  
  - Table:  P(B|Q,S,C,P)  
  - Parents: Q (5), S (3), C (4), P (3) → 5×3×4×3 = 180  
  - Domain(B) = 2  
  - Number of entries = 2 × 180 = 360

#### Step 3: Tabulate Meanings and Entries

| Variable | Probability Table          | Number of Entries |
|----------|---------------------------|------------------|
| Q        | `P(Q)`                    | 5                |
| C        | `P(C)`                    | 4                |
| S        | `P(S|Q,C)`                | 60               |
| P        | `P(P|Q,S)`                | 45               |
| B        | `P(B|Q,S,C,P)`            | 360              |

---

**Final Answer Table**

| Variable | CPT Meaning        | # Entries |
|----------|-------------------|-----------|
| Q        | `P(Q)`            | 5         |
| S        | `P(S|Q,C)`        | 60        |
| C        | `P(C)`            | 4         |
| P        | `P(P|Q,S)`        | 45        |
| B        | `P(B|Q,S,C,P)`    | 360       |


---

## Factorization of a Full Joint Event

To compute, for example,  
**P(good, small, red, cheap, yes):**

Use the product of the relevant CPTs (Bayesian Network chain rule):

The joint probability of all five variables in the Bayesian network can be factored (using the structure of the network) as follows:

The joint probability over all variables can be factored according to the structure of the Bayesian network. The chain rule yields:

P(Q, S, C, P, B) =  
  P(Q) × P(C) × P(S | Q, C) × P(P | Q, S) × P(B | Q, S, C, P)

For a specific assignment (Q = good, S = small, C = red, P = cheap, B = yes):

P(good, small, red, cheap, yes) =  
  P(good) ×  
  P(red) ×  
  P(small | good, red) ×  
  P(cheap | good, small) ×  
  P(yes | good, small, red, cheap)

This shows each factor, what it is conditioned on, and how the Bayesian network chain rule works.
