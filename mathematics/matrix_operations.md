# Mathematics Notes: Matrix Operations

**Objective:** Understand matrices mathematically, learn their fundamental operations, and develop the foundation required for coordinate transformations, linear systems, control theory, aircraft dynamics, and numerical simulation.

---

## 1. What is a Matrix?

A matrix is a rectangular arrangement of numbers.

A general matrix can be written as:

$$ A= \begin{bmatrix} a_{11}&a_{12}&\cdots&a_{1n}\\ a_{21}&a_{22}&\cdots&a_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{m1}&a_{m2}&\cdots&a_{mn} \end{bmatrix} $$

The matrix has:
- $m$ rows
- $n$ columns

Therefore, its order is:

$$ m\times n $$

Example:

$$ A= \begin{bmatrix} 1&2&3\\ 4&5&6 \end{bmatrix} $$

is a $2\times3$ matrix.

---

## 2. Elements of a Matrix

In:

$$ A= \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} $$

the element $a_{12}$ means:
- row 1
- column 2

Therefore:

$$ a_{12}=2 $$

---

## 3. Types of Matrices

### Row Matrix

Only one row:

$$ A= \begin{bmatrix} 1&2&3 \end{bmatrix} $$

### Column Matrix

Only one column:

$$ A= \begin{bmatrix} 1\\2\\3 \end{bmatrix} $$

A vector can therefore be represented as a column matrix.

### Square Matrix

Same number of rows and columns.

$$ 2\times2,\quad3\times3,\quad4\times4 $$

### Zero Matrix

All elements are zero.

$$ \begin{bmatrix} 0&0\\ 0&0 \end{bmatrix} $$

### Identity Matrix

The main diagonal contains ones and all other elements are zero.

$$ I= \begin{bmatrix} 1&0\\ 0&1 \end{bmatrix} $$

The identity matrix behaves like 1 in matrix multiplication:

$$ AI=IA=A $$

---

## 4. Matrix Addition

Matrices can be added only when they have the same dimensions.

$$ A+B $$

is calculated element by element.

Example:

$$ A= \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} \qquad B= \begin{bmatrix} 5&6\\ 7&8 \end{bmatrix} $$

Therefore:

$$ A+B= \begin{bmatrix} 6&8\\ 10&12 \end{bmatrix} $$

---

## 5. Matrix Subtraction

Similarly:

$$ A-B $$

is calculated element by element.

$$ A-B= \begin{bmatrix} 1-5&2-6\\ 3-7&4-8 \end{bmatrix} $$

Therefore:

$$ A-B= \begin{bmatrix} -4&-4\\ -4&-4 \end{bmatrix} $$

---

## 6. Scalar Multiplication

A matrix can be multiplied by a scalar.

$$ kA $$

Every element is multiplied by $k$.

Example:

$$ 3 \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} = \begin{bmatrix} 3&6\\ 9&12 \end{bmatrix} $$

---

## 7. Matrix Multiplication

Matrix multiplication is different from element-wise multiplication.

Suppose:

$$ A= \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} \qquad B= \begin{bmatrix} 5&6\\ 7&8 \end{bmatrix} $$

Then:

$$ AB= \begin{bmatrix} (1)(5)+(2)(7)&(1)(6)+(2)(8)\\ (3)(5)+(4)(7)&(3)(6)+(4)(8) \end{bmatrix} $$

Therefore:

$$ AB= \begin{bmatrix} 19&22\\ 43&50 \end{bmatrix} $$

---

## 8. Matrix Multiplication Rule

If $A$ has dimensions $m\times n$ and $B$ has dimensions $n\times p$, then $AB$ is possible and produces an $m\times p$ matrix.

The inner dimensions must match.

Example:

$$ (2\times3)(3\times4) $$

is valid and produces:

$$ 2\times4 $$

But:

$$ (2\times3)(2\times4) $$

is not valid.

---

## 9. Matrix Multiplication Is Not Commutative

In general:

$$ AB\neq BA $$

This is one of the most important differences between ordinary algebra and matrix algebra.

For example, two matrices may satisfy:

$$ AB=C $$

while:

$$ BA\neq C $$

or $BA$ may not even be defined.

---

## 10. Matrix-Vector Multiplication

A matrix can operate on a vector.

For example:

$$ A= \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} \qquad \mathbf{x} = \begin{bmatrix} 5\\6 \end{bmatrix} $$

Then:

$$ A\mathbf{x} = \begin{bmatrix} 1(5)+2(6)\\ 3(5)+4(6) \end{bmatrix} $$

Therefore:

$$ A\mathbf{x} = \begin{bmatrix} 17\\39 \end{bmatrix} $$

This operation is extremely important in engineering.

---

## 11. Transpose

The transpose of a matrix changes rows into columns.

It is represented as:

$$ A^T $$

Example:

$$ A= \begin{bmatrix} 1&2&3\\ 4&5&6 \end{bmatrix} $$

