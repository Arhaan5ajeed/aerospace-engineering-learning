# Determination of Pipe Friction Major Loss

> **Objective:** To experimentally determine the major head loss due to friction in a pipe and calculate the corresponding Fanning and Darcy friction factors at different flow rates.

---

## 1. Introduction

When a fluid flows through a pipe, its mechanical energy decreases because of friction between the moving fluid and the internal pipe surface. This energy loss is known as **major head loss due to pipe friction**.

Major losses occur along the length of a pipe. They differ from minor losses, which are associated with local disturbances such as bends, elbows, valves, sudden expansions and contractions.

The experiment measures the pressure difference between two points along a straight pipe using a manometer. The discharge is obtained by measuring the time required for water to produce a known rise in a collecting tank. These measurements are used to calculate the head loss, mean flow velocity and friction factor.

The program generalises the laboratory experiment so that users can enter their own pipe diameter, pressure-tap spacing, collecting tank dimensions, manometer readings and experimental observations rather than being restricted to one apparatus.

## 2. Objectives

- Calculate the actual volumetric discharge of water through a pipe.
- Determine the mean velocity of flow.
- Calculate the differential manometer head.
- Determine the major head loss due to pipe friction.
- Calculate the Fanning friction factor used in the laboratory manual.
- Calculate the corresponding Darcy–Weisbach friction factor.
- Investigate the relationship between discharge and major head loss.
- Plot discharge against head loss for experimental analysis.

## 3. Theory

### 3.1 Discharge

The volumetric discharge is the volume of fluid passing through a section per unit time.

The collecting tank method gives:

$$
Q=\frac{A_t\,\Delta y}{t}
$$

Where:

- $Q$ = volumetric discharge (m³/s)
- $A_t$ = collecting tank area (m²)
- $\Delta y$ = rise in water level in the collecting tank (m)
- $t$ = time taken for the specified rise (s)

For a rectangular tank:

$$
A_t=\text{tank length}\times\text{tank breadth}
$$

The program accepts the tank area directly, allowing different collecting tanks to be used.

### 3.2 Pipe cross-sectional area

For a circular pipe:

$$
A_p=\frac{\pi D^2}{4}
$$

Where $D$ is the internal pipe diameter in metres.

The diameter must be converted from millimetres to metres before calculating the area.

### 3.3 Mean velocity

Using the continuity equation:

$$
Q=A_pV
$$

Therefore:

$$
V=\frac{Q}{A_p}
$$

Where $V$ is the mean flow velocity in m/s.

### 3.4 Differential manometer head

The difference between the two manometer readings is:

$$
h_m=|h_1-h_2|
$$

The readings are entered in centimetres and converted into metres.

For a differential manometer containing a liquid denser than the flowing fluid, the equivalent head loss in the flowing fluid is:

$$
h_f=h_m\left(\frac{S_m}{S_f}-1\right)
$$

Where:

- $h_f$ = major head loss over the pressure-tap spacing (m)
- $h_m$ = difference between manometer readings (m)
- $S_m$ = relative density of the manometric liquid
- $S_f$ = relative density of the flowing fluid

For a mercury–water manometer:

$$
S_m=13.6,\qquad S_f=1.0
$$

Thus:

$$
h_f=12.6h_m
$$

This simplified relationship applies to the specified arrangement with a denser manometric liquid and water-like flowing fluid. The program uses the relative-density ratio rather than hardcoding the mercury–water conversion.

### 3.5 Darcy–Weisbach equation

The major head loss in a straight, constant-diameter pipe is represented by the Darcy–Weisbach equation:

$$
h_f=f_D\frac{L}{D}\frac{V^2}{2g}
$$

Rearranging:

$$
f_D=\frac{2gh_fD}{LV^2}
$$

Where:

- $f_D$ = Darcy friction factor (dimensionless)
- $L$ = distance between pressure taps (m)
- $D$ = internal pipe diameter (m)
- $V$ = mean velocity (m/s)
- $g$ = gravitational acceleration (m/s²)

The program uses $g=9.81\text{ m/s}^2$.

### 3.6 Fanning friction factor

The laboratory manual expresses the equation as:

$$
h_f=4f_F\frac{L}{D}\frac{V^2}{2g}
$$

Rearranging:

$$
f_F=\frac{gh_fD}{2LV^2}
$$

Where $f_F$ is the Fanning friction factor.

The relationship between the two conventions is:

$$
\boxed{f_D=4f_F}
$$

The code reports both values to avoid confusing the friction factor used in the manual with the Darcy friction factor commonly used in engineering calculations.

## 4. Experimental Procedure

1. Start the pump and select the pipe to be tested.
2. Open the appropriate inlet and outlet valves connected to the pressure taps.
3. Adjust the delivery valve to obtain a steady flow rate.
4. Record the two manometer readings, $h_1$ and $h_2$.
5. Measure the time required for the collecting tank water level to rise by the selected height.
6. Repeat the measurements at different flow rates by adjusting the delivery valve.
7. Enter the apparatus dimensions and experimental readings into the program.
8. Calculate discharge, velocity, manometer head, major head loss and friction factors.
9. Examine the calculated results and the discharge-versus-head-loss graph.

Follow the laboratory's operating and safety instructions when using the actual equipment.

## 5. Program Overview

The Python program automates the calculations associated with the experiment.

### User inputs

