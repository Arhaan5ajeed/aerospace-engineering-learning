# Determination of Coefficient of Impact of a Jet on Vanes

> **Objective:** To determine the coefficient of impact of a water jet acting on different vanes by comparing the actual force with the theoretical force.

---

## 1. Introduction

When a high-velocity fluid jet strikes a stationary vane, its momentum changes, producing a force on the vane. This principle is used in hydraulic machines, impulse turbines, and other fluid-energy systems.

In this experiment, a water jet from a nozzle strikes a vane. The force exerted by the jet is balanced using a weight-and-lever arrangement. The experimental force is compared with the theoretical force calculated from the jet velocity.

This Python program automates the calculations, displays the experimental results in a table, and generates plots for analysing the results.

## 2. Objectives

- Calculate the actual discharge of water using the collecting tank.
- Determine the jet velocity from the pressure gauge reading.
- Calculate the theoretical force exerted by the jet.
- Calculate the actual force using the balancing weight and lever arms.
- Determine the coefficient of impact.
- Compare measurements for flat and conical vanes.
- Plot actual force against theoretical force and coefficient of impact against discharge.

## 3. Apparatus and default values

The default values follow the AFDL laboratory manual.

| Parameter | Symbol | Default value |
|---|---|---:|
| Collecting tank length | $L_t$ | 0.5 m |
| Collecting tank breadth | $B_t$ | 0.3 m |
| Water-level rise | $\Delta y$ | 0.10 m |
| Nozzle diameter | $d$ | 10 mm |
| Fulcrum-to-weight arm | $L_1$ | 38 cm |
| Fulcrum-to-jet arm | $L_2$ | 7.5 cm |
| Gravitational acceleration | $g$ | 9.81 m/s² |
| Water density | $\rho$ | 1000 kg/m³ |

The program allows the tank dimensions, tank rise, nozzle diameter, and lever-arm lengths to be changed.

## 4. Theory and equations

### 4.1 Collecting tank area

The collecting tank area is:

$$
A_t=L_tB_t
$$

For the manual's default dimensions:

$$
A_t=0.5\times0.3=0.15\ \text{m}^2
$$

### 4.2 Actual discharge

The actual volumetric discharge is calculated by measuring the time required for the water level in the tank to rise by a known height.

$$
Q=\frac{A_t\Delta y}{t}
$$

Where:

- $Q$ = actual discharge in m³/s
- $A_t$ = collecting tank area in m²
- $\Delta y$ = tank water-level rise in m
- $t$ = measured time in seconds

### 4.3 Nozzle area

The nozzle is assumed to have a circular cross-section.

$$
A_N=\frac{\pi d^2}{4}
$$

The nozzle diameter must be converted from millimetres to metres before calculating the area.

For the default 10 mm nozzle:

$$
d=10\times10^{-3}\ \text{m}
$$

### 4.4 Pressure conversion and pressure head

The pressure gauge reading is entered in kgf/cm². It is converted to pascals using:

$$
P(\text{Pa})=P(\text{kgf/cm}^2)\times98066.5
$$

The pressure head is:

$$
H=\frac{P}{\rho g}
$$

Where:

- $H$ = pressure head in metres
- $P$ = gauge pressure in pascals
- $\rho$ = water density in kg/m³
- $g$ = gravitational acceleration in m/s²

### 4.5 Jet velocity

Using the Bernoulli relation specified in the manual:

$$
V_N=\sqrt{2gH}
$$

This assumes the gauge pressure head is converted into jet velocity head without accounting for losses between the pressure measurement location and the nozzle exit.

### 4.6 Theoretical force

The theoretical force is calculated using the expression in the AFDL manual:

$$
F_t=\rho A_NV_N^2
$$

Where:

- $F_t$ = theoretical force in newtons
- $\rho$ = water density in kg/m³
- $A_N$ = nozzle area in m²
- $V_N$ = jet velocity in m/s

This is the manual's theoretical-force model. The exact momentum-force expression for a real vane depends on how the jet's velocity magnitude and direction change after impact.

### 4.7 Actual force

The actual force is obtained from the balancing weight and lever arrangement:

$$
F_a=\left(W\frac{L_1}{L_2}\right)g
$$

Where:

- $F_a$ = actual force inferred from the lever balance in newtons
- $W$ = balancing mass in kg
- $L_1$ = fulcrum-to-weight arm length
- $L_2$ = fulcrum-to-jet arm length
- $g$ = gravitational acceleration