Then:

$$ A^T= \begin{bmatrix} 1&4\\ 2&5\\ 3&6 \end{bmatrix} $$

---

## 12. Symmetric Matrix

A square matrix is symmetric if:

$$ A^T=A $$

Example:

$$ A= \begin{bmatrix} 1&2\\ 2&3 \end{bmatrix} $$

Since $A^T=A$, the matrix is symmetric.

---

## 13. Determinant

The determinant is defined for square matrices.

For:

$$ A= \begin{bmatrix} a&b\\ c&d \end{bmatrix} $$

the determinant is:

$$ \det(A)=ad-bc $$

Example:

$$ A= \begin{bmatrix} 1&2\\ 3&4 \end{bmatrix} $$

Therefore:

$$ \det(A) = (1)(4)-(2)(3) = -2 $$

---

## 14. Why Determinants Matter

The determinant provides important information about a matrix.

If $\det(A)\neq0$, then $A$ is non-singular and has an inverse.

If $\det(A)=0$, then $A$ is singular and does not have an ordinary inverse.

---

## 15. Matrix Inverse

The inverse of $A$ is written $A^{-1}$ and satisfies:

$$ AA^{-1}=A^{-1}A=I $$

For:

$$ A= \begin{bmatrix} a&b\\ c&d \end{bmatrix} $$

the inverse is:

$$ A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d&-b\\ -c&a \end{bmatrix} $$

provided $ad-bc\neq0$.

---

## 16. Solving Linear Equations Using Matrices

Consider:

$$ 2x+y=5 $$

$$ x+3y=6 $$

This can be written:

$$ A\mathbf{x}=\mathbf{b} $$

where:

$$ A= \begin{bmatrix} 2&1\\ 1&3 \end{bmatrix} \qquad \mathbf{x} = \begin{bmatrix} x\\y \end{bmatrix} \qquad \mathbf{b} = \begin{bmatrix} 5\\6 \end{bmatrix} $$

Therefore:

$$ A\mathbf{x}=\mathbf{b} $$

This form is fundamental to numerical engineering.

---

## 17. Matrix as a Transformation

One of the most important ideas for aerospace engineering:

> A matrix can represent a transformation of a vector.

For example:

$$ \mathbf{x}_{new}=A\mathbf{x}_{old} $$

A matrix can represent:
- Rotation
- Scaling
- Coordinate transformation
- Reflection
- Projection

This is why matrices become fundamental to aircraft attitude and navigation.

---

## 18. Rotation Matrix

A 2D rotation matrix is:

$$ R(\theta)= \begin{bmatrix} \cos\theta&-\sin\theta\\ \sin\theta&\cos\theta \end{bmatrix} $$

If:

$$ \mathbf{v} = \begin{bmatrix} 1\\0 \end{bmatrix} \qquad \theta=90^\circ $$

then:

$$ R(90^\circ) = \begin{bmatrix} 0&-1\\ 1&0 \end{bmatrix} $$

and:

$$ R\mathbf{v} = \begin{bmatrix} 0\\1 \end{bmatrix} $$

The vector has been rotated by $90^\circ$.

---

## 19. Aerospace Importance of Matrices

Matrices appear in:
- Coordinate transformations
- Aircraft attitude
- Rotation matrices
- State-space models
- Control systems
- Kalman filters
- Navigation
- Computer vision
- Structural analysis
- Finite-element methods
- 6-DOF simulations

For example, an aircraft state can be represented as:

$$ \mathbf{x} = \begin{bmatrix} x\\y\\z\\ u\\v\\w\\ p\\q\\r\\ \phi\\\theta\\\psi \end{bmatrix} $$

and system equations can be represented using matrices.

---

## 20. Eigenvalues and Eigenvectors

For a matrix $A$, an eigenvector satisfies:

$$ A\mathbf{v} = \lambda\mathbf{v} $$

where:
- $\mathbf{v}$ = eigenvector
- $\lambda$ = eigenvalue

This means that multiplying the matrix by the eigenvector changes its magnitude but not its fundamental direction.

Eigenvalues and eigenvectors are important in:
- Stability analysis
- Structural dynamics
- Control systems
- Vibrations
- Principal-axis analysis

You will study them more deeply later.

---

## 21. Core Matrix Takeaways

- [ ] Matrix = rectangular numerical structure.
- [ ] Matrix dimensions are rows × columns.
- [ ] Addition requires identical dimensions.
- [ ] Matrix multiplication requires matching inner dimensions.
- [ ] Matrix multiplication is generally not commutative.
- [ ] $A^T$ = transpose.
- [ ] $\det(A)$ = determinant.
- [ ] $A^{-1}$ = inverse, when it exists.
- [ ] $A\mathbf{x}$ = matrix-vector transformation.
- [ ] Matrices are fundamental to coordinate transformations and aerospace simulation.
