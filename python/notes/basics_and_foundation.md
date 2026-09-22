
# Python Basics and Foundation

**Objective:** Build the Python foundation required for engineering computation, numerical methods, simulation, and future aerospace applications.

---

## 1. Why Python for an Aerospace Engineer?

Python is a high-level programming language widely used in:

- Engineering calculations
- Numerical methods
- Data analysis
- Scientific computing
- Simulation
- Visualisation
- Automation
- Control systems
- Computer vision
- Artificial intelligence and machine learning

For this learning journey, Python will primarily be treated as an **engineering and computational tool**, rather than simply a programming language.

**Engineering Workflow**

> Learn → Derive → Implement → Test → Validate → Document

This workflow should become a habit throughout the aerospace engineering journey.

---

## 2. Running a Python Program

Python programs normally use the `.py` file extension.

Example: `mech_stress_calculator.py`

A Python program can be executed from VS Code using the **Run Python File** button, or from the terminal:

```bash
python filename.py
```

Example:

```python
print("Hello, Aerospace Engineering!")
```

**Expected Output**

```
Hello, Aerospace Engineering!
```

---

## 3. Variables

A variable is a named reference used to store a value. Think of it as a labelled container for information.

Example:

```python
mass = 100
velocity = 50
temperature = 300
```

Here:
- `mass` stores 100
- `velocity` stores 50
- `temperature` stores 300

**Engineering Example**

```python
pressure = 101325
density = 1.225
velocity = 80
```

The names make the calculation easier to understand.

> **Engineering Principle:** Variable names should communicate what the quantity represents.

---

## 4. Data Types

Python has several fundamental data types.

| Data Type     | Python Keyword | Example  | Typical Engineering Use |
|---------------|-----------------|----------|---------------------------|
| Integer       | `int`           | `100`    | Counts and discrete values |
| Floating Point| `float`         | `3.14159`| Physical quantities |
| String        | `str`           | `"Air"`  | Names, labels and text |
| Boolean       | `bool`          | `True`   | Conditions and states |

### 4.1 Integer
Whole numbers.

```python
number_of_engines = 2
```

### 4.2 Float
Decimal numbers.

```python
velocity = 85.5
```

Most physical quantities will commonly be represented using `float`.

### 4.3 String
Text.

```python
fluid = "Air"
```

### 4.4 Boolean
Represents either `True` or `False`.

```python
is_turbulent = True
```

---

## 5. Arithmetic Operators

Python can perform mathematical operations directly.

| Operation       | Operator | Example |
|-----------------|----------|---------|
| Addition        | `+`      | `a + b` |
| Subtraction     | `-`      | `a - b` |
| Multiplication  | `*`      | `a * b` |
| Division        | `/`      | `a / b` |
| Exponentiation  | `**`     | `a ** 2`|
| Modulus         | `%`      | `a % b` |
| Floor Division  | `//`     | `a // b`|

Example:

```python
mass = 100
velocity = 50
momentum = mass * velocity
print(momentum)
```

The engineering equation is:

$$p = mv$$

Therefore:

$$p = (100)(50) = 5000 \text{ kg·m/s}$$

---

## 6. Order of Operations

Python follows the normal mathematical order of operations.

For example:

```python
result = 10 + 5 * 2
```

gives `20`, because multiplication occurs before addition.

Parentheses can be used to control the order:

```python
result = (10 + 5) * 2
```

which gives `30`.

> **Important:** Use parentheses when they make an engineering equation clearer or prevent ambiguity.

---

## 7. Comments

Comments explain the purpose of code. Python ignores comments during execution.

```python
# Calculate kinetic energy
mass = 100
velocity = 50
kinetic_energy = 0.5 * mass * velocity**2
```

Comments are useful for documenting:
- Equations
- Assumptions
- Units
- Purpose of calculations
- Important implementation details

---

## 8. Output Using `print()`

The `print()` function displays information.

```python
mass = 100
print(mass)
```

Output:
```
100
```

A more useful engineering output is:

```python
print("Mass =", mass, "kg")
```

Output:
```
Mass = 100 kg
```

**Formatted Output**

Python f-strings provide a cleaner method.

```python
print(f"Mass = {mass} kg")
```

Multiple quantities can be displayed:

```python
print(f"Mass = {mass} kg")
print(f"Velocity = {velocity} m/s")
```

---

## 9. User Input

The `input()` function allows the user to enter a value.

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

However, `input()` returns text (`str`) by default. Therefore, numerical input should normally be converted.

```python
mass = float(input("Enter mass in kg: "))
```

---

## 10. Type Conversion

Common conversion functions include:
- `int()`
- `float()`
- `str()`
- `bool()`

Example:

```python
mass = float(input("Enter mass: "))
```

