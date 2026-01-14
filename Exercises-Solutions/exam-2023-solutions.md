# Exam 2022 - Complete Solutions & Study Notes

---

## 📘 Exercise 1: Decision Trees & Neural Networks (22 points)

### Part (i): Decision Tree Classification

**Given tree structure:**

- **Root:** Cooked?
    - **Yes**
        - **Color?**
            - Green → **Vegetable**
            - Other → **Density?**
                - High → **Fruit**
                - Medium → **Shape?**
                    - Round → **Fruit**
                    - Long → **Vegetable**
                - Low → **Shape?**
                    - Round → **Vegetable**
                    - Long → **Fruit**
    - **No**
        - **Shape?**
            - Round → **Fruit**
            - Long → **Vegetable**

**Classifications:**

| Object       | Path                                             | Classification |
|--------------|--------------------------------------------------|----------------|
| Banana       | No cooked → Long shape                           | Vegetable      |
| Lettuce      | No cooked → Round shape                          | Fruit          |
| Aubergine    | Yes cooked → Purple (other) → High density       | Fruit          |
| Carrot       | Yes cooked → Orange (other) → High density       | Fruit          |
| Green peas   | Yes cooked → Green                               | Vegetable      |
| Grapes       | No cooked → Round                                | Fruit          |
| Apple        | No cooked → Round                                | Fruit          |
| Zucchini     | Yes cooked → Green                               | Vegetable      |


### Part (ii): Classification Metrics

**Given classifications:**

| Item         | Predicted      | Actual     | Outcome          |
|--------------|---------------|------------|------------------|
| Banana       | Vegetable      | Fruit      | False Negative   |
| Lettuce      | Fruit          | Vegetable  | False Positive   |
| Aubergine    | Vegetable      | Vegetable  | True Negative    |
| Carrot       | Vegetable      | Vegetable  | True Negative    |
| Green peas   | Vegetable      | Vegetable  | True Negative    |
| Grapes       | Fruit          | Fruit      | True Positive    |
| Apple        | Fruit          | Fruit      | True Positive    |
| Zucchini     | Vegetable      | Vegetable  | True Negative    |

**Metrics:**  
- **TP** (True Positives): 2 (Grapes, Apple)  
- **FP** (False Positives): 1 (Lettuce)  
- **TN** (True Negatives): 4 (Aubergine, Carrot, Green peas, Zucchini)  
- **FN** (False Negatives): 1 (Banana)

- **Accuracy**: $(TP + TN) / Total = (2 + 4) / 8 = 0.75$
- **Precision**: $TP / (TP + FP) = 2 / (2 + 1) ≈ 0.67$
- **Recall**: $TP / (TP + FN) = 2 / (2 + 1) ≈ 0.67$

---

### Part (iii): Information Gain for "Shape"

**Dataset:** 8 examples  
- Fruits: Banana, Grapes, Apple (3/8)  
- Vegetables: Lettuce, Aubergine, Carrot, Green peas, Zucchini (5/8)

**Entropy of whole dataset:**  

$$
H(S) = -[P(\mathrm{Fruit})\log_2P(\mathrm{Fruit}) + P(\mathrm{Veg})\log_2P(\mathrm{Veg})] \\
     = -[(3/8)\log_2(3/8) + (5/8)\log_2(5/8)] \\
     ≈ -[0.375 \times (-1.415) + 0.625 \times (-0.678)] \\
     ≈ -[-0.531 - 0.424] = 0.955
$$

**Split by Shape:**

- **Long (Banana, Aubergine, Carrot, Zucchini):**  
    $P(F) = 1/4, P(V) = 3/4$
    $$
    H(\text{Long}) = -[(1/4)\log_2(1/4) + (3/4)\log_2(3/4)] ≈ 0.811
    $$
- **Round (Lettuce, Green peas, Grapes, Apple):**  
    $P(F) = 1/2, P(V) = 1/2$
    $$
    H(\text{Round}) = -[(1/2)\log_2(1/2) + (1/2)\log_2(1/2)] = 1.0
    $$

