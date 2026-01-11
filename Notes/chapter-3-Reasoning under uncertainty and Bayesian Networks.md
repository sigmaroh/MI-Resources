Chapter 3: Reasoning under Uncertainty - Study Notes
(Includes Key Concepts, Examples, Exercises & Solutions)

1. Introduction
Reasoning under uncertainty deals with making decisions when we lack complete knowledge.

Logic alone is insufficient for reasoning under uncertainty because:

It cannot weigh alternatives.

It cannot handle incomplete or probabilistic knowledge.

2. Probability Basics
Probability = degree of belief given current knowledge.

Random Variable (RV): Variable that defines possible worlds.

Distribution: 
P
(
A
)
P(A) maps each value 
a
a of RV 
A
A to a probability.

Joint Distribution: 
P
(
A
1
,
.
.
.
,
A
k
)
P(A 
1
​
 ,...,A 
k
​
 ) assigns probabilities to tuples of RV values.

Atomic Event: Complete assignment to all RVs.

Example:

P
(
H
e
a
d
a
c
h
e
)
=
⟨
T
r
u
e
:
0.9
,
F
a
l
s
e
:
0.1
⟩
P(Headache)=⟨True:0.9,False:0.1⟩
P
(
W
e
a
t
h
e
r
)
=
⟨
s
u
n
n
y
:
0.7
,
r
a
i
n
:
0.2
,
c
l
o
u
d
y
:
0.08
,
s
n
o
w
:
0.02
⟩
P(Weather)=⟨sunny:0.7,rain:0.2,cloudy:0.08,snow:0.02⟩
3. Conditional Probability
P
(
p
∣
e
)
=
P
(
p
∧
e
)
P
(
e
)
(
P
(
e
)
≠
0
)
P(p∣e)= 
P(e)
P(p∧e)
​
 (P(e)

=0)
Posterior probability of 
p
p given evidence 
e
e.

Updates belief when new evidence is obtained.

Example:
Given:

P
(
t
o
o
t
h
a
c
h
e
)
=
0.2
P(toothache)=0.2

P
(
c
a
v
i
t
y
)
=
0.2
P(cavity)=0.2

P
(
t
o
o
t
h
a
c
h
e
∧
c
a
v
i
t
y
)
=
0.12
P(toothache∧cavity)=0.12

Then:

P
(
c
a
v
i
t
y
∣
t
o
o
t
h
a
c
h
e
)
=
0.12
0.2
=
0.6
P(cavity∣toothache)= 
0.2
0.12
​
 =0.6
4. Bayes’ Rule
P
(
a
∣
b
)
=
P
(
b
∣
a
)
⋅
P
(
a
)
P
(
b
)
P(a∣b)= 
P(b)
P(b∣a)⋅P(a)
​
 
Used to invert conditional probabilities.

Causal probabilities (e.g., 
P
(
s
y
m
p
t
o
m
∣
c
a
u
s
e
)
P(symptom∣cause)) are often easier to assess than diagnostic probabilities (
P
(
c
a
u
s
e
∣
s
y
m
p
t
o
m
)
P(cause∣symptom)).

Example:

P
(
t
o
o
t
h
a
c
h
e
∣
c
a
v
i
t
y
)
=
0.6
P(toothache∣cavity)=0.6

P
(
c
a
v
i
t
y
)
=
0.2
P(cavity)=0.2

P
(
t
o
o
t
h
a
c
h
e
)
=
0.2
P(toothache)=0.2

P
(
c
a
v
i
t
y
∣
t
o
o
t
h
a
c
h
e
)
=
0.6
⋅
0.2
0.2
=
0.6
P(cavity∣toothache)= 
0.2
0.6⋅0.2
​
 =0.6
5. Independence & Conditional Independence
Independence: 
P
(
a
∧
b
)
=
P
(
a
)
⋅
P
(
b
)
P(a∧b)=P(a)⋅P(b)

Conditional Independence:
P
(
Z
1
,
Z
2
∣
Z
)
=
P
(
Z
1
∣
Z
)
⋅
P
(
Z
2
∣
Z
)
P(Z 
1
​
 ,Z 
2
​
 ∣Z)=P(Z 
1
​
 ∣Z)⋅P(Z 
2
​
 ∣Z)

Example:
Hair length and Height are not independent, but they are conditionally independent given Sex.

6. Bayesian Networks (BNs)
A BN is a directed acyclic graph (DAG) where:

Nodes = RVs.

Edges = conditional dependencies.

Each node has a CPT: 
P
(
X
i
∣
P
a
r
e
n
t
s
(
X
i
)
)
P(X 
i
​
 ∣Parents(X 
i
​
 )).

BN Example: Alarm System
RVs: Burglary, Earthquake, Alarm, JohnCalls, MaryCalls

CPTs encode:

P
(
A
l
a
r
m
∣
B
u
r
g
l
a
r
y
,
E
a
r
t
h
q
u
a
k
e
)
P(Alarm∣Burglary,Earthquake)

