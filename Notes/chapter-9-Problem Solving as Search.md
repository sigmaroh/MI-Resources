# Chapter 9: Problem Solving as Search – Exam Notes

---

## 📘 1. Introduction to Search Problems

### What is a Classical Search Problem?
- **Initial state**
- **Actions** that change the state
- **Goal state(s)**
- **Performance measure**: minimize total action cost

### Examples
- Route planning (Aalborg → Madrid)
- 15-Puzzle
- Office robot navigation
- Bug finding in software

### Characteristics of Classical Search
- Finite states & actions
- Single-agent
- Fully observable
- Deterministic
- Static environment

---

## 📘 2. State Space Formalization

### Definition
A **state space** is a 6-tuple \(\Theta = (S, A, c, T, I, S^G)\) where:
- \(S\) = set of states
- \(A\) = set of actions
- \(c: A \to \mathbb{R}_0^+\) = cost function
- \(T \subseteq S \times A \times S\) = transition relation (deterministic)
- \(I \in S\) = initial state
- \(S^G \subseteq S\) = goal states

### Terminology
- **Successor**: \(s'\) is successor of \(s\) if \(s \xrightarrow{a} s'\)
- **Reachable**: \(s'\) is reachable from \(s\) if there exists a path
- **Solution**: path from \(I\) to any \(s \in S^G\)
- **Optimal solution**: solution with minimal cost

---

## 📘 3. Search Algorithms: General Framework

### Generic Best-First Search

frontier = {InitialState()}
explored = {}
while frontier not empty:
select node from frontier (by some criteria)
if GoalTest(node.state): return solution
add node.state to explored
for each action a in Actions(node.state):
child = ChildState(node.state, a)
if child not in explored ∪ frontier:
add child to frontier


### Search Node Representation
- **State**: current state
- **Parent**: node that generated this
- **Action**: action applied to parent
- **PathCost**: \(g(n)\) = cost from start

### Evaluation Criteria
- **Completeness**: always finds solution if exists
- **Optimality**: always finds optimal solution
- **Time complexity**: nodes expanded/generated
- **Space complexity**: memory used

---

## 📘 4. Blind Search Strategies

### Breadth-First Search (BFS)
- **Order**: FIFO queue
- **Complete**: Yes (if finite branching)
- **Optimal**: Yes (for unit costs)
- **Time**: \(O(b^d)\)
- **Space**: \(O(b^d)\)

### Depth-First Search (DFS)
- **Order**: LIFO stack
- **Complete**: No (may loop)
- **Optimal**: No
- **Time**: \(O(b^m)\)
- **Space**: \(O(bm)\)

### Uniform-Cost Search (Dijkstra)
- **Order**: priority queue by \(g(n)\)
- **Complete**: Yes
- **Optimal**: Yes
- **Time**: \(O(b^{1+\lfloor g^*/\epsilon \rfloor})\)
- **Space**: \(O(b^{1+\lfloor g^*/\epsilon \rfloor})\)

---

## 📘 5. Heuristic Functions

### Definition
\(h: S \to \mathbb{R}_0^+ \cup \{\infty\}\) where \(h(s) = 0\) for goal states  
\(h^*(s)\) = true goal distance (perfect heuristic)

### Properties
- **Admissible**: \(h(s) \leq h^*(s)\) for all \(s\)
- **Consistent**: \(h(s) \leq c(a) + h(s')\) for all \(s \xrightarrow{a} s'\)

### Theorem
Consistency ⇒ Admissibility

### Examples from Relaxed Problems
- **Straight-line distance** for route planning
- **Misplaced tiles** for 8-puzzle
- **Manhattan distance** for 8-puzzle
- **Pattern database** heuristics

---

## 📘 6. Informed Search Strategies

### Greedy Best-First Search
- **Order**: priority queue by \(h(n)\)
- **Complete**: Yes (with duplicate elimination)
- **Optimal**: No
- **Example**: Route to Bucharest using straight-line distance

### A* Search
- **Order**: priority queue by \(f(n) = g(n) + h(n)\)
- **Complete**: Yes
- **Optimal**: Yes (if \(h\) admissible)
- **Node re-opening**: needed if \(h\) admissible but inconsistent

### Weighted A* (WA*)
- **Order**: priority queue by \(g(n) + w \cdot h(n)\)
- **Complete**: Yes
- **Optimal**: No (but bounded suboptimality)

---

## 📘 7. A* Properties & Optimality

### Theorem (Optimality of A*)
If \(h\) is admissible, A* returns optimal solution.

### Theorem (Optimal Efficiency)
With consistent \(h\), A* expands minimal nodes among algorithms using same heuristic.

### \(f(n)\) Bounds
- A* expands all nodes with \(f(n) < C^*\)
- Some nodes with \(f(n) = C^*\)
- No nodes with \(f(n) > C^*\)

---

## 📘 8. Practical Examples

### Example 1: Route Planning in Romania

Cities: Arad, Sibiu, Timisoara, Bucharest, etc.
Heuristic: straight-line distance to Bucharest
Action costs: road distances

### Example 2: 8-Puzzle

Heuristics:

Misplaced tiles: count wrong positions

Manhattan distance: sum of tile distances

Pattern databases: precomputed subproblem distances


---

## 📘 9. Exercises & Solutions

### Exercise 1: Uniform-Cost Search
**Problem**: Find cheapest path from Arad to Bucharest with given road distances.

**Solution Steps**:
1. Start: Arad (g=0)
2. Expand Arad: Sibiu (g=140), Timisoara (g=118), Zerind (g=75)
3. Expand Zerind: Oradea (g=75+71=146)
4. Expand Timisoara: Lugoj (g=118+111=229)
5. Expand Sibiu: Rimnicu (g=140+80=220), Fagaras (g=140+99=239), etc.
6. Continue until Bucharest found with minimal g.

### Exercise 2: Heuristic Admissibility
**Problem**: Is Manhattan distance admissible for 8-puzzle?

**Proof**:
- Each move changes Manhattan distance by at most 1
- Need at least |MD| moves to reach goal
- Therefore \(h_{MD}(s) \leq h^*(s)\) ✓

### Exercise 3: A* Trace
**Given**: Start A, Goal G, heuristic values:
- h(A)=5, h(B)=4, h(C)=2, h(D)=6, h(G)=0
- Costs: A→B=3, A→C=2, B→G=4, C→D=1, D→G=3

**A* Steps**:
1. Frontier: A (f=0+5=5)
2. Expand A: B (f=3+4=7), C (f=2+2=4)
3. Expand C: D (f=3+6=9)
4. Expand B: G (f=7+0=7)
5. Goal found: A→B→G cost=7

### Exercise 4: Consistency Check
**Given**: Transition A→B cost=2, with h(A)=5, h(B)=2

**Check**: h(A) ≤ c(A,B) + h(B)?
5 ≤ 2 + 2? No (5 ≤ 4 false) → Inconsistent

---

## 📘 10. Advanced Topics (Not Covered in Depth)

### Bidirectional Search
- Search forward from start + backward from goal
- Time: \(O(b^{d/2})\)

### Iterative Deepening A* (IDA*)
- Depth-first with increasing f-limit
- Linear space complexity

### Real-Time Search
- Fixed deadline constraints

### Memory-Bounded Search
- MA*, SMA*

---

## 📘 11. Summary Table

| Algorithm | Ordering | Complete | Optimal | Time | Space |
|-----------|----------|----------|---------|------|-------|
| BFS | FIFO | Yes | Yes* | \(O(b^d)\) | \(O(b^d)\) |
| DFS | LIFO | No | No | \(O(b^m)\) | \(O(bm)\) |
| Uniform-Cost | g(n) | Yes | Yes | \(O(b^{1+\lfloor g^*/ϵ \rfloor})\) | Same |
| Greedy BFS | h(n) | Yes | No | \(O(b^m)\) | \(O(b^m)\) |
| A* | g(n)+h(n) | Yes | Yes† | Depends on h | Depends on h |

*For unit costs  
†If h admissible

---

## 📘 12. Key Formulas

- \(g(n)\) = cost from start to n
- \(h(n)\) = estimated cost from n to goal
- \(f(n) = g(n) + h(n)\) (A* evaluation)
- \(h^*(n)\) = true optimal cost to goal
- **Admissibility**: \(h(n) \leq h^*(n)\)
- **Consistency**: \(h(n) \leq c(n,n') + h(n')\)

---

## 📚 Recommended Reading
- Textbook: Chapter 3 (Sections 3.1–3.6)
- Moving AI Lab: https://www.movingai.com
- Interactive demos: PathFinding.js

---

**Author**: Álvaro Torralba  
**Course**: Machine Intelligence – Aalborg University, Fall 2025