The program asks for the weight in grams and converts it to kilograms before applying the equation.

### 4.8 Coefficient of impact

The coefficient is calculated as specified in the manual:

$$
C_i=\frac{F_a}{F_t}
$$

It is a dimensionless ratio comparing the experimentally inferred force with the theoretical force.

A value different from the idealised prediction may result from jet spreading, pressure-measurement uncertainty, friction in the lever mechanism, alignment errors, splashing, and the simplifying assumptions in the theoretical model.

## 5. Experimental procedure

1. Switch on the experimental setup.
2. Open the gate valve and record the pressure gauge reading.
3. Measure the time required for the collecting tank water level to rise by 10 cm, or by the selected rise.
4. Record the balancing weight for the observation.
5. Repeat the measurements at different gate-valve openings.
6. Repeat for the required vane types, such as the flat and conical vanes.
7. Enter the readings into the program and compare the calculated results.

Follow the laboratory supervisor's operating instructions when changing vanes or adjusting the apparatus.

## 6. Program inputs

| Input | Unit | Description |
|---|---|---|
| Tank length | m | Length of the collecting tank |
| Tank breadth | m | Breadth of the collecting tank |
| Tank rise | cm | Water-level rise used to measure discharge |
| Nozzle diameter | mm | Internal diameter of the nozzle |
| $L_1$ | cm | Fulcrum-to-weight arm |
| $L_2$ | cm | Fulcrum-to-jet arm |
| Vane type | — | Flat or conical vane |
| Balancing weight | g | Mass placed in the pan |
| Pressure gauge reading | kgf/cm² | Gauge pressure |
| Collection time | s | Time for the specified tank rise |

Multiple observations can be entered in a single run. Different vane types can be included in the same dataset.

## 7. Program outputs

For every observation, the program reports:

- Vane type
- Balancing weight
- Pressure gauge reading
- Collection time
- Actual discharge $Q$
- Jet velocity $V_N$
- Actual force $F_a$
- Theoretical force $F_t$
- Coefficient of impact $C_i$

## 8. Graphs generated

### Graph 1: Actual Force vs Theoretical Force

- **X-axis:** Theoretical force, $F_t$ (N)
- **Y-axis:** Actual force, $F_a$ (N)

This graph compares the experimental force with the force predicted by the theoretical model. Different vane types are shown separately.

### Graph 2: Coefficient of Impact vs Discharge

- **X-axis:** Actual discharge, $Q$ (m³/s)
- **Y-axis:** Coefficient of impact, $C_i$

This graph helps assess how the calculated coefficient varies with discharge for each vane type.

The plots are saved automatically as:

- `impact_force_comparison.png`
- `coefficient_of_impact_vs_discharge.png`

## 9. Python concepts used

- Functions for reusable input validation
- Loops for entering multiple observations
- Dictionaries and lists for storing experimental results
- NumPy for numerical calculations
- Matplotlib for plotting experimental data
- Unit conversions between grams and kilograms, millimetres and metres, and kgf/cm² and pascals
- Conditional selection for different vane types

## 10. Assumptions and limitations

- Water is treated as an incompressible fluid with density 1000 kg/m³.
- The pressure gauge reading is treated as gauge pressure.
- The jet velocity is estimated from the pressure head using the ideal Bernoulli relation.
- The nozzle is circular, with a uniform velocity profile.
- The lever is assumed to be in static equilibrium, and the lever-arm dimensions are measured from the fulcrum.
- Mechanical friction, splashing, jet misalignment, and other experimental losses are not explicitly modelled.
- The theoretical force follows the expression printed in the AFDL manual; it does not model the detailed momentum change for every vane geometry.

The calculated coefficient should therefore be interpreted alongside the experimental conditions and the assumptions of the manual's model.

## 11. Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries if they are not already available:

```bash
pip install numpy matplotlib
```

## 12. How to run

1. Save the Python program as `coefficient_of_impact.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python coefficient_of_impact.py
```

4. Enter the apparatus dimensions or press Enter to use the default values.
5. Enter the number of observations.
6. Provide the vane type, balancing weight, pressure gauge reading, and collection time for each observation.
7. Review the printed results and generated plots.

## 13. Conclusion

This program automates the determination of the coefficient of impact of a water jet on flat and conical vanes using the equations and apparatus dimensions in the AFDL manual. It reduces repetitive calculations, supports multiple observations, and provides plots for comparing the measured and theoretical forces.

The results remain dependent on the quality of the experimental measurements and the validity of the theoretical assumptions.
