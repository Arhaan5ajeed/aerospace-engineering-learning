# Day 3 — Conditional Statements, Loops & Reynolds Number

**Objective:** Learn how to make Python programs take decisions and repeat calculations, then apply these concepts to build a Reynolds-number calculator.

---

## Conditional Statements

Conditional statements allow a program to make decisions based on whether a condition is true or false.

**Basic structure:**

```python
if condition:
    statement
```

Example:

```python
velocity = 50
if velocity > 0:
    print("Positive velocity")
```

### `if` Statement

An `if` block executes only when its condition is `True`.

```python
temperature = 300
if temperature > 273.15:
    print("Temperature is above freezing")
```

### `if`-`else` Statement

Used when there are two possible outcomes.

```python
velocity = -10
if velocity >= 0:
    print("Positive velocity")
else:
    print("Negative velocity")
```

Structure:

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

### `if`-`elif`-`else`

Used when there are multiple possible conditions.

```python
temperature = 500
if temperature < 300:
    print("Low")
elif temperature < 600:
    print("Moderate")
else:
    print("High")
```

Python checks the conditions from top to bottom and executes the first condition that is true.

---

## Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==`     | Equal to | `a == b` |
| `!=`     | Not equal to | `a != b` |
| `>`      | Greater than | `a > b` |
| `<`      | Less than | `a < b` |
| `>=`     | Greater than or equal to | `a >= b` |
| `<=`     | Less than or equal to | `a <= b` |

> **Important:** `=` means assignment. `==` means comparison.

```python
x = 10
if x == 10:
    print("x is 10")
```

---

## Logical Operators

Logical operators combine conditions.

### `and`
Both conditions must be true.

```python
if velocity > 0 and velocity < 100:
    print("Velocity is within range")
```

### `or`
At least one condition must be true.

```python
if velocity <= 0 or velocity > 300:
    print("Check velocity")
```

### `not`
Reverses a condition.

```python
if not temperature > 300:
    print("Temperature is not above 300 K")
```

### Nested `if`

An `if` statement can be placed inside another `if`.

```python
velocity = 50
density = 1.225

if velocity > 0:
    if density > 0:
        print("Inputs are valid")
```

Use nested conditions only when they make the logic clearer.

---

## Why Loops?

A loop repeats a block of code.

For example, instead of writing:

```python
print(10)
print(20)
print(30)
print(40)
print(50)
```

we can use a loop.

Loops are useful for:
- Repeated calculations
- Processing experimental data
- Parameter studies
- Simulations
- Iterative numerical methods

Python mainly uses:
- `for` loops
- `while` loops

---

## `for` Loop

A `for` loop iterates through a sequence.

```python
for velocity in [10, 20, 30, 40, 50]:
    print(velocity)
```

Output:
```
10
20
30
40
50
```

The variable `velocity` takes one value at a time.

### `range()`

`range()` generates a sequence of integers.

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

The final value is excluded.

General form:

```python
range(start, stop, step)
```

```python
for velocity in range(10, 51, 10):
    print(velocity)
```

Output:
```
10
20
30
40
50
```

### Engineering Example — Repeated Calculation

Calculate kinetic energy for several velocities:

```python
mass = 1000

for velocity in range(10, 51, 10):
    KE = 0.5 * mass * velocity**2
    print("Velocity:", velocity, "KE:", KE)
```

The loop allows the same equation to be applied to multiple cases.

---

## `while` Loop

A `while` loop repeats as long as its condition remains true.

```python
velocity = 0

while velocity <= 50:
    print(velocity)
    velocity += 10
```

Output:
```
0
10
20
30
40
50
```

> The variable controlling the condition must eventually change; otherwise, an infinite loop can occur.

### `break`

`break` immediately terminates a loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:
```
0
1
2
3
4
```

### `continue`

`continue` skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:
```
0
1
3
4
```

---

## Input Validation

Engineering programs should check whether input values are physically meaningful.

```python
density = float(input("Enter density: "))

if density <= 0:
    print("Invalid density")
else:
    print("Density accepted")
```

For many basic calculations, quantities such as density, mass, length and viscosity should be positive.

> **Engineering principle:** A program should not blindly accept physically impossible input.

---

## Reynolds Number

### Definition

Reynolds number is a dimensionless quantity that indicates the relative importance of inertial effects and viscous effects in fluid flow.

$$Re = \frac{\rho V L}{\mu}$$

