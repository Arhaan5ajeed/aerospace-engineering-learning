# Verification of Bernoulli's Theorem

> **Objective:** To verify Bernoulli's theorem experimentally by calculating the pressure head, velocity head, hydraulic gradient line (HGL), and total energy line (TEL) at seven channel locations, and to examine the variation of total energy along the flow passage.

---

## 1. Introduction

Bernoulli's theorem is a fundamental principle of fluid mechanics that describes the relationship between pressure, velocity, and elevation in a flowing fluid.

For steady, incompressible flow with negligible viscous losses, the total mechanical energy per unit weight of a fluid remains constant along a streamline.

This project implements the calculations required for the **Verification of Bernoulli's Theorem — Experiment No. 3** from the Applied Fluid Dynamics Laboratory (AFDL) manual.

The program uses experimental piezometer readings and collecting-tank measurements to calculate flow velocity and the corresponding energy heads at seven locations. It then plots the Hydraulic Gradient Line (HGL) and Total Energy Line (TEL) for analysis.

## 2. Aim

To verify Bernoulli's theorem by determining the pressure head, velocity head, hydraulic gradient line, and total energy line at different sections of a flow passage.

## 3. Apparatus and Experimental Setup

The experiment uses a Bernoulli's theorem test rig and a stopwatch.

The apparatus contains a flow passage with seven measurement locations and piezometers that indicate the pressure head at each location. The flow rate is determined using a collecting tank.

### Apparatus dimensions from the AFDL manual

| Parameter | Value |
|---|---:|
| Collecting tank length | 0.30 m |
| Collecting tank breadth | 0.30 m |
| Collecting tank area | 0.09 m² |
| Water-level rise | 0.10 m |
| Gravitational acceleration | 9.81 m/s² |
| Channel breadth | 20 mm |
| Number of measurement locations | 7 |

The channel heights at locations 1–7 are 35, 32.5, 30, 25, 22.5, 18.5, and 14 mm, respectively.

These dimensions are treated as constants in the program, following the manual. Experimental piezometer readings and collection time are entered by the user.

## 4. Theory

### 4.1 Bernoulli's Theorem

For steady, incompressible flow with negligible energy losses, Bernoulli's equation is:

$$
\boxed{Z+\frac{P}{\rho g}+\frac{V^2}{2g}=\text{constant}}
$$

Where:

- $Z$ = datum or elevation head (m)
- $P$ = static pressure (Pa)
- $\rho$ = fluid density (kg/m³)
- $g$ = gravitational acceleration (m/s²)
- $V$ = flow velocity (m/s)

The three terms represent potential head, pressure head, and velocity head, respectively.

For the horizontal flow passage in this experiment, a common datum is assumed, so $Z=0$. The equation becomes:

$$
\boxed{\frac{P}{\rho g}+\frac{V^2}{2g}=\text{constant}}
$$

In an ideal flow, a decrease in pressure head is accompanied by an increase in velocity head, keeping the total head constant.

### 4.2 Actual Discharge

The volumetric flow rate is measured using the collecting tank:

$$
Q=\frac{\text{Volume collected}}{\text{Time taken}}
$$

For a rectangular tank:

$$
A_t=L\times B
$$

The collected volume is:

$$
\Delta \mathcal{V}=A_t\Delta y
$$

Therefore:

$$
\boxed{Q=\frac{A_t\Delta y}{t}}
$$

Where:

- $Q$ = volumetric discharge (m³/s)
- $A_t$ = collecting-tank area (m²)
- $\Delta y$ = rise of water in the tank (m)
- $t$ = time taken (s)

The manual specifies a 10 cm rise, so $\Delta y=0.10\text{ m}$.

For the specified tank dimensions:

$$
Q=\frac{(0.30)(0.30)(0.10)}{t}
$$

### 4.3 Cross-Sectional Area

The cross-sectional area at each measurement location is calculated using:

$$
\boxed{a_i=h_i b}
$$

Where:

- $a_i$ = flow-passage area at location $i$ (m²)
- $h_i$ = channel height at location $i$ (m)
- $b$ = common channel breadth (m)