**Weighted average entropy:**

$$
H(S|\text{Shape}) = (4/8) \times 0.811 + (4/8) \times 1.0 = 0.9055
$$

**Information Gain:**

$$
IG(\text{Shape}) = 0.955 - 0.9055 = 0.0495
$$

---

### Part (iv): Information Gain for "Cooked"

**Split by Cooked:**

- **Yes (Aubergine, Carrot, Green peas, Zucchini):** all Vegetables → $H(\text{Yes}) = 0$
- **No (Banana, Lettuce, Grapes, Apple):**
    - Fruits: 3/4
    - Vegetables: 1/4
    $$
    H(\text{No}) = -[(3/4)\log_2(3/4) + (1/4)\log_2(1/4)] ≈ 0.811
    $$

**Weighted average entropy:**

$$
H(S|\text{Cooked}) = (4/8)\times0 + (4/8)\times0.811 = 0.4055
$$

**Information Gain:**

$$
IG(\text{Cooked}) = 0.955 - 0.4055 = 0.5495
$$

---

### Part (v): Which attribute to choose?

Choose **"Cooked"** because it has higher information gain ($0.5495 > 0.0495$).  
Decision trees select the attribute that maximizes information gain (or minimizes entropy).

---

### Part (vi): Is the new tree preferable?

Yes, because:
- Perfect metrics (accuracy=precision=recall=1) on test set indicate perfect generalization.
- Tree (i) had errors (e.g., misclassified Banana, Lettuce).
- A model with perfect test performance is always preferable to one with errors, assuming test distribution is similar.

---

### Part (vii): Neural Network Backpropagation

- **What is learned automatically:**
    - ✓ The weights in the connections between the neurons

- **What is NOT learned automatically (hyperparameters):**
    - ✗ How many layers to use
    - ✗ What activation function to use
    - ✗ How many neurons to use in each layer

> These are architectural choices set before training.


---

## 📘 Exercise 2: K-Means Clustering (13 points)

### Part (i): Initial Classification

**Initial centroids:**  
- C₁ = (20, 1, 1)  
- C₂ = (80, 10, 10)

**Euclidean distances and assignments:**

| # | Point        | $d(\mathrm{C}_1)$ | $d(\mathrm{C}_2)$ | Cluster       |
|---|--------------|-------------------|-------------------|---------------|
| 1 | (25,2,9)     | ≈ 9.49            | ≈ 55.59           | 1             |
| 2 | (45,4,4)     | ≈ 25.36           | ≈ 36.01           | 1             |
| 3 | (70,8,7)     | ≈ 50.84           | ≈ 10.63           | 2             |
| 4 | (40,3,10)    | ≈ 22.02           | ≈ 40.61           | 1             |
| 5 | (30,5,9)     | ≈ 13.42           | ≈ 50.26           | 1             |
| 6 | (80,8,8)     | ≈ 60.81           | ≈ 2.83            | 2             |

- **Cluster 1:** #1, 2, 4, 5
- **Cluster 2:** #3, 6

---

### Part (ii): New Centroids after 1 iteration

**Cluster 1 points:** (25,2,9), (45,4,4), (40,3,10), (30,5,9)  
- Attr1: (25+45+40+30)/4 = 35  
- Attr2: (2+4+3+5)/4 = 3.5  
- Attr3: (9+4+10+9)/4 = 8  
- **C₁_new = (35, 3.5, 8)**

**Cluster 2 points:** (70,8,7), (80,8,8)
- Attr1: (70+80)/2 = 75  
- Attr2: (8+8)/2 = 8  
- Attr3: (7+8)/2 = 7.5  
- **C₂_new = (75, 8, 7.5)**

---

### Part (iii): Would algorithm stop?

No:  
The centroids changed (C₁: (20,1,1) → (35,3.5,8); C₂: (80,10,10) → (75,8,7.5))  
K-means continues until centroids stabilize (no/minimal change).

