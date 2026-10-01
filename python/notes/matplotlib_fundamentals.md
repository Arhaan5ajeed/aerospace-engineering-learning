# Matplotlib Fundamentals

**Objective: Learn the fundamentals of Matplotlib and use it to visualise engineering data clearly. By the end of today, you should be able to create, label, customise, and save basic engineering plots.**

---

## 1. Why Matplotlib?

Until now, we have mainly worked with numerical values.

For example:

```python
velocity = np.array([50, 100, 150, 200, 250])
```

The numbers tell us what is happening, but a graph can show the relationship much more clearly.

Matplotlib is a Python library used to create visualisations such as:

- Line plots
- Scatter plots
- Bar charts
- Histograms
- Engineering curves
- Experimental-data plots

For aerospace engineering, plotting is extremely useful for understanding:

- Velocity vs time
- Altitude vs time
- Pressure vs altitude
- Lift vs angle of attack
- Drag vs velocity
- Temperature vs time
- Engine performance
- Experimental and simulation data

> A graph is not decoration. It is a way of understanding data.

---

## 2. Importing Matplotlib

The most commonly used plotting module is `pyplot`.

```python
import matplotlib.pyplot as plt
```

The `plt` abbreviation is the conventional name used for `matplotlib.pyplot`.

---

## 3. Your First Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.show()
```

This creates a basic line plot.

Here:

- `x` → horizontal-axis values
- `y` → vertical-axis values
- `plt.plot()` → creates the line
- `plt.show()` → displays the figure

---

## 4. Why X and Y Must Correspond

Suppose:

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
```

There are five x-values and five y-values.

Matplotlib pairs them:

```text
(1, 10)
(2, 20)
(3, 30)
(4, 40)
(5, 50)
```

These points are then connected to create the line.

---

## 5. Plotting NumPy Arrays

Matplotlib works extremely well with NumPy.

```python
import numpy as np
import matplotlib.pyplot as plt

velocity = np.array([50, 100, 150, 200, 250])
kinetic_energy = 0.5 * 1000 * velocity**2

plt.plot(velocity, kinetic_energy)

plt.show()
```

This is the important connection from the previous days:

```text
NumPy
  ↓
Engineering calculation
  ↓
Matplotlib
  ↓
Visualisation
```

---

## 6. Adding a Title

A graph should communicate what it represents.

```python
plt.title("Kinetic Energy vs Velocity")
```

Example:

```python
plt.plot(velocity, kinetic_energy)

plt.title("Kinetic Energy vs Velocity")

plt.show()
```

---

## 7. Labelling the Axes

Use:

```python
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")
```

Complete example:

```python
plt.plot(velocity, kinetic_energy)

plt.title("Kinetic Energy vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

plt.show()
```

> Always include units when plotting physical quantities.

---

## 8. Adding a Grid

A grid makes numerical relationships easier to read.

```python
plt.grid()
```

Example:

```python
plt.plot(velocity, kinetic_energy)

plt.title("Kinetic Energy vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")
plt.grid()

plt.show()
```

---

## 9. Marking Data Points

You can display individual data points using a marker.

```python
plt.plot(
    velocity,
    kinetic_energy,
    marker="o"
)
```

The `"o"` represents circular markers.

Other common markers include:

| Marker | Shape |
|--------|-------|
| `"o"` | Circle |
| `"s"` | Square |
| `"^"` | Triangle |
| `"x"` | X |

Do not memorise all of them. You can look them up when required.

---

## 10. Line Styles

Matplotlib allows different line styles.

Examples:

```python
plt.plot(x, y, linestyle="-")
```

Solid line.

```python
plt.plot(x, y, linestyle="--")
```

Dashed line.

```python
plt.plot(x, y, linestyle=":")
```

Dotted line.

For now, focus on understanding the concept rather than memorising every style.

---

## 11. Plotting Multiple Lines

You can put multiple datasets on the same graph.

```python
velocity = np.array([50, 100, 150, 200, 250])

ke_mass_1000 = 0.5 * 1000 * velocity**2
ke_mass_1500 = 0.5 * 1500 * velocity**2

plt.plot(velocity, ke_mass_1000, label="Mass = 1000 kg")
plt.plot(velocity, ke_mass_1500, label="Mass = 1500 kg")

plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Kinetic Energy for Different Masses")

plt.legend()
plt.grid()

plt.show()
```

---

## 12. Legend

When multiple datasets are plotted, the viewer needs to know which line represents which dataset.

Use:

```python
plt.legend()
```

The labels come from:

```python
label="Mass = 1000 kg"
```

This is especially useful when comparing:

- Different aircraft
- Different masses
- Different air densities
- Experimental vs theoretical results
- Different simulation conditions

