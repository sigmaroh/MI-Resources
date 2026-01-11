# Introduction to Artificial Intelligence & Autonomous Agents — Exam Study Notes

## Table of Contents

1. [Course Information](#course-information)
2. [What is AI?](#what-is-ai)
3. [AI History & Subfields](#ai-history--subfields)
4. [Intelligent Agents](#intelligent-agents)
5. [Problem Representation](#problem-representation)
6. [Exercises & Solutions](#exercises--solutions)
7. [Exam Tips](#exam-tips)

---

## 1. Course Information

**Course Structure**

- **Lectures:** Monday 8:15–12:00 (first half: lecture, second half: exercises)
- **Exam:** Written Moodle questionnaire in January

**Main Textbook:**  
Poole & Mackworth — *Artificial Intelligence: Foundations of Computational Agents*

**Reference Book:**  
Russell & Norvig — *Artificial Intelligence: A Modern Approach*

**Study Materials:**
- Background slides: Pre-lecture reading
- Pre-handouts: Slides for note-taking
- Post-handouts: Complete study material
- **Exercises:** *Critical for exam preparation*

---

## 2. What is AI?

### Common Misconceptions

```python
# MISCONCEPTION 1: AI = Mimicking Humans
# Reality: AI doesn't need to mimic human cognition
# Example: Airplanes don't fly like birds

# MISCONCEPTION 2: AI = Machine Learning/Neural Networks
# Reality: ML is one technique among many
# Other techniques: Search, Reasoning, Planning, CSP

# MISCONCEPTION 3: AI = Data Analysis
# Reality: Can also learn from interaction (reinforcement learning)

# MISCONCEPTION 4: AI = No Human Interaction
# Reality: Human-AI interaction is important subfield
```

### Formal Definitions

> **Poole & Mackworth:**  
> "AI is the field that studies the synthesis and analysis of computational agents that act intelligently."

**Russell & Norvig — Four Categories:**

|               | Humanly        | Rationally                 |
|---------------|---------------|----------------------------|
| **Thinking**  | Cognitive Science | Logics, Machine Learning    |
| **Acting**    | Turing Test       | Applications                |

**The Turing Test**

- **Setup:** Interrogator communicates with human and machine via terminals.
- **Goal:** Machine "passes" if interrogator cannot distinguish which participant is the machine.
- **Limitations:** Tests observable behavior only, not actual internal cognitive processes.

**Winograd Schema (scientific alternative):**

> "The city councilmen refused the demonstrators a permit because they feared/advocated violence."

- Who *feared* violence? → City councilmen  
- Who *advocated* violence? → Demonstrators

### AI Success Stories

- Deep Blue (1997): Chess champion
- AlphaGo/AlphaZero (2016–2017): Go and Chess world champion
- AlphaFold (2020): Protein folding prediction
- Watson (2011): Jeopardy! champion
- GPT-3/4 (2020+): Advanced language models
- DARPA Challenge (2005): Autonomous driving
- ImageNet (2012): Image classification breakthrough

---

## 3. AI History & Subfields

### Historical Timeline

```python
1956: Dartmouth Workshop — "Artificial Intelligence" term coined
1960s: Early AI in microworlds
1970s: Knowledge-based systems
1980s: Expert systems (commercial AI success)
Late 1980s: "AI Winter" (disappointment, reduced funding)
1990s–2000s: Formalization, mathematical approaches
2010s: Neural networks resurgence
2020s: Language models, generative AI
```

### Subfields of AI

```
Artificial Intelligence
├── Machine Learning
│   ├── Deep Learning
│   ├── Reinforcement Learning
│   └── Classification/Regression
├── Reasoning
│   ├── CSP & SAT
│   ├── Knowledge Representation
│   └── Epistemic Reasoning
├── Decision-Making
│   ├── Search
│   ├── Planning
│   └── Multi-agent Systems
├── Perception
│   ├── Computer Vision
│   ├── Natural Language Processing
│   └── Speech Recognition
└── Ethics
    ├── Trustworthy AI
    ├── Explainability
    └── Human-AI Interaction
```

### Symbolic vs. Subsymbolic AI

| Aspect      | **Symbolic AI**                       | **Subsymbolic AI**                       |
|-------------|---------------------------------------|------------------------------------------|
| Approach    | Explicit knowledge, rules, logic      | Pattern recognition, neural networks     |
| Example     | "A chair has a seat and back"         | Learns 'chair' from many examples        |
| Pros        | Explainable, verifiable, instant      | High performance, handles complexity     |
| Cons        | Modeling cost, scalability            | Black box, needs data, training time     |
| Era         | Pre-2012 dominant                     | Post-2012 dominant                       |

---

## 4. Intelligent Agents

### Agent Definition

- **Agent:** System that perceives its environment through sensors and acts through actuators.
- **Percepts:** Inputs from sensors.
- **Actions:** Outputs via actuators.

### PEAS Framework

- **P:** Performance measure
- **E:** Environment
- **A:** Actuators
- **S:** Sensors

**Example: Medical Diagnosis System**

|    |                              |
|----|------------------------------|
| P  | Accuracy of diagnosis        |
| E  | Patient, medical staff       |
| A  | Display questions/diagnoses  |
| S  | Keyboard (entry of symptoms) |

---

### Rational Agents

- **Definition:** Agent that selects actions to maximize expected performance measure.

**Formula:**

```
Rational Action = argmaxₐ E[Performance | Percepts, Knowledge]
```

#### Key Distinctions

- *Rational ≠ Omniscient*: Operates with available knowledge, not complete information.
- *Rational ≠ Perfect*: May have sensor/actuator or computational limitations.
- **Bounded Rationality:** Considers computational/resource constraints.

---

### Environment Properties

| Property       | Options               | Description                                |
|----------------|----------------------|--------------------------------------------|
| Observability  | Fully / Partially     | Does agent see all relevant aspects?       |
| Determinism    | Deterministic / Stochastic | Is next state predictable?           |
| Episodicity    | Episodic / Sequential | Is each step independent?                  |
| Dynamics       | Static / Dynamic      | Does environment change during decision?   |
| Discreteness   | Discrete / Continuous | Finite vs. infinite state/action spaces    |
| Agents         | Single / Multi        | Number of agents                           |

**Example Analysis: Chess**

- **Observable:** Fully (perfect information)
- **Deterministic:** Strategic (depends on both agents' moves)
- **Episodic:** Sequential (moves affect the future)
- **Static:** Does not change except for agents' actions (static)
- **Discrete:** Finite positions/moves
- **Agents:** Multi-agent (two-player)

---

## 5. Problem Representation

### Representation–Interpretation Cycle

```
Real-world Problem → Representation → Computation → Interpretation → Solution
```

### Three Representation Levels

- **State-based:**  
  Represent individual states (e.g., configurations in a game)

- **Feature-based:**  
  Variables with values (e.g., egg=whole, butter_in=pan)

- **Relational:**  
  Objects and the relationships between them (e.g., in(butter, pan))

**Example: Cooking Problem**

```python
# State-based: S1, S2, S3, ... (abstract states)
# Feature-based:
#   egg ∈ {whole, broken}
#   butter_in ∈ {pan, plate, table}
#   egg_in ∈ {pan, plate, table}
#   3 variables × 3 values each = 18 possible states

# Relational:
#   state(egg, whole)
```
