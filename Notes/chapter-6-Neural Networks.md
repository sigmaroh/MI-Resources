# Neural Networks - Exam Study Notes

## Table of Contents
1. [Linear Regression Recap](#1-linear-regression-recap)
2. [Gradient Descent](#2-gradient-descent)
3. [Neural Networks Architecture](#3-neural-networks-architecture)
4. [Backpropagation Algorithm](#4-backpropagation-algorithm)
5. [Discrete Attributes & Classification](#5-discrete-attributes--classification)
6. [Expressive Power](#6-expressive-power)
7. [Exercises with Solutions](#7-exercises-with-solutions)
8. [Exam Tips](#8-exam-tips)

---

## 1. Linear Regression Recap

### Basic Formula

$$
\hat{y} = w_0 + w_1x_1 + w_2x_2 + \ldots + w_nx_n
$$

or in vector form:

$$
\hat{y} = w \cdot x
$$

---

### Sum Squared Error (SSE)

$$
SSE = \sum (y_i - \hat{y}_i)^2
$$

Error function:

$$
E(w) = \frac{1}{2} \sum (y_i - w \cdot x_i)^2
$$

*The factor ½ is for derivative simplification.*

- **Convex function** → one global minimum

---

### Notation

- **X**: Input matrix (M×N, M examples, N features)
- **y**: Target vector (M×1)
- **w**: Parameter/weight vector (N×1)
- **o or ŷ**: Predicted output vector

---

## 2. Gradient Descent

### Basic Gradient Descent

**Goal:** Minimize error function $E(w)$ by updating weights in direction of steepest descent.

**Update rule:**

$$
w := w - \alpha \nabla E(w)
$$

where $\alpha =$ learning rate (hyperparameter)

For Linear Regression (SSE):

$$
\frac{\partial E}{\partial w_j} = \sum (y_i - w \cdot x_i)(-x_{ij})
$$

#### Algorithm
1. Initialize w randomly
2. Repeat until convergence:
    - Compute gradient $\nabla E(w)$
    - Update: $w := w - \alpha \nabla E(w)$

---

### Stochastic Gradient Descent (SGD)

- Uses single example (or mini-batch) instead of all data.
- **Update per example k:**

$$
\frac{\partial E}{\partial w_j} = (y_k - w \cdot x_k)(-x_{kj})
$$

- Pros: Faster per-iteration, escapes local minima better
- Cons: More iterations/updates needed

#### Properties

- Linear Regression SSE: *Convex* → converges to global minimum
- Neural Networks SSE: *Non-convex* → may converge to local minima
- Learning rate $\alpha$: Too small → slow, too large → overshooting

---

## 3. Neural Networks Architecture

### Single Neuron (Perceptron)

$$
\text{Output} = \text{activation\_function}\left( \sum w_ix_i + \text{bias} \right)
$$

- Bias: $w_0$ with input always = 1
- Two steps: Weighted sum → Activation

---

### Activation Functions

| Function  | Formula                     | Range     | Derivative              | Use Case                |
|-----------|-----------------------------|-----------|-------------------------|-------------------------|
| Sigmoid   | $\sigma(x) = 1/(1+e^{-x})$| (0, 1)    | $\sigma(x)(1-\sigma(x))$ | Hidden layers        |
| ReLU      | $\max(0,x)$               | [0, ∞)    | 0 if x ≤ 0, 1 if x > 0  | Hidden layers           |
| Identity  | $f(x) = x$                | all ℝ     | 1                       | Output layer (regression)|
| Sign      | $\text{sign}(x)$          | {-1, 1}   | 0 (not diff.)           | Classification          |

---

### Multi-Layer Perceptron (MLP)

- **Structure:** Input Layer → Hidden Layer(s) → Output Layer
- **Feedforward:** Compute activations layer by layer
- **Universal approximation:** ≥1 hidden layer can approximate any continuous function

#### Forward Propagation Example

**Given:**  
Input: $I_1 = 1, I_2 = 0$  
Weights: all = 0.1  
Activation: sigmoid  
Architecture: 2 input → 1 hidden → 1 output

**Hidden neuron H:**  

$$
\text{input} = 1\times0.1 + 0\times0.1 + 1\times0.1 = 0.2\\
o_H = \sigma(0.2) = \frac{1}{1 + e^{-0.2}} \approx 0.5498
$$

**Output neuron O:**  

$$
\text{input} = 1\times0.1 + 0.5498\times0.1 = 0.15498\\
o_O = \sigma(0.15498) \approx 0.5387
$$

---

## 4. Backpropagation Algorithm

### Error Terms ($\delta$)

- **Output neuron** (sigmoid):

$$
\delta_o = o_o (1-o_o)(y - o_o)
$$

- **Hidden neuron:**

$$
\delta_h = o_h (1-o_h) \sum (w_{hk} \delta_k)
$$

(*sum over neurons k in the next layer*)

---

### Weight Update Rule

$$
w_{ab}^{\text{new}} = w_{ab}^{\text{current}} + \alpha \delta_b x_{ab}
$$

where:  
- $\alpha$ = learning rate  
- $\delta_b$ = error term at neuron b  
- $x_{ab}$ = input to neuron b from a

---

### Backpropagation Steps

1. Forward pass: Compute all outputs $o_i$
2. Compute output errors $\delta$ for output layer
3. Backpropagate: Compute $\delta$ for hidden layers (backwards)
4. Update weights: $w += \alpha \delta \text{ input}$
5. Repeat until convergence

---

### Example Calculation

**Given:** Target $y=1$, $\alpha=0.3$, $o_O=0.53867$

$$
\begin{align*}
\delta_O &= o_O(1-o_O)(y-o_O)\\
&= 0.53867 \times (1-0.53867) \times (1-0.53867) \\
&\approx 0.1146
\end{align*}
$$

Update $w_O$ (bias to output):  
$w_{O,\text{new}} = 0.1 + 0.3 \times 0.1146 \times 1 = 0.13438$

Update $w_{HO}$ (hidden-to-output):  
$w_{HO,\text{new}} = 0.1 + 0.3 \times 0.1146 \times 0.5498 \approx 0.1189$

---

## 5. Discrete Attributes & Classification

### Encoding Discrete Variables

1. **Numerical Encoding** (not recommended for nominal data):
    - True/False → 1/0
    - Low/Medium/High → 0/1/2
    - Kellogs/Nabisco/Bells → 0/1/2

    *Problem: Implies ordinal relationships that do not exist.*

2. **Indicator Variables (One-Hot Encoding):**

    - Manufacturer ∈ {Kellogs, Nabisco, Bells}
    - Create 3 binary features:  
        - $M_{Kellogs}$, $M_{Nabisco}$, $M_{Bells}$  
    - Example: Kellogs → [1, 0, 0]

---

### Neural Networks for Classification

- Multi-class: One output neuron per class
- Use sigmoid or softmax activation
- Predict class with highest output value

**Example:** Handwritten digit recognition (0–9)
- 10 output neurons
- Input: 28×28 = 784 pixels
- Hidden layers for feature extraction
- Output: Probability distribution over digits

---

## 6. Expressive Power

### Perceptron (Single Neuron)

- Can represent *linearly separable* functions only:
    - AND: ✓  ($w = [-1, 1, 1]$)
    - OR: ✓   ($w = [1, 1, 1]$)
    - XOR: ✗  (not linearly separable)

- **Decision boundary:** Hyperplane in n-dim space

---

### Multi-Layer Networks

**Universal Approximation Theorem:**  
Any continuous function $f: [0,1]^n \to [0,1]$ can be approximated arbitrarily well by a neural network with:
- At least 1 hidden layer
- Finite number of neurons
- Nonlinear activation function

**Example: XOR with 2-layer network**
- $XOR = (X_1 \wedge \neg X_2) \vee (\neg X_1 \wedge X_2)$
- $H_1 = X_1 \wedge \neg X_2$
- $H_2 = \neg X_1 \wedge X_2$
- Output = $H_1 \vee H_2$

---

### Depth vs Width

- **Depth** (more layers): Represent complex functions more efficiently
- **Width** (more neurons/layer): Alternative, but may require exponentially more neurons
- **Feature reuse:** Hidden neurons can be shared across outputs

---

## 7. Exercises with Solutions

---

### Exercise 1: Gradient Descent for Linear Regression

**Problem:**  
Given data points (1,2), (2,3), (3,5), initial $w = [0,0]$, $\alpha = 0.1$, perform one iteration of gradient descent.

**Solution:**

- Data: $x = [1,2,3]$, $y = [2,3,5]$, $M = 3$
- Model: $\hat{y} = w_0 + w_1x$

Initial: $w_0 = 0, w_1 = 0$  
Predictions: $\hat{y} = [0,0,0]$

- Gradient:
    - $\frac{\partial E}{\partial w_0} = \sum (y_i - \hat{y}_i)(-1) = (2-0)(-1)+(3-0)(-1)+(5-0)(-1) = -10$
    - $\frac{\partial E}{\partial w_1} = \sum (y_i - \hat{y}_i)(-x_i) = (2)(-1)+(3)(-2)+(5)(-3) = -23$

- Update:
    - $w_0 \gets 0 - 0.1 \times (-10) = 1$
    - $w_1 \gets 0 - 0.1 \times (-23) = 2.3$

---

### Exercise 2: Forward Propagation

**Problem:**  
Network: 2 inputs → 1 hidden (sigmoid) → 1 output (identity)  
Weights: $w_{IH} = [[0.2, -0.3], [0.4, 0.1]]$, $w_{HO} = [0.5, -0.6]$  
Bias: $b_H = 0.1$, $b_O = -0.2$  
Input: [0.5, 0.8]

**Solution:**

- Hidden layer:

$$
z_H = b_H + x_1w_{11} + x_2w_{12} = 0.1 + 0.5\times0.2 + 0.8\times(-0.3) = 0.1 + 0.1 - 0.24 = -0.04 \\
o_H = \sigma(-0.04) = \frac{1}{1+e^{0.04}} \approx 0.4900
$$

- Output:

$$
z_O = b_O + o_H \times w_{HO} = -0.2 + 0.4900 \times 0.5 = -0.2 + 0.245 = 0.045\\
o_O = \text{identity}(0.045) = 0.045
$$

---

### Exercise 3: Backpropagation Step

**Problem:**  
Continue from Exercise 2, target $y = 1$, $\alpha = 0.1$, sigmoid activation for output.

**Solution:**

Given: $o_O = \sigma(0.045) \approx 0.5112$, $o_H \approx 0.4900$

1. **Output error $\delta_O$:**

$$
\delta_O = o_O (1 - o_O) (y - o_O)\\
= 0.5112 \times 0.4888 \times 0.4888 \approx 0.1222
$$

2. **Update $w_{HO}$ (hidden→output):**

$$
\Delta w_{HO} = \alpha \delta_O o_H = 0.1 \times 0.1222 \times 0.4900 \approx 0.0060\\
w_{HO,new} = 0.5 + 0.0060 = 0.5060
$$

3. **Update bias $b_O$:**

$$
\Delta b_O = \alpha \delta_O \times 1 = 0.1 \times 0.1222 = 0.0122 \\
b_{O,new} = -0.2 + 0.0122 = -0.1878
$$

4. **Hidden error $\delta_H$:**

$$
\delta_H = o_H (1-o_H) w_{HO} \delta_O\\
= 0.4900 \times 0.5100 \times 0.5 \times 0.1222 \approx 0.0153
$$

5. **Update weights $w_{IH}$:**  
    For $w_{11}$ (input1→hidden):

$$
\Delta w_{11} = \alpha \delta_H x_1 = 0.1 \times 0.0153 \times 0.5 \approx 0.000765 \\
w_{11,\text{new}} = 0.2 + 0.000765 = 0.200765
$$

    Similarly for other weights...

---

### Exercise 4: Perceptron Decision Boundary

**Problem:** Perceptron with weights $w = [-2, 1, 1]$.  
Find decision boundary equation and classify (2, 1).

**Solution:**

- Decision boundary: $w_0 + w_1 x_1 + w_2 x_2 = 0$

$$
-2 + 1x_1 + 1x_2 = 0 \implies x_1 + x_2 = 2
$$

- Classify (2,1):
    $z = -2 + 1 \times 2 + 1 \times 1 = 1 > 0 \rightarrow 1$ (positive class)
- Visual: Line $x_2 = 2 - x_1$

---

### Exercise 5: XOR Network Design

**Problem:** Design a 2-layer network for XOR.

**Solution:**

- $XOR = (X_1 \wedge \neg X_2) \vee (\neg X_1 \wedge X_2)$
- Network:

    - **Input**: $X_1, X_2$
    - **Hidden (2 neurons):**
        - $H_1 = X_1 \wedge \neg X_2$ (weights: [0.5, -0.5, -0.2])
        - $H_2 = \neg X_1 \wedge X_2$ (weights: [-0.5, 0.5, -0.2])
    - **Output:**
        - $O = H_1 \vee H_2$ (weights: [0, 1, 1, -0.5])

- Use sigmoid to approximate step function.

---

## 8. Exam Tips

### Key Concepts to Memorize

- Gradient descent update rule
- Backpropagation weight update formula
- Activation functions and derivatives
- Indicator variable encoding
- Universal approximation theorem
- Perceptron limitations (linear separability)

---

### Common Calculations

- Forward propagation: layer-by-layer computation
- Error calculation: SSE, $\delta$ terms
- Weight updates: using $\delta$ and learning rate
- Decision boundaries: weights → equations

---

### Algorithm Steps

**Gradient Descent:**
1. Initialize weights
2. Forward pass: compute predictions
3. Compute error/SSE
4. Compute gradients
5. Update weights: $w := w - \alpha \times$ gradient
6. Repeat until convergence

**Backpropagation:**
1. Forward pass: compute activations
2. Compute output $\delta$
3. Backward pass: compute hidden $\delta$
4. Update all weights
5. Repeat

---

### Important Properties

- Sigmoid derivative: $\sigma(x)(1-\sigma(x))$
- Linear regression SSE: Convex → global minimum
- NN SSE: Non-convex → possible local minima
- Learning rate: critical for convergence
- Vanishing gradient: deep sigmoidal networks

---

### Typical Exam Questions

- “Compute forward propagation for a given network”
- “Perform one backpropagation step”
- “Design a network for a specific function”
- “Explain why a perceptron cannot compute XOR”
- “Compare gradient descent vs stochastic GD”
- “Convert categorical data for a neural network”

---

### Problem-Solving Strategy

**For forward/backprop problems:**
1. Write down all weights and activations
2. Compute layer by layer systematically
3. Use chain rule for derivatives
4. Check that dimensions match

**For design problems:**
1. Identify input/output dimensions
2. Choose an adequate hidden layer size
3. Select proper activation functions
4. Sketch the network diagram

---