If the user enters `100`, Python converts it into `100.0` rather than treating it as text.

**Why This Matters**

Without conversion:

```python
a = input("Enter a number: ")
b = input("Enter another number: ")
print(a + b)
```

Entering `5` and `10` can produce:
```
510
```
because both values are strings.

With conversion:

```python
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print(a + b)
```

The result is:
```
15.0
```

---

## 11. Comparison Operators

Comparison operators compare values.

| Operator | Meaning |
|----------|---------|
| `==`     | Equal to |
| `!=`     | Not equal to |
| `>`      | Greater than |
| `<`      | Less than |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to |

Example:

```python
velocity = 100
print(velocity > 50)
```

Output:
```
True
```

---

## 12. Logical Operators

The three fundamental logical operators are:

| Operator | Meaning |
|----------|---------|
| `and`    | Both conditions must be true |
| `or`     | At least one condition must be true |
| `not`    | Reverses a condition |

Example:

```python
velocity = 80
altitude = 5000

if velocity > 50 and altitude > 1000:
    print("Condition satisfied")
```

These become particularly useful when implementing engineering decision logic.

---

## 13. Conditional Statements

Conditional statements allow a program to make decisions.

**`if`**

```python
temperature = 120

if temperature > 100:
    print("Temperature is above 100°C")
```

**`if` and `else`**

```python
reynolds_number = 1500

if reynolds_number < 2300:
    print("Laminar flow")
else:
    print("Turbulent flow")
```

**`if`, `elif` and `else`**

```python
reynolds_number = 3000

if reynolds_number < 2300:
    print("Laminar flow")
elif reynolds_number < 4000:
    print("Transitional flow")
else:
    print("Turbulent flow")
```

> **Note:** Always check the exact criteria and assumptions appropriate to the engineering problem. A programming condition should not replace engineering judgement.

---

## 14. Loops

Loops allow a block of code to execute repeatedly.

### 14.1 `for` Loop

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

A `for` loop is useful for:
- Repeated calculations
- Processing datasets
- Iterative numerical methods
- Running simulations over multiple time steps

### 14.2 `while` Loop

A `while` loop continues while a condition remains true.

```python
velocity = 0

while velocity < 100:
    velocity += 10

print(velocity)
```

---

## 15. Functions

A function is a reusable block of code designed to perform a specific task.

**Basic Structure**

```python
def function_name(parameters):
    # code
    return result
```

**Engineering Example**

The kinetic energy equation is:

$$KE = \frac{1}{2}mv^2$$

It can be implemented as:

```python
def kinetic_energy(mass, velocity):
    energy = 0.5 * mass * velocity**2
    return energy
```

Then:

```python
energy = kinetic_energy(100, 50)
print(f"Kinetic energy = {energy} J")
```

Functions are extremely important because larger engineering programs should be divided into small, understandable and reusable components.

---

## 16. Lists

A list stores multiple values in a single variable.

```python
velocities = [10, 20, 30, 40, 50]
```

Individual elements can be accessed using an index.

```python
print(velocities[0])
```

Output:
```
10
```

Python indexing starts from 0.

**Engineering Applications**

Lists can be useful for:
- Experimental measurements
- Velocity data
- Temperature readings
- Sensor measurements
- Simulation results

```python
temperature_data = [290, 295, 301, 308, 315]
```

---

## 17. Dictionaries

A dictionary stores information using key-value pairs.

```python
air = {
    "density": 1.225,
    "R": 287,
    "Cp": 1005
}
```

Values can be accessed using their keys.

```python
print(air["density"])
```

Output:
```
1.225
```

Dictionaries are useful for storing related engineering properties.

---

## 18. Importing Modules

Python contains modules that provide additional functionality. The `math` module provides mathematical functions and constants.

```python
import math

radius = 0.5
area = math.pi * radius**2
print(area)
```

The equation is:

$$A = \pi r^2$$

