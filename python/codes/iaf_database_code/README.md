# Indian Air Force Fighter Jet Database

> **Status:** Week 1 Complete
> **Project Stage:** Python Foundations → Engineering Application
> **Language:** Python
> **Repository:** `aerospace-engineering-learning`

---

## Project Overview

The **Indian Air Force Fighter Jet Database** is a menu-driven Python program designed to store, search, compare, calculate engineering parameters for, and manage information about fighter aircraft.

The project was developed as part of **Week 1 of my Aerospace Engineering + Python learning roadmap**.

The primary purpose of this project is not simply to create an aircraft database, but to apply fundamental Python programming concepts to a practical aerospace engineering problem.

The program currently includes:

* Fighter aircraft data storage
* Aircraft search
* Aircraft comparison
* Wing loading calculation
* Thrust-to-weight ratio calculation
* Database display
* Adding new aircraft
* Updating aircraft information
* Deleting aircraft information
* Continuous menu operation
* Basic input handling and validation

---

# Current Aircraft Database

The database currently contains information for:

* Sukhoi Su-30MKI
* Dassault Rafale
* HAL Tejas
* MiG-29UPG
* Mirage 2000
* SEPECAT Jaguar

Each aircraft is represented using a Python dictionary containing parameters such as:

| Parameter             | Description           | Unit |
| --------------------- | --------------------- | ---- |
| `name`                | Aircraft name         | —    |
| `role`                | Primary aircraft role | —    |
| `empty_mass_kg`       | Empty aircraft mass   | kg   |
| `max_takeoff_mass_kg` | Maximum takeoff mass  | kg   |
| `length_m`            | Aircraft length       | m    |
| `wingspan_m`          | Wingspan              | m    |
| `wing_area_m2`        | Reference wing area   | m²   |
| `max_speed_mach`      | Maximum speed         | Mach |
| `service_ceiling_m`   | Service ceiling       | m    |
| `engine_count`        | Number of engines     | —    |

---

# Python Concepts Learned

This project was used to apply and reinforce several fundamental Python concepts.

## 1. Variables

Variables are used to store values such as:

```python
jet_name = input(...)
weight_N = ...
wing_loading = ...
```

This reinforced the relationship between **data storage and computation**.

---

## 2. Data Types

The project uses several Python data types:

* `str`
* `int`
* `float`
* `bool`
* `list`
* `dict`
* `None`

For example:

```python
max_takeoff_mass_kg = 34000
wing_area_m2 = 62
max_speed_mach = 2.0
```

---

## 3. Lists

The complete database is stored inside a list:

```python
fighter_jet_database = [
    {...},
    {...},
    {...}
]
```

This allows multiple aircraft records to be stored together.

---

## 4. Dictionaries

Each aircraft is represented using a dictionary:

```python
{
    "name": "Rafale",
    "role": "Multirole",
    "empty_mass_kg": 10000,
    "wing_area_m2": 45.7
}
```

This was an important step toward understanding **structured engineering data**.

---

## 5. Nested Data Structures

The project combines:

```text
List
 └── Dictionary
      ├── Aircraft name
      ├── Mass
      ├── Wing area
      ├── Speed
      └── Other parameters
```

This demonstrates how Python can represent real-world engineering datasets.

---

## 6. Conditional Statements

The menu system uses:

```python
if
elif
else
```

to determine which operation the user selects.

Example:

```python
elif user_choice == '4':
```

---

## 7. `while True`

The main menu is placed inside:

```python
while True:
```

This allows the program to continue running until the user explicitly chooses to exit.

---

## 8. `for` Loops

The database is searched using:

```python
for jet in fighter_jet_database:
```

This allows the program to inspect each aircraft one by one.

---

## 9. Boolean Flags

Variables such as:

```python
found = False
```

are used to track whether an aircraft was successfully located.

When a match is found:

```python
found = True
```

This helped develop an understanding of **program state**.

---

## 10. `break`

`break` is used to stop searching once the required aircraft has been found:

```python
break
```

It is also used to terminate the main `while True` loop when the user selects Exit.

An important distinction learned during this project:

> `break` exits the **nearest loop in which it is executed**.

---

## 11. User Input

The program accepts user input using:

```python
input()
```

Input is cleaned using:

```python
.strip()
.lower()
```

For example:

```python
jet_name = input("Enter aircraft name: ").strip()
```

This makes the program more tolerant of unnecessary spaces and capitalization differences.

---

## 12. Type Conversion

User input initially arrives as a string.

Numerical calculations therefore require conversion:

```python
float(input(...))
```

or:

```python
int(input(...))
```

This reinforced the importance of understanding **data types in engineering calculations**.

---

## 13. F-Strings

Formatted output is produced using f-strings:

```python
print(f"Wing Loading of {jet['name']}: {wing_loading:.2f} N/m²")
```

