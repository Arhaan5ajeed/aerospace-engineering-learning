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

## 11. CSV Files and Data Export

Exporting experimental datasets using the built-in `csv` module:

```python
import csv

data = [
    {"reading": 1, "discharge": 0.0012, "reynolds": 2100},
    {"reading": 2, "discharge": 0.0015, "reynolds": 2600}
]

fieldnames = ["reading", "discharge", "reynolds"]

with open("lab_results.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

---

## 12. Formatted Output and f-Strings

f-Strings provide concise syntax for output formatting:

```python
discharge = 0.00123456
reynolds = 2450.7

print(f"Discharge: {discharge:.4e} m^3/s")  # Scientific notation -> 1.2346e-03
print(f"Reynolds No: {reynolds:.1f}")       # Fixed float decimal -> 2450.7
```

---

## 13. Errors, Exceptions, and Debugging

Use `try-except` blocks to handle runtime conversion errors gracefully:

```python
while True:
    try:
        time_s = float(input("Enter collection time (s): "))
        if time_s <= 0:
            print("Time must be positive.")
            continue
        break
    except ValueError:
        print("Invalid numerical input. Please enter a number.")
```

---

## 14. Program Structure and Execution

Recommended modular file structure for laboratory calculators:

```python
import math
import csv
import matplotlib.pyplot as plt

def collect_inputs():
    """Handles user input collection and validation."""
    pass

def calculate_results(inputs):
    """Executes fluid mechanics equations."""
    pass

def main():
    """Main execution flow."""
    inputs = collect_inputs()
    results = calculate_results(inputs)
    # Output tables, plot graphs, and export CSV

if __name__ == "__main__":
    main()
```

---

## 15. Engineering Units and Numerical Reliability

- Always convert parameters to base **SI units** ($\mathrm{m}$, $\mathrm{kg}$, $\mathrm{s}$, $\mathrm{Pa}$, $\mathrm{m^3/s}$) prior to evaluation.
- Avoid comparing floating point numbers directly using equality (`==`). Use `math.isclose()` or check tolerances:

```python
import math
if math.isclose(actual_val, theoretical_val, rel_tol=1e-3):
    print("Values match within tolerance.")
```

---

## 16. Complete Mini-Example

Below is a complete, executable lab calculator script for determining flow rate via a collection tank:

```python
import math

def calculate_pipe_flow(diameter_mm, level_rise_cm, time_s):
    # 1. Unit Conversions
    diameter_m = diameter_mm / 1000.0
    level_rise_m = level_rise_cm / 100.0
    
    # 2. Geometry & Physics Calculations
    tank_area = 0.5 * 0.5  # 0.5m x 0.5m collecting tank
    volume_m3 = tank_area * level_rise_m
    discharge_m3_s = volume_m3 / time_s
    
    pipe_area = (math.pi * diameter_m**2) / 4.0
    velocity_m_s = discharge_m3_s / pipe_area
    
    return {
        "discharge": discharge_m3_s,
        "velocity": velocity_m_s
    }

def main():
    print("=== Pipe Flow Rate Calculator ===")
    try:
        d_mm = float(input("Enter pipe inner diameter (mm): "))
        h_cm = float(input("Enter water level rise (cm): "))
        t_s = float(input("Enter collection time (s): "))
        
        if d_mm <= 0 or h_cm <= 0 or t_s <= 0:
            print("Error: All inputs must be positive numbers.")
            return

        results = calculate_pipe_flow(d_mm, h_cm, t_s)
        
        print("\n--- Results ---")
        print(f"Discharge (Q) : {results['discharge']:.6f} m^3/s ({results['discharge']*1000:.3f} L/s)")
        print(f"Velocity (V)  : {results['velocity']:.3f} m/s")

    except ValueError:
        print("Error: Invalid numerical input entered.")

if __name__ == "__main__":
    main()
```

---

## 17. Common Errors and Their Solutions

| Error | Typical Cause | Solution |
| :--- | :--- | :--- |
| `ValueError: could not convert string to float` | User typed text or empty space into `input()` | Wrap `input()` inside a `try-except ValueError` loop. |
| `ZeroDivisionError: division by zero` | Time or area evaluated to `0.0` | Validate inputs to ensure non-zero denominators. |
| `TypeError: unsupported operand type(s)` | Operating on strings instead of numbers | Convert strings using `float()` or `int()`. |
| `IndexError: list index out of range` | Accessing an index outside list bounds | Verify list length with `len()` before indexing. |
| `FileNotFoundError` | Reading or writing to an invalid path | Verify relative paths and directory permissions. |

---

## 18. Python Syntax Quick Reference

```python
# Variables & Basic Types
x = 10                  # int
y = 3.14                # float
name = "Venturi"        # str
is_laminar = True       # bool

# Data Structures
my_list = [1, 2, 3]     # List
my_dict = {"a": 1}      # Dictionary
my_tuple = (10, 20)     # Tuple

# Controls
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Lesser")

# Functions
def area(d):
    return math.pi * (d**2) / 4
```

---

## 19. Learning Checklist

- [ ] Can convert raw user input strings to floating-point numbers safely.
- [ ] Understand how to convert lab measurement units into SI units in Python.
- [ ] Know how to structure equations using `math` functions (`math.sqrt`, `math.pi`, `math.log`).
- [ ] Able to store observations using lists and dictionaries.
- [ ] Understand how to plot and format line/scatter plots using `matplotlib.pyplot`.
- [ ] Can export calculated summary tables to `.csv` files using the `csv` module.
- [ ] Know how to prevent program crashes using `try-except` blocks.