The dimensions are converted from millimetres to metres before calculating the areas.

### 4.4 Velocity of Flow

For steady, incompressible flow, the continuity equation gives:

$$
Q=a_iV_i
$$

Therefore:

$$
\boxed{V_i=\frac{Q}{a_i}}
$$

The same discharge is used at all seven locations under the steady-flow assumption. Since the channel area changes, the calculated velocity changes along the passage.

### 4.5 Velocity Head

Velocity head represents the kinetic energy per unit weight of the fluid:

$$
\boxed{h_{v,i}=\frac{V_i^2}{2g}}
$$

Its unit is metres.

As velocity increases, the velocity head increases quadratically.

### 4.6 Pressure Head

The pressure head is the pressure energy per unit weight of the fluid:

$$
\boxed{h_{p,i}=\frac{P_i}{\rho g}}
$$

In this experiment, the piezometers directly indicate the pressure head. The program accepts readings in centimetres and converts them to metres.

### 4.7 Hydraulic Gradient Line (HGL)

The Hydraulic Gradient Line represents the sum of elevation head and pressure head:

$$
\boxed{\mathrm{HGL}_i=Z_i+h_{p,i}}
$$

Since the manual assumes a common datum with $Z_i=0$:

$$
\boxed{\mathrm{HGL}_i=h_{p,i}}
$$

Thus, the HGL corresponds to the pressure-head distribution for the chosen datum.

### 4.8 Total Energy Line (TEL)

The Total Energy Line represents the total mechanical head:

$$
\boxed{\mathrm{TEL}_i=Z_i+h_{p,i}+\frac{V_i^2}{2g}}
$$

For the common datum used in this experiment:

$$
\boxed{\mathrm{TEL}_i=h_{p,i}+\frac{V_i^2}{2g}}
$$

According to ideal Bernoulli flow, the TEL should remain constant along a streamline. In a real experiment, it may decrease slightly because of frictional and other hydraulic losses.

## 5. Experimental Procedure

The experiment follows the procedure in the AFDL manual:

1. Switch on the pump power supply.
2. Adjust the delivery and drain valves to establish a steady flow rate.
3. Record the seven piezometer pressure-head readings.
4. Measure the time required for a 10 cm rise in the collecting tank.
5. Enter the readings and time into the Python program.
6. Calculate the discharge, velocities, velocity heads, HGL, and TEL.
7. Plot HGL and TEL against the seven channel locations.
8. Examine the energy distribution and identify any variation in total head.

The program processes the recorded measurements; it does not control the experimental apparatus.

## 6. Program Inputs

| Input | Description | Unit |
|---|---|---|
| $h_{p,1}$ | Pressure head at location 1 | cm |
| $h_{p,2}$ | Pressure head at location 2 | cm |
| $h_{p,3}$ | Pressure head at location 3 | cm |
| $h_{p,4}$ | Pressure head at location 4 | cm |
| $h_{p,5}$ | Pressure head at location 5 | cm |
| $h_{p,6}$ | Pressure head at location 6 | cm |
| $h_{p,7}$ | Pressure head at location 7 | cm |
| $t$ | Time for a 10 cm collecting-tank rise | s |

The apparatus dimensions, channel breadth, tank area, rise height, and gravitational acceleration are defined in the program based on the manual.

## 7. Program Outputs

The program calculates and displays:

- Collecting-tank area
- Actual volumetric discharge
- Cross-sectional area at each channel location
- Velocity at each location
- Velocity head at each location
- Pressure head at each location
- Hydraulic Gradient Line (HGL)
- Total Energy Line (TEL)
- Mean HGL and TEL
- Range of the calculated TEL values

The output table allows the seven locations to be compared systematically.

## 8. Graphical Representation

The program generates a graph titled **Verification of Bernoulli's Theorem**.

- **X-axis:** Channel location, from 1 to 7
- **Y-axis:** Head in metres
- **First curve:** Hydraulic Gradient Line (HGL)
- **Second curve:** Total Energy Line (TEL)

The HGL represents pressure head for the common datum. The TEL includes both pressure and velocity heads.