Common modules that will become important during this journey include:
- `math`
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`

> **Important:** These modules will be learned progressively. Do not try to learn all of them at once.

---

## 19. Basic Error Awareness

Programming errors are normal. Three broad categories are useful to recognise:

**Syntax Errors**

The Python code does not follow Python's syntax.

```python
print("Hello"
```

The closing parenthesis is missing.

**Runtime Errors**

The program starts but encounters a problem while running.

```python
result = 10 / 0
```

**Logical Errors**

The program runs but produces an incorrect result. These are particularly dangerous in engineering because the output can look completely valid while being physically wrong.

```python
# Incorrect equation
stress = force * area
```

When the correct equation is:

$$\sigma = \frac{F}{A}$$

Therefore:

```python
stress = force / area
```

---

## 20. Units and Dimensional Awareness

Python does not automatically know whether a number represents:
- metres
- kilograms
- seconds
- pascals
- joules
- newtons

Therefore, the engineer must manage units correctly.

```python
mass = 100      # kg
velocity = 50   # m/s
momentum = mass * velocity
```

The resulting unit is `kg·m/s`.

> **Golden Rule:** A numerically correct calculation with incorrect units is still an incorrect engineering result.

---

## 21. Engineering Validation

A program should not be trusted simply because it runs without errors. After obtaining a result, ask:

- Is the governing equation correct?
- Are the inputs reasonable?
- Are the units consistent?
- Does the output have the correct units?
- Can the result be checked manually?
- Does the result make physical sense?
- What happens if the input changes?

**Example**

Suppose a program calculates the momentum of an object.

Equation: $p = mv$

For $m = 100$ kg and $v = 50$ m/s, we expect:

$$p = 5000 \text{ kg·m/s}$$

If the program produces `5000000`, do not simply accept the result — investigate the calculation.

---

## 22. Readability and Naming

Compare:

```python
m = 100
v = 50
x = m * v
```

with:

```python
mass = 100
velocity = 50
momentum = mass * velocity
```

The second version is easier to understand. Good variable names should describe the physical quantity they represent.

**Prefer:** `mass`, `velocity`, `pressure`, `temperature`, `density`, `force`, `area`

**Avoid unnecessary names:** `x`, `abc`, `thing`, `value1`, `num` — unless their meaning is genuinely obvious from context.

---

## 23. Basic Program Structure

A simple engineering program can follow this structure:

```python
# 1. Inputs
mass = 100
velocity = 50

# 2. Calculation
momentum = mass * velocity

# 3. Output
print(f"Momentum = {momentum} kg·m/s")
```

As programs become more sophisticated, this can evolve into:

> Inputs → Validation → Calculation → Processing → Output → Validation

This structure will become increasingly important when building engineering software.

---

## 24. Mini Engineering Example

**Problem**

Calculate the kinetic energy of an object with:
- Mass = 100 kg
- Velocity = 50 m/s

**Governing Equation**

$$KE = \frac{1}{2}mv^2$$

**Python Implementation**

```python
mass = 100
velocity = 50
kinetic_energy = 0.5 * mass * velocity**2
print(f"Kinetic energy = {kinetic_energy} J")
```

**Manual Validation**

$$KE = \frac{1}{2}(100)(50)^2 = 125000 \text{ J}$$

Therefore, the program should produce:

```
Kinetic energy = 125000.0 J
```

---

## 25. Python Foundation Checklist

**Core Syntax**
- [ ] Understand variables
- [ ] Understand `int`, `float`, `str` and `bool`
- [ ] Use arithmetic operators
- [ ] Understand order of operations
- [ ] Write comments
- [ ] Use `print()`
- [ ] Use `input()`
- [ ] Understand type conversion

**Programming Logic**
- [ ] Use comparison operators
- [ ] Use `and`, `or` and `not`
- [ ] Write `if` / `elif` / `else` statements
- [ ] Use `for` loops
- [ ] Use `while` loops
- [ ] Create functions
- [ ] Use parameters and return

**Data Handling**
- [ ] Create and manipulate lists
- [ ] Understand indexing
- [ ] Create dictionaries
- [ ] Access dictionary values
- [ ] Import modules

**Engineering Programming**
- [ ] Translate an equation into Python
- [ ] Keep track of units
- [ ] Use meaningful variable names
- [ ] Test calculations
- [ ] Validate results manually
- [ ] Identify logical errors
- [ ] Explain what the program is doing

---

## 26. What Comes Next?

After this foundation, the next stage is to move from **Basic Python Syntax → Engineering Computation**.

The next concepts to develop include:
- More practice with functions
- Better handling of lists and data
- Modules and packages
- NumPy arrays
- Vector and matrix operations
- Numerical calculations
- Basic plotting with Matplotlib
- Engineering-oriented problem solving

These skills will eventually support:

> Python → Numerical Computing → Mathematics → Engineering Simulation → 6DoF Dynamics → GNC → Estimation → Autonomous Aerospace Systems

---

## Key Takeaways

Python is a tool. The objective is not to "learn Python"; the objective is to use Python to think, calculate, simulate and solve engineering problems.

Remember:
- Understand the equation before coding it.
- Know what every variable represents.
- Track units.
- Test your code.
- Validate results independently.
- Write readable programs.
- Don't copy code you don't understand.

The ultimate goal is:

> **Engineering Understanding + Mathematics + Programming**

rather than programming skill in isolation.

**Learning Philosophy**

> Learn → Derive → Implement → Test → Validate → Document

This principle will remain applicable throughout the entire aerospace engineering learning journey.
