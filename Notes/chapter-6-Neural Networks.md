Neural Networks - Exam Study Notes
Table of Contents
1. Linear Regression Recap

2. Gradient Descent

3. Neural Networks Architecture

4. Backpropagation Algorithm

5. Discrete Attributes & Classification

6. Expressive Power

7. Exercises with Solutions

8. Exam Tips

1. Linear Regression Recap
Basic Formula
text
ŷ = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ
or in vector form: ŷ = w·x

Sum Squared Error (SSE)
text
SSE = Σ(yᵢ - ŷᵢ)²
Error function: E(w) = ½ Σ(yᵢ - w·xᵢ)²
Multiplied by ½ to simplify derivatives

Convex function → one global minimum

Notation
X: Input matrix (M×N, M examples, N features)

y: Target vector (M×1)

w: Parameter/weight vector (N×1)

o or ŷ: Predicted output vector

2. Gradient Descent
Basic Gradient Descent
Goal: Minimize error function E(w) by updating weights in direction of steepest descent

Update Rule:

text
w := w - α∇E(w)
where α = learning rate (hyperparameter)

For Linear Regression (SSE):

text
∂E/∂wⱼ = Σ(yᵢ - w·xᵢ)(-xᵢⱼ)
Algorithm
text
1. Initialize w randomly
2. Repeat until convergence:
   a. Compute gradient ∇E(w)
   b. Update: w := w - α∇E(w)
Stochastic Gradient Descent (SGD)
Uses single example (or mini-batch) instead of full dataset

Update rule per example k:

text
∂E/∂wⱼ = (yₖ - w·xₖ)(-xₖⱼ)
Faster per iteration, more iterations needed

Can escape local minima better

Properties
Linear Regression: SSE is convex → converges to global minimum

Neural Networks: SSE non-convex → may converge to local minima

Learning rate α: Too small → slow convergence, too large → overshooting

3. Neural Networks Architecture
Single Neuron (Perceptron)
text
Output = activation_function(Σ(wᵢxᵢ) + bias)
Bias: w₀ with input always = 1

Two steps: Weighted sum → Activation function

Activation Functions
Function	Formula	Range	Derivative	Use Case
Sigmoid	σ(x) = 1/(1+e⁻ˣ)	(0,1)	σ(x)(1-σ(x))	Hidden layers
ReLU	max(0,x)	[0,∞)	0 if x≤0, 1 if x>0	Hidden layers
Identity	f(x)=x	(-∞,∞)	1	Output layer (regression)
Sign	sign(x)	{-1,1}	0 (not differentiable)	Classification
Multi-Layer Perceptron (MLP)
text
Input Layer → Hidden Layer(s) → Output Layer
Feedforward: Compute layer by layer

Each neuron: Weighted sum of previous layer outputs

Universal approximation: 1+ hidden layers can approximate any continuous function

Forward Propagation Example
Given:

Input: I₁=1, I₂=0

Weights: all = 0.1

Activation: sigmoid

Architecture: 2 input → 1 hidden → 1 output

text
Hidden neuron H:
  input = 1*0.1 + 0*0.1 + 1*0.1 = 0.2
  o_H = σ(0.2) = 1/(1+e⁻⁰·²) ≈ 0.5498

Output neuron O:
  input = 1*0.1 + 0.5498*0.1 = 0.15498
  o_O = σ(0.15498) ≈ 0.5387
4. Backpropagation Algorithm
Error Terms (δ)
For output neuron with sigmoid:

text
δₒ = oₒ(1-oₒ)(y - oₒ)
For hidden neuron:

text
δₕ = oₕ(1-oₕ) Σ(wₕₖ·δₖ)  [sum over neurons k it connects to]
Weight Update Rule
text
wₐₑⁿᵉʷ = wₐₑᶜᵘʳʳᵉⁿᵗ + α·δ₆·xₐ₆
where:

α = learning rate

δ₆ = error term of neuron b

xₐ₆ = input to neuron b via connection from a

Backpropagation Steps
text
1. Forward pass: Compute all outputs oᵢ
2. Compute output errors δ for output layer
3. Backpropagate: Compute δ for hidden layers (backwards)
4. Update weights using: w += α·δ·input
5. Repeat until convergence
Example Calculation
Given: Target y=1, α=0.3, o_O=0.53867