The `.2f` formatting displays the numerical result to two decimal places.

---

## 14. List Operations

The program uses operations such as:

```python
append()
remove()
```

to modify the database.

For example:

```python
fighter_jet_database.append(new_jet)
```

allows a new aircraft to be added.

---

# Aerospace Engineering Concepts Applied

The project is also an introduction to using programming for engineering calculations.

## 1. Wing Loading

The program calculates conventional aerodynamic wing loading:

$$
\boxed{\frac{W}{S}}
$$

where:

* \(W\) = aircraft weight in N
* \(S\) = wing reference area in m²

Aircraft weight is calculated from:

$$
W = mg
$$

Therefore:

$$
\boxed{\frac{W}{S}=\frac{mg}{S}}
$$

The program uses:

```python
weight_N = jet['max_takeoff_mass_kg'] * 9.81
wing_loading = weight_N / jet['wing_area_m2']
```

### Physical significance

Wing loading is an important aerodynamic parameter related to aircraft performance.

From the lift equation:

$$
L = \frac{1}{2}\rho V^2 S C_L
$$

For steady, level flight:

$$
L=W
$$

Therefore:

$$
\boxed{\frac{W}{S}=\frac{1}{2}\rho V^2C_L}
$$

This connects the programming calculation to actual aircraft aerodynamics.

---

## 2. Thrust-to-Weight Ratio

The program also calculates:

$$
\boxed{T/W}
$$

where:

* \(T\) = total thrust
* \(W\) = aircraft weight

Currently, the program uses a **simplified assumed thrust value per engine**.

This is intentionally a learning approximation rather than a representation of the exact operational thrust of every aircraft.

---

# Program Functionality

The main menu currently contains:

```text
1. Display all fighter jets
2. Search fighter jet by name
3. Compare two fighter jets
4. Calculate wing loading
5. Calculate thrust-to-weight ratio
6. Display database
7. Add fighter jet
8. Update fighter jet information
9. Delete fighter jet information
10. Exit
```

The program therefore goes beyond a static dataset and introduces **basic CRUD operations**.

### CRUD

| Operation | Program Function            |
| --------- | --------------------------- |
| Create    | Add aircraft                |
| Read      | Search/display aircraft     |
| Update    | Modify aircraft information |
| Delete    | Remove aircraft             |

This is an early introduction to how real software manages structured data.

---

# What I Learned During Week 1

Week 1 was primarily about moving from **Python syntax → actual engineering programming**.

### Programming

I learned and practiced:

* Variables
* Data types
* Input/output
* Type conversion
* Lists
* Dictionaries
* Nested data structures
* `if / elif / else`
* `for` loops
* `while` loops
* `break`
* Boolean flags
* String methods
* F-strings
* List methods
* Basic program flow
* Menu-driven programs
* Searching through datasets
* Adding, updating and deleting records

### Engineering

I also practiced:

* Dimensional awareness
* Mass vs. weight
* SI units
* Wing loading
* Thrust-to-weight ratio
* Using physical equations inside programs
* Connecting aircraft parameters to aerodynamic concepts

---

# Programming Lessons From Mistakes

One of the goals of this project was to **debug my own mistakes instead of simply copying corrected code**.

For example, an early version contained:

```python
empty_mass = float(input("Enter empty mass(Kg): ")).strip()
```

This was incorrect because `float()` converts the input into a floating-point number before `.strip()` is called.

The correct order is:

```python
empty_mass = float(input("Enter empty mass(Kg): ").strip())
```

This reinforced the importance of understanding **the order in which Python operations are performed**.

---

# Current Limitations

The project is functional, but it is still an early-stage program.

### 1. No persistent storage

All data currently exists only while the program is running.

When the program closes, newly added or modified aircraft are lost.

---

### 2. Limited input validation

The program does not yet comprehensively handle:

* Negative masses
* Zero wing area
* Invalid numerical input
* Invalid engine counts
* Incorrect data ranges

For example:

```python
float(input(...))
```

can generate an error if the user enters non-numerical text.

---

### 3. Simplified thrust model

The current thrust-to-weight calculation assumes the same thrust per engine for every aircraft.

This is useful for learning the programming concept but is **not suitable for accurate aircraft performance analysis**.

---

### 4. Hard-coded database

Aircraft information is manually written into the Python source code.

A larger database would require an external data format.

---

### 5. Repeated code

Some operations currently repeat similar search logic.

This can eventually be reduced using functions.

---

### 6. No automated testing

The program currently relies primarily on manual testing.

A future version could include dedicated test cases.

---

# Future Scope of Improvement

The project can eventually evolve from a beginner Python program into a much more structured aerospace data-analysis application.

## Phase 1 — Code Structure

Refactor repeated sections into functions:

```python
def display_aircraft():
    ...

def search_aircraft():
    ...

def compare_aircraft():
    ...

def calculate_wing_loading():
    ...

def calculate_thrust_to_weight():
    ...

def add_aircraft():
    ...

def update_aircraft():
    ...

def delete_aircraft():
    ...
```

This will improve:

* Readability
* Maintainability
* Reusability
* Debugging
* Program organization

---

## Phase 2 — Better Validation

Add proper validation for:

* Numerical input
* Positive values
* Valid aircraft names
* Duplicate aircraft
* Invalid menu selections
* Impossible physical values

Potential tools:

```python
try
except
```

and validation loops.

---

## Phase 3 — Aircraft-Specific Engine Data

Instead of assuming identical engine thrust, the database could contain:

```python
"engine_thrust_kN": ...
```

This would allow:

$$
T_{\text{total}} =
T_{\text{engine}}\times N_{\text{engines}}
$$

and:

$$
T/W =
\frac{T_{\text{total}}}{W}
$$

using aircraft-specific values.

---

## Phase 4 — Persistent Data

The database could eventually be stored in:

* JSON
* CSV
* SQLite

This would allow changes to survive after the program closes.

---

## Phase 5 — Engineering Analysis

Additional calculations could include:

* Aspect ratio
* Taper ratio
* Power-to-weight ratio
* Fuel fraction
* Thrust loading
* Estimated stall speed
* Dynamic pressure
* Lift coefficient
* Drag coefficient
* Drag force
* Range estimation
* Endurance estimation

These should be implemented only after understanding the underlying aerospace equations.

---

## Phase 6 — Data Analysis

After developing stronger Python fundamentals, the project could use:

* NumPy
* Pandas
* Matplotlib

This could enable:

* Aircraft parameter comparisons
* Wing-loading plots
* Thrust-to-weight plots
* Mass comparisons
* Speed comparisons
* Statistical analysis

Example future visualization:

$$
\text{Wing Loading} \quad \text{vs.} \quad \text{Maximum Speed}
$$

---

## Phase 7 — Engineering Simulation

Eventually, the database could become a component of a larger aerospace simulation environment.

Possible future integration:

```text
Aircraft Database
       ↓
Aircraft Parameters
       ↓
Aerodynamic Model
       ↓
Performance Calculations
       ↓
Simulation
       ↓
Visualization
```

This connects the project to future work in:

* Flight dynamics
* Aircraft performance
* 6-DoF simulation
* Guidance, Navigation & Control
* Control systems
* Numerical methods

---

# Week 1 Milestone

## Status: COMPLETE 

The objective of Week 1 was to begin transitioning from **learning Python syntax** to **using Python as an engineering tool**.

By completing this project, I have demonstrated that I can:

* Store structured aerospace data
* Process user input
* Search datasets
* Manipulate dictionaries and lists
* Implement menu-driven logic
* Perform engineering calculations
* Apply SI units
* Debug basic Python errors
* Build a complete interactive program
* Think about software limitations and future architecture

> **The important achievement of Week 1 is not the size of the program. It is learning to translate an engineering problem into computational logic.**

---

# Development Philosophy

This project will be developed incrementally.

The goal is **not** to immediately add advanced libraries, graphical interfaces, databases, or machine learning.

Instead:

```text
Python Fundamentals
        ↓
Engineering Calculations
        ↓
Structured Programs
        ↓
Numerical Methods
        ↓
Simulation
        ↓
Data Analysis
        ↓
Control & Estimation
        ↓
Advanced Aerospace Systems
```

Each stage should be built on an understanding of the previous stage.

---

# Project Status

| Component                     | Status    |
| ----------------------------- | ----------|
| Aircraft database             |  Complete |
| Aircraft search               |  Complete |
| Aircraft comparison           |  Complete |
| Wing loading                  |  Complete |
| Thrust-to-weight calculation  |  Complete |
| Add aircraft                  |  Complete |
| Update aircraft               |  Complete |
| Delete aircraft               |  Complete |
| Menu system                   |  Complete |
| Basic debugging               |  Complete |
| Input validation              |  Future   |
| Functions/refactoring         |  Future   |
| Persistent storage            |  Future   |
| Data analysis                 |  Future   |
| Visualization                 |  Future   |
| Advanced aircraft performance |  Future   |

---

# Week 1 Conclusion

**Week 1 is officially complete.**

This project represents the first step toward using programming not merely as a computer-science skill, but as a tool for **aerospace engineering, mathematical modelling, numerical computation, and simulation**.

The next stage will build on these fundamentals rather than abandoning them for unnecessarily advanced tools.

> **Build → Understand → Debug → Improve → Apply.**

---

**Author:** Arhaan Sajeed
**Degree:** B.Tech Aerospace Engineering
**Academic Year:** 2025–2029
**Project:** `aerospace-engineering-learning`
**Milestone:** **Week 1 — Completed**