In an ideal system, the TEL would remain constant. In practice, a small reduction may occur due to friction and other energy losses.

The generated graph is saved as:

`bernoulli_theorem_verification.png`

## 9. Python Concepts Used

### Variables and data types

Variables store apparatus dimensions, measurement readings, discharge, velocities, and calculated heads.

### User input

The `input()` function allows experimental readings and collection time to be entered at runtime.

### Conditional statements

The program validates the collection time and rejects negative piezometer readings.

### Lists

A list temporarily stores the seven measured pressure-head readings.

### NumPy arrays

NumPy stores the section dimensions and experimental readings and performs vectorised calculations across all seven locations.

### Mathematical operations

The program uses multiplication, division, and exponentiation (squaring) to calculate areas, discharge, velocity, and energy heads.

### Matplotlib

Matplotlib generates the HGL and TEL graph, with labels, a legend, grid lines, and a title.

## 10. Advantages

- Automates repetitive calculations.
- Reduces manual arithmetic errors.
- Calculates results for all seven locations consistently.
- Uses the apparatus dimensions specified in the laboratory manual.
- Presents the results in a structured table.
- Generates a graph suitable for laboratory analysis and reporting.
- Provides a practical example of applying Python to experimental fluid mechanics.

## 11. Assumptions and Limitations

- The flow is treated as steady and incompressible.
- The same volumetric discharge is assumed at all seven locations.
- The channel breadth is assumed to be constant.
- The specified channel heights and collecting-tank dimensions are treated as accurate.
- The datum head is taken as zero at all locations, as specified in the manual.
- The piezometer readings are assumed to represent pressure head in the flowing fluid.
- The collecting tank is assumed to have a constant cross-sectional area.
- The water-level rise is assumed to be exactly 10 cm.
- The program does not model friction, turbulence, local losses, or measurement uncertainty directly.

The calculation is only as reliable as the recorded measurements and the assumptions used.

## 12. Accuracy and Experimental Errors

Potential sources of error include:

- Parallax when reading piezometer levels
- Stopwatch reaction time
- Fluctuations in pump discharge
- Air bubbles in the piezometer tubes
- Errors in channel dimensions
- Uncertainty in the collecting-tank dimensions
- Flow disturbances and energy losses

Numerical precision and experimental accuracy are different. Printing more decimal places does not remove measurement uncertainty.

The variation in TEL can help identify departures from ideal Bernoulli behaviour, but it should be interpreted alongside the experimental conditions and measurement errors.

## 13. Future Scope of Improvement

The program can be extended to include:

- Multiple flow-rate trials and comparison between operating conditions
- CSV or Excel export of experimental data
- Automatic generation of laboratory reports
- Measurement-uncertainty calculations
- Improved graphical presentation with error bars
- Comparison with ideal Bernoulli predictions
- Estimation of head loss between successive sections
- A graphical user interface for entering measurements
- Automated comparison of experimental and theoretical energy distributions

These improvements would make the program more suitable for extended laboratory analysis and engineering data processing.

## 14. Requirements and Execution

### Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the program:

```bash
python bernoulli_theorem_verification.py
```

Enter the seven piezometer readings in centimetres, followed by the time taken for the 10 cm collecting-tank rise.

The program prints the calculated values and displays the HGL and TEL graph.

## 15. Project Structure

```text
simple-engineering-calculations/
├── bernoulli_theorem_verification.py
└── README.md
```

## 16. Conclusion

This project demonstrates the application of Bernoulli's theorem and the continuity equation to an experimental flow passage. By calculating the discharge, cross-sectional areas, velocities, velocity heads, pressure heads, HGL, and TEL, the program provides a systematic method for analysing the measured flow.

The graphical comparison of HGL and TEL helps illustrate the relationship between pressure energy and kinetic energy, while deviations in total head highlight the difference between idealised theory and real fluid flow.

The project also demonstrates how Python, NumPy, and Matplotlib can be used to automate engineering calculations and present experimental results clearly.

---

*Developed as part of an Applied Fluid Dynamics Laboratory learning project, combining fluid mechanics theory, numerical computation, experimental data analysis, and scientific visualisation.*
