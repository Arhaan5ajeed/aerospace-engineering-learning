"""
Experiment 10: Performance Test on Two-Stage Twin-Cylinder
Reciprocating Air Compressor
AFDL - Applied Fluid Dynamics Laboratory
"""

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt

# Apparatus constants from the AFDL manual
CD = 0.62
ORIFICE_DIAMETER = 0.015       # m
LP_CYLINDER_DIAMETER = 0.070   # m
STROKE_LENGTH = 0.085          # m
COMPRESSOR_SPEED = 950.0       # rpm

RHO_WATER = 1000.0             # kg/m^3
G = 9.81                       # m/s^2
R_AIR = 287.0                  # J/(kg K)
ATM_PRESSURE = 1.01325e5       # Pa

ENERGY_METER_C = 1600.0        # pulses/kWh
MOTOR_EFFICIENCY = 0.88
BELT_EFFICIENCY = 0.95
KGF_CM2_TO_PA = 98066.5

OUTPUT_DIR = Path("experiment_10_results")
OUTPUT_DIR.mkdir(exist_ok=True)


def get_number(prompt, minimum=None, strict=False):
    while True:
        try:
            value = float(input(prompt))
            valid = math.isfinite(value)

            if minimum is not None:
                valid = valid and (
                    value > minimum if strict else value >= minimum
                )

            if valid:
                return value

            print("Invalid value. Please check the required range.")

        except ValueError:
            print("Enter a valid number.")


def get_integer(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a whole number of at least {minimum}.")
        except ValueError:
            print("Enter a valid whole number.")


def calculate_reading(
    index,
    room_temp_c,
    delivery_pressure_kgf_cm2,
    h1_cm,
    h2_cm,
    time_for_5_pulses,
):
    """Calculate flow rates, powers and compressor efficiencies."""

    if time_for_5_pulses <= 0:
        raise ValueError("Pulse time must be greater than zero.")

    temperature_k = room_temp_c + 273.15
    if temperature_k <= 0:
        raise ValueError("Temperature must be above absolute zero.")

    # Density of atmospheric air at room temperature
    rho_air = ATM_PRESSURE / (R_AIR * temperature_k)

    # Differential manometer head, in metres of water
    h_m = abs(h1_cm - h2_cm) / 100.0

    # Equivalent head of air, according to the manual
    head_air = h_m * (RHO_WATER / rho_air - 1.0)

    if head_air < 0:
        raise ValueError("Negative air head. Check the manometer readings.")

    # Actual air volume flow rate
    orifice_area = math.pi * ORIFICE_DIAMETER**2 / 4.0
    actual_volume = (
        CD * orifice_area * math.sqrt(2.0 * G * head_air)
    )

    # Theoretical displacement flow rate of the LP cylinder
    lp_area = math.pi * LP_CYLINDER_DIAMETER**2 / 4.0
    theoretical_volume = (
        lp_area * STROKE_LENGTH * COMPRESSOR_SPEED / 60.0
    )

    volumetric_efficiency = (
        actual_volume / theoretical_volume * 100.0
    )

    # Input power formula as printed in the laboratory manual
    input_power = (
        (5.0 / time_for_5_pulses)
        * (3600.0 / ENERGY_METER_C)
        * MOTOR_EFFICIENCY
        * BELT_EFFICIENCY
    )

    # Convert gauge delivery pressure to Pa
    delivery_pressure_pa = (
        delivery_pressure_kgf_cm2 * KGF_CM2_TO_PA
    )

    # Absolute compression ratio
    compression_ratio = (
        delivery_pressure_pa + ATM_PRESSURE
    ) / ATM_PRESSURE

    if compression_ratio <= 0:
        raise ValueError("Compression ratio must be positive.")

    # Isothermal power, in kW
    isothermal_power = (
        ATM_PRESSURE
        * actual_volume
        * math.log(compression_ratio)
        / 1000.0
    )

    # Isothermal efficiency
    isothermal_efficiency = (
        isothermal_power / input_power * 100.0
    )

    return {
        "Reading": index,
        "Room temperature (deg C)": room_temp_c,
        "Delivery pressure (kgf/cm^2)": delivery_pressure_kgf_cm2,
        "Manometer difference (cm)": abs(h1_cm - h2_cm),
        "Air density (kg/m^3)": rho_air,
        "Air head (m)": head_air,
        "Actual volume (m^3/s)": actual_volume,
        "Theoretical volume (m^3/s)": theoretical_volume,
        "Time for 5 pulses (s)": time_for_5_pulses,
        "Input power (kW)": input_power,
        "Isothermal power (kW)": isothermal_power,
        "Volumetric efficiency (%)": volumetric_efficiency,
        "Isothermal efficiency (%)": isothermal_efficiency,
        "Compression ratio": compression_ratio,
    }


def collect_readings():
    print("=" * 65)
    print("EXPERIMENT 10: RECIPROCATING AIR COMPRESSOR")
    print("=" * 65)

    room_temp_c = get_number(
        "Atmospheric temperature (deg C): ",
        minimum=-273.15,
        strict=True,
    )

    count = get_integer("Number of readings: ", minimum=1)
    results = []

    for i in range(1, count + 1):
        print(f"\nReading {i}")

        pressure = get_number(
            "  Delivery gauge pressure (kgf/cm^2): ",
            minimum=0,
        )
        h1 = get_number("  Orifice manometer h1 (cm): ", minimum=0)
        h2 = get_number("  Orifice manometer h2 (cm): ", minimum=0)

        pulse_time = get_number(
            "  Time for 5 energy-meter pulses (s): ",
            minimum=0,
            strict=True,
        )

        results.append(
            calculate_reading(
                i, room_temp_c, pressure, h1, h2, pulse_time
            )
        )

    return results


def print_results(results):
    print("\nCALCULATED RESULTS")
    print("-" * 112)
    print(
        f"{'No.':>3} {'Pd (kgf/cm²)':>13} {'Ha (m)':>10} "
        f"{'Va (m³/s)':>12} {'VT (m³/s)':>12} "
        f"{'Input (kW)':>12} {'Wiso (kW)':>12} "
        f"{'ηvol (%)':>11} {'ηiso (%)':>11}"
    )
    print("-" * 112)

    for r in results:
        print(
            f"{r['Reading']:>3} "
            f"{r['Delivery pressure (kgf/cm^2)']:>13.4f} "
            f"{r['Air head (m)']:>10.4f} "
            f"{r['Actual volume (m^3/s)']:>12.6f} "
            f"{r['Theoretical volume (m^3/s)']:>12.6f} "
            f"{r['Input power (kW)']:>12.4f} "
            f"{r['Isothermal power (kW)']:>12.4f} "
            f"{r['Volumetric efficiency (%)']:>11.2f} "
            f"{r['Isothermal efficiency (%)']:>11.2f}"
        )

    print("-" * 112)


def save_csv(results):
    path = OUTPUT_DIR / "experiment_10_results.csv"

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"\nCSV saved to: {path}")


