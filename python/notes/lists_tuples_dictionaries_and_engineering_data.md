# Lists, Tuples, Dictionaries & Engineering Data

**Objective:** Learn how to store, organise, access and manipulate multiple related engineering values using Python collections, and apply them to an aircraft parameter database.

---

## Why Collections Are Important

In engineering programs, we rarely work with only one value.

For example, an aircraft may have:
- Mass
- Length
- Wing span
- Wing area
- Maximum velocity
- Engine thrust
- Number of engines

Instead of creating many unrelated variables, Python provides data structures that allow us to store related values together.

The three important collection types for today are:
- Lists
- Tuples
- Dictionaries

> **Engineering principle:** Good code should represent the structure of the engineering problem, not just perform the calculation.

---

## Lists

A list is an ordered and changeable collection of values.

**Syntax:**

```python
my_list = [value1, value2, value3]
```

Example:

```python
velocities = [50, 100, 150, 200]
```

A list can contain different types of data:

```python
data = ["Fighter", 15000, 250, True]
```

However, in engineering programs, it is usually better to keep related data logically organised.

### Indexing Lists

Python uses zero-based indexing.

```python
velocities = [50, 100, 150, 200]
```

| Index | 0  | 1   | 2   | 3   |
|-------|----|-----|-----|-----|
| Value | 50 | 100 | 150 | 200 |

Accessing values:

```python
velocities[0]
velocities[2]
```

Result:
```
50
150
```

Negative indexing starts from the end:

```python
velocities[-1]
```

Result:
```
200
```

### Modifying Lists

Lists are mutable, meaning their contents can be changed.

```python
velocities[1] = 120
```

Now:
```python
[50, 120, 150, 200]
```

Adding an element:

```python
velocities.append(250)
```

Removing an element:

```python
velocities.remove(150)
```

Removing an element using its index:

```python
velocities.pop(1)
```

Finding the number of elements:

```python
len(velocities)
```

### Useful List Operations

| Method | Description |
|--------|-------------|
| `append()` | Add an element |
| `remove()` | Remove a specific value |
| `pop()` | Remove using an index |
| `insert()` | Insert at a specific position |
| `len()` | Number of elements |
| `sort()` | Sort the list |
| `max()` | Largest value |
| `min()` | Smallest value |
| `sum()` | Sum of numerical values |

Example:

```python
velocities = [150, 80, 220, 120]

maximum_velocity = max(velocities)
minimum_velocity = min(velocities)
average_velocity = sum(velocities) / len(velocities)
```

### Looping Through a List

Lists work very well with loops.

```python
velocities = [50, 100, 150, 200]

for velocity in velocities:
    print(velocity)
```

This processes every value in the list.

**Engineering example:**

```python
velocities = [50, 100, 150, 200]

for velocity in velocities:
    kinetic_energy = 0.5 * mass * velocity**2
    print(kinetic_energy)
```

This allows us to perform the same engineering calculation for multiple conditions.

---

## Tuples

A tuple is similar to a list, but it is immutable.

**Syntax:**

```python
my_tuple = (value1, value2, value3)
```

Example:

```python
aircraft_dimensions = (35.8, 122.4, 37.6)
```

The values can be accessed using indexing:

```python
aircraft_dimensions[0]
```

A tuple cannot normally be modified after creation. For example:

```python
aircraft_dimensions[0] = 40
```

will produce an error.

### Lists vs Tuples

| | List | Tuple |
|---|------|-------|
| Syntax | `dimensions = [35.8, 122.4, 37.6]` | `dimensions = (35.8, 122.4, 37.6)` |
| Behaviour | Mutable | Immutable |

Use a list when the data may need to change. Use a tuple when the collection represents a fixed group of values.

**Example:** A set of experimental measurements may be stored in a list because new measurements can be added. A fixed coordinate such as `(x, y, z)` can naturally be represented using a tuple.

---

## Dictionaries

A dictionary stores data using key-value pairs.

**Syntax:**

```python
dictionary = {
    "key": value,
    "key": value
}
```

Example:

```python
aircraft = {
    "mass": 79000,
    "wing_span": 35.8,
    "wing_area": 122.4,
    "max_velocity": 250
}
```