where:
- ρ = fluid density, kg/m³
- V = characteristic velocity, m/s
- L = characteristic length, m
- μ = dynamic viscosity, Pa·s

Reynolds number has no units.

### Physical Meaning

Reynolds number can be interpreted approximately as:

- **Low Reynolds number** → viscous effects are relatively important.
- **High Reynolds number** → inertial effects are relatively important.

Reynolds number is important in:
- Pipe flow
- Aircraft aerodynamics
- Boundary layers
- Wind tunnels
- Scale modelling
- Turbomachinery
- UAV aerodynamics

### Reynolds Number Calculation

Given:
- ρ = 1.225 kg/m³
- V = 50 m/s
- L = 1 m
- μ = 1.81 × 10⁻⁵ Pa·s

$$Re = \frac{(1.225)(50)(1)}{1.81 \times 10^{-5}} \approx 3.38 \times 10^{6}$$

---

## Reynolds Number Calculator

Create: `reynolds_number.py`

**Basic program:**

```python
rho = float(input("Enter density (kg/m^3): "))
V = float(input("Enter velocity (m/s): "))
L = float(input("Enter characteristic length (m): "))
mu = float(input("Enter dynamic viscosity (Pa.s): "))

Re = (rho * V * L) / mu

print("Reynolds number =", Re)
```

**Add Input Validation**

```python
rho = float(input("Enter density (kg/m^3): "))
V = float(input("Enter velocity (m/s): "))
L = float(input("Enter characteristic length (m): "))
mu = float(input("Enter dynamic viscosity (Pa.s): "))

if rho <= 0 or V <= 0 or L <= 0 or mu <= 0:
    print("Error: Values must be positive.")
else:
    Re = (rho * V * L) / mu
    print("Reynolds number =", Re)
```

### Flow Classification

For internal pipe flow, the commonly used approximate classification is:

| Reynolds Number | Flow Regime |
|------------------|-------------|
| Re < 2300 | Laminar |
| 2300 ≤ Re ≤ 4000 | Transitional |
| Re > 4000 | Turbulent |

> These limits are specific to the conventional pipe-flow classification and should not be blindly applied to external aircraft flow.

Add the classification:

```python
if Re < 2300:
    print("Flow regime: Laminar")
elif Re <= 4000:
    print("Flow regime: Transitional")
else:
    print("Flow regime: Turbulent")
```

### Reynolds Number Calculator — Complete Version

```python
rho = float(input("Enter density (kg/m^3): "))
V = float(input("Enter velocity (m/s): "))
L = float(input("Enter characteristic length (m): "))
mu = float(input("Enter dynamic viscosity (Pa.s): "))

if rho <= 0 or V <= 0 or L <= 0 or mu <= 0:
    print("Error: All values must be positive.")
else:
    Re = (rho * V * L) / mu
    print("Reynolds number =", Re)

    if Re < 2300:
        print("Flow regime: Laminar")
    elif Re <= 4000:
        print("Flow regime: Transitional")
    else:
        print("Flow regime: Turbulent")
```

---

## Using a Loop with Reynolds Number

A loop can be used to investigate how Reynolds number changes with velocity.

```python
rho = 1.225
L = 1.0
mu = 1.81e-5

for V in range(10, 101, 10):
    Re = (rho * V * L) / mu
    print("Velocity:", V, "m/s")
    print("Reynolds number:", Re)
```

Since $Re = \dfrac{\rho V L}{\mu}$ and ρ, L, and μ all remain constant, Reynolds number is directly proportional to velocity.

This is a simple parameter study.

---

## Engineering Validation

Always verify the program independently. Check:
- The equation is correct.
- All quantities use compatible units.
- Reynolds number is dimensionless.
- Increasing velocity should increase Reynolds number.
- Compare at least one result with a manual/calculator calculation.

> **Engineering principle:** Never trust a program merely because it runs without errors. Verify the physics and the result.

---

## Day 3 Checklist

- [ ] Understand `if`
- [ ] Understand `elif`
- [ ] Understand `else`
- [ ] Use comparison operators
- [ ] Use `and`, `or`, `not`
- [ ] Understand nested conditions
- [ ] Understand `for` loops
- [ ] Use `range()`
- [ ] Understand `while` loops
- [ ] Use `break` and `continue`
- [ ] Perform basic input validation
- [ ] Understand Reynolds number
- [ ] Calculate Reynolds number using Python
- [ ] Classify pipe flow using Reynolds number
- [ ] Use a loop for a Reynolds-number parameter study
- [ ] Independently verify the result
