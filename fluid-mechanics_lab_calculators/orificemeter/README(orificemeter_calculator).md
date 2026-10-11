# Orificemeter Discharge Calculator

> **Objective:** To calculate the theoretical discharge, actual discharge, and coefficient of discharge of an orificemeter using experimental manometer readings and collecting-tank measurements, and to visualise the relationship between theoretical and actual discharge using Python.

---

## 1. Introduction

An **orificemeter** is a differential-pressure flow-measuring device used to determine the discharge rate of a fluid flowing through a pipe. It consists of a thin plate containing a circular opening, known as an *orifice*, installed inside the pipe.

As the fluid passes through the smaller opening, its velocity increases and its static pressure decreases. The pressure difference between the upstream section and the orifice section can be used to estimate the flow rate.

Orificemeters are widely used in fluid mechanics laboratories and industrial flow-measurement systems because of their simple construction, relatively low initial cost, and ease of installation.

This project implements the fundamental orificemeter discharge equations in Python and uses NumPy and Matplotlib to perform calculations and visualise experimental results.

---

## 2. Working Principle

The orificemeter operates primarily on the principles of **Bernoulli's equation and the continuity equation**.

### 2.1 Continuity Equation

For steady, incompressible flow, conservation of mass requires:

$$
A_1V_1=A_oV_o
$$

Where:

- $A_1$ = cross-sectional area of the pipe
- $A_o$ = area of the orifice
- $V_1$ = average velocity in the upstream pipe
- $V_o$ = ideal velocity through the orifice section

Because the orifice area is smaller than the pipe area, the fluid accelerates as it passes through the restriction.

### 2.2 Bernoulli's Equation

For an idealised horizontal flow, Bernoulli's equation between the upstream pipe section and the orifice section is:

$$
\frac{p_1}{\rho g}+\frac{V_1^2}{2g} = \frac{p_o}{\rho g}+\frac{V_o^2}{2g}
$$

Rearranging:

$$
\frac{p_1-p_o}{\rho g} = \frac{V_o^2-V_1^2}{2g}
$$

The pressure difference is related to the differential head measured using a manometer.

Combining Bernoulli's equation with continuity gives the theoretical discharge:

$$
\boxed{Q_t=A_o\sqrt{\frac{2gH}{1-(A_o/A_1)^2}}}
$$

Where:

- $Q_t$ = theoretical discharge in $\text{m}^3/\text{s}$
- $A_o$ = orifice area in $\text{m}^2$
- $A_1$ = upstream pipe area in $\text{m}^2$
- $g$ = gravitational acceleration, $9.81\text{ m/s}^2$
- $H$ = differential pressure head expressed in metres of the flowing fluid

This equation assumes idealised flow and neglects energy losses.

---

## 3. Differential Manometer Head

A differential manometer measures the pressure difference between two points in the flow system. For a conventional differential U-tube manometer containing a heavier manometric fluid:

$$
h_m=|h_1-h_2|
$$

Where:

- $h_1$ = first manometer reading in cm
- $h_2$ = second manometer reading in cm
- $h_m$ = differential reading in cm

Convert the differential reading to metres:

$$
h_m(\text{m})=\frac{|h_1-h_2|}{100}
$$

When both pressure connections contain the same flowing fluid, and the heavier manometric liquid is immiscible with it, the equivalent pressure head in metres of the flowing fluid is:

$$
\boxed{H=h_m\left(\frac{\rho_m}{\rho_f}-1\right)}
$$

Where:

- $\rho_m$ = density of the manometric fluid
- $\rho_f$ = density of the flowing fluid

Both densities must use the same units.

The program accepts **relative densities** instead of absolute densities. Relative density is the ratio of a fluid's density to the density of water, so the equivalent expression is:

$$
H=h_m\left(\frac{RD_m}{RD_f}-1\right)
$$

Examples:

| Fluid | Approximate relative density |
|---|---:|
| Water | 1.00 |
| Mercury | 13.6 |
| Oil | 0.85 |

For a mercury manometer measuring water flow:

$$
H=h_m(13.6-1)=12.6h_m
$$

For a mercury manometer measuring oil flow, using oil relative density $0.85$:

$$
H=h_m\left(\frac{13.6}{0.85}-1\right)
$$

The appropriate flowing-fluid density must therefore be used rather than assuming that the fluid is always water.

**Important:** This expression applies to the specified conventional arrangement. Other manometer configurations, lighter manometric fluids, or different pressure-tap elevations may require a modified hydrostatic pressure relation.

---

## 4. Actual Discharge

The actual discharge is determined experimentally using a collecting tank.

If the tank's cross-sectional area is known and the time required for the liquid level to rise by a measured height is recorded, the actual discharge is:

$$
Q_a=\frac{\text{Volume collected}}{\text{Time taken}}
$$

For a constant-area tank:

$$
\text{Volume collected}=A_t\Delta y
$$

Therefore:

$$
\boxed{Q_a=\frac{A_t\Delta y}{t}}
$$

Where:

- $Q_a$ = actual discharge in $\text{m}^3/\text{s}$
- $A_t$ = collecting-tank cross-sectional area in $\text{m}^2$
- $\Delta y$ = vertical rise of liquid in the tank in metres
- $t$ = time taken in seconds

In this program, the tank rise is fixed at 10 cm:

$$
\Delta y=0.10\text{ m}
$$

Hence:

$$
\boxed{Q_a=\frac{A_t(0.10)}{t}}
$$

The tank area must be its horizontal cross-sectional area, not the area of its walls or wetted surface.

---

## 5. Coefficient of Discharge

The coefficient of discharge compares the measured actual discharge with the ideal theoretical discharge:

$$
\boxed{C_d=\frac{Q_a}{Q_t}}
$$

Where:

- $C_d$ = coefficient of discharge
- $Q_a$ = actual discharge
- $Q_t$ = theoretical discharge

The coefficient accounts empirically for the difference between idealised theoretical flow and real flow through the orificemeter.

Real flow involves energy losses, viscous effects, flow contraction, and other non-ideal phenomena. Consequently, the actual discharge is generally lower than the ideal theoretical prediction for a correctly conducted experiment.

The coefficient of discharge is dimensionless.

A result substantially greater than 1 should prompt checks of the units, experimental readings, pressure-head calculation, collecting-tank measurements, and applicability of the theoretical model.

---

## 6. Orificemeter vs Venturimeter

| Feature | Orificemeter | Venturimeter |
|---|---|---|
| Construction | Thin plate with an opening | Converging section, throat and diverging section |
| Initial cost | Generally lower | Generally higher |
| Installation | Relatively simple | Requires more installation space |
| Permanent pressure loss | Generally higher | Generally lower |
| Flow contraction | Significant; a vena contracta forms downstream | More gradual flow acceleration and recovery |
| Maintenance | Plate inspection and possible replacement | More complex construction |
| Typical use | Economical flow measurement | Applications prioritising pressure recovery |

Both devices infer discharge from a pressure difference. Their geometry and associated flow losses differ, so their discharge coefficients are not interchangeable.

---

## 7. Project Overview

The program accepts geometric measurements, fluid properties, manometer readings, and collection times. It then calculates the theoretical and actual discharge, evaluates the coefficient of discharge, displays a summary of all trials, and generates a graph.

### Input parameters

| Parameter | Description | Unit |
|---|---|---|
| $d_1$ | Internal diameter of the pipe | mm |
| $d_o$ | Diameter of the orifice | mm |
| $A_t$ | Collecting-tank cross-sectional area | m² |
| $RD_m$ | Relative density of the manometric fluid | Dimensionless |
| $RD_f$ | Relative density of the flowing fluid | Dimensionless |
| $h_1,h_2$ | Manometer readings | cm |
| $t$ | Time for a 10 cm tank rise | s |

The user also specifies the number of experimental trials.

### Output parameters

| Output | Description | Unit |
|---|---|---|
| $h_m$ | Absolute difference between manometer readings | cm |
| $H$ | Equivalent differential head of the flowing fluid | m |
| $Q_a$ | Actual discharge | m³/s |
| $Q_t$ | Theoretical discharge | m³/s |
| $C_d$ | Coefficient of discharge | Dimensionless |

---

## 8. Python Concepts Used

### 8.1 Variables and data types

Variables store the input readings, dimensions, fluid properties, calculated areas, and discharge values.

The `float()` function converts numerical inputs into floating-point values so that calculations can use decimal numbers.

### 8.2 User input

The `input()` function allows the user to provide measurements at runtime. This makes the program reusable for different orificemeter configurations and experimental trials.

### 8.3 Conditional statements

`if` statements check whether diameters, tank area, densities, trial count, and collection time satisfy basic validity requirements.

### 8.4 Loops

A `for` loop processes multiple experimental trials without requiring the calculation code to be duplicated.

### 8.5 Lists

Lists store the calculated heads, discharges, and coefficients so that the program can display a summary and plot all experimental results.

### 8.6 NumPy

NumPy provides:

- `np.pi` for the value of $\pi$
- `np.sqrt()` for square-root calculations
- Numerical operations for the theoretical discharge equation

### 8.7 Matplotlib

Matplotlib creates the graph of theoretical discharge against actual discharge and saves it as a high-resolution PNG image.

---

## 9. Graphical Representation

The program plots:

- **X-axis:** Actual discharge, $Q_a$, in $\text{m}^3/\text{s}$
- **Y-axis:** Theoretical discharge, $Q_t$, in $\text{m}^3/\text{s}$

Each experimental trial appears as a separate point.

The graph helps visualise the relationship between actual and theoretical flow rates across the tested operating conditions.

Because the axes are deliberately assigned as requested, this is not the conventional plot used to estimate $C_d$ as the slope of a straight line. Since $Q_a=C_dQ_t$, a plot of $Q_t$ against $Q_a$ has slope $1/C_d$ only when a suitable proportional relationship holds and the fit is constrained appropriately. For estimating $C_d$ directly from the slope, plotting $Q_a$ on the y-axis against $Q_t$ on the x-axis is more convenient.

---

