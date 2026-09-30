# Matrix Operations and Dot Product

«Objective: Learn how to represent and manipulate engineering vectors and matrices using NumPy, understand broadcasting, and perform dot-product/matrix operations that will form the foundation for aerospace mathematics and simulation.»

---

# DAY 10 — Matrix Operations & Dot Product

## 1. What is a Matrix?

A matrix is a rectangular arrangement of numbers.

Example:

\[
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\]

In NumPy:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])
```

Check its dimensions:

```python
print(A.shape)
```

Output:

```text
(2, 2)
```

---

# 2. Matrix Addition

Two matrices of the same shape can be added element by element.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A + B
```

Result:

```text
[[ 6  8]
 [10 12]]
```

---

# 3. Matrix Subtraction

```python
C = A - B
```

This also operates element by element.

---

# 4. Scalar Multiplication of a Matrix

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = 3 * A
```

Result:

```text
[[ 3  6]
 [ 9 12]]
```

---

# 5. Element-wise Matrix Multiplication

This is important:

```python
A * B
```

performs element-wise multiplication.

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A * B)
```

Output:

```text
[[ 5 12]
 [21 32]]
```

This is different from mathematical matrix multiplication.

---

# 6. Matrix Multiplication

Mathematical matrix multiplication is performed using:

```python
A @ B
```

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A @ B

print(C)
```

Result:

```text
[[19 22]
 [43 50]]
```

The `@` operator represents matrix multiplication in Python.

---

# 7. Dot Product

For two vectors:

\[
\mathbf{A}\cdot\mathbf{B}
=
A_xB_x+A_yB_y+A_zB_z
\]

Using NumPy:

```python
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

dot_product = np.dot(A, B)

print(dot_product)
```

Result:

```text
32
```

because:

\[
(1)(4)+(2)(5)+(3)(6)=4+10+18=32
\]

You can also use:

```python
A @ B
```

for the dot product of two 1D vectors.

---

# 8. Engineering Meaning of Dot Product

The dot product has major engineering applications.

For example, mechanical work:

\[
W = \mathbf{F}\cdot\mathbf{d}
\]

where:

- `F` = force vector
- `d` = displacement vector

Example:

```python
force = np.array([100, 0, 0])
displacement = np.array([5, 0, 0])

work = np.dot(force, displacement)

print(work)
```

Result:

```text
500 J
```

---

# 9. Dot Product and Angle Between Vectors

The relationship is:

\[
\mathbf{A}\cdot\mathbf{B}
=
|\mathbf{A}||\mathbf{B}|\cos\theta
\]

Therefore:

\[
\theta =
\cos^{-1}
\left(
\frac{\mathbf{A}\cdot\mathbf{B}}
{|\mathbf{A}||\mathbf{B}|}
\right)
\]

NumPy provides:

```python
np.arccos()
```

Remember that NumPy returns the angle in radians.

To convert to degrees:

```python
angle_degrees = np.degrees(angle_radians)
```

---

# 10. Matrix-Vector Multiplication

This is particularly important for aerospace engineering.

A matrix can transform a vector.

Example:

```python
A = np.array([
    [1, 0],
    [0, 1]
])

v = np.array([10, 20])

result = A @ v

print(result)
```

The result is another vector.

This concept will later become important for:

- Coordinate transformations
- Rotation matrices
- Aircraft attitude
- Navigation
- 6-DOF simulation
- Control systems
- Robotics

---

# 11. Transpose

The transpose changes rows into columns and columns into rows.

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.T)
```

Result:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# 12. Matrix Determinant

For a square matrix, NumPy can calculate the determinant.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

det_A = np.linalg.det(A)

print(det_A)
```

Result:

```text
-2.0
```

The determinant becomes important when studying matrix properties and solving systems of equations.

---

# 13. Matrix Inverse

For an invertible square matrix:

```python
A_inv = np.linalg.inv(A)
```

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

A_inv = np.linalg.inv(A)

print(A_inv)
```

«Do not use a matrix inverse blindly. Later, when solving engineering systems, we will learn why solving equations directly is usually preferable.»

---

# 14. Aerospace Example — Rotation Matrix

A simple 2D rotation matrix is:

\[
R =
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
\]

In NumPy:

```python
import numpy as np

theta = np.radians(90)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

v = np.array([1, 0])

rotated_v = R @ v

print(rotated_v)
```

The vector `[1, 0]` is rotated by 90°.

This is only an introduction. Rotation matrices will be studied properly later in the roadmap.

---

# MATRIX PRACTICAL TASK

Create:

```text
python/codes/numpy/day10_matrix_operations.py
```

Build a **Matrix & Vector Engineering Calculator**.

Your program should demonstrate:

1. Matrix addition
2. Matrix subtraction
3. Scalar multiplication
4. Element-wise multiplication
5. Matrix multiplication using `@`
6. Dot product of two vectors
7. Vector magnitude
8. Matrix transpose
9. Matrix-vector multiplication

### Required engineering application

Implement:

\[
W = \mathbf{F}\cdot\mathbf{d}
\]

where the user enters:

```text
Force vector: Fx Fy Fz
Displacement vector: dx dy dz
```

Then calculate the work done.

---

# Vector + Matrix Combined Mini-Project

If you finish both daily tasks early, combine them into:

```text
python/codes/numpy/
└── aerospace_vector_matrix_calculator.py
```

The program can contain:

```text
========== AEROSPACE VECTOR & MATRIX CALCULATOR ==========

1. Vector Addition
2. Vector Subtraction
3. Vector Magnitude
4. Unit Vector
5. Dot Product
6. Matrix Addition
7. Matrix Multiplication
8. Matrix-Vector Multiplication
9. Force × Displacement (Work)
10. Exit
```

Do this only after the individual Day 9 and Day 10 programs work.

---

# Key Concepts to Remember

| Concept | NumPy |
|---|---|
| Create vector | `np.array([...])` |
| Vector addition | `A + B` |
| Vector subtraction | `A - B` |
| Scalar multiplication | `k * A` |
| Element-wise multiplication | `A * B` |
| Vector magnitude | `np.linalg.norm(A)` |
| Dot product | `np.dot(A, B)` |
| Matrix multiplication | `A @ B` |
| Transpose | `A.T` |
| Determinant | `np.linalg.det(A)` |
| Inverse | `np.linalg.inv(A)` |
| Shape | `A.shape` |
| Dimensions | `A.ndim` |
| Broadcasting | Operations on compatible shapes |

---

# Completion Checklist

## Day 10

□ Understand matrices  
□ Matrix addition/subtraction  
□ Element-wise multiplication  
□ Matrix multiplication with `@`  
□ Dot product  
□ Matrix-vector multiplication  
□ Transpose  
□ Determinant  
□ Basic matrix inverse  
□ Complete `day10_matrix_operations.py`

## Final Check

□ I can explain the difference between `A * B` and `A @ B`  
□ I understand what a dot product physically represents  
□ I understand why array shape matters  
□ I can use broadcasting without writing unnecessary loops  
□ I can represent a 3D aerospace quantity as a NumPy vector
