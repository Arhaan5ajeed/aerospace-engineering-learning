# Experiment 8 — Performance Test on Air Blower Test Rig

> **Objective:** To evaluate the performance of a centrifugal air blower for different impeller vane configurations by calculating discharge, input power, output power and efficiency.

---

## 1. Aim

To conduct a performance test on a centrifugal blower and study its characteristics for the following impeller configurations:

- Radial vanes
- Forward-curved vanes
- Backward-curved vanes

The program calculates the blower's performance parameters and plots them against air discharge.

## 2. Apparatus

- Centrifugal air blower test rig
- Interchangeable impellers
- Manometers
- Energy meter
- Stopwatch

## 3. Apparatus Constants

| Parameter | Symbol | Value |
|---|---|---:|
| Pipe diameter | $d_1$ | 70 mm |
| Orifice diameter | $d_2$ | 50.4 mm |
| Coefficient of discharge | $C_d$ | 0.62 |
| Density of water | $\rho_w$ | 1000 kg/m³ |
| Density of air | $\rho_a$ | 1.225 kg/m³ |
| Energy-meter constant | $C$ | 1600 pulses/kWh |
| Motor efficiency | $\eta_m$ | 77.5% |
| Gravitational acceleration | $g$ | 9.81 m/s² |

These are the values specified in the laboratory manual. If the apparatus or instructor specifies different values, update the constants in the Python program.

## 4. Theory and Formulae

### 4.1 Manometer level differences

For each manometer, the difference between the two observed levels is:

$$
H=\frac{|h_1-h_2|}{100}
$$

where the readings $h_1$ and $h_2$ are entered in centimetres, and $H$ is obtained in metres.

### 4.2 Equivalent air heads

The manual specifies the following relationships:

$$
H_d=H_1\left(\frac{\rho_w}{\rho_a}-1\right)
$$

$$
H_s=H_2\left(\frac{\rho_w}{\rho_a}-1\right)
$$

$$
H_o=H_3\left(\frac{\rho_w}{\rho_a}-1\right)
$$

Here, $H_d$ is the delivery head, $H_s$ is the suction head, and $H_o$ is the orifice-meter head used for discharge calculation.

### 4.3 Areas of pipe and orifice

$$
a_1=\frac{\pi d_1^2}{4}
$$

$$
a_2=\frac{\pi d_2^2}{4}
$$

The diameters must be converted from millimetres to metres before calculating the areas.

### 4.4 Air discharge

The discharge equation given in the manual is:

$$
Q=\frac{C_d a_1a_2\sqrt{2gH_o}}{\sqrt{a_1^2-a_2^2}}
$$

where $Q$ is the volume of air flowing per second in m³/s.

### 4.5 Input power

The program follows the formula printed in the manual:

$$
P_{\mathrm{in}}=\left(\frac{5}{t}\right)\left(\frac{3600}{C}\right)\eta_m
$$

where:

- $t$ = time taken for five energy-meter pulses, in seconds
- $C$ = energy-meter constant
- $\eta_m=0.775$

**Important:** Confirm this input-power expression with your instructor before using the calculated efficiency in a formal report. The manual's printed multiplication by motor efficiency may require clarification depending on how the apparatus defines measured input power.

### 4.6 Output power

$$
P_{\mathrm{out}}=\frac{\rho_a gQH_d}{1000}
$$

Output power is calculated in kilowatts.

### 4.7 Blower efficiency

$$
\eta=\frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}\times100\%
$$

Efficiency represents the ratio of calculated output power to input power, expressed as a percentage.

## 5. Experimental Procedure

1. Ensure that the delivery valve is fully open before starting the blower.
2. Start the blower according to the laboratory's safety procedure.
3. Adjust the delivery valve to obtain a different flow condition.
4. Record both levels in the delivery, suction and orifice manometers.
5. Record the time required for five energy-meter pulses.
6. Repeat the measurements for multiple valve positions.
7. Repeat the experiment for the impeller configurations available in the laboratory.
8. Enter the readings into the program and compare the performance curves.

Follow your instructor's procedure for changing impellers and never change an impeller while the equipment is running.

## 6. Software Requirements

- Python 3.10 or later
- Matplotlib

Install Matplotlib if it is not already installed:

```bash
python -m pip install matplotlib
```

## 7. Running the Program

Save the program as:

```text
air_blower_performance.py
```

Run it from the VS Code terminal:

```bash
python air_blower_performance.py
```

The program asks how many readings you have for each impeller:

- Radial
- Forward-curved
- Backward-curved

Enter `0` for any impeller configuration that you did not test.

For every reading, enter the two levels of each manometer and the time for five energy-meter pulses. Enter manometer levels in **cm** and time in **seconds**.

## 8. Generated Outputs

The program creates an `experiment_8_results/` folder containing:

| File | Description |
|---|---|
| `experiment_8_results.csv` | Calculated values for every reading |
| `efficiency_vs_discharge.png` | Blower efficiency against discharge |
| `input_power_vs_discharge.png` | Input power against discharge |
| `output_power_vs_discharge.png` | Output power against discharge |

The graphs distinguish the impeller configurations using separate plotted series.

The manual's graph section lists discharge versus output power and discharge versus blower efficiency. The input-power graph is also included because the stated aim refers to input power versus discharge.

## 9. Validation and Limitations

- The program uses the apparatus constants supplied in the manual.
- Manometer level differences are converted from centimetres to metres.
- The program uses the absolute difference between the two observed levels.
- Calculations depend on correct experimental readings and the manual's specified equations.
- An efficiency greater than 100% or below 0% should prompt a check of the readings, units, and input-power formula.
- The program does not independently determine whether the observed blower performance is physically realistic; compare the output with the experiment and instructor's expectations.

## 10. Engineering Applications

Centrifugal blowers are used in ventilation systems, air-conditioning plants, industrial furnaces, mines, combustion-air supply, and other systems requiring relatively high air flow at moderate pressure.

Comparing impeller configurations helps engineers understand how vane geometry influences discharge, power requirements and operating efficiency.

## 11. Conclusion

The program automates the calculations required for the centrifugal air blower performance test. It compares radial, forward-curved and backward-curved impellers using discharge, input power, output power and efficiency, and generates plots and a CSV file for further analysis.

**Engineering workflow:** Measure → Calculate → Validate → Plot → Interpret → Document.
