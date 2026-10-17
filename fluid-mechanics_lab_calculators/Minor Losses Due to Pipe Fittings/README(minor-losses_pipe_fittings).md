# Determination of Minor Losses Due to Pipe Fittings

> **Objective:** To determine the minor head loss associated with pipe fittings and calculate their loss coefficients using experimental manometer readings and discharge measurements.

---

## 1. Introduction

When a fluid flows through a piping system, its mechanical energy decreases because of friction and disturbances in the flow. Losses caused by local disturbances such as elbows, bends, sudden expansions and sudden contractions are called **minor losses**.

Despite their name, minor losses can be significant in systems containing many fittings or operating at high flow rates.

This experiment uses a manometer connected across a pipe fitting to measure the pressure difference. The actual discharge is determined using a collecting tank and stopwatch. The measured head loss is then compared with the theoretical velocity-head expression for the selected fitting.

This Python program generalises the AFDL laboratory experiment. It allows users to enter their own apparatus dimensions, fluid properties, fitting types, manometer readings and collection times.

## 2. Objectives

- Calculate the actual volumetric discharge.
- Determine the upstream and downstream flow velocities.
- Calculate the differential manometer head.
- Determine the actual head loss across a fitting.
- Calculate the theoretical or reference velocity head loss.
- Calculate the conventional loss coefficient.
- Compare the behaviour of elbows, bends, sudden enlargements and sudden contractions.
- Plot discharge against measured minor head loss.

## 3. Theory

### 3.1 Actual discharge

The volumetric discharge is calculated using the collecting tank method:

$$
Q=\frac{A_t\Delta y}{t}
$$

Where:

- $Q$ = volumetric discharge (m³/s)
- $A_t$ = collecting tank area (m²)
- $\Delta y$ = water-level rise in the tank (m)
- $t$ = collection time (s)

The tank water-level rise is entered in centimetres and converted into metres by the program.

### 3.2 Pipe cross-sectional area

For a circular pipe:

$$
A=\frac{\pi D^2}{4}
$$

Where $D$ is the internal pipe diameter in metres.

### 3.3 Flow velocity

The continuity equation is:

$$
Q=AV
$$

Therefore:

$$
V=\frac{Q}{A}
$$

For fittings with different upstream and downstream pipe diameters:

$$
V_1=\frac{Q}{A_1},\qquad V_2=\frac{Q}{A_2}
$$

Where:

- $V_1$ = upstream mean velocity (m/s)
- $V_2$ = downstream mean velocity (m/s)
- $A_1,A_2$ = upstream and downstream cross-sectional areas (m²)

### 3.4 Actual head loss from the manometer

The difference between the two manometer readings is:

$$
h_m=|h_1-h_2|
$$

For a differential manometer containing a liquid denser than the flowing fluid:

$$
h_f=h_m\left(\frac{S_m}{S_f}-1\right)
$$

Where:

- $h_f$ = measured head loss in the flowing fluid (m)
- $h_m$ = differential manometer reading converted to metres
- $S_m$ = relative density of the manometric liquid
- $S_f$ = relative density of the flowing fluid

For mercury and water:

$$
S_m=13.6,\qquad S_f=1.0
$$

Therefore:

$$
h_f=12.6h_m
$$

The program allows the user to change the relative densities instead of restricting the calculation to mercury and water.

This conversion assumes the conventional differential-manometer arrangement with a denser manometric liquid and the appropriate pressure-tap configuration.

### 3.5 Theoretical head loss expressions

The program uses the expressions specified in the laboratory manual.

#### Elbow and bend

$$
h_v=\frac{V^2}{2g}
$$

Here, $V$ is the mean velocity in the constant-diameter pipe.

#### Sudden enlargement

$$
h_v=\frac{(V_1-V_2)^2}{2g}
$$

Here, $V_1$ is the upstream velocity in the smaller pipe and $V_2$ is the downstream velocity in the larger pipe.

#### Sudden contraction

$$
h_v=0.5\frac{V_2^2}{2g}
$$

Here, $V_2$ is the velocity in the smaller downstream pipe, following the convention in the manual.

In these expressions, $g=9.81\text{ m/s}^2$.

The theoretical expressions are simplified laboratory relationships. Actual losses depend on fitting geometry, Reynolds number, surface conditions and other flow characteristics.

### 3.6 Loss coefficient

A conventional local loss coefficient is defined as:

$$
K=\frac{h_f}{V_{\mathrm{ref}}^2/(2g)}
$$

Where $V_{\mathrm{ref}}$ is the velocity in the pipe section used as the reference for that fitting.

The program uses:

- Elbow and bend: velocity in the constant-diameter pipe
- Sudden enlargement: upstream velocity in the smaller pipe
- Sudden contraction: downstream velocity in the smaller pipe

The manual also prints a ratio of theoretical head loss to actual head loss:

$$
\frac{h_v}{h_f}
$$

This ratio is displayed separately for comparison, but it is not the conventional definition of the local loss coefficient. The code therefore reports both quantities to make the distinction clear.

## 4. Experimental Procedure

1. Start the pump according to the laboratory instructions.
2. Adjust the delivery valve to establish a steady flow rate.
3. Select the fitting to be tested.
4. Connect the appropriate manometer pressure taps across that fitting.
5. Record the two manometer readings.
6. Measure the time taken for the collecting tank water level to rise by the specified height.
7. Repeat the measurements at other flow rates.
8. Repeat the experiment for the remaining fittings, selecting the correct pressure-tap connections each time.
9. Enter the measurements into the Python program.
10. Compare the calculated head losses and coefficients.

Ensure that the correct manometer connections are selected and that unrelated fitting connections are closed as required by the apparatus instructions.