| Input | Unit | Purpose |
|---|---|---|
| Collecting tank area | m² | Determines the collected water volume |
| Tank water-level rise | cm | Specifies the volume collected |
| Pipe internal diameter | mm | Calculates the pipe flow area |
| Distance between pressure taps | m | Defines the pipe length over which head loss is measured |
| Manometric relative density | Dimensionless | Converts the manometer difference into equivalent flowing-fluid head |
| Flowing-fluid relative density | Dimensionless | Used in the manometer-head calculation |
| Number of trials | Count | Determines the number of experimental observations |
| Manometer readings $h_1,h_2$ | cm | Determines the differential head |
| Collection time | s | Determines the actual discharge |

The program uses $g=9.81\text{ m/s}^2$ and assumes a circular pipe flowing full.

### Calculated outputs

- Differential manometer head, $h_m$ (cm and converted to m)
- Major head loss, $h_f$ (m)
- Actual discharge, $Q$ (m³/s)
- Mean velocity, $V$ (m/s)
- Fanning friction factor, $f_F$
- Darcy friction factor, $f_D$
- Mean values for the experimental trials
- A graph of discharge versus major head loss

## 6. Graphical Analysis

The program plots:

- **X-axis:** Discharge, $Q$ (m³/s)
- **Y-axis:** Major head loss, $h_f$ (m)

The graph is saved as:

`pipe_friction_major_loss_graph.png`

For a fixed pipe and fixed pressure-tap spacing, head loss generally increases as flow rate and mean velocity increase. Under many turbulent-flow conditions, head loss varies approximately with the square of velocity if the friction factor changes relatively little. The exact relationship depends on the flow regime and friction factor.

The graph should be interpreted using the actual experimental data rather than assuming a perfectly linear relationship.

## 7. Python Concepts Used

The project applies the following Python concepts:

- Variables and numerical data types
- User input and output
- Functions for reusable input validation
- Conditional statements and exception handling
- `for` loops for repeated experimental trials
- Lists for storing experimental observations
- NumPy arrays for numerical calculations
- Mathematical operations and unit conversions
- `numpy.pi` and `numpy.abs`
- NumPy sorting and mean calculations
- Matplotlib for scientific plotting
- File output through saving the graph as a PNG image

## 8. Assumptions

The calculations are based on the following assumptions:

1. The fluid is incompressible.
2. The flow is steady during each measurement.
3. The pipe is circular and flows full.
4. The pipe diameter is constant between the pressure taps.
5. The discharge measured using the collecting tank represents the discharge through the test pipe.
6. The manometer readings correspond to the two pressure taps across the tested pipe length.
7. The measured differential head represents the major head loss over the selected section.
8. The manometric liquid is denser than the flowing fluid.
9. The pipe's internal diameter and pressure-tap spacing are measured accurately.
10. The experiment is conducted under conditions where the measured pressure difference can be attributed primarily to friction along the test section.

The last assumption is important: pressure taps near valves, bends, entrances or other disturbances may include local losses in addition to straight-pipe friction.

## 9. Accuracy and Limitations

The calculated results depend on the quality of the experimental measurements.

### Possible sources of error

- Human reaction time when operating the stopwatch
- Parallax error while reading the manometer
- Fluctuations in pump delivery or flow rate
- Incorrect measurement of pipe diameter or pressure-tap spacing
- Air bubbles in manometer tubes
- Leakage from the apparatus
- Uncertainty in collecting tank area and water-level rise
- Local losses affecting the measured pressure difference
- Changes in fluid temperature and viscosity

### Limitations of the current program

- It assumes a circular pipe of constant diameter.
- It assumes the same pipe diameter and pressure-tap spacing for all trials in one run.
- It assumes a manometer with a denser liquid than the flowing fluid.
- It does not automatically correct for local losses or measurement uncertainty.
- It does not calculate Reynolds number because fluid viscosity and density are not requested as inputs.
- It does not independently predict a theoretical friction factor from pipe roughness.

The calculated friction factors are experimental estimates and should not be treated as exact material constants.

## 10. Future Scope of Improvement

The program could be extended to include:

- Multiple pipe diameters in a single dataset
- Automatic calculation of Reynolds number
- Fluid density, dynamic viscosity and kinematic viscosity inputs
- Pipe roughness and relative roughness calculations
- Theoretical Darcy friction-factor estimates using suitable correlations
- A comparison between experimental and theoretical friction factors
- Uncertainty propagation for discharge and head loss
- Exporting results to CSV or Excel
- Separate graphs for head loss versus velocity and head loss versus discharge
- Comparison of multiple pipe materials or pipe diameters
- A graphical user interface for laboratory use

## 11. Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required libraries if they are not already available:

```bash
pip install numpy matplotlib
```

## 12. How to Run

1. Save the program as `pipe_friction_major_loss.py`.
2. Open the project folder in VS Code.
3. Ensure Python, NumPy and Matplotlib are installed.
4. Run the script.
5. Enter the apparatus details when prompted.
6. Enter the manometer readings and collection time for each trial.
7. Review the printed results and the generated graph.

The graph is saved in the working directory from which the program is run.

## 13. Conclusion

This project provides a reusable Python tool for determining major head loss due to pipe friction from laboratory measurements. It calculates actual discharge, mean flow velocity, differential manometer head and the corresponding friction factors.

By reporting both the Fanning and Darcy friction factors, the program remains compatible with the AFDL laboratory manual while making the results easier to interpret using standard fluid-mechanics conventions. Its configurable dimensions and experimental inputs make it suitable for repeated trials and different compatible pipe-friction apparatus.

The program is intended as a learning and laboratory-analysis tool. Its accuracy depends on valid measurements and on the assumptions used to interpret the experimental pressure difference.
