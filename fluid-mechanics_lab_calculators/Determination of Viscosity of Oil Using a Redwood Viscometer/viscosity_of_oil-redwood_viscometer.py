"""
Experiment 9: Determination of Viscosity of Oil
Using a Redwood Viscometer

AFDL - Applied Fluid Dynamics Laboratory
"""

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt


COLLECTED_VOLUME_M3 = 50e-6  # 50 mL in m^3
OUTPUT_DIR = Path("experiment_9_results")
OUTPUT_DIR.mkdir(exist_ok=True)


def get_number(prompt, minimum=None, strict=False):
    """Read a finite numerical value and validate its range."""
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Enter a finite numerical value.")
                continue

            if minimum is not None:
                valid = value > minimum if strict else value >= minimum
                if not valid:
                    operator = "greater than" if strict else "at least"
                    print(f"Value must be {operator} {minimum}.")
                    continue

            return value

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


def get_redwood_constants(flow_time):
    """
    Return the Redwood viscometer constants C and beta
    specified in the laboratory manual.
    """
    if 40 <= flow_time <= 85:
        return 0.264, 190.0
    elif 85 < flow_time <= 2000:
        return 0.247, 65.0
    else:
        raise ValueError(
            "The manual's formula is specified for flow times "
            "from 40 to 2000 seconds. Check the experiment reading."
        )


def calculate_properties(temperature, flow_time, empty_mass, filled_mass):
    """Calculate density, kinematic viscosity and dynamic viscosity."""

    if filled_mass <= empty_mass:
        raise ValueError(
            "Mass of flask plus oil must exceed the empty flask mass."
        )

    oil_mass = filled_mass - empty_mass

    # Density = mass of oil / volume of oil
    density = oil_mass / COLLECTED_VOLUME_M3

    # Redwood formula constants depend on flow time
    C, beta = get_redwood_constants(flow_time)

    # Kinematic viscosity in m^2/s
    kinematic_viscosity = (
        C * flow_time - beta / flow_time
    ) * 1e-6

    if kinematic_viscosity <= 0:
        raise ValueError(
            "Calculated kinematic viscosity is not positive. "
            "Check the time and measurements."
        )

    # Dynamic viscosity in Pa.s (equivalent to N.s/m^2)
    dynamic_viscosity = kinematic_viscosity * density

    return {
        "Temperature (deg C)": temperature,
        "Flow time (s)": flow_time,
        "Empty flask mass (kg)": empty_mass,
        "Flask plus oil mass (kg)": filled_mass,
        "Oil mass (kg)": oil_mass,
        "Density (kg/m^3)": density,
        "Redwood constant C": C,
        "Redwood constant beta": beta,
        "Kinematic viscosity (m^2/s)": kinematic_viscosity,
        "Dynamic viscosity (Pa.s)": dynamic_viscosity,
    }


def save_results(results):
    path = OUTPUT_DIR / "redwood_viscometer_results.csv"

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {path}")


def print_results(results):
    print("\nCALCULATED RESULTS")
    print("-" * 110)
    print(
        f"{'Temp (C)':>10}{'Time (s)':>11}{'Density':>14}"
        f"{'Kinematic nu':>22}{'Dynamic mu':>22}"
    )
    print(
        f"{'':>35}{'(kg/m^3)':>14}"
        f"{'(m^2/s)':>22}{'(Pa.s)':>22}"
    )
    print("-" * 110)

    for row in results:
        print(
            f"{row['Temperature (deg C)']:>10.2f}"
            f"{row['Flow time (s)']:>11.2f}"
            f"{row['Density (kg/m^3)']:>14.3f}"
            f"{row['Kinematic viscosity (m^2/s)']:>22.6e}"
            f"{row['Dynamic viscosity (Pa.s)']:>22.6e}"
        )

    print("-" * 110)


def plot_property(results, property_key, ylabel, filename, title):
    """Plot a viscosity property against oil temperature."""
    ordered = sorted(results, key=lambda row: row["Temperature (deg C)"])

    temperatures = [r["Temperature (deg C)"] for r in ordered]
    values = [r[property_key] for r in ordered]

    plt.figure(figsize=(8, 6))
    plt.plot(temperatures, values, marker="o", linewidth=1.8)
    plt.xlabel("Oil temperature (°C)")
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
    print("=" * 65)
    print("EXPERIMENT 9: REDWOOD VISCOMETER")
    print("Determination of Kinematic and Dynamic Viscosity of Oil")
    print("=" * 65)

    oil_type = input("Enter the type/name of oil: ").strip()
    if not oil_type:
        oil_type = "Unspecified oil"

    room_temperature = get_number(
        "Enter room temperature (deg C): "
    )

    empty_mass = get_number(
        "Enter mass of empty measuring flask (kg): ",
        minimum=0,
    )

    count = get_integer(
        "Enter number of temperature readings: ",
        minimum=1,
    )

    results = []

    for i in range(1, count + 1):
        print(f"\nReading {i}")

        temperature = get_number(
            "  Oil temperature (deg C): "
        )

        flow_time = get_number(
            "  Time to collect 50 mL of oil (s): ",
            minimum=0,
            strict=True,
        )

        filled_mass = get_number(
            "  Mass of flask + 50 mL oil (kg): ",
            minimum=0,
        )

        try:
            result = calculate_properties(
                temperature,
                flow_time,
                empty_mass,
                filled_mass,
            )
            results.append(result)

        except ValueError as error:
            print(f"Reading not included: {error}")
            print("Recheck this reading and enter it again if needed.")

    if not results:
        print("\nNo valid readings were recorded. Exiting.")
        return

    print(f"\nOil type: {oil_type}")
    print(f"Room temperature: {room_temperature:.2f} °C")

    print_results(results)
    save_results(results)

    plot_property(
        results,
        "Kinematic viscosity (m^2/s)",
        "Kinematic viscosity, ν (m²/s)",
        "kinematic_viscosity_vs_temperature.png",
        "Kinematic Viscosity vs Temperature",
    )

    plot_property(
        results,
        "Dynamic viscosity (Pa.s)",
        "Dynamic viscosity, μ (Pa·s)",
        "dynamic_viscosity_vs_temperature.png",
        "Dynamic Viscosity vs Temperature",
    )

    print("\nExperiment 9 calculations completed.")


if __name__ == "__main__":
    main()