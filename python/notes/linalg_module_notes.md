# Python / NumPy Notes: numpy.linalg

**Objective:** Learn the NumPy linalg module well enough to perform common linear-algebra operations required for engineering computation, numerical methods, dynamics, control systems, and future aerospace simulations.

---

## 1. What is numpy.linalg?

NumPy provides a dedicated linear-algebra module: `numpy.linalg`

Usually imported as:

```python
import numpy as np
```

and accessed through `np.linalg`.

The module provides functions for operations involving:
- Vectors
- Matrices
- Norms
- Determinants
- Matrix inverses
- Solving linear systems
- Eigenvalues
- Eigenvectors
- Least-squares problems
- Matrix decompositions

---

## 2. Why linalg Matters

You have already learned that NumPy arrays can represent:
- vectors
- matrices
- engineering datasets

The linalg module gives you mathematical tools for working with those structures.

The progression is:

```text
NumPy arrays
      ↓
Vectors
      ↓
Matrices
      ↓
Linear algebra
      ↓
Engineering mathematics
```

This becomes important later for:
- Aircraft dynamics
- State-space models
- Control systems
- Navigation
- Kalman filtering
- Coordinate transformations
- 6-DOF simulation

---

## 3. Vector Norm — `np.linalg.norm()`

The norm gives the magnitude of a vector.

```python
import numpy as np

v = np.array([3, 4])

magnitude = np.linalg.norm(v)

print(magnitude)
```

Output:
```
5.0
```

Mathematically:

$$ ||\mathbf{v}|| = \sqrt{v_1^2+v_2^2} $$

For a 3D vector:

```python
v = np.array([3, 4, 12])

magnitude = np.linalg.norm(v)

print(magnitude)
```

$$ ||\mathbf{v}|| = \sqrt{3^2+4^2+12^2} = 13 $$

---

## 4. Normalising a Vector

Once we know the magnitude:

```python
v = np.array([3, 4])

magnitude = np.linalg.norm(v)

unit_v = v / magnitude
```

Output:
```
[0.6 0.8]
```

Check:

```python
print(np.linalg.norm(unit_v))
```

Output:
```
1.0
```

This is useful for obtaining direction vectors.

---

## 5. Matrix Norm

`np.linalg.norm()` can also operate on matrices.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

result = np.linalg.norm(A)

print(result)
```

By default, for a matrix, this corresponds to the Frobenius norm.

$$ ||A||_F = \sqrt{ \sum_{i,j}|a_{ij}|^2 } $$

For this matrix:

$$ ||A||_F = \sqrt{1^2+2^2+3^2+4^2} = \sqrt{30} $$

---

## 6. Dot Product — `np.dot()`

Although `np.dot()` is not inside `np.linalg`, it is an important linear-algebra operation.

```python
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

result = np.dot(A, B)

print(result)
```

Output:
```
32
```

because:

$$ 1(4)+2(5)+3(6)=32 $$

For 1D vectors:

```python
A @ B
```

also gives the dot product.

---

## 7. Cross Product — `np.cross()`

Similarly, cross product is provided directly by NumPy rather than `np.linalg`.

```python
A = np.array([1, 0, 0])
B = np.array([0, 1, 0])

result = np.cross(A, B)

print(result)
```

Output:
```
[0 0 1]
```

Mathematically:

$$ \mathbf{i}\times\mathbf{j}=\mathbf{k} $$

This is particularly important for:

$$ \boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} $$

---

## 8. Determinant — `np.linalg.det()`

The determinant is calculated using:

```python
np.linalg.det(A)
```

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

det_A = np.linalg.det(A)

print(det_A)
```

Output:
```
-2.0
```

For a 2×2 matrix:

$$ \det(A)=ad-bc $$

---

## 9. Why Determinants Matter

The determinant helps determine whether a square matrix is singular.

If $\det(A)=0$, the matrix is singular.

