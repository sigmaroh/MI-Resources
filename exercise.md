# Mean Squared Error (MSE)

## Definition
**Mean Squared Error (MSE)** is a common loss function used in regression problems to measure the average squared difference between predicted values and actual observed values.

## Formula
Mean Squared Error (MSE) is calculated as:

MSE = (1/n) × Σ(yᵢ - ŷᵢ)²

Where:
- n = number of data points
- yᵢ = actual value for the i-th data point
- ŷᵢ = predicted value for the i-th data point

## Calculation Steps
1. **Compute predictions** using your model
2. **Calculate errors**: eᵢ = yᵢ - ŷᵢ
3. **Square each error**: (eᵢ)²
4. **Sum all squared errors**
5. **Divide by n** to get the average

## Example
Given predictions and actual values:
- Predicted: \([5, -1, 5, 2, -3]\)
- Actual: \([4, 2, 1, 3, -1]\)

**Errors**: \([-1, 3, -4, 1, 2]\)  
**Squared errors**: \([1, 9, 16, 1, 4]\)  
**Sum**: \(31\)  
**MSE**: \(31 / 5 = 6.2\)

## Properties
- **Always non-negative** (squares are ≥ 0)
- **Penalizes large errors more** (due to squaring)
- **Differentiable everywhere** (useful for gradient-based optimization)
- Measured in **squared units** of the original data

## Use Cases
- Evaluating regression model performance
- Training machine learning models (as a loss function)
- Comparing different regression models
- Hyperparameter tuning

## Interpretation
- Lower MSE = better model fit
- MSE = 0 means perfect predictions
- Higher MSE indicates larger prediction errors


# Linear Regression MSE Calculation

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


## 📊 Data and Parameters
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

## 🔢 Predicted Values (ŷ)
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

## 📈 Error Calculation
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

## 🧮 MSE Calculation
**Sum of squared errors:** 1 + 9 + 16 + 1 + 4 = 31

**MSE formula:**  
MSE = (1/n) × Σ(y - ŷ)²  
MSE = 31 ÷ 5 = **6.2**

## 📋 Final Results
ŷ of first row: **5**  
ŷ of second row: **-1**  
ŷ of third row: **5**  
ŷ of fourth row: **2**  
ŷ of fifth row: **-3**  

**Mean Squared Error (MSE) for the model: 6.2**