def plot_efficiency(results, key, ylabel, filename, title):
    ordered = sorted(
        results,
        key=lambda r: r["Delivery pressure (kgf/cm^2)"],
    )

    pressure = [
        r["Delivery pressure (kgf/cm^2)"] for r in ordered
    ]
    efficiency = [r[key] for r in ordered]

    plt.figure(figsize=(9, 6))
    plt.plot(pressure, efficiency, marker="o", linewidth=1.8)
    plt.xlabel("Delivery gauge pressure (kgf/cm²)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    path = OUTPUT_DIR / filename
    plt.savefig(path, dpi=300)
    plt.show()
    plt.close()

    print(f"Graph saved to: {path}")


def main():
    results = collect_readings()
    print_results(results)
    save_csv(results)

    plot_efficiency(
        results,
        "Volumetric efficiency (%)",
        "Volumetric efficiency (%)",
        "delivery_pressure_vs_volumetric_efficiency.png",
        "Delivery Pressure vs Volumetric Efficiency",
    )

    plot_efficiency(
        results,
        "Isothermal efficiency (%)",
        "Isothermal efficiency (%)",
        "delivery_pressure_vs_isothermal_efficiency.png",
        "Delivery Pressure vs Isothermal Efficiency",
    )

    if any(
        not 0 <= r["Volumetric efficiency (%)"] <= 100
        or not 0 <= r["Isothermal efficiency (%)"] <= 100
        for r in results
    ):
        print(
            "\nWARNING: An efficiency is outside 0-100%. Check the readings, "
            "units and manual's input-power convention."
        )

    print("\nExperiment 10 calculations completed.")


if __name__ == "__main__":
    main()