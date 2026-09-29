# Day 8 — NumPy Fundamentals, Arrays & Indexing

**Objective:** Introduce NumPy as the foundation for numerical and scientific computing in Python, learn how to create and manipulate NumPy arrays, understand indexing and slicing, and perform vectorised engineering calculations.

---

## 1. What is NumPy?

NumPy (Numerical Python) is a Python library designed for numerical and scientific computing.

It provides:
- Multidimensional arrays
- Fast numerical operations
- Mathematical functions
- Array manipulation
- Tools for linear algebra
- Foundations for scientific computing and simulation

NumPy is widely used in:
- Engineering
- Physics
- Aerospace
- Data analysis
- Numerical methods
- Simulation
- Machine learning
- Control systems

> Python lists are general-purpose containers. NumPy arrays are designed for numerical computation.

---

## 2. Why NumPy?

So far, we have used Python lists:

```python
velocity = [50, 100, 150, 200]
```

Lists are useful, but numerical engineering problems often involve thousands or millions of values.

Examples:
- Velocity measurements
- Pressure measurements
- Temperature data
- Flight-test data
- Simulation time steps
- Sensor measurements
- Position and acceleration data

NumPy allows us to perform mathematical operations on entire collections of numerical values efficiently.

---

## 3. Importing NumPy

NumPy must first be imported.

```python
import numpy as np
```

`np` is the conventional abbreviation for NumPy.

We can then use:

```python
np.array()
```

to create NumPy arrays.

---

## 4. Creating a NumPy Array

Example:

```python
import numpy as np

velocity = np.array([50, 100, 150, 200])

print(velocity)
```

Output:
```
[ 50 100 150 200]
```

The object created is a NumPy `ndarray`.

```python
print(type(velocity))
```

Output:
```
<class 'numpy.ndarray'>
```

`ndarray` means N-dimensional array.

---

## 5. NumPy Arrays vs Python Lists

Python list:

```python
velocity = [50, 100, 150, 200]
```

NumPy array:

```python
velocity = np.array([50, 100, 150, 200])
```

A NumPy array is specifically designed for numerical operations. For example:

```python
velocity = np.array([50, 100, 150, 200])

velocity_squared = velocity ** 2
```

Output:
```
[ 2500 10000 22500 40000]
```

The operation is applied to every element.

> NumPy allows us to treat an array of values as a mathematical object.

---

## 6. Indexing

NumPy uses zero-based indexing, just like Python lists.

```python
velocity = np.array([50, 100, 150, 200])
```

The indexing is:

| Index | 0  | 1   | 2   | 3   |
|-------|----|-----|-----|-----|
| Value | 50 | 100 | 150 | 200 |

Access the first element:

```python
velocity[0]
```

Output:
```
50
```

Access the third element:

```python
velocity[2]
```

Output:
```
150
```

---

## 7. Negative Indexing

Negative indexing starts from the end.

```python
velocity[-1]
```

returns:
```
200
```

Similarly:

```python
velocity[-2]
```

returns:
```
150
```

---

## 8. Modifying Array Elements

NumPy arrays can be modified.

```python
velocity[1] = 120
```

The array becomes:
```
[50 120 150 200]
```

This is similar to modifying a Python list.

---

## 9. Array Slicing

Slicing allows us to select a section of an array.

**Syntax:**

```python
array[start:stop]
```

The stop index is not included.

Example:

```python
velocity = np.array([50, 100, 150, 200])

velocity[1:4]
```

Output:
```
[100 150 200]
```

---

## 10. More Slicing Examples

First three elements:

```python
velocity[:3]
```

Output:
```
[50 100 150]
```

From index 2 onwards:

```python
velocity[2:]
```

Output:
```
[150 200]
```

Every second element:

```python
velocity[::2]
```

Output:
```
[50 150]
```

Reverse the array:

```python
velocity[::-1]
```

Output:
```
[200 150 100 50]
```

---

## 11. Mathematical Operations on Arrays

NumPy allows mathematical operations to be performed element-by-element.

```python
velocity = np.array([50, 100, 150, 200])
```

**Addition**

```python
velocity + 10
```

Output:
```
[60 110 160 210]
```

**Subtraction**

```python
velocity - 10
```

Output:
```
[40 90 140 190]
```

**Multiplication**

```python
velocity * 2
```

Output:
```
[100 200 300 400]
```

**Division**

```python
velocity / 2
```

Output:
```
[25 50 75 100]
```

**Power**

```python
velocity ** 2
```

Output:
```
[2500 10000 22500 40000]
```

---

## 12. Vectorised Operations

Performing an operation on an entire array without explicitly looping through each element is called a **vectorised operation**.

```python
velocity = np.array([50, 100, 150, 200])

velocity_squared = velocity ** 2
```

Instead of manually doing:

```python
velocity_squared = []

for v in velocity:
    velocity_squared.append(v ** 2)
```

NumPy allows:

```python
velocity_squared = velocity ** 2
```

> Vectorisation allows mathematical operations to be expressed in a form closer to the mathematical equation itself.

---

## 13. Engineering Example — Kinetic Energy

The kinetic energy equation is:

$$KE = \frac{1}{2}mv^2$$

Suppose:

```python
mass = 1000
velocity = np.array([50, 100, 150, 200])
```

We can calculate the kinetic energy for every velocity:

```python
kinetic_energy = 0.5 * mass * velocity ** 2
```

The result is an array containing the kinetic energy corresponding to each velocity. This is much more useful than calculating each velocity separately.

---

## 14. Array Properties

NumPy provides useful properties for understanding an array.

**`shape`**

```python
velocity.shape
```

For:

```python
velocity = np.array([50, 100, 150, 200])
```

the result is:
```
(4,)
```