If $\det(A)\neq0$, the matrix is non-singular and has an inverse.

In numerical Python, however, don't normally determine invertibility by comparing floating-point determinants to exactly zero without considering numerical tolerance.

---

## 10. Matrix Inverse — `np.linalg.inv()`

The inverse can be calculated using:

```python
np.linalg.inv(A)
```

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

A_inverse = np.linalg.inv(A)

print(A_inverse)
```

The inverse satisfies:

$$ AA^{-1}=I $$

You can verify it:

```python
print(A @ A_inverse)
```

You should obtain values very close to:
```
[[1. 0.]
 [0. 1.]]
```

Because floating-point arithmetic is approximate, you may see extremely small values such as `2.22044605e-16` instead of exactly zero.

---

## 11. Do Not Automatically Use `inv()`

Suppose you want to solve:

$$ A\mathbf{x}=\mathbf{b} $$

You might mathematically write:

$$ \mathbf{x}=A^{-1}\mathbf{b} $$

But in numerical computing, it is generally better to use:

```python
np.linalg.solve(A, b)
```

rather than explicitly calculating:

```python
np.linalg.inv(A) @ b
```

**Why?** Because `solve()` is designed specifically for solving the system and is generally more efficient and numerically preferable.

This is an important engineering programming habit.

---

## 12. Solving Linear Systems — `np.linalg.solve()`

Consider:

$$ 2x+y=5 $$

$$ x+3y=6 $$

Represent the equations as:

$$ A\mathbf{x}=\mathbf{b} $$

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

x = np.linalg.solve(A, b)

print(x)
```

The result contains `[x, y]`.

You can verify:

```python
print(A @ x)
```

which should return:
```
[5. 6.]
```

---

## 13. Why `solve()` Is Important for Engineering

Many engineering problems can eventually be expressed as:

$$ A\mathbf{x}=\mathbf{b} $$

Examples include:
- Structural systems
- Circuit systems
- Equilibrium equations
- Numerical methods
- Control systems
- State estimation
- Discretised differential equations

So `np.linalg.solve()` is one of the most practically important functions in the module.

---

## 14. Eigenvalues — `np.linalg.eig()`

Eigenvalues and eigenvectors satisfy:

$$ A\mathbf{v} = \lambda\mathbf{v} $$

NumPy can calculate them using:

```python
np.linalg.eig(A)
```

Example:

```python
A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
```

The function returns two objects:
- eigenvalues
- eigenvectors

---

## 15. Understanding the Eigenvalue Result

For:

$$ A= \begin{bmatrix} 2&0\\ 0&3 \end{bmatrix} $$

the eigenvalues are:

$$ \lambda_1=2 \qquad \lambda_2=3 $$

The corresponding eigenvectors describe special directions associated with those eigenvalues.

You do not need to master the theory today. The important thing is to understand what the function computes.

---

## 16. Symmetric Matrices — `np.linalg.eigh()`

For real symmetric or Hermitian matrices, NumPy provides:

```python
np.linalg.eigh(A)
```

Example:

```python
A = np.array([
    [2, 1],
    [1, 2]
])

eigenvalues, eigenvectors = np.linalg.eigh(A)

print(eigenvalues)
print(eigenvectors)
```

`eigh()` is preferable to the general `eig()` when you know the matrix is symmetric/Hermitian.

This becomes useful in areas such as:
- Structural mechanics
- Vibration analysis
- Principal axes
- Inertia-related calculations

---

## 17. Singular Value Decomposition — `np.linalg.svd()`

Singular Value Decomposition is written:

$$ A=U\Sigma V^T $$

```python
U, S, Vt = np.linalg.svd(A)
```

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

U, S, Vt = np.linalg.svd(A)

print("U:")
print(U)

print("Singular values:")
print(S)

