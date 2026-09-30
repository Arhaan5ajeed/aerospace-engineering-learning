# NumPy Vectors Operations and Broadcasting

**Objective:** Learn how to represent and manipulate engineering vectors and using NumPy and understand broadcasting that will form the foundation for aerospace mathematics and simulation.

---

## 1. What is a Vector?

A vector is a quantity represented by multiple numerical components.

Examples in aerospace engineering:

- Velocity: `[Vx, Vy, Vz]`
- Position: `[x, y, z]`
- Acceleration: `[ax, ay, az]`
- Force: `[Fx, Fy, Fz]`

In NumPy, a vector can be represented using a one-dimensional array.

```python
import numpy as np

velocity = np.array([100, 20, -5])
```

Here:

- `100` → x-component
- `20` → y-component
- `-5` → z-component

---

## 2. Vector Addition

Two vectors can be added component by component.

\[
\mathbf{A} + \mathbf{B}
=
[A_x+B_x,\ A_y+B_y,\ A_z+B_z]
\]

```python
A = np.array([10, 20, 30])
B = np.array([5, 10, 15])

C = A + B

print(C)
```

Output:

```text
[15 30 45]
```

### Engineering interpretation

If `A` and `B` are two force vectors, `C` is their resultant force vector.

---

## 3. Vector Subtraction

```python
A = np.array([10, 20, 30])
B = np.array([5, 10, 15])

C = A - B
```

Result:

```text
[5 10 15]
```

The subtraction is also performed component by component.

---

## 4. Scalar Multiplication

A vector can be multiplied by a scalar.

\[
k\mathbf{A}
=
[kA_x,\ kA_y,\ kA_z]
\]

```python
velocity = np.array([10, 20, 30])

new_velocity = 2 * velocity

print(new_velocity)
```

Output:

```text
[20 40 60]
```

This is useful when scaling physical quantities.

---

## 5. Element-wise Multiplication

NumPy also allows two arrays of the same shape to be multiplied element by element.

```python
A = np.array([2, 3, 4])
B = np.array([5, 6, 7])

C = A * B

print(C)
```

Output:

```text
[10 18 28]
```

Important:

`A * B` is **not** the mathematical vector dot product.

It is element-wise multiplication.

---

# 6. Vector Magnitude

The magnitude of a vector is:

\[
|\mathbf{A}| =
\sqrt{A_x^2+A_y^2+A_z^2}
\]

For:

```python
A = np.array([3, 4, 0])
```

we can calculate:

```python
magnitude = np.linalg.norm(A)

print(magnitude)
```

Output:

```text
5.0
```

The `np.linalg` module contains many linear-algebra operations.

---

# 7. Vector Normalisation

A unit vector has magnitude 1.

To normalise a vector:

\[
\hat{\mathbf{A}} =
\frac{\mathbf{A}}{|\mathbf{A}|}
\]

```python
A = np.array([3, 4, 0])

magnitude = np.linalg.norm(A)

unit_vector = A / magnitude

print(unit_vector)
```

Output:

```text
[0.6 0.8 0. ]
```

«A unit vector preserves direction but has magnitude 1.»

This becomes extremely important later when dealing with coordinate systems, forces, velocities, and attitude.

---

# 8. Broadcasting

Broadcasting is one of the most useful NumPy features.

It allows NumPy to perform operations between arrays of compatible shapes without manually repeating values.

Example:

```python
velocity = np.array([50, 100, 150, 200])

velocity_kmh = velocity * 3.6
```

The scalar `3.6` is effectively applied to every element.

```text
[50, 100, 150, 200]
        × 3.6
        ↓
[180, 360, 540, 720]
```

No loop is required.

---

# 9. Broadcasting with Two Arrays

Broadcasting can also work with arrays of compatible shapes.

```python
forces = np.array([100, 200, 300])
areas = np.array([2, 4, 5])

pressure = forces / areas
```

Each force is divided by the corresponding area.

\[
P = \frac{F}{A}
\]

---

# 10. Broadcasting with a Matrix

Suppose:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

and:

```python
B = np.array([10, 20, 30])
```

Then:

```python
C = A + B
```

NumPy broadcasts `B` across each row.

Result:

```text
[[11 22 33]
 [14 25 36]]
```

This is extremely useful when applying the same operation across multiple engineering datasets.

---

# 11. Shape Matters

Always understand the shape of your arrays.

```python
A.shape
```

For:

```text
[[1, 2, 3],
 [4, 5, 6]]
```

the shape is:

```text
(2, 3)
```

Meaning:

- 2 rows
- 3 columns

For:

```python
B = np.array([10, 20, 30])
```

the shape is:

```text
(3,)
```

Understanding shapes is essential because many NumPy operations depend on compatible dimensions.

---

# 12. Engineering Example — Velocity Vector

```python
import numpy as np

velocity = np.array([120, 40, -10])

speed = np.linalg.norm(velocity)

unit_velocity = velocity / speed

print("Velocity vector:", velocity)
print("Speed:", speed)
print("Unit velocity vector:", unit_velocity)
```

This is a simple but genuine aerospace-style vector operation.

---

# PRACTICAL TASK

Create:

```text
python/codes/numpy/day9_vector_operations.py
```

Build a **3D Aerospace Vector Calculator**.

It should:

1. Accept two 3D vectors from the user.
2. Add the vectors.
3. Subtract the vectors.
4. Multiply one vector by a scalar.
5. Calculate the magnitude of each vector.
6. Calculate the unit vector of each vector.
7. Demonstrate broadcasting by applying a scalar to an array.

Example concept:

```text
Vector A: [100, 20, -5]
Vector B: [30, -10, 15]

A + B
A - B
2 × A

|A|
|B|

Unit A
Unit B
```

### challenge

Use NumPy operations rather than manually writing loops for the vector calculations.

---

# Completion Checklist

## Day 9

□ Understand vectors  
□ Vector addition/subtraction  
□ Scalar multiplication  
□ Element-wise operations  
□ Vector magnitude  
□ Unit vectors  
□ Broadcasting  
□ Understand array shapes  
□ Complete `day9_vector_operations.py`
