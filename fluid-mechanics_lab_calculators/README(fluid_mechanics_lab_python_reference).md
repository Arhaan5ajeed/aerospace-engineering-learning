# Python Reference — Fluid Mechanics Lab Calculations

> **Objective:** Understand, explain, implement, and debug the Python concepts, standard-library tools, and third-party libraries used to build engineering calculation programs for the Applied Fluid Dynamics Laboratory.

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How a Lab Calculator Works](#2-how-a-lab-calculator-works)
3. [Python Fundamentals Used in the Codes](#3-python-fundamentals-used-in-the-codes)
4. [User Input and Type Conversion](#4-user-input-and-type-conversion)
5. [Conditions, Loops, and Input Validation](#5-conditions-loops-and-input-validation)
6. [Lists, Dictionaries, and Structured Data](#6-lists-dictionaries-and-structured-data)
7. [Functions and Code Reusability](#7-functions-and-code-reusability)
8. [Mathematical Operations and the `math` Module](#8-mathematical-operations-and-the-math-module)
9. [NumPy for Numerical Engineering](#9-numpy-for-numerical-engineering)
10. [Matplotlib for Engineering Graphs](#10-matplotlib-for-engineering-graphs)
11. [CSV Files and Data Export](#11-csv-files-and-data-export)
12. [Formatted Output and f-Strings](#12-formatted-output-and-f-strings)
13. [Errors, Exceptions, and Debugging](#13-errors-exceptions-and-debugging)
14. [Program Structure and Execution](#14-program-structure-and-execution)
15. [Engineering Units and Numerical Reliability](#15-engineering-units-and-numerical-reliability)
16. [Complete Mini-Example](#16-complete-mini-example)
17. [Common Errors and Their Solutions](#17-common-errors-and-their-solutions)
18. [Python Syntax Quick Reference](#18-python-syntax-quick-reference)
19. [Learning Checklist](#19-learning-checklist)

---

## 1. Purpose and Scope

This document records the Python knowledge needed to understand the calculation programs developed for the Fluid Mechanics Lab module.

The experiments involve different engineering calculations, including:

- Flow measurement using a venturimeter and an orifice meter.
- Verification of Bernoulli's theorem.
- Determination of pipe friction factors and minor losses.
- Impact of a water jet on vanes.
- Reynolds number and flow visualisation.
- Air blower performance.
- Oil viscosity using a Redwood viscometer.
- Reciprocating air compressor performance.

Each experiment has different physical equations, but the software often follows the same computational pattern:

$$\text{Read observations} \longrightarrow \text{Validate inputs} \longrightarrow \text{Convert units} \longrightarrow \text{Calculate results} \longrightarrow \text{Display table} \longrightarrow \text{Plot graphs} \longrightarrow \text{Export data}$$

The purpose of learning these tools is not merely to run the programs. It is to understand the implementation well enough to modify, test, and eventually develop the calculators independently.

### 1.1 Knowledge assumed before this module

The following topics were studied previously or form part of the existing Python foundation:

- Variables and basic data types.
- Arithmetic and comparison operators.
- Lists, tuples, and dictionaries.
- Basic loops and conditional statements.
- NumPy arrays, vectors, and matrices.
- Vector operations, dot products, and matrix multiplication.
- Basic linear algebra using `numpy.linalg`.
- Matplotlib fundamentals and basic graph plotting.

This document builds on those topics and explains the additional programming techniques used in the experiment calculators.

### 1.2 The main tools

| Tool | Type | Purpose |
| :--- | :--- | :--- |
| **Python** | Programming language | Implements calculations and program logic |
| `math` | Standard-library module | Mathematical functions and constants |
| `csv` | Standard-library module | Writes calculated results to CSV files |
| **NumPy** | Third-party library | Numerical arrays and matrix operations |
| **Matplotlib** | Third-party library | Generates graphs and saves figures |
| `input()` | Built-in function | Collects observations from the user |
| `try` / `except` | Python syntax | Handles invalid input and runtime errors |
| **f-strings** | String formatting | Displays readable results and units |
| **Functions** | Language feature | Organises reusable calculations |
| **Lists & Dicts** | Data structures | Stores observations and results |

> **Important distinction:** NumPy and Matplotlib must be installed in the Python environment. Modules such as `math` and `csv` are included with Python by default.

---

## 2. How a Lab Calculator Works

A typical experiment calculator can be understood as a pipeline:

```text
                     USER
                      |
                      v
              Enter observations
                      |
                      v
               Validate inputs
                      |
                      v
                Convert units
                      |
                      v
           Apply physical equations
                      |
                      v
            Store calculated data
                      |
          +-----------+-----------+
          |                       |
          v                       v
  Print result table       Generate graphs
          |                       |
          +-----------+-----------+
                      |
                      v
               Export CSV data
```

For example, consider a flow measurement experiment. The user supplies the collecting-tank area, water-level rise, and collection time.

The discharge is calculated using:

$$Q = \frac{A \cdot h}{t}$$

where:
- $Q$ = volumetric discharge in $\mathrm{m^3/s}$
- $A$ = collecting-tank cross-sectional area in $\mathrm{m^2}$
- $h$ = rise in water level in $\mathrm{m}$
- $t$ = collection time in seconds

The program then stores the calculated discharge alongside the input observations. Multiple readings can be used to construct a table and plot discharge against another measured or calculated quantity.

---

## 3. Python Fundamentals Used in the Codes

### 3.1 Variables

A variable is a name that refers to a value.

```python
gravity = 9.81
density = 1000.0
pipe_diameter = 0.020
```

Python does not require an explicit declaration of a variable's type.

```python
time_seconds = 12
time_seconds = 12.5
```

#### Naming conventions
Use descriptive `snake_case` names for variables and functions.

```python
actual_discharge = 0.0025
theoretical_discharge = 0.0028

coefficient_of_discharge = actual_discharge / theoretical_discharge
```

Short names are still reasonable when they are standard engineering symbols, such as `Q`, `Re`, `Cd`, or `hf`.

### 3.2 Basic data types

| Type | Meaning | Example |
| :--- | :--- | :--- |
| `int` | Integer | `950` |
| `float` | Floating-point number | `9.81` |
| `str` | Text | `"Backward-curved"` |
| `bool` | Logical value | `True` |
| `NoneType` | Absence of a value | `None` |

Check a value's type using `type()`:

```python
value = 9.81
print(type(value))
# Output: <class 'float'>
```

### 3.3 Arithmetic operators

| Operator | Operation | Example |
| :---: | :--- | :--- |
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `**` | Exponentiation | `a ** 2` |
| `//` | Floor division | `7 // 2` (gives `3`) |
| `%` | Remainder (Modulo) | `7 % 2` (gives `1`) |

```python
diameter = 0.020
area = 3.141592653589793 * diameter**2 / 4
```

> **Important:** `/` performs ordinary division and always returns a floating-point result, even if both operands are integers.

### 3.4 Operator precedence

Python follows standard mathematical operator precedence (PEMDAS/BODMAS). Use parentheses to make engineering equations clear and unambiguous:

```python
area = (3.141592653589793 * diameter**2) / 4
```

### 3.5 Comments

Comments start with `#` and are ignored during execution:

```python
# Calculate the cross-sectional area of the pipe.
area = math.pi * diameter**2 / 4
```

### 3.6 Import statements

Importing modules makes external functions and constants available:

```python
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
```

The `as` keyword assigns an alias (`np` for NumPy and `plt` for Matplotlib Pyplot).

---

## 4. User Input and Type Conversion

### 4.1 The `input()` function

`input()` displays a prompt and captures user input as a string:

```python
diameter_text = input("Enter pipe diameter in mm: ")
```

If the user enters `20`, the value stored is string `"20"`, not numeric `20`.

### 4.2 Converting strings into numbers

Use `float()` or `int()` to convert string inputs into numerical types:

```python
diameter_mm = float(input("Enter pipe diameter in mm: "))
number_of_readings = int(input("Enter number of readings: "))
```

| Function | Purpose | Example |
| :--- | :--- | :--- |
| `int(x)` | Convert to integer | `int("5")` $\rightarrow$ `5` |
| `float(x)` | Convert to floating-point number | `float("5.2")` $\rightarrow$ `5.2` |
| `str(x)` | Convert to text string | `str(12)` $\rightarrow$ `"12"` |

> Calling `int("5.2")` directly will raise a `ValueError`.

### 4.3 Converting units after input

Convert all inputs to standard SI units before performing calculations:

```python
diameter_mm = float(input("Diameter (mm): "))
diameter_m = diameter_mm / 1000

pressure_kgf_cm2 = float(input("Gauge pressure (kgf/cm^2): "))
pressure_pa = pressure_kgf_cm2 * 98066.5
```

---

## 5. Conditions, Loops, and Input Validation

### 5.1 `if`, `elif`, and `else`

Conditional statements allow logic branching based on fluid dynamic parameters:

```python
if reynolds_number < 2000:
    flow_type = "Laminar"
elif reynolds_number <= 4000:
    flow_type = "Transitional"
else:
    flow_type = "Turbulent"
```

### 5.2 Comparison & Logical operators

- **Comparison:** `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`
- **Logical:** `and`, `or`, `not`

```python
if diameter_m > 0 and time_seconds > 0:
    print("Inputs are positive and valid.")
```

### 5.3 Loops

#### The `for` loop
Iterates over lists or range sequences:

```python
times = [12.5, 10.8, 9.4]
for time in times:
    discharge = 0.015 / time
    print(discharge)
```

Using `range()`:

```python
number_of_readings = 5
for i in range(number_of_readings):
    print(f"Reading {i + 1}")
```

#### The `while` loop
Repeats as long as a condition evaluates to `True`:

```python
time_seconds = 0.0
while time_seconds <= 0:
    time_seconds = float(input("Enter positive time (s): "))
```

### 5.4 Input validation

Prevent invalid physical quantities using explicit exceptions:

```python
diameter_mm = float(input("Diameter (mm): "))
if diameter_mm <= 0:
    raise ValueError("Diameter must be positive.")
```

#### Validation Checklist
- Diameters, areas, and fluid properties must be positive ($> 0$).
- Collection time must be non-zero to prevent division by zero.
- Entered values must be real finite numbers (`math.isfinite()`).

---

## 6. Lists, Dictionaries, and Structured Data

### 6.1 Lists

Lists are ordered, mutable sequences:

```python
discharges = [0.0012, 0.0015, 0.0019]

# Indexing
first_reading = discharges[0]    # 0.0012
last_reading = discharges[-1]    # 0.0019

# Appending
discharges.append(0.0022)

# List Comprehension
diameters_mm = [15, 20, 25]
diameters_m = [d / 1000 for d in diameters_mm]
```

### 6.2 Dictionaries

Dictionaries store key-value pairs:

```python
reading = {
    "time_s": 12.5,
    "diameter_m": 0.020,
    "discharge_m3_s": 0.0012
}

# Accessing and modifying
print(reading["time_s"])
reading["flow_type"] = "Turbulent"
```

### 6.3 Lists of Dictionaries

Ideal for managing multiple experimental test runs:

```python
results = [
    {"time_s": 12.5, "discharge_m3_s": 0.0012},
    {"time_s": 10.8, "discharge_m3_s": 0.0014}
]

print(results[1]["discharge_m3_s"]) # 0.0014
```

---

## 7. Functions and Code Reusability

Functions structure code into modular, repeatable calculation blocks.

```python
def calculate_discharge(area, rise, time_seconds):
    """Calculates volumetric discharge Q = A * h / t"""
    return area * rise / time_seconds

# Calling the function with named arguments
Q = calculate_discharge(area=0.15, rise=0.10, time_seconds=12.0)
```

### Parameters vs Arguments
- **Parameter:** The variable listed inside the function definition (`area`).
- **Argument:** The actual value passed during a function call (`0.15`).

---

## 8. Mathematical Operations and the `math` Module

### 8.1 Functions in `math`

```python
import math

# Constants
pi_val = math.pi

# Common operations
root_val = math.sqrt(25)     # 5.0
ln_val = math.log(2.71828)   # Natural log (ln)
log10_val = math.log10(100)  # Base-10 log
```

### 8.2 Common Fluid Formulas in Python

#### Pipe Cross-Sectional Area: $A = \frac{\pi D^2}{4}$
```python
area = math.pi * diameter**2 / 4
```

#### Torricelli / Ideal Velocity: $V = \sqrt{2gH}$
```python
velocity = math.sqrt(2 * 9.81 * head)
```

#### Isothermal Compressor Work: $W_{\text{iso}} = P_a Q \ln(r)$
```python
isothermal_work = atmospheric_pressure * volume_flow_rate * math.log(pressure_ratio)
```

---

## 9. NumPy for Numerical Engineering

### 9.1 Creating Arrays and Basic Operations

```python
import numpy as np

times = np.array([12.5, 10.8, 9.4])
discharges = 0.001 / times  # Element-wise operations
```

### 9.2 Element-wise vs Matrix Multiplication

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise product
elem_product = A * B

# Matrix multiplication
matrix_product = A @ B
```

---

## 10. Matplotlib for Engineering Graphs

### 10.1 Complete Plotting Pipeline

```python
import matplotlib.pyplot as plt

discharge = [0.001, 0.0015, 0.0018, 0.0020]
head_loss = [0.12, 0.25, 0.38, 0.51]

plt.figure(figsize=(8, 5))
plt.plot(discharge, head_loss, marker="o", linestyle="-", color="b", label="Head Loss")

plt.xlabel("Discharge ($m^3/s$)")
plt.ylabel("Head Loss ($m$)")
plt.title("Head Loss vs Discharge in Pipe Flow")
plt.grid(True)
plt.legend()

# Save figure before show/close
plt.savefig("head_loss_vs_discharge.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
```

---