## 5. Program Overview

### User inputs

| Input | Unit | Purpose |
|---|---|---|
| Collecting tank area | m² | Determines collected water volume |
| Tank water-level rise | cm | Determines the volume collected |
| Manometric relative density | Dimensionless | Converts manometer difference into head loss |
| Flowing-fluid relative density | Dimensionless | Used in the manometer-head calculation |
| Number of observations | Count | Specifies the number of measurements |
| Fitting type | Selection | Chooses elbow, bend, enlargement or contraction |
| Upstream diameter | mm | Calculates upstream pipe area |
| Downstream diameter | mm | Calculates downstream pipe area |
| Manometer readings $h_1,h_2$ | cm | Determines differential head |
| Collection time | s | Determines actual discharge |

For elbows and bends, both diameter inputs should be identical. For sudden enlargement, the downstream diameter must be larger than the upstream diameter. For sudden contraction, it must be smaller.

### Calculated outputs

- Differential manometer reading, $h_m$
- Actual head loss, $h_f$
- Actual discharge, $Q$
- Upstream velocity, $V_1$
- Downstream velocity, $V_2$
- Theoretical/reference head loss, $h_v$
- Conventional loss coefficient, $K$
- Manual's printed ratio, $h_v/h_f$
- Discharge-versus-head-loss graph

## 6. Graphical Analysis

The program plots:

- **X-axis:** Discharge, $Q$ (m³/s)
- **Y-axis:** Actual minor head loss, $h_f$ (m)

The graph is saved as:

`minor_losses_pipe_fittings_graph.png`

Separate plotted series are created for the fitting types represented in the entered observations.

For a given fitting and unchanged geometry, the measured head loss generally increases as the flow velocity increases. The exact relationship depends on the fitting geometry and flow conditions.

For a useful trend, record several observations for the same fitting at different flow rates. A single observation per fitting is enough to calculate a result but is not sufficient to establish a meaningful curve.

## 7. Python Concepts Used

- Variables and numerical data types
- User input and formatted output
- Functions for input validation and fitting selection
- Dictionaries for mapping menu choices to fitting types
- Conditional statements and loops
- Lists and dictionaries for storing experimental data
- NumPy for numerical calculations and sorting
- Circular-pipe area calculations
- Unit conversions
- Matplotlib for scientific plotting
- Saving a graph as a PNG image

## 8. Assumptions

1. The fluid is incompressible.
2. The flow is steady during each measurement.
3. The pipe is circular and flows full.
4. The measured tank discharge represents the discharge through the test section.
5. The manometer readings correspond to the selected fitting's pressure taps.
6. The manometric liquid is denser than the flowing fluid.
7. The entered pipe diameters are internal diameters.
8. The theoretical equations used are those specified by the laboratory manual.
9. The flow geometry and selected fitting are correctly identified.
10. The measured differential head represents the loss associated with the selected fitting.

The final assumption requires particular care: pressure taps placed too far from a fitting may include straight-pipe friction, while nearby disturbances may affect the measured pressure difference.

## 9. Accuracy and Limitations

### Possible sources of error

- Stopwatch reaction time
- Manometer-reading and parallax errors
- Unsteady pump delivery
- Incorrect pipe-diameter measurements
- Air bubbles in manometer tubes
- Leakage in the apparatus
- Incorrect pressure-tap selection
- Additional straight-pipe friction between the pressure taps
- Differences between actual fitting geometry and simplified theoretical expressions

### Limitations of the current program

- It supports the four fitting types covered in the manual: elbows, bends, sudden enlargement and sudden contraction.
- It assumes circular pipes.
- It requires both diameter inputs even for a constant-diameter fitting.
- It assumes a denser manometric liquid.
- It does not automatically separate straight-pipe friction from fitting losses.
- It does not calculate Reynolds number or account for fluid viscosity.
- The theoretical expressions are simplified and may not capture all real fitting behaviour.
- The conventional loss coefficient depends on the reference velocity selected for the fitting.

Consequently, the results are experimental estimates rather than exact universal values for each fitting type.

## 10. Future Scope of Improvement

Possible enhancements include:

- Adding entrance and exit losses
- Supporting other fitting types and geometries
- Allowing multiple fittings to be measured in one run
- Automatically calculating Reynolds number
- Adding fluid density and viscosity inputs
- Separating pipe-friction losses from fitting losses
- Comparing measured coefficients with reference engineering correlations
- Calculating uncertainty from repeated observations
- Exporting observations and results to CSV or Excel
- Generating separate plots for each fitting
- Building a graphical user interface for laboratory use

## 11. Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required libraries if necessary:

```bash
pip install numpy matplotlib
```

## 12. How to Run

1. Save the Python program as `minor_losses_pipe_fittings.py`.
2. Open the project folder in VS Code.
3. Confirm that Python, NumPy and Matplotlib are installed.
4. Run the program.
5. Enter the collecting tank area and water-level rise.
6. Enter the relative densities of the manometric and flowing fluids.
7. Enter the number of observations.
8. For each observation, select the fitting and enter the pipe diameters, manometer readings and collection time.
9. Review the calculated results and the generated graph.

The graph is saved in the working directory from which the program is run.

## 13. Conclusion

This project provides a configurable Python tool for analysing minor head losses in common pipe fittings. It calculates discharge, flow velocity, measured head loss and theoretical reference head loss, and it reports the conventional loss coefficient alongside the ratio printed in the laboratory manual.

The configurable inputs make the program useful for analysing different compatible pipe-fitting arrangements rather than being restricted to one fixed laboratory setup. Reliable results still depend on correct measurements, appropriate pressure-tap selection and an understanding of the assumptions behind the theoretical equations.