print("V transpose:")
print(Vt)
```

SVD is widely used in:
- Numerical linear algebra
- Data analysis
- Least-squares problems
- Computer vision
- Dimensionality reduction
- Robotics

You do not need to derive SVD yet.

---

## 18. Least Squares — `np.linalg.lstsq()`

Sometimes a system has more equations than unknowns. For example:

$$ A\mathbf{x}\approx\mathbf{b} $$

Instead of finding an exact solution, we find the solution that minimises the error.

```python
A = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
])

b = np.array([2, 3, 4])

x, residuals, rank, singular_values = np.linalg.lstsq(
    A,
    b,
    rcond=None
)

print(x)
```

This is useful for fitting models to experimental data.

---

## 19. Matrix Rank — `np.linalg.matrix_rank()`

The rank tells us the number of linearly independent rows or columns.

```python
A = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(A)

print(rank)
```

Output:
```
1
```

The second row is simply twice the first row, so there is only one independent row.

---

## 20. Condition Number — `np.linalg.cond()`

The condition number gives information about how sensitive a numerical problem may be to perturbations.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

condition_number = np.linalg.cond(A)

print(condition_number)
```

A very large condition number can indicate an ill-conditioned problem.

This matters in numerical engineering because small input errors can sometimes produce relatively large changes in the calculated solution.

---

## 21. Matrix Norms and Specific Norm Types

`np.linalg.norm()` can calculate different norms depending on the `ord` argument.

For a vector:

```python
v = np.array([3, -4])
```

Euclidean norm:

```python
np.linalg.norm(v, ord=2)
```

Manhattan / L1 norm:

```python
np.linalg.norm(v, ord=1)
```

Infinity norm:

```python
np.linalg.norm(v, ord=np.inf)
```

For engineering work, the Euclidean norm is often the most familiar:

$$ ||v||_2 = \sqrt{\sum_i v_i^2} $$

---

## 22. QR Decomposition — `np.linalg.qr()`

QR decomposition expresses a matrix as:

$$ A=QR $$

where:
- $Q$ is an orthogonal matrix
- $R$ is an upper triangular matrix

```python
Q, R = np.linalg.qr(A)
```

QR decomposition is used in numerical linear algebra and can be useful for solving least-squares problems and other computational tasks.

---

## 23. Cholesky Decomposition — `np.linalg.cholesky()`

For an appropriate symmetric positive-definite matrix:

$$ A=LL^T $$

```python
L = np.linalg.cholesky(A)
```

Example:

```python
A = np.array([
    [4, 2],
    [2, 3]
])

L = np.linalg.cholesky(A)

print(L)
```

Cholesky decomposition is important in numerical methods and can appear in estimation and optimisation algorithms.

---

## 24. np.linalg Function Summary

| Function | Purpose |
|----------|---------|
| `np.linalg.norm()` | Vector/matrix norm |
| `np.linalg.det()` | Determinant |
| `np.linalg.inv()` | Matrix inverse |
| `np.linalg.solve()` | Solve $Ax=b$ |
| `np.linalg.eig()` | Eigenvalues/eigenvectors |
| `np.linalg.eigh()` | Eigenvalues/eigenvectors for symmetric/Hermitian matrices |
| `np.linalg.svd()` | Singular Value Decomposition |
| `np.linalg.lstsq()` | Least-squares solution |
| `np.linalg.matrix_rank()` | Matrix rank |
| `np.linalg.cond()` | Condition number |
| `np.linalg.qr()` | QR decomposition |
| `np.linalg.cholesky()` | Cholesky decomposition |

---

## 25. Important Functions to Master First

Do not try to memorise the entire module.

For your current aerospace roadmap, prioritise:

### Tier 1 — Master
- `np.linalg.norm()`
- `np.linalg.solve()`
- `np.linalg.det()`
- `np.linalg.inv()`

### Tier 2 — Understand
- `np.linalg.eig()`
- `np.linalg.eigh()`
- `np.linalg.matrix_rank()`
- `np.linalg.lstsq()`