This means the array contains four elements along one dimension.

**`size`**

```python
velocity.size
```

Result:
```
4
```

`size` gives the total number of elements.

**`ndim`**

```python
velocity.ndim
```

Result:
```
1
```

`ndim` gives the number of dimensions.

---

## 15. Summary of Array Properties

For:

```python
velocity = np.array([50, 100, 150, 200])
```

we have:

| Property | Result | Meaning |
|----------|--------|---------|
| `shape` | `(4,)` | Structure/dimensions of the array |
| `size` | `4` | Total number of elements |
| `ndim` | `1` | Number of dimensions |

---

## 16. Scalar and Array Operations

A scalar is a single numerical value.

```python
mass = 1000
```

An array contains multiple values:

```python
velocity = np.array([50, 100, 150, 200])
```

NumPy allows operations between scalars and arrays.

```python
velocity * 2
```

The scalar `2` is effectively applied to every element.

Result:
```
[100 200 300 400]
```

This behaviour is fundamental to numerical computing.

---

## 17. Aerospace Example — Multiple Flight Conditions

Suppose an aircraft is tested at several velocities:

```python
velocity = np.array([50, 100, 150, 200, 250])
```

The corresponding kinetic energy can be calculated using:

```python
mass = 10000

kinetic_energy = 0.5 * mass * velocity ** 2
```

Now one equation has been applied to an entire set of flight conditions.

This idea becomes extremely important when working with:
- Flight simulations
- Aerodynamic calculations
- Experimental data
- Propulsion calculations
- Trajectory calculations
- Control systems

---

## 18. Why This Matters for Aerospace Engineering

Future aerospace simulations may contain arrays representing:
- Time
- Position
- Velocity
- Acceleration
- Altitude
- Temperature
- Pressure
- Density
- Sensor measurements

For example:

```python
time = np.array([0, 1, 2, 3, 4, 5])

velocity = np.array([0, 20, 42, 65, 91, 120])

altitude = np.array([0, 10, 35, 70, 120, 190])
```

These arrays can later be used to analyse and visualise the behaviour of an aircraft or spacecraft over time.

---

## 19. Important Difference: List vs NumPy Array

Python list:

```python
velocity = [50, 100, 150, 200]
```

NumPy array:

```python
velocity = np.array([50, 100, 150, 200])
```

The NumPy version is specifically designed for numerical operations. For example:

```python
velocity * 2
```

with a NumPy array performs element-wise multiplication.

With a normal Python list, multiplication behaves differently:

```python
velocity = [50, 100, 150, 200]

velocity * 2
```

produces:
```
[50, 100, 150, 200, 50, 100, 150, 200]
```

It repeats the list rather than multiplying each number.

This is one reason NumPy is so useful for engineering computation.

---

## 20. Day 8 Practical Exercise

Create: `python/codes/numpy/day8_numpy_basics.py`

The program should demonstrate:
- [ ] Importing NumPy
- [ ] Creating a NumPy array
- [ ] Checking the array type
- [ ] Indexing
- [ ] Negative indexing
- [ ] Modifying an element
- [ ] Slicing
- [ ] Addition
- [ ] Subtraction
- [ ] Multiplication
- [ ] Division
- [ ] Power
- [ ] `shape`
- [ ] `size`
- [ ] `ndim`
- [ ] Vectorised calculation

---

## 21. Day 8 Mini Engineering Project

Create an array of aircraft velocities:

```python
velocity = np.array([50, 100, 150, 200, 250])
```

Assume:

```python
mass = 1000
```

Calculate kinetic energy using NumPy. Do not use an explicit `for` loop for the calculation.

Your program should display something similar to:

```
Velocity: [ 50 100 150 200 250 ]

Kinetic Energy:
[... ... ... ... ...]
```

---

## 22. Challenges

### Challenge 1 — Find a Specific Velocity

Given:

```python
velocity = np.array([50, 100, 150, 200, 250])
```

access the value `150` using indexing.

### Challenge 2 — Extract Flight Conditions

Extract only `100, 150, 200` using slicing.

### Challenge 3 — Acceleration

Given:

```python
velocity = np.array([20, 40, 60, 80, 100])
time = 2
```

calculate:

$$a = \frac{v}{t}$$

for every velocity using vectorisation.

### Challenge 4 — Dynamic Pressure

Given:

```python
rho = 1.225
velocity = np.array([50, 100, 150, 200])
```

calculate:

$$q = \frac{1}{2} \rho V^2$$

for every velocity.

This is your first proper aerodynamics + NumPy exercise.

---

## 23. Day 8 Key Concepts

Remember these:

| Concept | Meaning |
|---------|---------|
| `np.array()` | Create a NumPy array |
| `array[index]` | Access an element |
| `array[a:b]` | Slice an array |
| `array.shape` | Array dimensions/structure |
| `array.size` | Number of elements |
| `array.ndim` | Number of dimensions |

> **Note:** The original notes had an additional line here ("And:") with no content after it — likely lost in export. Worth checking your source material for what should complete this section.

---

## 24. Day 8 Checklist

- [ ] I understand why NumPy is used.
- [ ] I can import NumPy.
- [ ] I can create a NumPy array.
- [ ] I understand zero-based indexing.
- [ ] I can use negative indexing.
- [ ] I can modify array elements.
- [ ] I understand slicing.
- [ ] I can perform mathematical operations on arrays.
- [ ] I understand vectorised operations.
- [ ] I understand `shape`, `size`, and `ndim`.
- [ ] I can use NumPy for an engineering calculation.
- [ ] I understand the difference between a Python list and a NumPy array.

> **Day 8 principle:** Stop thinking of numerical values as isolated numbers. Start thinking of them as datasets that can be manipulated mathematically as a whole.
