# Multi-Agent Systems: Adversarial Search and Game Theory – Exam Notes

---

## 1. Introduction to Multi-Agent Systems

- **New dimension:** Other agents with possibly competing objectives.
- **Game theory:** Mathematical models of strategic interactions among rational agents.

---

## 2. Definition of a Game

A game is defined by:
- **States** \(S\):  
  - Terminal states (\(S^T\)): where the game ends.  
  - Intermediate states (\(S^I\)): where players still move.
- **Players** \(P\): Each has set of actions (\(A_p\)) and a utility function (\(u_p\)).

- **Utility function:** assigns a score to terminal states.
- **Objective:** Each agent picks actions to maximize its own utility.

**Types of Games Covered:**
- Two-player
- Zero-sum
- Turn-taking
- Fully observable
- Deterministic
- Finite

---

## 3. Minimax Algorithm

**Purpose:** Compute optimal move for Max (first player) assuming perfect play by Min (the opponent).

**Procedure:**
1. Perform depth-first search in the game tree.
2. Apply utility function to terminal states.
3. For internal nodes:
   - If Max’s turn → take **max** of children’s utilities.
   - If Min’s turn → take **min** of children’s utilities.
4. At root, choose move leading to child with highest utility.

**Example (Tic-Tac-Toe):**
- Max (\(x\)) → Min (\(o\)) → Max (\(x\)) → Terminal states with utilities:
    - Win: +100
    - Draw: 0
    - Loss: -100

**Minimax Pseudo-Code:**
```python
def minimax_decision(s):
    v = max_value(s)
    return action leading to v

def max_value(s):
    if terminal(s): return u(s)
    v = -float('inf')
    for a in actions(s):
        v = max(v, min_value(child(s, a)))
    return v

def min_value(s):
    if terminal(s): return u(s)
    v = float('inf')
    for a in actions(s):
        v = min(v, max_value(child(s, a)))
    return v
```

---

## 4. Alpha-Beta Pruning

- **Idea:** Prune branches that cannot influence the final decision.
- **Alpha:** Best value **Max** can guarantee so far.
- **Beta:** Best value **Min** can guarantee so far.

**Prune when:**
- In Max node: child value ≥ beta.
- In Min node: child value ≤ alpha.

**Example:**  
In a game tree, if Min can force a value ≤ current alpha in a subtree, prune remaining siblings.

---

## 5. Evaluation Functions

**Purpose:** Estimate utility of non-terminal states when search depth is limited.

**General Form:**
\[
h(s) = w_1 f_1(s) + \cdots + w_n f_n(s)
\]
where:
- **Features \(f_i\):** e.g., material advantage, mobility, king safety (domain-specific).
- **Weights \(w_i\):** set by experts or learned.

**Example (Chess Evaluation):**
\[
h(s) = \Delta\text{pawn} + 3 \cdot \Delta\text{knight} + 3 \cdot \Delta\text{bishop} + 5 \cdot \Delta\text{rook} + 9 \cdot \Delta\text{queen} + w_{\text{king safety}} + w_{\text{pawn structure}}
\]

---

## 6. Learning in Games

### Supervised Learning
- Learn \( h(s) \) or policy \( p(s) \) from labeled expert data.
- Example: AlphaGo used 30 million expert moves from the KGS Go Server.

### Reinforcement Learning via Self-Play
- Play games using current \( h \) or \( p \).
- Update parameters based on game outcomes.
- Example: AlphaGo also used self-play to generate training data.

---

## 7. Beyond Turn-Based Zero-Sum Games

### Simultaneous Move Games
- Example: Rock-Paper-Scissors.
- Represented using **information sets** (states indistinguishable to a player).

### Normal Form Representation
- Matrix: Rows/columns = player strategies, cells = utilities for joint actions.
- Example: Prisoner’s Dilemma.

### Nash Equilibrium
- **Definition:** Strategy profile where no player can improve utility by unilaterally changing strategy.
- **Existence:** Every finite game has at least one Nash equilibrium (possibly mixed strategies).
- **Example:** In Prisoner’s Dilemma, (testify, testify) is the only Nash equilibrium.

---

## 8. Example Exercises

### Exercise 1: Minimax Computation

**Given Game Tree (Max at root):**
```
        Max
      /   |   \
    3    12    8
   / \   / \   / \
  2   4 6  14 5   2
```
**Solution Steps:**
- Compute from leaves: Min nodes take min of children.
- Root Max takes max of children.

**Values:**
- Left branch: min(2, 4) = 2
- Middle branch: min(6, 14) = 6
- Right branch: min(5, 2) = 2

- **Root value = max(2, 6, 2) = 6** → choose middle branch.

---

### Exercise 2: Alpha-Beta Pruning

**Apply alpha-beta pruning to the same tree. Show which branches are pruned.**

**Solution:**
- After exploring left branch (value = 2), alpha = 2.
- In middle branch: first child yields 6 ≥ alpha → update alpha = 6.
- In right branch: first child yields 5 ≤ alpha? No, but second child yields 2 < alpha.
- For Min node, prune if value ≤ alpha. Here alpha=6, child=5 not ≤6, so no prune.
- If Min can force ≤2, pruning occurs earlier in deeper trees.

---

### Exercise 3: Evaluation Function

**In chess position, compute \( h(s) \) given:**

- White: 1 pawn, 1 knight, 1 rook.
- Black: 2 pawns, 1 bishop.
- Weights: pawn = 1, knight = 3, bishop = 3, rook = 5

\[
h(s) = (1-2) + 3(1-0) + 3(0-1) + 5(1-0) = -1 + 3 - 3 + 5 = 4
\]

---

### Exercise 4: Nash Equilibrium

**Game Matrix:**

|       | Bob: L | Bob: R |
|-------|--------|--------|
|Alice: U | 3, 2  | 0, 0  |
|Alice: D | 0, 0  | 2, 3  |

**Solution:**
- (U, L): Alice deviates? **No.** Bob deviates? **No.** → Nash
- (U, R): Alice deviates? **Yes (to D).** → Not Nash
- (D, L): Alice deviates? **Yes (to U).** → Not Nash
- (D, R): Alice deviates? **No.** Bob deviates? **No.** → Nash

**Equilibria:** (U, L) and (D, R)

---

## 9. Key Points to Remember for Exam

- **Minimax:** Optimal play under perfect opponent.
- **Alpha-beta pruning:** Reduces search cost, does not affect optimality.
- **Evaluation functions:** Estimate state value when search is depth-limited.
- **Nash equilibrium:** Stable strategy profile; always exists for finite games (possibly in mixed strategies).
- **Simultaneous/incomplete information games:** Use information sets and normal form.