### Tier 3 — Learn when needed
- `np.linalg.svd()`
- `np.linalg.qr()`
- `np.linalg.cholesky()`
- `np.linalg.cond()`

The goal is not memorising function names. The goal is knowing:

> "What mathematical problem am I solving, and which numerical tool should I use?"

---

## 26. linalg + Aerospace Example

Suppose you have a simple transformation:

$$ A\mathbf{x}=\mathbf{b} $$

You can solve it directly:

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

x = np.linalg.solve(A, b)

print("Solution:", x)
```

Then verify:

```python
verification = A @ x

print("Verification:", verification)
```

This pattern is extremely useful:

```text
Define mathematical system
        ↓
Represent it using NumPy arrays
        ↓
Use linalg
        ↓
Obtain numerical solution
        ↓
Verify the result
```

---

## 27. Numerical Precision

Python uses floating-point numbers for most numerical calculations.

Therefore, you may sometimes see `0.9999999999999999` instead of `1.0`.

This does not necessarily mean your mathematics is wrong. Floating-point arithmetic has finite precision.

For comparisons, consider:

```python
np.isclose(a, b)
```

or:

```python
np.allclose(A, B)
```

Example:

```python
A = np.eye(3)

B = A + 1e-12

print(np.allclose(A, B))
```

Output:
```
True
```

---

## 28. A Very Important Engineering Habit

After performing a numerical calculation, verify it whenever possible.

```python
x = np.linalg.solve(A, b)

check = A @ x

print(check)
```

You should compare `check` against `b`.

Similarly, after calculating an inverse:

```python
A_inv = np.linalg.inv(A)

print(np.allclose(A @ A_inv, np.eye(A.shape[0])))
```

This should return `True`.

> Don't blindly trust numerical output. Verify it against the mathematical relationship.

---

## 29. Common Mistakes

### Mistake 1 — Using `*` instead of `@`

```python
A * B
```

means element-wise multiplication.

```python
A @ B
```

means matrix multiplication.

### Mistake 2 — Using `inv()` unnecessarily

Avoid:

```python
x = np.linalg.inv(A) @ b
```

when your goal is simply to solve $Ax=b$.

Prefer:

```python
x = np.linalg.solve(A, b)
```

### Mistake 3 — Ignoring matrix dimensions

Always check `A.shape` before performing matrix operations.

### Mistake 4 — Treating every array as a matrix

A NumPy array can represent many things:
- scalar
- vector
- matrix
- higher-dimensional data

Its shape matters.

---

## 30. Recommended Learning Order

For your aerospace roadmap:

```text
NumPy arrays
      ↓
Vector operations
      ↓
Matrix operations
      ↓
np.linalg.norm()
      ↓
np.linalg.solve()
      ↓
Determinants and inverses
      ↓
Eigenvalues/eigenvectors
      ↓
Numerical ODEs
      ↓
Rotation matrices
      ↓
Quaternions
      ↓
6-DOF simulation
```

---

## 31. Final Takeaways

- [ ] `np.linalg` provides numerical linear-algebra tools.
- [ ] `np.linalg.norm()` calculates vector/matrix norms.
- [ ] `np.linalg.det()` calculates determinants.
- [ ] `np.linalg.inv()` calculates matrix inverses.
- [ ] `np.linalg.solve()` solves $Ax=b$.
- [ ] `np.linalg.eig()` calculates eigenvalues and eigenvectors.
- [ ] `np.linalg.eigh()` is preferred for symmetric/Hermitian matrices.
- [ ] `np.linalg.lstsq()` solves least-squares problems.
- [ ] `np.linalg.svd()` performs singular-value decomposition.
- [ ] `np.linalg.matrix_rank()` calculates matrix rank.
- [ ] `np.linalg.cond()` gives a condition number.
- [ ] `np.linalg.qr()` performs QR decomposition.
- [ ] `np.linalg.cholesky()` performs Cholesky decomposition.
