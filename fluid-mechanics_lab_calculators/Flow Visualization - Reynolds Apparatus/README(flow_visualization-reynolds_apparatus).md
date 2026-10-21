# Experiment 7 — Flow Visualization Using Reynolds Apparatus

> **Objective:** To demonstrate flow visualization and determine whether the flow of water through a pipe is laminar, transitional, or turbulent using the Reynolds number.

---

## 1. Introduction

Fluid flow through a pipe can occur in different regimes depending on the fluid's velocity, density, viscosity, and the pipe diameter.

The Reynolds apparatus demonstrates these regimes by injecting a thin filament of dye into flowing water. The dye's behaviour provides a visual indication of the flow pattern.

- **Laminar flow:** The dye filament remains relatively straight and distinct, indicating orderly fluid motion.
- **Transitional flow:** The dye filament begins to oscillate and become unstable.
- **Turbulent flow:** The dye mixes rapidly with the surrounding water because of irregular fluctuations and mixing.

The Reynolds number is a dimensionless quantity used to characterize the flow regime.

## 2. Aim

To demonstrate flow visualization in a pipe and calculate the Reynolds number for different flow rates.

## 3. Apparatus Required

- Reynolds apparatus experimental setup
- Water supply and flow-control valve
- Dye injection system
- Measuring or collecting tank
- Stopwatch

## 4. Software Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries using:

```bash
pip install numpy matplotlib
```

## 5. Theory

### 5.1 Discharge

The volumetric discharge is the volume of fluid passing through a section per unit time.

$$
Q=\frac{\mathcal{V}}{t}
$$

Where:

- $Q$ = volumetric discharge (m³/s)
- $\mathcal{V}$ = collected volume (m³)
- $t$ = collection time (s)

The program uses a default collection volume of 1 litre.

$$
1\text{ litre}=10^{-3}\text{ m}^3
$$

### 5.2 Pipe Cross-Sectional Area

For a circular pipe:

$$
A=\frac{\pi D^2}{4}
$$

Where:

- $A$ = pipe cross-sectional area (m²)
- $D$ = internal pipe diameter (m)

The diameter must be converted from millimetres to metres before calculation.

### 5.3 Mean Flow Velocity

The mean velocity is calculated using the continuity relationship:

$$
V=\frac{Q}{A}
$$

Where:

- $V$ = mean fluid velocity (m/s)
- $Q$ = volumetric discharge (m³/s)
- $A$ = pipe cross-sectional area (m²)

### 5.4 Reynolds Number

The Reynolds number is defined as:

$$
Re=\frac{VD}{\nu}
$$

Where:

- $Re$ = Reynolds number (dimensionless)
- $V$ = mean flow velocity (m/s)
- $D$ = internal pipe diameter (m)
- $\nu$ = kinematic viscosity (m²/s)

For water, the manual uses:

$$
\nu=1.01\times10^{-6}\text{ m}^2/\text{s}
$$

This value is an approximation and may vary with water temperature.

## 6. Flow Regime Classification

The program uses the following approximate limits for pipe flow:

| Reynolds number | Flow regime | Typical dye behaviour |
|---|---|---|
| $Re<2000$ | Laminar | Straight, distinct filament |
| $2000\leq Re\leq4000$ | Transitional | Wavy or unstable filament |
| $Re>4000$ | Turbulent | Dye disperses and mixes |

These limits are approximate. The actual transition depends on factors such as disturbances, inlet conditions, and pipe characteristics. The calculated regime should be compared with the flow pattern observed in the apparatus.

## 7. Experimental Procedure

1. Switch on the Reynolds apparatus.
2. Adjust the water inflow using the flow-control valve.
3. Measure the time required to collect the specified volume of water.
4. Inject a thin filament of dye into the water stream.
5. Observe whether the dye remains straight, begins oscillating, or disperses.
6. Repeat the measurements at different flow rates.
7. Enter the collection times into the Python program.
8. Compare the calculated Reynolds numbers with the observed flow patterns.

Follow the laboratory's safety instructions and apparatus-specific operating procedure.

## 8. Program Overview

The Python program performs the following tasks:

1. Accepts the collection volume, pipe diameter, and kinematic viscosity.
2. Accepts the number of experimental observations.
3. Calculates discharge for each observation.
4. Calculates pipe area and mean velocity.
5. Calculates the Reynolds number.
6. Classifies the calculated flow regime.
7. Displays a formatted results table.
8. Generates and saves two graphs.

### User Inputs

| Parameter | Default value | Unit |
|---|---:|---|
| Collection volume | 1.0 | litre |
| Internal pipe diameter | 20.0 | mm |
| Kinematic viscosity | $1.01\times10^{-6}$ | m²/s |
| Collection time | Entered for each observation | s |

The default apparatus values match the specifications listed in the AFDL manual. The program allows these values to be changed for other apparatus configurations.

## 9. How to Run the Program

Save the code as:

```text
reynolds_apparatus.py
```

Run it from the VS Code terminal:

```bash
python reynolds_apparatus.py
```

Enter the apparatus parameters or press Enter to accept a displayed default. Then enter the number of observations and the collection time for each one.

## 10. Output

The program displays:

- Collection time
- Discharge
- Mean velocity
- Reynolds number
- Calculated flow regime

It also saves the following graphs in the current working directory:

### Graph 1 — Reynolds Number vs Discharge

File: `reynolds_number_vs_discharge.png`

This graph shows how the Reynolds number changes with volumetric discharge. For a fixed pipe diameter and fluid viscosity, increasing discharge increases the mean velocity and Reynolds number.

### Graph 2 — Mean Velocity vs Reynolds Number

File: `velocity_vs_reynolds_number.png`

This graph shows the relationship between the calculated mean velocity and Reynolds number for the recorded observations.

**Note:** These graphs are generated from calculated measurements. They do not independently determine the actual dye pattern; that must be observed experimentally.

## 11. Assumptions and Limitations

- The fluid is treated as incompressible.
- The pipe diameter is assumed to be constant and circular.
- The collection volume and timing measurements are assumed accurate.
- The input kinematic viscosity is assumed representative of the fluid temperature.
- The velocity calculated from discharge is the cross-sectional mean velocity, not the local velocity at every point.
- Reynolds-number limits provide approximate classification; visual observation remains an important part of this experiment.

Errors in timing, volume measurement, diameter measurement, or viscosity can affect the calculated Reynolds number.

## 12. Engineering Applications

Understanding flow regimes is important in:

- Aircraft fuel and hydraulic systems
- Cooling systems and heat exchangers
- Aircraft engine lubrication systems
- Pipeline and duct design
- Pressure-loss and fluid-flow calculations
- Experimental fluid mechanics and aerodynamic testing

The Reynolds number is also useful when comparing flow behaviour in geometrically similar systems and during scaled experiments.

## 13. Conclusion

The Reynolds apparatus demonstrates the transition from orderly laminar flow to transitional and turbulent flow through dye visualization. The Python program calculates discharge, mean velocity, and Reynolds number from experimental measurements and provides a systematic way to compare numerical predictions with observed flow behaviour.

The experiment connects fundamental fluid mechanics theory with experimental measurement and engineering computation.
