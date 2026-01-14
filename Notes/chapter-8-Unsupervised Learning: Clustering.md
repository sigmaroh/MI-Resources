# Chapter 8: Unsupervised Learning: Clustering – Exam Notes

---

## 📘 1. Introduction to Unsupervised Learning

### Key Idea
- Learns patterns from **unlabeled data**.
- Useful when labeling is expensive or unknown.

### Example: Iris Dataset (Unlabeled)
| SL  | SW  | PL  | PW  |
|-----|-----|-----|-----|
| 5.1 | 3.5 | 1.4 | 0.2 |
| 4.9 | 3.0 | 1.4 | 0.2 |
| 6.3 | 2.9 | 6.0 | 2.1 |
| 6.3 | 2.5 | 4.9 | 1.5 |

**Goal**: Discover natural groupings without species labels.

---

## 📘 2. What is Clustering?

### Definition
A clustering of examples $E = e_1, \dots, e_N$ is:
- A set of cluster labels $C = \{ c_1, \dots, c_k \}$
- A cluster assignment function $ca : E \to C$

### Good Clustering Criterion
- **Maximize** between-cluster distance
- **Minimize** within-cluster distance

---

## 📘 3. k-Means Clustering Algorithm

### Assumptions
- Number of clusters $k$ is known.
- Distance measure $d(x_i, x_j)$ (e.g., Euclidean).
- Can compute centroid (mean) of points.

### Algorithm Steps
1. **Initialize**: Randomly choose $k$ points as centroids.
2. **Repeat**:
   - **Assignment**: Assign each point to nearest centroid.
   - **Update**: Recompute centroids as mean of assigned points.
3. **Until**: Centroids do not change.

### Example: k=3
- Iterative diagrams show centroids moving and points reassigning.

### Properties
- **Converges** (finite steps, SSE decreases).
- **Not optimal globally** (depends on initialization).
- **Solution**: Multiple random restarts.

---

## 📘 4. Evaluating Clustering

### Supervised Evaluation
- Uses external labels (e.g., Iris species).
- Compare clustering to ground truth.
- **Limitation**: Labels may not reflect natural clusters.

### Unsupervised Evaluation
- Uses only data and clustering result.
- Metrics: Silhouette score, Davies–Bouldin index.
- **Note**: No single best metric.

---

## 📘 5. Preprocessing for Clustering

### Outliers
- Can skew centroids.
- **Solution**: Detect and remove outliers before clustering.

### Normalization
- Needed when features have different scales.
- **Methods**:
  - **Min-Max**: $A' = \frac{A - \min(A)}{\max(A) - \min(A)}$
  - **Z-score**: $A' = \frac{A - \text{mean}(A)}{\text{std}(A)}$

---

## 📘 6. Soft Clustering & EM Algorithm

### Hard vs. Soft Clustering
- **Hard**: Each point belongs to one cluster.
- **Soft**: Each point has probabilities of belonging to each cluster.

### Model: Naive Bayes with Hidden Cluster Variable
- Use Naive Bayes to model $P(C | F_1, F_2, F_3)$.
- Cluster variable $C$ is hidden.

### Expectation-Maximization (EM) Steps
1. **Initialize** probabilities randomly.
2. **E-step**: Compute $P(C | \text{data})$ using current probabilities.
3. **M-step**: Update probabilities using weighted counts.
4. **Repeat** until convergence.

### Example with Discrete Features
Given:
- $P(C) = (0.6, 0.4)$
- Conditional probability tables for $F_1, F_2, F_3$
- Compute posteriors and update probabilities.

---

## 📘 7. Autoencoders for Unsupervised Learning

### Idea
- Train neural network to reconstruct input.
- **Encoder**: Compresses input to latent representation.
- **Decoder**: Reconstructs input from latent representation.

### Use Cases
- Dimensionality reduction.
- Generating new data (via decoder).
- Semi-supervised learning (pretrain on unlabeled data).

---

## 📘 8. Semi-Supervised Learning

### Scenario
- Some data labeled, most unlabeled.
- Combine supervised and unsupervised methods.

### Example with Autoencoders
1. Train autoencoder on all data.
2. Use latent features to train classifier on labeled subset.
3. Better performance with few labels.

---

## 📘 9. Summary of Key Points

| Concept | Description |
|---------|-------------|
| **Clustering** | Grouping similar data points without labels |
| **k-Means** | Partitional clustering using centroids |
| **EM Algorithm** | Soft clustering using probabilistic models |
| **Normalization** | Essential for features on different scales |
| **Autoencoders** | Neural networks for unsupervised representation learning |
| **Semi-Supervised** | Combines labeled and unlabeled data |

---

## 📝 Exercises & Solutions

### Exercise 1: k-Means by Hand
**Data**:
(2,3), (4,5), (7,8), (9,10), (12,13)
**k=2**, initial centroids: (2,3), (4,5)

**Step-by-Step**:
1. Assign points to nearest centroid.
2. Recompute centroids.
3. Repeat until stable.

**Solution**:
- Iteration 1: Clusters: {(2,3)}, {(4,5),(7,8),(9,10),(12,13)}  
  New centroids: (2,3), (8,9)
- Iteration 2: Clusters: {(2,3),(4,5)}, {(7,8),(9,10),(12,13)}  
  New centroids: (3,4), (9.33,10.33)
- Stabilizes.

---

### Exercise 2: EM with Naive Bayes
**Data** (binary features):
(F1,F2,F3): (t,t,t), (t,f,t), (t,f,f), (f,f,t)

**Given**:
- $P(C=\oplus)=0.6, P(C=\ominus)=0.4$
- $P(F1=t|C=\oplus)=0.6$, $P(F1=t|C=\ominus)=0.4$
- Similar for F2, F3.

**Compute** $P(C=\oplus | t,t,t)$:

$$
P(C=\oplus|t,t,t) \propto 0.6 \times (0.6)^3 = 0.1296
$$

$$
P(C=\ominus|t,t,t) \propto 0.4 \times (0.4)^3 = 0.0256
$$

Normalize:

$$
P(C=\oplus|t,t,t) = \frac{0.1296}{0.1296+0.0256} \approx 0.84
$$

---

### Exercise 3: Normalization
**Data**: Age=[20, 60, 30], Income=[50000, 200000, 80000]

**Apply Min-Max Normalization**:

Age: min=20, max=60  
- 20 → 0
- 60 → 1
- 30 → (30-20)/(60-20)=0.25

Income: min=50000, max=200000  
- 50000 → 0
- 200000 → 1
- 80000 → (80000-50000)/(200000-50000)=0.2

**Result**:
(0, 0), (1, 1), (0.25, 0.2)

---

## 📚 Recommended Reading
- “Artificial Intelligence: Foundations of Computational Agents” – Chapter 10.2
- Stanford CS229 Lecture Notes on Unsupervised Learning

---

**Author**: Álvaro Torralba  
**Course**: Machine Intelligence – Aalborg University, Fall 2024