# Experiment 10 — Performance Test on a Two-Stage Reciprocating Air Compressor

> **Objective:** To calculate volumetric and isothermal efficiencies of a two-stage reciprocating air compressor at different delivery pressures and plot its performance curves.

---

## 1. Aim

To conduct a performance test on a two-stage twin-cylinder reciprocating air compressor and determine:

- Volumetric efficiency
- Isothermal efficiency

The program calculates these efficiencies at different delivery pressures and generates the two graphs required by the laboratory manual.

## 2. Apparatus

- Two-stage twin-cylinder reciprocating air compressor test rig
- Orifice meter and water manometer
- Energy meter
- Stopwatch
- Temperature and pressure measuring instruments

## 3. Apparatus Specifications

| Parameter | Symbol | Value |
|---|---|---:|
| Orifice diameter | $d_o$ | 15 mm |
| Low-pressure cylinder bore | $D_L$ | 70 mm |
| High-pressure cylinder bore | $D_H$ | 50 mm |
| Stroke length | $L$ | 85 mm |
| Compressor speed | $N_c$ | 950 rpm |
| Coefficient of discharge | $C_d$ | 0.62 |
| Atmospheric pressure | $P_a$ | 101325 Pa |
| Air gas constant | $R$ | 287 J/(kg·K) |
| Energy-meter constant | $C$ | 1600 pulses/kWh |
| Motor efficiency | $\eta_m$ | 0.88 |
| Belt transmission efficiency | $\eta_t$ | 0.95 |
| Density of water | $\rho_w$ | 1000 kg/m³ |
| Gravitational acceleration | $g$ | 9.81 m/s² |

## 4. Theory and Formulae

### 4.1 Atmospheric air density

The density of air at the measured room temperature is:

$$
\rho_a=\frac{P_a}{RT}
$$

where $T$ is the absolute temperature:

$$
T=T_{^\circ\mathrm{C}}+273.15
$$

### 4.2 Manometer head

The difference between the two manometer levels is converted into metres:

$$
H=\frac{|h_1-h_2|}{100}
$$

The equivalent head of air is calculated using the manual's equation:

$$
H_a=H\left(\frac{\rho_w}{\rho_a}-1\right)
$$

### 4.3 Actual volume flow rate

The orifice area is:

$$
a=\frac{\pi d_o^2}{4}
$$

The actual volume flow rate is:

$$
V_a=C_d a\sqrt{2gH_a}
$$

Here, $V_a$ is expressed in m³/s.

### 4.4 Theoretical volume flow rate

Using the low-pressure cylinder dimensions:

$$
V_T=\frac{\pi D_L^2}{4}\frac{LN_c}{60}
$$

where $N_c$ is the compressor speed in revolutions per minute.

### 4.5 Volumetric efficiency

$$
\eta_{\mathrm{vol}}=\frac{V_a}{V_T}\times100\%
$$

Volumetric efficiency compares the actual air intake with the theoretical cylinder displacement rate.

### 4.6 Compressor input power

The program follows the expression printed in the manual:

$$
P_{\mathrm{in}}=\left(\frac{5}{t}\right)\left(\frac{3600}{C}\right)\eta_m\eta_t
$$

where $t$ is the time in seconds for five energy-meter pulses.

**Important:** Verify this expression with your instructor. The correct treatment of motor and belt efficiencies depends on whether the measured energy-meter power is electrical input power or whether the calculation seeks shaft power. Multiplying by both efficiencies is reproduced from the manual rather than independently validated.

### 4.7 Compression ratio

The delivery pressure is entered as gauge pressure in kgf/cm² and converted to pascals.

$$
P_d(\mathrm{Pa})=P_d(\mathrm{kgf/cm^2})\times98066.5
$$

The absolute compression ratio is:

$$
r=\frac{P_d+P_a}{P_a}
$$

### 4.8 Isothermal power

The isothermal power is calculated as:

$$
P_{\mathrm{iso}}=\frac{P_a V_a\ln(r)}{1000}
$$

where $P_a$ is atmospheric pressure in pascals and $V_a$ is the actual volume flow rate in m³/s. The resulting power is in kW.

### 4.9 Isothermal efficiency

$$
\eta_{\mathrm{iso}}=\frac{P_{\mathrm{iso}}}{P_{\mathrm{in}}}\times100\%
$$

## 5. Experimental Procedure

1. Close the delivery valve and check the manometer connections.
2. Record atmospheric temperature and pressure.
3. Start the compressor following the laboratory's safety instructions.
4. Adjust the delivery valve to maintain the required delivery pressure.
5. Record the orifice-manometer levels.
6. Record the time for five energy-meter pulses.
7. Repeat the measurements at different delivery pressures.
8. Enter the observations into the Python program.
9. Examine the calculated efficiencies and performance curves.

Only operate the test rig under laboratory supervision and follow the prescribed startup and shutdown procedure.

## 6. Software Requirements

- Python 3.10 or later
- Matplotlib

Install Matplotlib if needed:

```bash
python -m pip install matplotlib
```

The `csv`, `math` and `pathlib` modules are included with Python.

## 7. Running the Program

Save the code as:

```text
air_compressor_performance.py
```

Run it from the VS Code terminal:

```bash
python air_compressor_performance.py
```

Enter:

- Atmospheric temperature in °C
- Number of readings
- Delivery gauge pressure in kgf/cm²
- Both orifice-manometer levels in cm
- Time for five energy-meter pulses in seconds

The program then calculates the results and plots the required graphs.

## 8. Generated Outputs

The program creates an `experiment_10_results/` folder containing:

| File | Purpose |
|---|---|
| `experiment_10_results.csv` | Calculated values for all readings |
| `delivery_pressure_vs_volumetric_efficiency.png` | Volumetric efficiency curve |
| `delivery_pressure_vs_isothermal_efficiency.png` | Isothermal efficiency curve |

## 9. Validation and Limitations

- All pressures used in thermodynamic calculations must be handled consistently; the program converts gauge delivery pressure to absolute pressure when calculating the compression ratio.
- Manometer differences are converted from centimetres to metres.
- The program assumes the theoretical displacement rate is based on the low-pressure cylinder and the formula specified in the manual.
- Results depend on the accuracy of experimental readings and the assumptions in the manual.
- Efficiencies outside the range 0–100% should trigger a review of the readings, units and input-power equation.
- Confirm the input-power convention with your instructor before using the values in a formal laboratory report.

## 10. Engineering Applications

Reciprocating air compressors are used in pneumatic systems, workshops, industrial process equipment, air-storage systems and applications requiring compressed air at elevated pressures.

Two-stage compression allows air to be compressed in successive stages, commonly with intercooling, which can reduce compression work and improve operating performance compared with single-stage compression at high pressure ratios.

## 11. Conclusion

The program automates the calculations for the two-stage reciprocating compressor experiment. It estimates actual and theoretical air-flow rates, input and isothermal power, and volumetric and isothermal efficiencies. The generated CSV and graphs support comparison of compressor performance at different delivery pressures.

**Engineering workflow:** Measure → Calculate → Validate → Plot → Interpret → Document.