P
(
J
o
h
n
C
a
l
l
s
∣
A
l
a
r
m
)
P(JohnCalls∣Alarm)

P
(
M
a
r
y
C
a
l
l
s
∣
A
l
a
r
m
)
P(MaryCalls∣Alarm)

Joint distribution factorization:

P
(
B
,
E
,
A
,
J
,
M
)
=
P
(
B
)
⋅
P
(
E
)
⋅
P
(
A
∣
B
,
E
)
⋅
P
(
J
∣
A
)
⋅
P
(
M
∣
A
)
P(B,E,A,J,M)=P(B)⋅P(E)⋅P(A∣B,E)⋅P(J∣A)⋅P(M∣A)
7. Constructing BNs
Order variables: causes before effects.

Choose minimal parent set for each node to satisfy conditional independence.

Network size depends on variable ordering.

Size of BN:

size
(
B
N
)
=
∑
i
∣
D
i
∣
⋅
∏
X
j
∈
P
a
r
e
n
t
s
(
X
i
)
∣
D
j
∣
size(BN)= 
i
∑
​
 ∣D 
i
​
 ∣⋅ 
X 
j
​
 ∈Parents(X 
i
​
 )
∏
​
 ∣D 
j
​
 ∣
Much smaller than full joint distribution if each node has few parents.

8. Inference in BNs
Recover full joint from BN using chain rule:

P
(
X
1
,
.
.
.
,
X
n
)
=
∏
i
=
1
n
P
(
X
i
∣
P
a
r
e
n
t
s
(
X
i
)
)
P(X 
1
​
 ,...,X 
n
​
 )= 
i=1
∏
n
​
 P(X 
i
​
 ∣Parents(X 
i
​
 ))
Compute probabilities of queries given evidence.

9. Exercises & Solutions
Exercise 1: Conditional Probability
Given:

P
(
A
)
=
0.3
P(A)=0.3

P
(
B
)
=
0.4
P(B)=0.4

P
(
A
∧
B
)
=
0.1
P(A∧B)=0.1

Find 
P
(
A
∣
B
)
P(A∣B) and 
P
(
B
∣
A
)
P(B∣A).

Solution:

P
(
A
∣
B
)
=
0.1
0.4
=
0.25
P(A∣B)= 
0.4
0.1
​
 =0.25
P
(
B
∣
A
)
=
0.1
0.3
≈
0.333
P(B∣A)= 
0.3
0.1
​
 ≈0.333
Exercise 2: Bayes’ Rule
A disease affects 1% of population. A test is 95% accurate for diseased people and 90% accurate for healthy people.
If a person tests positive, what is the probability they have the disease?

Solution:
Let 
D
D = disease, 
T
+
T 
+
  = positive test.

P
(
D
)
=
0.01
,
P
(
T
+
∣
D
)
=
0.95
,
P
(
T
+
∣
¬
D
)
=
0.1
P(D)=0.01,P(T 
+
 ∣D)=0.95,P(T 
+
 ∣¬D)=0.1
P
(
T
+
)
=
P
(
T
+
∣
D
)
P
(
D
)
+
P
(
T
+
∣
¬
D
)
P
(
¬
D
)
=
0.95
⋅
0.01
+
0.1
⋅
0.99
=
0.1085
P(T 
+
 )=P(T 
+
 ∣D)P(D)+P(T 
+
 ∣¬D)P(¬D)=0.95⋅0.01+0.1⋅0.99=0.1085
P
(
D
∣
T
+
)
=
0.95
⋅
0.01
0.1085
≈
0.0876
(
8.76
%
)
P(D∣T 
+
 )= 
0.1085
0.95⋅0.01
​
 ≈0.0876(8.76%)
Exercise 3: BN Construction
Given RVs: Rain, Sprinkler, WetGrass.

WetGrass is true if either Rain or Sprinkler is true.

Rain and Sprinkler are independent.

Draw the BN and write CPTs.

Solution:

Nodes: Rain (R), Sprinkler (S), WetGrass (W)

Edges: 
R
→
W
R→W, 
S
→
W
S→W

CPT for 
W
W:
P
(
W
=
t
r
u
e
∣
R
=
t
r
u
e
,
S
=
t
r
u
e
)
=
1
P(W=true∣R=true,S=true)=1
P
(
W
=
t
r
u
e
∣
R
=
t
r
u
e
,
S
=
f
a
l
s
e
)
=
1
P(W=true∣R=true,S=false)=1
P
(
W
=
t
r
u
e
∣
R
=
f
a
l
s
e
,
S
=
t
r
u
e
)
=
1
P(W=true∣R=false,S=true)=1
P
(
W
=
t
r
u
e
∣
R
=
f
a
l
s
e
,
S
=
f
a
l
s
e
)
=
0
P(W=true∣R=false,S=false)=0