---

### Part (iv): Data issues

- **Problem:** Different attribute scales!  
    - HP (att1): 25-80
    - STR (att2): 2-8
    - SPD (att3): 4-10

- **Solution:** Normalize data (min-max scaling, z-score, etc.)  
  So all attributes contribute equally to distance computation.

---

## 📘 Exercise 3: Bayesian Networks (18 points)

### Part (i): d-Separation

**Rules:**
- Two nodes are d-connected if there is an unblocked path between them.
- A path is *blocked* if:
    - It contains a chain $A \to B \to C$ or a fork $A \leftarrow B \to C$ with evidence on $B$
    - It contains a collider $A \to B \leftarrow C$ with *no* evidence on $B$ or its descendants

**Sample Answers:**

- S and U d-separated? **No** (direct S→U)
- S, U d-separated given W? **Yes** (evidence on W on S→U→W)
- S, U d-separated given V? **No** (S→V←U collider, evidence on V opens path)
- S and U d-separated given V, W? **Yes** (W blocks S→U→W, but V evidence activates collider path)
- U, V d-separated? **No** (common parent S)
- U, V d-separated given S? **Yes** (evidence blocks at S)
- U, V d-separated given W? **No** (U→W←V collider, evidence opens path)
- U, V d-separated given S and W? **Yes** (S blocks one path, W another)
- S, W d-separated? **No** (S→U→W and S→V→W)
- S, W d-sep given U? **No** (S→V→W remains)

---

### Part (ii): $P(u, \lnot v, w, s)$

- Factorization: $P(s) \times P(u|s) \times P(\lnot v|s) \times P(w|u, \lnot v)$

$$
\begin{align*}
P(s) &= 2/10 = 0.2 \\
P(u|s) &= 3/5 = 0.6 \\
P(\lnot v|s) &= 1 - P(v|s) = 1 - 7/10 = 0.3 \\
P(w|u, \lnot v) &= 2/5 = 0.4 \\
\text{Product: } \quad 0.2 \times 0.6 \times 0.3 \times 0.4 = 0.0144
\end{align*}
$$

---

### Part (iii): $P(\lnot u \mid s)$

$$
P(\lnot u|s) = 1 - P(u|s) = 1 - 3/5 = 0.4
$$

---

### Part (iv): $P(s \mid u, w)$

Apply Bayes:

$$
P(s|u,w) = \frac{P(u,w|s)P(s)}{P(u,w)}
$$

Compute:

- $P(u,w|s) = P(u|s) \times P(w|u,s)$

But $P(w|u,s) = \sum_v P(w|u,v)P(v|s)$

$$
\begin{align*}
P(w|u,s) &= P(w|u,v)P(v|s) + P(w|u,\lnot v)P(\lnot v|s) \\
        &= (5/8)\times(7/10) + (2/5)\times(3/10) \\
        &= 0.4375 + 0.12 = 0.5575 \\
P(u,w|s) &= (3/5) \times 0.5575 = 0.3345 \\
\\
P(u|{\lnot s}) &= 0.75 \\
P(v|{\lnot s}) = 0.2;\ P(\lnot v|{\lnot s}) = 0.8 \\
P(w|u,v) = 0.625;\ P(w|u,\lnot v) = 0.4 \\
P(w|u,\lnot s) &= 0.625 \times 0.2 + 0.4 \times 0.8 = 0.125 + 0.32 = 0.445 \\
P(u,w|{\lnot s}) &= 0.75 \times 0.445 = 0.33375 \\
\\
P(u,w) &= P(u,w|s)P(s) + P(u,w|{\lnot s})P({\lnot s}) \\
       &= 0.3345 \times 0.2 + 0.33375 \times 0.8 = 0.0669 + 0.267 = 0.3339 \\
\\
P(s|u,w) &= 0.0669 / 0.3339 \approx 0.2004
\end{align*}
$$