text
δ_O = o_O(1-o_O)(y-o_O)
    = 0.53867×(1-0.53867)×(1-0.53867)
    ≈ 0.1146

Update w_O (bias to output):
w_O_new = 0.1 + 0.3×0.1146×1 = 0.13438

Update w_HO (hidden to output):
w_HO_new = 0.1 + 0.3×0.1146×0.5498 ≈ 0.1189
5. Discrete Attributes & Classification
Encoding Discrete Variables
1. Numerical Encoding (not recommended for nominal data):

text
True/False → 1/0
Low/Medium/High → 0/1/2
Kellogs/Nabisco/Bells → 0/1/2
Problem: Implies ordinal relationships that don't exist

2. Indicator Variables (One-Hot Encoding):

text
Manufacturer ∈ {Kellogs, Nabisco, Bells}
→ Create 3 binary features:
   M_Kellogs, M_Nabisco, M_Bells
Example: Kellogs → [1, 0, 0]
Neural Networks for Classification
Multi-class classification:

One output neuron per class

Use sigmoid or softmax activation

Predict class with highest output value

Example: Handwritten digit recognition (0-9)

10 output neurons

Input: 28×28 = 784 pixel values

Hidden layers extract features

Output: probability distribution over digits

6. Expressive Power
Perceptron (Single Neuron)
Can represent linearly separable functions only:

AND: ✓ (w = [-1, 1, 1])

OR: ✓ (w = [1, 1, 1])

XOR: ✗ (not linearly separable)

Decision boundary: Hyperplane in n-dimensional space

Multi-Layer Networks
Universal Approximation Theorem:
Any continuous function f: [0,1]ⁿ → [0,1] can be approximated arbitrarily well by a neural network with:

At least 1 hidden layer

Finite number of neurons

Non-linear activation function

Example: XOR with 2-layer network

text
XOR = (X₁ ∧ ¬X₂) ∨ (¬X₁ ∧ X₂)
H₁ = X₁ ∧ ¬X₂
H₂ = ¬X₁ ∧ X₂
Output = H₁ ∨ H₂
Depth vs Width
Depth (more layers): Can represent complex functions more efficiently

Width (more neurons per layer): Alternative but may require exponentially more neurons

Feature reuse: Hidden neurons shared across outputs

7. Exercises with Solutions
Exercise 1: Gradient Descent for Linear Regression
Problem: Given data points (1,2), (2,3), (3,5), initial w=[0,0], α=0.1, perform one iteration of gradient descent.

Solution:

text
Data: x=[1,2,3], y=[2,3,5], M=3
Model: ŷ = w₀ + w₁x

Initial: w₀=0, w₁=0
Predictions: ŷ = [0,0,0]

Gradient:
∂E/∂w₀ = Σ(yᵢ-ŷᵢ)(-1) = (2-0)(-1)+(3-0)(-1)+(5-0)(-1) = -10
∂E/∂w₁ = Σ(yᵢ-ŷᵢ)(-xᵢ) = (2)(-1)+(3)(-2)+(5)(-3) = -23

Update:
w₀_new = 0 - 0.1×(-10) = 1
w₁_new = 0 - 0.1×(-23) = 2.3
Exercise 2: Forward Propagation
Problem: Network: 2 inputs → 1 hidden (sigmoid) → 1 output (identity)
Weights: w_IH = [[0.2,-0.3],[0.4,0.1]], w_HO = [0.5,-0.6]
Bias: b_H = 0.1, b_O = -0.2
Input: [0.5, 0.8]

Solution:

text
Hidden layer:
z_H = b_H + x₁w₁₁ + x₂w₁₂
     = 0.1 + 0.5×0.2 + 0.8×(-0.3) = 0.1 + 0.1 - 0.24 = -0.04
o_H = σ(-0.04) = 1/(1+e⁰·⁰⁴) ≈ 0.4900

Output:
z_O = b_O + o_H×w_HO
     = -0.2 + 0.4900×0.5 = -0.2 + 0.245 = 0.045
