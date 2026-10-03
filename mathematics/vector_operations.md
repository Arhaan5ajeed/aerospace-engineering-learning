# Mathematics Notes: Vector Operations

**Objective:** Build a strong mathematical understanding of vectors before using them extensively in aerospace engineering, mechanics, dynamics, control systems, and 6-DOF simulation.

---

## 1. What is a Vector?

A vector is a mathematical quantity that has both:
- Magnitude
- Direction

Examples in aerospace engineering:
- Velocity
- Acceleration
- Force
- Momentum
- Position
- Angular velocity

A vector in 3D Cartesian coordinates can be written as:

$$ \mathbf{A} = \begin{bmatrix} A_x\\ A_y\\ A_z \end{bmatrix} $$

where:
- $A_x$ = x-component
- $A_y$ = y-component
- $A_z$ = z-component

Example:

$$ \mathbf{V} = \begin{bmatrix} 100\\ 20\\ -5 \end{bmatrix} \text{ m/s} $$

---

## 2. Scalars vs Vectors

A scalar has only magnitude.

Examples:
- Mass
- Temperature
- Density
- Pressure
- Time
- Energy

A vector has magnitude and direction.

Examples:
- Force
- Velocity
- Acceleration
- Displacement

---

## 3. Vector Components

A vector can be decomposed into components.

For:

$$ \mathbf{A} = \begin{bmatrix} A_x\\ A_y\\ A_z \end{bmatrix} $$

the vector can also be written using unit vectors:

$$ \mathbf{A} = A_x\mathbf{i} + A_y\mathbf{j} + A_z\mathbf{k} $$

where:

$$ \mathbf{i} = \begin{bmatrix} 1\\0\\0 \end{bmatrix} \qquad \mathbf{j} = \begin{bmatrix} 0\\1\\0 \end{bmatrix} \qquad \mathbf{k} = \begin{bmatrix} 0\\0\\1 \end{bmatrix} $$

---

## 4. Magnitude of a Vector

For:

$$ \mathbf{A} = \begin{bmatrix} A_x\\ A_y\\ A_z \end{bmatrix} $$

the magnitude is:

$$ |\mathbf{A}| = \sqrt{A_x^2+A_y^2+A_z^2} $$

Example:

$$ \mathbf{A} = \begin{bmatrix} 3\\4\\0 \end{bmatrix} $$

Therefore:

$$ |\mathbf{A}| = \sqrt{3^2+4^2} = 5 $$

---

## 5. Unit Vector

A unit vector has magnitude equal to 1.

The unit vector in the direction of $\mathbf{A}$ is:

$$ \hat{\mathbf{A}} = \frac{\mathbf{A}}{|\mathbf{A}|} $$

Example:

$$ \mathbf{A} = \begin{bmatrix} 3\\4\\0 \end{bmatrix}, \qquad |\mathbf{A}|=5 $$

Therefore:

$$ \hat{\mathbf{A}} = \begin{bmatrix} 3/5\\ 4/5\\ 0 \end{bmatrix} = \begin{bmatrix} 0.6\\ 0.8\\ 0 \end{bmatrix} $$

---

## 6. Vector Addition

Given:

$$ \mathbf{A} = \begin{bmatrix} A_x\\ A_y\\ A_z \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} B_x\\ B_y\\ B_z \end{bmatrix} $$

then:

$$ \mathbf{A}+\mathbf{B} = \begin{bmatrix} A_x+B_x\\ A_y+B_y\\ A_z+B_z \end{bmatrix} $$

Example:

$$ \mathbf{A} = \begin{bmatrix} 10\\20\\30 \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} 5\\10\\15 \end{bmatrix} $$

Therefore:

$$ \mathbf{A}+\mathbf{B} = \begin{bmatrix} 15\\30\\45 \end{bmatrix} $$

---

## 7. Vector Subtraction

$$ \mathbf{A}-\mathbf{B} = \begin{bmatrix} A_x-B_x\\ A_y-B_y\\ A_z-B_z \end{bmatrix} $$

Example:

$$ \begin{bmatrix} 10\\20\\30 \end{bmatrix} - \begin{bmatrix} 5\\10\\15 \end{bmatrix} = \begin{bmatrix} 5\\10\\15 \end{bmatrix} $$

---

## 8. Scalar Multiplication

A vector can be multiplied by a scalar.

$$ k\mathbf{A} = \begin{bmatrix} kA_x\\ kA_y\\ kA_z \end{bmatrix} $$

Example:

$$ 2 \begin{bmatrix} 10\\20\\30 \end{bmatrix} = \begin{bmatrix} 20\\40\\60 \end{bmatrix} $$

The direction remains the same for positive $k$, while the magnitude changes.

If $k<0$, the direction reverses.

---

## 9. Dot Product

The dot product produces a scalar.

For:

$$ \mathbf{A} = \begin{bmatrix} A_x\\A_y\\A_z \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} B_x\\B_y\\B_z \end{bmatrix} $$

the dot product is:

$$ \mathbf{A}\cdot\mathbf{B} = A_xB_x+A_yB_y+A_zB_z $$

It can also be written as:

$$ \mathbf{A}\cdot\mathbf{B} = |\mathbf{A}||\mathbf{B}|\cos\theta $$

where $\theta$ is the angle between the vectors.

---

## 10. Physical Meaning of Dot Product

The dot product measures how much one vector acts in the direction of another.

A major engineering example is work:

$$ W=\mathbf{F}\cdot\mathbf{d} $$

where:
- $\mathbf{F}$ = force
- $\mathbf{d}$ = displacement

If force and displacement point in the same direction:

$$ \theta=0^\circ $$

so:

$$ W=Fd $$

If they are perpendicular:

$$ \theta=90^\circ $$

then:

$$ W=0 $$

---

## 11. Dot Product and Perpendicular Vectors

If:

$$ \mathbf{A}\cdot\mathbf{B}=0 $$

then the vectors are perpendicular, assuming neither vector is the zero vector.

This gives an important test:

> Zero dot product → perpendicular vectors.

---

## 12. Angle Between Two Vectors

From:

$$ \mathbf{A}\cdot\mathbf{B} = |\mathbf{A}||\mathbf{B}|\cos\theta $$

we obtain:

$$ \cos\theta = \frac{\mathbf{A}\cdot\mathbf{B}} {|\mathbf{A}||\mathbf{B}|} $$

Therefore:

$$ \theta = \cos^{-1} \left( \frac{\mathbf{A}\cdot\mathbf{B}} {|\mathbf{A}||\mathbf{B}|} \right) $$

---

## 13. Cross Product

The cross product produces a vector.

$$ \mathbf{A}\times\mathbf{B} $$

For:

$$ \mathbf{A} = \begin{bmatrix} A_x\\A_y\\A_z \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} B_x\\B_y\\B_z \end{bmatrix} $$

the cross product is:

$$ \mathbf{A}\times\mathbf{B} = \begin{bmatrix} A_yB_z-A_zB_y\\ A_zB_x-A_xB_z\\ A_xB_y-A_yB_x \end{bmatrix} $$

Its magnitude is:

$$ |\mathbf{A}\times\mathbf{B}| = |\mathbf{A}||\mathbf{B}|\sin\theta $$

The resulting vector is perpendicular to both $\mathbf{A}$ and $\mathbf{B}$.

---

## 14. Physical Meaning of Cross Product

A major engineering example is torque:

$$ \boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} $$

where:
- $\mathbf{r}$ = position vector from the reference point
- $\mathbf{F}$ = force
- $\boldsymbol{\tau}$ = torque

This becomes extremely important in aircraft dynamics.

---

## 15. Right-Hand Rule

The direction of a cross product is determined using the right-hand rule.

For:

$$ \mathbf{i}\times\mathbf{j} = \mathbf{k} \qquad \mathbf{j}\times\mathbf{k} = \mathbf{i} \qquad \mathbf{k}\times\mathbf{i} = \mathbf{j} $$

Reversing the order reverses the direction:

$$ \mathbf{B}\times\mathbf{A} = -(\mathbf{A}\times\mathbf{B}) $$

---

## 16. Dot Product vs Cross Product

| Property | Dot Product | Cross Product |
|----------|-------------|----------------|
| Operation | $\mathbf{A}\cdot\mathbf{B}$ | $\mathbf{A}\times\mathbf{B}$ |
| Result | Scalar | Vector |
| Formula | $AB\cos\theta$ | $AB\sin\theta$ |
| Zero when | Vectors perpendicular | Vectors parallel |
| Engineering example | Work | Torque |

---

## 17. Vector Projection

The scalar projection of $\mathbf{A}$ onto $\mathbf{B}$ is:

$$ \operatorname{proj}_{B}(A) = \frac{\mathbf{A}\cdot\mathbf{B}} {|\mathbf{B}|} $$

The vector projection is:

$$ \operatorname{Proj}_{B}(\mathbf{A}) = \frac{\mathbf{A}\cdot\mathbf{B}} {|\mathbf{B}|^2} \mathbf{B} $$

Projection is useful when resolving forces and velocities along specific directions.

---

## 18. Aerospace Applications of Vectors

Vectors appear throughout aerospace engineering.

**Aircraft motion**

$$ \mathbf{v} = \begin{bmatrix} u\\v\\w \end{bmatrix} $$

**Forces**

$$ \mathbf{F} = \begin{bmatrix} F_x\\F_y\\F_z \end{bmatrix} $$

**Moments**

$$ \mathbf{M} = \begin{bmatrix} L\\M\\N \end{bmatrix} $$

**Position**

$$ \mathbf{r} = \begin{bmatrix} x\\y\\z \end{bmatrix} $$

**Angular velocity**

$$ \boldsymbol{\omega} = \begin{bmatrix} p\\q\\r \end{bmatrix} $$

This is why vector mathematics is fundamental to 6-DOF aircraft simulation.

---

## 19. Essential Vector Identities

$$ \mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A} $$

$$ \mathbf{A}\cdot\mathbf{B} = \mathbf{B}\cdot\mathbf{A} $$

But:

$$ \mathbf{A}\times\mathbf{B} = -\mathbf{B}\times\mathbf{A} $$

Also:

$$ \mathbf{A}\cdot(\mathbf{B}+\mathbf{C}) = \mathbf{A}\cdot\mathbf{B} + \mathbf{A}\cdot\mathbf{C} $$

and:

$$ \mathbf{A}\times(\mathbf{B}+\mathbf{C}) = \mathbf{A}\times\mathbf{B} + \mathbf{A}\times\mathbf{C} $$

---

## 20. Core Takeaways

- [ ] A vector has magnitude and direction.
- [ ] Components describe a vector relative to a coordinate system.
- [ ] Magnitude: $|\mathbf{A}|=\sqrt{A_x^2+A_y^2+A_z^2}$
- [ ] Unit vector: $\hat{\mathbf{A}}=\frac{\mathbf{A}}{|\mathbf{A}|}$
- [ ] Dot product → scalar.
- [ ] Cross product → vector.
- [ ] Dot product is related to work and projections.
- [ ] Cross product is related to torque and rotational mechanics.
- [ ] Vectors are fundamental to aerospace dynamics and simulation.