---

## 13. Scatter Plots

A line plot connects points.

A scatter plot displays individual data points.

Use:

```python
plt.scatter(x, y)
```

Example:

```python
import matplotlib.pyplot as plt

velocity = [50, 100, 150, 200, 250]
drag = [120, 450, 980, 1700, 2600]

plt.scatter(velocity, drag)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.title("Measured Drag vs Velocity")

plt.grid()

plt.show()
```

Scatter plots are particularly useful for experimental measurements.

---

## 14. Line Plot vs Scatter Plot

| Plot | Typical use |
|---|---|
| `plt.plot()` | Continuous relationship / trend |
| `plt.scatter()` | Individual measurements / experimental data |

For example:

Experimental wind-tunnel measurements:

```text
scatter plot
```

Theoretical drag curve:

```text
line plot
```

You can also plot both together.

---

## 15. Bar Charts

Bar charts are useful when comparing discrete quantities.

```python
aircraft = ["A", "B", "C"]
mass = [13500, 38800, 24500]

plt.bar(aircraft, mass)

plt.xlabel("Aircraft")
plt.ylabel("Mass (kg)")
plt.title("Aircraft Maximum Takeoff Mass")

plt.show()
```

Bar charts are useful for comparisons rather than continuous physical relationships.

---

## 16. Figure Size

You can control the size of the figure.

```python
plt.figure(figsize=(8, 5))
```

The numbers represent:

```text
(width, height)
```

in inches.

---

## 17. Saving a Figure

Instead of only displaying a graph, you can save it.

```python
plt.savefig("kinetic_energy_vs_velocity.png")
```

Example:

```python
plt.plot(velocity, kinetic_energy)

plt.title("Kinetic Energy vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")
plt.grid()

plt.savefig("kinetic_energy_vs_velocity.png")
plt.show()
```

This creates an image file that can be used in:

- Reports
- Research notes
- Presentations
- GitHub documentation

---

## 18. Plot Limits

You can control the visible range.

```python
plt.xlim(50, 250)
plt.ylim(0, 35000000)
```

Use this carefully.

Do not manipulate limits simply to make a graph look better.

> The graph should represent the data honestly.

---

## 19. A Complete Engineering Example

```python
import numpy as np
import matplotlib.pyplot as plt

mass = 1000

velocity = np.array([50, 100, 150, 200, 250])

kinetic_energy = 0.5 * mass * velocity**2

plt.figure(figsize=(8, 5))

plt.plot(
    velocity,
    kinetic_energy,
    marker="o",
    label="Kinetic Energy"
)

plt.title("Kinetic Energy vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

plt.grid()
plt.legend()

plt.savefig("kinetic_energy_vs_velocity.png")

plt.show()
```

This is now a complete small engineering visualisation.

---

## 20. The NumPy → Matplotlib Workflow

You are now building an important engineering workflow.

```text
INPUT DATA
    ↓
NumPy array
    ↓
Engineering equation
    ↓
Calculated dataset
    ↓
Matplotlib
    ↓
Engineering graph
```

For example:

```text
Velocity
   ↓
NumPy array
   ↓
KE = ½mV²
   ↓
Kinetic energy array
   ↓
Plot
   ↓
KE vs Velocity graph
```

This workflow will appear repeatedly in engineering simulations.

---

## 21. Basic Plotting Structure

A clean basic plotting program usually follows this structure:

```python
import numpy as np
import matplotlib.pyplot as plt

## 1. Input / data
x = np.array([...])

## 2. Engineering calculation
y = ...

## 3. Create plot
plt.plot(x, y)

## 4. Labels
plt.title("...")
plt.xlabel("...")
plt.ylabel("...")

## 5. Improve readability
plt.grid()
plt.legend()

## 6. Display
plt.show()
```

Don't overcomplicate this structure at the beginning.

---

## 22. Common Mistakes

### Mistake 1 — Forgetting `plt.show()`

Without:

```python
plt.show()
```

the figure may not display in a normal Python script.

### Mistake 2 — Missing units

Bad:

```python
plt.xlabel("Velocity")
```

Better:

```python
plt.xlabel("Velocity (m/s)")
```

### Mistake 3 — X and Y have different lengths

For example:

```python
x = [1, 2, 3]
y = [10, 20]
```

This cannot produce a normal corresponding x-y plot.

### Mistake 4 — Using a line plot for everything

Experimental measurements may be better represented using:

```python
plt.scatter()
```

rather than automatically connecting every point.

### Mistake 5 — Making graphs unnecessarily complicated

Your first goal is:

```text
Correct data
+
Correct calculation
+
Clear labels
+
Readable graph
```

Fancy styling comes later.

---

## 23. Practical Task

Create:

```text
python/codes/matplotlib/
└── day11_matplotlib_fundamentals.py
```

Build an **Aerospace Engineering Performance Plotter**.

Your program should calculate and plot at least two engineering relationships.

## Plot 1 — Kinetic Energy vs Velocity

Use:

$$KE = \frac{1}{2}mV^2$$

Choose an aircraft mass, for example:

```python
mass = 1000
```

and create a NumPy velocity array.

Plot:

```text
X-axis → Velocity (m/s)
Y-axis → Kinetic Energy (J)
```

## Plot 2 — Dynamic Pressure vs Velocity

Use:

$$q = \frac{1}{2}\rho V^2$$

Use a reasonable air density such as:

```python
rho = 1.225
```

Plot:

```text
X-axis → Velocity (m/s)
Y-axis → Dynamic Pressure (Pa)
```

---

## 24. Challenge

Add a third plot:

## Momentum vs Velocity

$$p = mV$$

Plot:

```text
X-axis → Velocity (m/s)
Y-axis → Momentum (kg·m/s)
```

---

## 25. Bonus Challenge

Create a comparison plot.

For example, calculate kinetic energy for:

```text
Mass 1 = 1000 kg
Mass 2 = 1500 kg
Mass 3 = 2000 kg
```

Plot all three curves on the same graph.

Use:

```python
plt.legend()
```

to identify them.

This will combine:

- NumPy arrays
- Vectorised calculations
- Matplotlib
- Multiple datasets
- Legends

---

## 26. Deliverable

Your final file should be:

```text
python/
└── codes/
    └── matplotlib/
        └── day11_matplotlib_fundamentals.py
```

Your program should demonstrate:

- [ ] NumPy data  
- [ ] Engineering calculations  
- [ ] `plt.plot()`  
- [ ] `plt.scatter()`  
- [ ] Title  
- [ ] X-axis label  
- [ ] Y-axis label  
- [ ] Units  
- [ ] Grid  
- [ ] Legend  
- [ ] Figure size  
- [ ] Saving a plot  
- [ ] Displaying a plot  

You do **not** need to use every feature in the main program. The important thing is to understand what each feature does.

---

## 27. Engineering Mindset

Up to Day 10:

```text
Python
  ↓
Numerical calculations
  ↓
NumPy
  ↓
Vectors
  ↓
Matrices
```

Today:

```text
Numerical data
      ↓
Engineering calculation
      ↓
Visualisation
```

This is an important transition.

> Engineers don't just calculate numbers. They interpret what those numbers mean.

---

## 28. Quick Reference

| Task | Matplotlib |
|---|---|
| Line plot | `plt.plot(x, y)` |
| Scatter plot | `plt.scatter(x, y)` |
| Bar chart | `plt.bar(x, y)` |
| Title | `plt.title()` |
| X-axis label | `plt.xlabel()` |
| Y-axis label | `plt.ylabel()` |
| Grid | `plt.grid()` |
| Legend | `plt.legend()` |
| Figure size | `plt.figure(figsize=(8, 5))` |
| Save figure | `plt.savefig("name.png")` |
| Display | `plt.show()` |
| X limits | `plt.xlim()` |
| Y limits | `plt.ylim()` |

---

## Completion Checklist

## Concepts

- [ ] I understand why Matplotlib is used  
- [ ] I can create a basic line plot  
- [ ] I can create a scatter plot  
- [ ] I can label axes  
- [ ] I can add a title  
- [ ] I can add a grid  
- [ ] I understand legends  
- [ ] I can plot multiple datasets  
- [ ] I can save a figure  

## Engineering

- [ ] I can use NumPy data as Matplotlib input  
- [ ] I can plot an engineering equation  
- [ ] I include units on physical axes  
- [ ] I can distinguish measured data from a calculated curve  

## Practical

- [ ] `day11_matplotlib_fundamentals.py` completed  
- [ ] Kinetic energy plot completed  
- [ ] Dynamic pressure plot completed  
- [ ] Momentum plot attempted  
- [ ] At least one figure saved as an image  
- [ ] Code committed and pushed to GitHub

---

## Where Takes You Next

```text
Day 8
NumPy arrays
      ↓
Day 9
Vectors + broadcasting
      ↓
Day 10
Matrices + dot products
      ↓
Day 11
Matplotlib visualisation
      ↓
Numerical mathematics
      ↓
ODEs
      ↓
Integration
      ↓
Rotation matrices
      ↓
Quaternions
      ↓
6-DOF simulation
```

The eventual goal is not simply:

> "I know NumPy and Matplotlib."

The goal is:

> "I can take an aerospace engineering problem, represent it mathematically, compute it numerically, and visualise the result."

That is the computational engineering skill we are building.