o_O = identity(0.045) = 0.045
Exercise 3: Backpropagation Step
Problem: Continue from Exercise 2, with target y=1, α=0.1, sigmoid for output too.

Solution:

text
Given: o_O = σ(0.045) ≈ 0.5112, o_H ≈ 0.4900

1. Output error δ_O:
δ_O = o_O(1-o_O)(y-o_O)
    = 0.5112×(1-0.5112)×(1-0.5112)
    ≈ 0.5112×0.4888×0.4888 ≈ 0.1222

2. Update w_HO (hidden→output):
Δw_HO = α×δ_O×o_H = 0.1×0.1222×0.4900 ≈ 0.0060
w_HO_new = 0.5 + 0.0060 = 0.5060

3. Update bias b_O:
Δb_O = α×δ_O×1 = 0.1×0.1222 = 0.0122
b_O_new = -0.2 + 0.0122 = -0.1878

4. Hidden error δ_H:
δ_H = o_H(1-o_H)×w_HO×δ_O
    = 0.4900×(1-0.4900)×0.5×0.1222
    ≈ 0.4900×0.5100×0.5×0.1222 ≈ 0.0153

5. Update weights w_IH:
For w₁₁ (input1→hidden):
Δw₁₁ = α×δ_H×x₁ = 0.1×0.0153×0.5 ≈ 0.000765
w₁₁_new = 0.2 + 0.000765 = 0.200765

Similarly for other weights...
Exercise 4: Perceptron Decision Boundary
Problem: Perceptron with weights w=[-2, 1, 1]. Find decision boundary equation and classify point (2,1).

Solution:

text
Decision boundary: w₀ + w₁x₁ + w₂x₂ = 0
-2 + 1×x₁ + 1×x₂ = 0
x₁ + x₂ = 2

Classify (2,1):
z = -2 + 1×2 + 1×1 = 1 > 0
Prediction: 1 (positive class)

Visual: Line x₂ = 2 - x₁
Exercise 5: XOR Network Design
Problem: Design a 2-layer network to compute XOR.

Solution:

text
XOR = (X₁ ∧ ¬X₂) ∨ (¬X₁ ∧ X₂)

Network architecture:
Input: X₁, X₂
Hidden layer (2 neurons):
  H₁ = X₁ ∧ ¬X₂ (weights: [0.5, -0.5, -0.2])
  H₂ = ¬X₁ ∧ X₂ (weights: [-0.5, 0.5, -0.2])
Output:
  O = H₁ ∨ H₂ (weights: [0, 1, 1, -0.5])

With sigmoid approximating step function.
8. Exam Tips
Key Concepts to Memorize
Gradient descent update rule

Backpropagation weight update formula

Activation functions and derivatives

Indicator variable encoding

Universal approximation theorem

Perceptron limitations (linear separability)

Common Calculations
Forward propagation: Layer-by-layer computation

Error calculation: SSE, δ terms

Weight updates: Using δ and learning rate

Decision boundaries: From weights to equation

Algorithm Steps
Gradient Descent:

text
1. Initialize weights
2. Forward pass: compute predictions
3. Compute error/SSE
4. Compute gradients
5. Update weights: w -= α×gradient
6. Repeat until convergence
Backpropagation:

text
1. Forward pass: compute all activations
2. Compute output δ
3. Backward pass: compute hidden δ
4. Update all weights
5. Repeat
Important Properties
Sigmoid derivative: σ(x)(1-σ(x))

Linear regression SSE: Convex → global minimum

NN SSE: Non-convex → local minima possible

Learning rate: Critical for convergence

Vanishing gradient: Deep networks with sigmoid

Typical Exam Questions
"Compute forward propagation for given network"

"Perform one backpropagation step"

"Design network for specific function"

"Explain why perceptron cannot compute XOR"

"Compare gradient descent vs stochastic GD"

"Convert categorical data for neural network"

Problem-Solving Strategy
text
For forward/backprop problems:
1. Write down all weights and activations
2. Compute layer by layer systematically
3. For derivatives, use chain rule step by step
4. Check dimensions match

For design problems:
1. Identify input/output dimensions
2. Consider necessary hidden layer size
3. Choose appropriate activation functions
4. Sketch network diagram
