# Chapter 10: Classical Planning – Exam Notes

---

## 1. Introduction to Planning

### What is Planning?
- **Automated sequential decision-making** in simple environments.
- **Input**: Logical description of states, initial state, goal condition, actions.
- **Output**: Sequence of actions (plan) transforming initial state to goal state.

### Planning Applications
- Card games (e.g., Solitaire)
- Natural language generation
- Business process automation (e.g., SAP)
- Security testing/attack planning
- Logistics and transportation

---

## 2. STRIPS Planning Formalism

### Definition

A STRIPS planning task is a 4-tuple $\Pi = (P, A, I, G)$ where:

- $P =$ finite set of **facts** (propositions)
- $A =$ finite set of **actions**
- $I \subseteq P =$ initial state
- $G \subseteq P =$ goal

### Action Structure

Each action $a \in A$ is a triple $(pre_a, add_a, del_a)$:
- $pre\_a \subseteq P$: preconditions (must be true to apply)
- $add\_a \subseteq P$: add effects (facts that become true after action)
- $del\_a \subseteq P$: delete effects (facts that become false after action)
- Requirement: $add_a \cap del_a = \emptyset$

---

## 3. State Space Semantics

### States
- States are subsets of $P$: $S = 2^P$
- A state $s$ is the set of facts true in that state

### Action Application
- Action $a$ is **applicable** in state $s$ if $pre_a \subseteq s$
- Resulting state: $appl(s, a) = (s \cup add_a) \setminus del_a$

### Goal States
- State $s$ is a goal state if $G \subseteq s$

### Plan
A sequence of actions $\langle a_1, ..., a_n \rangle$ such that:
$$
G \subseteq appl(\ldots appl(appl(I, a_1), a_2) \ldots, a_n)
$$

---

## 4. Example: "TSP in Australia"

### Facts
- $at(x)$ for $x \in \{$Sydney, Adelaide, Brisbane, Perth, Darwin$\}$
- $visited(x)$ for same cities

### Initial State
- $\{at(\text{Sydney}), visited(\text{Sydney})\}$

### Goal
- $\{at(\text{Sydney})\} \cup \{visited(x) \mid x \in$ all cities$\}$

### Actions
- $drive(x, y)$: 
    - pre: $\{at(x)\}$ 
    - add: $\{at(y), visited(y)\}$ 
    - del: $\{at(x)\}$

### Plan Example
- $drive(\text{Sydney}, \text{Brisbane})$, $drive(\text{Brisbane}, \text{Sydney})$, ...

---

## 5. Blocksworld Example

### Facts
- $on(x, y)$
- $onTable(x)$
- $clear(x)$
- $holding(x)$
- $armEmpty()$

### Actions
- $pickup(x)$:  
  - pre: $\{onTable(x), clear(x), armEmpty()\}$  
  - add: $\{holding(x)\}$  
  - del: $\{onTable(x), clear(x), armEmpty()\}$  
- $putdown(x)$:  
  - pre: $\{holding(x)\}$  
  - add: $\{onTable(x), clear(x), armEmpty()\}$  
  - del: $\{holding(x)\}$  
- $stack(x, y)$:  
  - pre: $\{holding(x), clear(y)\}$  
  - add: $\{on(x, y), armEmpty()\}$  
  - del: $\{holding(x), clear(y)\}$  
- $unstack(x, y)$:  
  - pre: $\{on(x, y), clear(x), armEmpty()\}$  
  - add: $\{holding(x), clear(y)\}$  
  - del: $\{on(x, y), armEmpty()\}$  

---

## 6. PDDL (Planning Domain Definition Language)

### Domain File

```pddl
(define (domain blocksworld)
  (:predicates (clear ?x) (holding ?x) (on ?x ?y) 
               (on-table ?x) (arm-empty))
  (:action stack
    :parameters (?x ?y)
    :precondition (and (clear ?y) (holding ?x))
    :effect (and (arm-empty)
                 (on ?x ?y)
                 (not (clear ?y))
                 (not (holding ?x)))))
```

### Problem File

```pddl
(define (problem bw-abcde)
  (:domain blocksworld)
  (:objects a b c d e)
  (:init (on-table a) (clear a) ... (arm-empty))
  (:goal (and (on e c) (on c a) (on b d))))
```

---

## 7. Planning as Heuristic Search

### The Problem

- State spaces are HUGE (combinatorial explosion)
- Need to search efficiently

### Approaches

- **Blind search**: BFS, DFS, Uniform-Cost (inefficient for large spaces)
- **Heuristic search**: Use domain knowledge to guide search

### Heuristic Functions for Planning

- $h(s)$ = estimate of cost from state $s$ to goal

- **Perfect heuristic**: $h^*(s)$ = true optimal remaining cost

---

## 8. Delete Relaxation

- **Idea**: Ignore delete effects — facts never become false.

### Definition

For planning task $\Pi = (P, A, I, G)$, the **delete relaxation** $\Pi^+$ has:

- Same $P, I, G$
- Actions $A^+$ with: 
    - $pre_a^+ = pre_a$
    - $add_a^+ = add_a$
    - $del_a^+ = \emptyset$

