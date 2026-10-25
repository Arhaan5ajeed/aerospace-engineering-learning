# Experiment 9 — Determination of Viscosity of Oil Using a Redwood Viscometer

> **Objective:** To determine the density, kinematic viscosity, and dynamic viscosity of an oil sample at different temperatures using Redwood viscometer measurements.

---

## 1. Aim

To determine the kinematic and dynamic viscosity of a given oil sample at different temperatures using a Redwood viscometer, and to plot:

1. Kinematic viscosity vs temperature
2. Dynamic viscosity vs temperature

## 2. Apparatus Required

- Redwood viscometer
- Stopwatch
- Thermometers
- Oil sample
- 50 mL measuring flask
- Heating arrangement

## 3. Theory

Viscosity is a measure of a fluid's resistance to deformation and flow. For liquids such as oil, viscosity generally decreases as temperature increases because heating reduces the effects of intermolecular resistance to motion.

The Redwood viscometer estimates viscosity by measuring the time required for a specified volume of oil to flow through a calibrated orifice under specified conditions.

The experiment determines oil density from its measured mass and volume, calculates kinematic viscosity using the viscometer calibration equation, and then obtains dynamic viscosity.

## 4. Formulae

### 4.1 Mass of oil

$$
m_{\text{oil}}=W_2-W_1
$$

where:

- $W_1$ = mass of the empty measuring flask, in kg
- $W_2$ = mass of the flask containing 50 mL of oil, in kg

### 4.2 Density of oil

The collected volume is:

$$
V=50\text{ mL}=50\times10^{-6}\text{ m}^3
$$

Therefore,

$$
\rho=\frac{W_2-W_1}{50\times10^{-6}}
$$

Density is obtained in kg/m³.

### 4.3 Kinematic viscosity

The manual gives the Redwood viscometer equation:

$$
\nu=\left(Ct-\frac{\beta}{t}\right)\times10^{-6}
$$

where:

- $\nu$ = kinematic viscosity in m²/s
- $t$ = measured flow time in seconds
- $C$ = viscometer constant
- $\beta$ = coefficient of kinetic energy

The constants depend on the flow time:

| Flow time, $t$ | $C$ | $\beta$ |
|---|---:|---:|
| 40–85 seconds | 0.264 | 190 |
| Above 85–2000 seconds | 0.247 | 65 |

The code selects the corresponding constants based on the entered time. Measurements outside the stated calibration ranges should be checked against the laboratory instructions.

### 4.4 Dynamic viscosity

$$
\mu=\nu\rho
$$

where:

- $\mu$ = dynamic viscosity in Pa·s or N·s/m²
- $\nu$ = kinematic viscosity in m²/s
- $\rho$ = oil density in kg/m³

## 5. Experimental Procedure

1. Level the viscometer using its leveling screws.
2. Clean the oil cup and ensure that the jet is free from dirt.
3. Fill the water bath to the prescribed level.
4. Position the brass bath and close the orifice with the ball valve.
5. Fill the oil cup up to the indicator tip.
6. Position the 50 mL measuring flask below the jet.
7. Heat and stir the oil and water bath as directed by the laboratory procedure.
8. At the selected oil temperature, remove the ball valve and start the stopwatch simultaneously.
9. Stop the stopwatch when 50 mL of oil has been collected.
10. Measure the mass of the flask containing the oil.
11. Repeat the procedure at the other required temperatures.
12. Enter the readings into the Python program and compare the calculated viscosities.

Follow the laboratory's temperature-control and hot-oil safety instructions.

## 6. Software Requirements

- Python 3.10 or later
- Matplotlib

Install Matplotlib from the VS Code terminal:

```bash
python -m pip install matplotlib
```

## 7. Running the Program

Save the code as:

```text
redwood_viscometer.py
```

Run:

```bash
python redwood_viscometer.py
```

The program asks for:

- Oil type/name
- Room temperature
- Mass of the empty measuring flask
- Number of temperature readings
- Oil temperature for each reading
- Time to collect 50 mL of oil
- Mass of the flask plus oil for each reading

Enter masses in **kilograms**, temperatures in **degrees Celsius**, and flow times in **seconds**.

## 8. Generated Outputs

The program creates an `experiment_9_results/` folder containing:

| File | Purpose |
|---|---|
| `redwood_viscometer_results.csv` | Calculated properties for each valid reading |
| `kinematic_viscosity_vs_temperature.png` | Kinematic viscosity vs temperature |
| `dynamic_viscosity_vs_temperature.png` | Dynamic viscosity vs temperature |

The CSV contains the input readings, oil density, calibration constants, and both viscosity values.

## 9. Validation and Limitations

- The program assumes that each collected sample has a volume of 50 mL.
- The empty flask mass is entered once and reused for all observations.
- The mass of the flask plus oil must exceed the empty flask mass.
- The Redwood constants are selected from the calibration ranges in the laboratory manual.
- Correct temperature control, clean equipment, accurate timing, and correct mass measurements are essential for reliable results.
- The program does not correct for experimental errors or independently calibrate the viscometer.

## 10. Engineering Applications

Viscosity measurements are important in:

- Lubricant selection for bearings and rotating machinery
- Engine oil and transmission-fluid testing
- Hydraulic systems
- Industrial lubrication and maintenance
- Studying the temperature dependence of liquid properties

## 11. Conclusion

The program automates the calculation of oil density, kinematic viscosity, and dynamic viscosity from Redwood viscometer observations. It also generates the two temperature-dependent plots required by the laboratory manual.

**Engineering workflow:** Measure → Calculate → Validate → Plot → Interpret → Document.