---

### Part (v): Naive Bayes characteristics

- ✓ The nodes are connected so the class is parent of all features  
- ✓ Assumes effects (features) are independent given class

---

## 📘 Exercise 4: Planning (18 points)

### Part (i): Shortest plan

- **Initial**: Robot at $t_1$, all tiles clear
- **Goal**: Paint $t_1, t_2, t_3$
- **Constraints**: move to clear tiles only, paint only adjacent tiles

**Plan:**

1. paint($t_1$, $t_1$) &nbsp;&rarr; paints current tile  
2. move($t_1$, $t_2$) &nbsp;&rarr; $t_2$ clear  
3. paint($t_2$, $t_2$)  
4. move($t_2$, $t_3$) &nbsp;&rarr; $t_3$ clear  
5. paint($t_3$, $t_3$)

**Plan length:** 5 actions

---

### Part (ii): Shortest relaxed plan

(Relaxed planning = ignores delete effects)

1. paint($t_1$, $t_1$)
2. paint($t_1$, $t_2$)
3. paint($t_1$, $t_3$)

**Length:** 3 actions (can paint all from $t_1$ without moving)

---

### Part (iii): $h^{+}(I)$

$h^{+} = $ length of shortest relaxed plan $= 3$

---

### Part (iv): $h^{*}(I)$

$h^{*} = $ length of optimal real plan $= 5$

---

### Part (v): A* successors from initial state

**Initial state $I = \{ \text{at}(t_1), c(t_0), c(t_1), c(t_2), c(t_3) \}$**

**Applicable actions:**
- move($t_1$, $t_0$): pre $\{at(t_1), c(t_0)\}$  
  New state: $\{at(t_0), c(t_1), c(t_2), c(t_3)\}$  
- move($t_1$, $t_2$): pre $\{at(t_1), c(t_2)\}$  
  New state: $\{at(t_2), c(t_0), c(t_1), c(t_3)\}$
- paint($t_1$, $t_0$): pre $\{at(t_1), c(t_0)\}$
- paint($t_1$, $t_1$): pre $\{at(t_1), c(t_1)\}$
- paint($t_1$, $t_2$): pre $\{at(t_1), c(t_2)\}$

All actions: $g=1$, $h=?$  
(Typically $h^+$ decreases with progress)

---

### Part (vi): A* vs GBFS selection

**A*:** uses $f = g + h$  
| State  | $g$ | $h$ | $f$ |
|--------|-----|-----|-----|
| $s_1$  | 2   | 2   | 4   |
| $s_2$  | 3   | 3   | 6   |
| $s_3$  | 5   | 1   | 6   |
| $s_4$  | 2   | 3   | 5   |
| $s_5$  | 7   | 2   | 9   |
| $s_6$  | 1   | 5   | 6   |

- **A\*** selects: $s_1$ (lowest $f=4$)

**GBFS:** uses only $h$
| State  | $h$ |
|--------|-----|
| $s_1$  | 2   |
| $s_2$  | 3   |
| $s_3$  | 1   |
| $s_4$  | 3   |
| $s_5$  | 2   |
| $s_6$  | 5   |

- **GBFS** selects: $s_3$ (lowest $h=1$)

---

### Part (vii): Optimal algorithms

- ✓ **A\*** with admissible heuristic (e.g., $h^+$, $h^{FF}$) is optimal
- ✗ GBFS (greedy best-first search) is not optimal, regardless of heuristic

---

## 📘 Exercise 5: Game Theory (15 points)

### Part (i): Zero-sum game?

No, because utilities don't sum to zero for all outcomes.  
e.g. (A,E): $2 + (-4) = -2 \ne 0$

---

### Part (ii): Nash Equilibria

Nash Equilibrium: No player can unilaterally improve their payoff.

**Check each:**

