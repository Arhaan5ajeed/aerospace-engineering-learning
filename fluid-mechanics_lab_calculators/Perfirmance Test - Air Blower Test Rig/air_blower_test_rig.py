"""
Experiment 8: Performance Test on Air Blower Test Rig
AFDL - Applied Fluid Dynamics Laboratory

Enter readings for radial, forward-curved, and/or backward-curved impellers.
Manometer readings are entered in cm; time for 5 energy-meter pulses is in seconds.
"""

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt


# Apparatus constants from the laboratory manual
D1 = 0.070              # Pipe diameter (m)
D2 = 0.0504             # Orifice diameter (m)
CD = 0.62               # Coefficient of discharge
RHO_WATER = 1000.0      # Water density (kg/m^3)
RHO_AIR = 1.225         # Air density (kg/m^3)
ENERGY_METER_C = 1600.0 # Energy-meter constant (pulses/kWh)
MOTOR_EFFICIENCY = 0.775
G = 9.81                # Acceleration due to gravity (m/s^2)

OUTPUT_DIR = Path("experiment_8_results")
OUTPUT_DIR.mkdir(exist_ok=True)


def get_number(prompt, minimum=None, strict=False):
    """Read and validate a finite numerical input."""
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

            condition = "greater than" if strict else "at least"
            print(f"Enter a finite number {condition} {minimum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_integer(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a whole number of at least {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_manometer_difference(label):
    """Read both manometer levels in cm; return their difference in metres."""
    print(f"  {label} manometer readings:")
    h1 = get_number("    h1 (cm): ", minimum=0)
    h2 = get_number("    h2 (cm): ", minimum=0)
    return abs(h1 - h2) / 100.0


def calculate_reading(impeller, reading_no, h1, h2, h3, time_for_pulses):
    """
    h1, h2 and h3 are the delivery, suction and orifice
    manometer level differences, respectively, in metres.
    """
    density_ratio = RHO_WATER / RHO_AIR - 1.0

    delivery_head = h1 * density_ratio
    suction_head = h2 * density_ratio
    orifice_head = h3 * density_ratio

    area_1 = math.pi * D1**2 / 4.0
    area_2 = math.pi * D2**2 / 4.0

    discharge = (
        CD * area_1 * area_2 * math.sqrt(2 * G * orifice_head)
        / math.sqrt(area_1**2 - area_2**2)
    )

    # Input-power formula reproduced as printed in the lab manual.
    input_power = (
        (5.0 / time_for_pulses)
        * (3600.0 / ENERGY_METER_C)
        * MOTOR_EFFICIENCY
    )

    output_power = RHO_AIR * G * discharge * delivery_head / 1000.0

    efficiency = output_power / input_power * 100.0

    return {
        "Impeller": impeller,
        "Reading": reading_no,
        "Delivery head (m)": delivery_head,
        "Suction head (m)": suction_head,
        "Orifice head (m)": orifice_head,
        "Discharge (m^3/s)": discharge,
        "Input power (kW)": input_power,
        "Output power (kW)": output_power,
        "Efficiency (%)": efficiency,
        "Time for 5 pulses (s)": time_for_pulses,
    }


def collect_impeller_data(impeller):
    print("\n" + "=" * 60)
    print(f"IMPELLER: {impeller.upper()}")
    print("=" * 60)

    count = get_integer(
        "Number of readings (enter 0 to skip this impeller): ",
        minimum=0,
    )

    results = []

    for i in range(1, count + 1):
        print(f"\nReading {i}")

        delivery_difference = read_manometer_difference("Delivery")
        suction_difference = read_manometer_difference("Suction")
        orifice_difference = read_manometer_difference("Orifice")

        time_for_pulses = get_number(
            "  Time for 5 energy-meter pulses (s): ",
            minimum=0,
            strict=True,
        )

        results.append(
            calculate_reading(
                impeller,
                i,
                delivery_difference,
                suction_difference,
                orifice_difference,
                time_for_pulses,
            )
        )

    return results


def save_csv(results):
    path = OUTPUT_DIR / "experiment_8_results.csv"

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"\nCalculated data saved to: {path}")


def print_results(results):
    print("\nCALCULATED RESULTS")
    print("-" * 115)
    print(
        f"{'Impeller':<17}{'No.':>4}{'Hd (m)':>11}{'Hs (m)':>11}"
        f"{'Ho (m)':>11}{'Q (m^3/s)':>14}{'Input (kW)':>12}"
        f"{'Output (kW)':>13}{'Eff. (%)':>11}"
    )
    print("-" * 115)

    for r in results:
        print(
            f"{r['Impeller']:<17}{r['Reading']:>4}"
            f"{r['Delivery head (m)']:>11.4f}"
            f"{r['Suction head (m)']:>11.4f}"
            f"{r['Orifice head (m)']:>11.4f}"
            f"{r['Discharge (m^3/s)']:>14.6f}"
            f"{r['Input power (kW)']:>12.4f}"
            f"{r['Output power (kW)']:>13.4f}"
            f"{r['Efficiency (%)']:>11.2f}"
        )

    print("-" * 115)


def plot_metric(results, key, ylabel, filename, title):
    """Plot a performance variable against discharge for each impeller."""
    import matplotlib.pyplot as plt

    plt.figure(figsize=(9, 6))

    impellers = sorted({r["Impeller"] for r in results})

    for impeller in impellers:
        subset = sorted(
            [r for r in results if r["Impeller"] == impeller],
            key=lambda r: r["Discharge (m^3/s)"],
        )

        x = [r["Discharge (m^3/s)"] for r in subset]
        y = [r[key] for r in subset]

        plt.plot(x, y, marker="o", linewidth=1.8, label=impeller.title())

    plt.xlabel("Discharge, Q (m³/s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    path = OUTPUT_DIR / filename
    plt.savefig(path, dpi=300)
    plt.show()
    plt.close()

    print(f"Graph saved to: {path}")


def main():
    print("=" * 60)
    print("EXPERIMENT 8: PERFORMANCE TEST ON AIR BLOWER")
    print("=" * 60)
    print("Enter the two levels for each manometer in centimetres.")
    print("Only enter readings for impellers tested in your lab.")

    all_results = []

    for impeller in ("radial", "forward-curved", "backward-curved"):
        all_results.extend(collect_impeller_data(impeller))

    if not all_results:
        print("\nNo readings entered. Nothing to calculate.")
        return

    print_results(all_results)
    save_csv(all_results)

    plot_metric(
        all_results,
        "Efficiency (%)",
        "Blower efficiency (%)",
        "efficiency_vs_discharge.png",
        "Blower Efficiency vs Discharge",
    )

    plot_metric(
        all_results,
        "Input power (kW)",
        "Input power (kW)",
        "input_power_vs_discharge.png",
        "Input Power vs Discharge",
    )

    plot_metric(
        all_results,
        "Output power (kW)",
        "Output power (kW)",
        "output_power_vs_discharge.png",
        "Output Power vs Discharge",
    )

    if any(
        r["Efficiency (%)"] > 100 or r["Efficiency (%)"] < 0
        for r in all_results
    ):
        print(
            "\nWARNING: An efficiency lies outside 0-100%. Check the readings "
            "and confirm the input-power formula with your instructor. "
            "The formula above follows the manual as printed."
        )

    print("\nExperiment 8 calculations completed.")


if __name__ == "__main__":
    main()