Here:
- `"mass"` → key, `79000` → value
- `"wing_span"` → key, `35.8` → value

### Accessing Dictionary Values

Instead of using an index, dictionaries use keys.

```python
aircraft["mass"]
```

Output:
```
79000
```

Another example:

```python
aircraft["wing_area"]
```

Output:
```
122.4
```

This is particularly useful for engineering data because the parameter name tells us exactly what the value represents.

### Modifying Dictionary Values

Dictionary values can be changed.

```python
aircraft["mass"] = 80000
```

A new key-value pair can also be added:

```python
aircraft["number_of_engines"] = 2
```

The dictionary now contains another parameter.

### Removing Dictionary Values

A key-value pair can be removed using:

```python
del aircraft["max_velocity"]
```

Another method is:

```python
aircraft.pop("max_velocity")
```

> Use these carefully because removing important engineering parameters may affect later calculations.

### Useful Dictionary Methods

Important methods:
- `keys()`
- `values()`
- `items()`
- `get()`

```python
aircraft.keys()      # returns the keys
aircraft.values()    # returns the values
aircraft.items()     # returns key-value pairs
```

Example:

```python
for parameter, value in aircraft.items():
    print(parameter, value)
```

This is useful for displaying an engineering database.

### The `get()` Method

You can retrieve a value using:

```python
aircraft.get("mass")
```

One advantage of `get()` is that it can provide a default value if the key does not exist.

```python
aircraft.get("fuel_capacity", "Not available")
```

If `"fuel_capacity"` does not exist, Python returns:

```
Not available
```

This can be useful when working with incomplete datasets.

---

## Lists and Dictionaries Together

Lists and dictionaries can be combined. For example, suppose we want to store multiple aircraft.

```python
aircraft_database = [
    {
        "name": "Aircraft A",
        "mass": 79000,
        "wing_span": 35.8
    },
    {
        "name": "Aircraft B",
        "mass": 60000,
        "wing_span": 30.0
    }
]
```

Here:
- The outer structure is a list.
- Each aircraft is represented by a dictionary.
- Each dictionary contains the aircraft's parameters.

This is a very important pattern for engineering programming.

### Accessing Data from Nested Structures

```python
aircraft_database[0]["mass"]
```

This means:
1. Select the first aircraft.
2. Access its `"mass"` parameter.

Similarly:

```python
aircraft_database[1]["wing_span"]
```

accesses the wing span of the second aircraft.

### Looping Through Multiple Aircraft

```python
for aircraft in aircraft_database:
    print(aircraft["name"])
```

To display several parameters:

```python
for aircraft in aircraft_database:
    print("Aircraft:", aircraft["name"])
    print("Mass:", aircraft["mass"])
    print("Wing span:", aircraft["wing_span"])
```

This allows the same code to process many aircraft.

---

## Choosing the Right Data Structure

A simple guideline:

**List** — Use when:
- Order matters
- Data may change
- Multiple similar values are being stored

**Tuple** — Use when:
- Order matters
- Data should remain fixed
- Values naturally form a fixed group

**Dictionary** — Use when:
- Values have meaningful names
- You need key-value relationships
- You want readable access to parameters

**List + Dictionary** — Use when:
- You have multiple objects
- Each object contains several named parameters

---

## Engineering Example — Aircraft Parameters

A single aircraft can be represented as:

```python
aircraft = {
    "name": "Example Aircraft",
    "mass": 79000,
    "length": 37.6,
    "wing_span": 35.8,
    "wing_area": 122.4,
    "max_velocity": 250,
    "engine_thrust": 120000,
    "number_of_engines": 2
}
```

Now calculations can use the stored parameters. For example:

```python
mass = aircraft["mass"]
velocity = aircraft["max_velocity"]

kinetic_energy = 0.5 * mass * velocity**2
```

This is much more organised than having unrelated variables scattered throughout the program.

---

## Aircraft Parameter Database

Today's main programming task is to create an aircraft parameter database.

Your program should contain several aircraft. For example:

```python
aircraft_database = [
    {
        "name": "Aircraft A",
        "mass": ...,
        "wing_span": ...,
        "wing_area": ...,
        "max_velocity": ...,
        "number_of_engines": ...
    },

    {
        "name": "Aircraft B",
        "mass": ...,
        "wing_span": ...,
        "wing_area": ...,
        "max_velocity": ...,
        "number_of_engines": ...
    }
]
```

Use realistic values from aircraft specifications rather than randomly invented values.

### Suggested Program Features

Your aircraft database should be able to:
- [ ] Store multiple aircraft
- [ ] Display aircraft names
- [ ] Display individual aircraft parameters
- [ ] Access a parameter using its key
- [ ] Modify a parameter
- [ ] Calculate a quantity using stored parameters
- [ ] Loop through all aircraft
- [ ] Display the stored information clearly

For example:

```
Aircraft: Example Aircraft
Mass: 79000 kg
Wing Span: 35.8 m
Wing Area: 122.4 m²
Maximum Velocity: 250 m/s
```

---

## Combining Today's Knowledge with Functions

This connects directly with Day 4. Instead of putting everything into one large program, create functions.

```python
def display_aircraft(aircraft):
    print("Aircraft:", aircraft["name"])
    print("Mass:", aircraft["mass"])
    print("Wing span:", aircraft["wing_span"])
```

Then:

```python
display_aircraft(aircraft)
```

This is where collections and functions begin working together.

---

## Important Engineering Programming Principle

Avoid creating unnecessary variables such as:

```python
aircraft_1_mass
aircraft_1_wing_span
aircraft_1_area

aircraft_2_mass
aircraft_2_wing_span
aircraft_2_area
```

This becomes difficult to maintain as the number of aircraft increases.

Instead, `aircraft_database` can contain all aircraft and their parameters.

> **Good data structure = simpler code + easier calculations + easier expansion.**

---

## Common Mistakes

**Confusing indexing**
Python starts indexing from 0, not 1.

**Using a list when a dictionary would be clearer**

```python
[79000, 35.8, 122.4]
```

does not immediately tell us what each number represents. A dictionary is clearer:

```python
{
    "mass": 79000,
    "wing_span": 35.8,
    "wing_area": 122.4
}
```

**Trying to modify a tuple**
Tuples are immutable.

**Misspelling dictionary keys**

```python
aircraft["wing_span"]
```

is different from:

```python
aircraft["wing span"]
```

**Mixing units**
Always document the units of engineering data. For example:

| Quantity | Unit |
|----------|------|
| mass | kg |
| velocity | m/s |
| length | m |
| area | m² |
| force | N |

> A numerically correct calculation with inconsistent units is still an incorrect engineering result.

---

## Engineering Application

These concepts will later become extremely important.

**Lists can store:**
- Simulation time steps
- Velocity measurements
- Temperature measurements
- Sensor readings
- Experimental data

**Tuples can represent:**
- Coordinates
- Fixed dimensions
- Vector-like groups of values

**Dictionaries can represent:**
- Aircraft parameters
- Simulation settings
- Sensor configurations
- Engine specifications
- Mission parameters

Later, more advanced tools such as NumPy arrays and Pandas data structures will handle larger numerical datasets.

---

## Day 5 Deliverable

Create: `python/codes/aircraft_parameter_database.py`

The program should demonstrate:
- [ ] Lists
- [ ] Tuples
- [ ] Dictionaries
- [ ] Indexing
- [ ] Dictionary keys
- [ ] Modifying data
- [ ] Loops through collections
- [ ] Multiple aircraft
- [ ] At least one engineering calculation
- [ ] At least one function from Day 4

---

## Day 5 Checklist

- [ ] I understand what a list is.
- [ ] I can create and modify a list.
- [ ] I understand indexing.
- [ ] I understand what a tuple is.
- [ ] I understand the difference between a list and tuple.
- [ ] I can create and access a dictionary.
- [ ] I can add and modify dictionary values.
- [ ] I can loop through a dictionary.
- [ ] I understand nested lists/dictionaries.
- [ ] I can store multiple aircraft using a list of dictionaries.
- [ ] I can use stored aircraft parameters in an engineering calculation.
- [ ] I can combine functions with dictionaries