## 10. Accuracy and Precision

The program performs calculations using standard theoretical relations and the input values supplied by the user. Its numerical results are only as reliable as the measurements, assumptions, and model used.

### Sources of experimental uncertainty

- Errors when reading the manometer levels
- Parallax and meniscus-reading errors
- Stopwatch reaction time
- Uncertainty in the collecting-tank area
- Uncertainty in pipe and orifice diameters
- Changes in flow conditions during a trial
- Incorrect fluid-density assumptions
- Leakage, air bubbles, or improper pressure-tap connections

### Numerical precision vs experimental accuracy

**Numerical precision** concerns how consistently and finely the program represents its calculated values.

**Experimental accuracy** concerns how close the calculated result is to the actual physical quantity.

Printing additional decimal places does not improve experimental accuracy. The displayed digits should not be interpreted as a guarantee of measurement precision.

The current program does not calculate uncertainty bounds or compare results against a calibrated reference instrument.

---

## 11. Advantages

- Automates repetitive discharge calculations.
- Reduces manual arithmetic errors.
- Supports multiple experimental trials.
- Accepts different flowing fluids and manometric liquids through relative-density inputs.
- Displays actual and theoretical discharge alongside the coefficient of discharge.
- Produces a graph for experimental analysis.
- Saves the plot at 300 dpi for reports and laboratory records.
- Provides a foundation for future computational fluid mechanics tools.

---

## 12. Limitations

- Assumes steady, incompressible flow.
- Uses a simplified theoretical equation that neglects energy losses.
- Does not calculate the discharge coefficient from a calibrated correlation.
- Assumes the collecting tank has a constant cross-sectional area.
- Assumes the tank rises by exactly 10 cm in each trial.
- Assumes the specified differential-manometer configuration and a denser manometric liquid.
- Does not automatically identify outliers or estimate measurement uncertainty.
- Does not account explicitly for pipe roughness, Reynolds number, or installation effects.
- Does not validate the calculated coefficient against a prescribed reference range.

The program is intended as an educational calculation tool, not a substitute for instrument calibration or applicable engineering standards.

---

## 13. Challenges in Development

The main implementation challenges include:

1. **Unit conversion:** Converting diameters from millimetres to metres and manometer readings from centimetres to metres before applying the equations.
2. **Fluid-density handling:** Distinguishing the manometric fluid from the flowing fluid and using the correct relative-density ratio.
3. **Theoretical modelling:** Applying the appropriate area ratio in the discharge equation.
4. **Experimental data management:** Storing multiple trials in a consistent format.
5. **Input validation:** Preventing invalid geometry, non-positive collection times, and unsupported density combinations.
6. **Graph construction:** Assigning the requested quantities to the correct axes and ensuring the plot is saved before display.

These challenges reinforce the connection between programming, mathematical modelling, and experimental fluid mechanics.

---

## 14. Future Scope of Improvement

The program can be developed further by adding:

- **Automatic coefficient analysis:** Calculate the mean, standard deviation, and variation of $C_d$ across trials.
- **Uncertainty analysis:** Propagate measurement uncertainties in the diameters, tank area, manometer readings, and collection time.
- **Data export:** Export trial results to CSV or Excel.
- **Experimental data import:** Read measurements from a file instead of entering each value manually.
- **Improved plotting:** Add a fitted trendline, equation, $R^2$, and an optional reference line.
- **Calibration:** Incorporate an experimentally determined discharge coefficient or an appropriate standard correlation.
- **Advanced flow modelling:** Consider Reynolds number, orifice geometry, pressure-tap arrangement, pipe roughness, and installation effects.
- **Graphical user interface:** Build an interface for entering measurements and viewing results without using a terminal.
- **Automated reporting:** Generate a laboratory report containing inputs, calculations, tables, plots, and conclusions.

Any advanced correlation should be selected for the actual orifice geometry and operating conditions rather than assumed to apply universally.

---

## 15. Conclusion

This project demonstrates how Python can be applied to a practical fluid mechanics experiment. By combining fundamental fluid-flow equations with input validation, numerical computation, data storage, and graphical visualisation, the program automates the analysis of an orificemeter.

It calculates actual discharge from collecting-tank measurements, theoretical discharge from differential pressure head, and the coefficient of discharge from their ratio. It also provides a basis for comparing multiple trials and studying the difference between idealised theory and real experimental flow.

The project serves as a foundation for further work in engineering computation, experimental data analysis, and computational fluid mechanics.

---

## 16. Requirements and Execution

### Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required libraries using:

```bash
pip install numpy matplotlib
```

### Run the program

```bash
python orificemeter_calculator.py
```

Follow the prompts to enter the pipe and orifice dimensions, collecting-tank area, fluid relative densities, and experimental readings.

After the calculations, the program displays the trial summary and generates:

`orificemeter_discharge_graph.png`

---

## 17. Project Structure

```text
simple-engineering-calculations/
├── orificemeter_calculator.py
└── README.md
```

---

*This project is part of an engineering programming portfolio focused on applying mathematical and physical principles to practical aerospace and mechanical engineering problems.*