- (A,E): Alice 2, Bob -4; neither can improve unilaterally: **✓ Nash Eq**
- (B,E): Alice 2, Bob -1; neither can improve: **✓ Nash Eq**
- (C,E): Alice 0, could improve: ✗ not NE
- (A,F): Alice 2, could improve: ✗ not NE
- (B,F): Alice 5, Bob can improve: ✗ not NE
- (C,F): Alice -2, could improve: ✗ not NE

**Nash Equilibria:** (A,E), (B,E)

---

### Part (iii): What would players choose?

- For Alice: No action strictly dominates (mixed dominance check)
- For Bob: F may dominate E in some responses

**Likely outcome:**  
(B, F): Alice maximizes, Bob minimizes loss (depending on risk preferences and payoff matrix)

---

### Part (iv): Minimax tree

**Bottom-up:**

- Left MIN: $\min(0, 8) = 0$
- Center MIN: $\min(-5, -2) = -5$
- Right MIN: $\min(0, 1, -1) = -1$

**MAX:** $\max(0, -5, -1) = 0$

---

### Part (v): Max's move

- Max should choose: **Left** (value $0$)

---

### Part (vi): Who wins with perfect play?

- **Max** wins (0 is greater than all other MIN outcomes)

---

## 📘 Exercise 6: Markov Decision Processes (14 points)

### Part (i): Discounted reward

Sequence: $s_1 \rightarrow s_2 \rightarrow s_2 \rightarrow s_1$  
Rewards: $0, 1, 1, 0$  
Discounted sum ($\gamma = 0.9$):

$$
R = 0 + 0.9 \times 1 + 0.9^2 \times 1 + 0.9^3 \times 0 = 0 + 0.9 + 0.81 + 0 = 1.71
$$

(Transition probabilities needed for full expected value calculation.)

---

### Part (ii): Best action from $s_1$ using $V_0$

- Compute Q-values for each action:
    - **Relax:** $R(s_1, \mathrm{relax}) + \gamma \sum_{s'} P(s'|s_1, \mathrm{relax}) V_0(s')$
    - **Work-light:** $R(s_1, \mathrm{worklight}) + \gamma \sum_{s'} P(s'|s_1, \mathrm{worklight}) V_0(s')$
    - **Work-hard:** $R(s_1, \mathrm{workhard}) + \gamma \sum_{s'} P(s'|s_1, \mathrm{workhard}) V_0(s')$

- Choose the action with highest Q-value.

---

### Parts (iii)-(iv): Value Iteration

Update rule:

$$
V_{k+1}(s) = \max_a \left[R(s,a) + \gamma \sum_{s'}P(s'|s,a)V_k(s')\right]
$$

- For $s_\mathrm{inj}$: $V_{new}(s_\mathrm{inj}) = -10 + 0.9 \times V_0(s_\mathrm{inj}) = -10 -1.8 = -11.8 $

- For $s_1$: Compute for each action, take $\max$

---

## 🎯 Exam Preparation Summary

### Key Topics Covered

- Decision Trees: information gain, classification, metrics
- Clustering: K-means, distance calculations, normalization
- Bayesian Networks: d-separation, probability calculations
- Planning: STRIPS, relaxed planning, heuristics, search algorithms
- Game Theory: Nash Equilibrium, zero-sum games, minimax
- MDPs: Value iteration, discounted rewards

### Important Formulas

- **Information Gain:**  
  $IG(A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$
- **Entropy:**  
  $H(S) = -\sum p \log_2 p$
- **Accuracy:**  
  $(TP+TN)/\text{Total}$
- **Precision:**  
  $TP/(TP+FP)$
- **Recall:**  
  $TP/(TP+FN)$
- **Euclidean distance:**  
  $\sqrt{\sum_i (x_i - y_i)^2}$
- **Nash Equilibrium:**  
  No unilateral improvement
- **Minimax:**  
  Max minimizes Min's maximum gain
- **Value Iteration:**  
  $V_{k+1}(s) = \max_a [R(s,a) + \gamma \sum P(s'|s,a)V_k(s')]$.