### Relaxed Plan

A plan for $\Pi^+$ (easier to find).

### Properties

- Any real plan is also a relaxed plan.
- Relaxed planning is in P (polynomial time).
- Real planning is PSPACE-complete.

---

## 9. The $h^+$ Heuristic

### Definition

- $h^+(s)$ = length of optimal relaxed plan for state $s$

### Properties

- **Admissible**: $h^+(s) \leq h^*(s)$
- **Consistent** (implies admissibility)
- But **NP-complete** to compute exactly

**Example: TSP Australia**  
- Real optimal plan: 8 actions  
- $h^+$ value: 4 actions  

---

## 10. Approximating $h^+$: $h_{FF}$ (Fast Forward)

### Relaxed Planning Graph (RPG) Construction

1. $F_0 := s$, $t := 0$
2. While $G \not\subseteq F_t$ do:
    - $A_t := \{a \in A \mid pre_a \subseteq F_t \}$
    - $F_{t+1} := F_t \cup \bigcup_{a \in A_t} add_a$
    - If $F_{t+1} = F_t$, then return $\infty$
    - $t := t + 1$
3. End while

### Plan Extraction (Backward Chaining)
- Compute $\text{level}(p)$ = first time fact $p$ appears in RPG
- Compute $\text{level}(a)$ = first time action $a$ applicable
- Backward from goals at max level, select supporting actions
- $h_{FF}(s)$ = number of selected actions

### Properties

- $h_{FF}(s) \geq h^+(s)$ (may overestimate)
- **Not admissible** (can overestimate true cost)
- Used for satisficing planning (not optimal)

---

## 11. Planning Algorithms

### Greedy Best-First Search (GBFS)
- Uses $h_{FF}$
- Complete but not optimal
- Good for satisficing planning

### A\* Search
- Uses admissible heuristic (like $h^+$, if computable)
- Complete and optimal
- Good for optimal planning

---

## 12. Exercises & Solutions

### Exercise 1: STRIPS Encoding

**Problem:** Encode "make coffee" task

- **Facts**: `has_water`, `has_coffee`, `coffee_made`
- **Actions**: 
  - `boil_water`  
  - `add_coffee`
- **Initial State**: `{has_water, has_coffee}`
- **Goal**: `{coffee_made}`

**Solution:**
- `boil_water`:  
  - pre: `{has_water}`  
  - add: `{hot_water}`  
  - del: `∅`  
- `add_coffee`:  
  - pre: `{has_coffee, hot_water}`  
  - add: `{coffee_made}`  
  - del: `{has_coffee, hot_water}`  

---

### Exercise 2: Delete Relaxation

**Given:**  
Action `drive(x, y)`  
- pre: `{at(x)}`
- add: `{at(y)}`
- del: `{at(x)}`

**Relaxed version:**  
- pre: `{at(x)}`  
- add: `{at(y)}`  
- del: `∅`

**Effect:** In the relaxed problem, you can be at multiple cities simultaneously.

---

### Exercise 3: RPG Computation

**Given:**  
Initial: `{A}`

**Actions:**  
- `a1`: pre `{A}`, add `{B}`  
- `a2`: pre `{B}`, add `{C}`  

**Goal:** `{C}`

**RPG Construction:**
- $F_0 = \{A\}$
- $A_0 = \{a1\}$
- $F_1 = \{A, B\}$
- $A_1 = \{a1, a2\}$
- $F_2 = \{A, B, C\}$

- $\text{level}(C) = 2$

**Backward:** support $C$ with $a2$ (level 1), support $B$ with $a1$ (level 0).  
So, $h_{FF} = 2$

---

### Exercise 4: Admissibility Check

**Claim:** $h_{FF}$ is not admissible.

**Proof:** Counterexample exists where $h_{FF}(s) > h^*(s)$ because $h_{FF}$ may count unnecessary actions in relaxed plan.

---

## 13. Summary Table

| Concept             | Description                         | Complexity/Properties        |
|---------------------|-------------------------------------|-----------------------------|
| STRIPS              | Boolean planning language           | Simple but expressive       |
| Delete Relaxation   | Ignore delete effects               | Makes planning polynomial   |
| $h^+$               | Optimal relaxed plan length         | Admissible, NP-complete     |
| $h_{FF}$            | RPG approx. of $h^+$                | Not admissible, fast        |
| GBFS                | Greedy search with heuristic        | Complete, not optimal       |
| A*                  | Optimal search with admissible $h$  | Complete and optimal        |


---

## 14. Key Algorithms

### PlanEx$^+$ Decision Algorithm

```pseudo
F := I
while G ⊈ F do
    F' := F ∪ ⋃_{a: pre_a ⊆ F} add_a
    if F' = F then return "unsolvable"
    F := F'
endwhile
return "solvable"
```

RPG Construction for $h_{FF}$ (as described in Section 10).

---

## 📚 Recommended Reading

- STRIPS original paper (Fikes & Nilsson, 1971)
- FF planner (Hoffmann & Nebel, 2001)
- PDDL specification

