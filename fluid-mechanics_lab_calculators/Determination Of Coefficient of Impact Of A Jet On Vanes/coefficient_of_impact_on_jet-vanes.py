
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# INPUT VALIDATION FUNCTIONS
# ============================================================

def positive_float(prompt):
    """Read a positive floating-point number."""
    while True:
        try:
            value = float(input(prompt))

            if np.isfinite(value) and value > 0:
                return value

            print("Value must be a finite number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def positive_integer(prompt):
    """Read a positive integer."""
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Enter an integer greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_dimension(prompt, default):
    """Read a positive dimension, using a default if Enter is pressed."""
    while True:
        try:
            raw_value = input(
                f"{prompt} [default {default}]: "
            ).strip()

            value = float(raw_value) if raw_value else default

            if np.isfinite(value) and value > 0:
                return value

            print("Value must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def choose_vane():
    """Allow the user to select the vane type."""
    print("\nSelect the vane type:")
    print("1. Flat vane")
    print("2. Conical vane")

    while True:
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            return "Flat vane"

        if choice == "2":
            return "Conical vane"

        print("Invalid choice. Please enter 1 or 2.")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 72)
    print("       DETERMINATION OF COEFFICIENT OF IMPACT OF A JET")
    print("=" * 72)

    # --------------------------------------------------------
    # 1. CONSTANTS
    # --------------------------------------------------------

    g = 9.81                  # Gravitational acceleration (m/s^2)
    rho = 1000.0              # Density of water (kg/m^3)
    pressure_conversion = 98066.5  # kgf/cm^2 to Pa

    # --------------------------------------------------------
    # 2. APPARATUS DIMENSIONS
    # --------------------------------------------------------

    print("\n--- APPARATUS DIMENSIONS ---")

    tank_length = read_dimension(
        "Collecting tank length (m)", 0.5
    )

    tank_breadth = read_dimension(
        "Collecting tank breadth (m)", 0.3
    )

    tank_rise_cm = read_dimension(
        "Water-level rise in tank (cm)", 10.0
    )

    nozzle_diameter_mm = read_dimension(
        "Nozzle diameter (mm)", 10.0
    )

    L1_cm = read_dimension(
        "Fulcrum-to-weight arm L1 (cm)", 38.0
    )

    L2_cm = read_dimension(
        "Fulcrum-to-jet arm L2 (cm)", 7.5
    )

    # Convert dimensions to SI units
    tank_area = tank_length * tank_breadth
    tank_rise_m = tank_rise_cm / 100.0
    nozzle_diameter_m = nozzle_diameter_mm / 1000.0

    L1 = L1_cm / 100.0
    L2 = L2_cm / 100.0

    nozzle_area = np.pi * nozzle_diameter_m**2 / 4.0

    # --------------------------------------------------------
    # 3. NUMBER OF OBSERVATIONS
    # --------------------------------------------------------

    print("\n--- EXPERIMENTAL OBSERVATIONS ---")

    number_of_observations = positive_integer(
        "Enter the number of observations: "
    )

    results = []

    print("\nFor every observation, enter:")
    print("- Vane type")
    print("- Weight placed in the pan (grams)")
    print("- Pressure gauge reading (kgf/cm^2)")
    print("- Time for the specified tank rise (seconds)")

    # --------------------------------------------------------
    # 4. COLLECT DATA AND PERFORM CALCULATIONS
    # --------------------------------------------------------

    for i in range(number_of_observations):

        print("\n" + "-" * 24)
        print(f"OBSERVATION {i + 1}")
        print("-" * 24)

        vane = choose_vane()

        weight_g = positive_float(
            "Weight placed in pan (g): "
        )

        pressure_kgf_cm2 = positive_float(
            "Pressure gauge reading (kgf/cm^2): "
        )

        time_s = positive_float(
            f"Time for {tank_rise_cm:g} cm tank rise (s): "
        )

        # Convert input values to SI units
        weight_kg = weight_g / 1000.0

        pressure_pa = (
            pressure_kgf_cm2 * pressure_conversion
        )

        # Actual discharge from the collecting tank
        Q = (tank_area * tank_rise_m) / time_s

        # Pressure head
        pressure_head = pressure_pa / (rho * g)

        # Jet velocity using the manual's Bernoulli relation
        jet_velocity = np.sqrt(2.0 * g * pressure_head)

        # Theoretical force as specified in the AFDL manual
        theoretical_force = (
            rho * nozzle_area * jet_velocity**2
        )

        # Actual force from the balancing weight and lever arms
        actual_force = (
            weight_kg * (L1 / L2) * g
        )

        # Coefficient of impact
        coefficient = actual_force / theoretical_force

        # Store calculated values
        results.append({
            "vane": vane,
            "weight_g": weight_g,
            "pressure": pressure_kgf_cm2,
            "time": time_s,
            "Q": Q,
            "head": pressure_head,
            "velocity": jet_velocity,
            "actual_force": actual_force,
            "theoretical_force": theoretical_force,
            "coefficient": coefficient
        })

    # --------------------------------------------------------
    # 5. DISPLAY RESULTS
    # --------------------------------------------------------

    print("\n" + "=" * 145)
    print("              COEFFICIENT OF IMPACT - EXPERIMENTAL RESULTS")
    print("=" * 145)

    print(
        f"{'No.':<5}"
        f"{'Vane':<16}"
        f"{'Weight(g)':<12}"
        f"{'Pressure':<13}"
        f"{'Time(s)':<11}"
        f"{'Q (m^3/s)':<15}"
        f"{'V (m/s)':<12}"
        f"{'Fa (N)':<13}"
        f"{'Ft (N)':<13}"
        f"{'Ci':<10}"
    )

    print("-" * 145)

    for i, r in enumerate(results, start=1):

        print(
            f"{i:<5}"
            f"{r['vane']:<16}"
            f"{r['weight_g']:<12.2f}"
            f"{r['pressure']:<13.4f}"
            f"{r['time']:<11.3f}"
            f"{r['Q']:<15.8e}"
            f"{r['velocity']:<12.4f}"
            f"{r['actual_force']:<13.4f}"
            f"{r['theoretical_force']:<13.4f}"
            f"{r['coefficient']:<10.4f}"
        )

    print("-" * 145)

    # --------------------------------------------------------
    # 6. CALCULATION SUMMARY
    # --------------------------------------------------------

    print("\n--- CALCULATION SUMMARY ---")

    print(f"Collecting tank area : {tank_area:.4f} m^2")
    print(f"Tank water rise      : {tank_rise_m:.4f} m")
    print(f"Nozzle area          : {nozzle_area:.8e} m^2")
    print(f"L1                   : {L1_cm:.2f} cm")
    print(f"L2                   : {L2_cm:.2f} cm")

    print("\nEquations used:")
    print("Q  = Tank area x tank rise / time")
    print("H  = Pressure / (water density x g)")
    print("V  = sqrt(2 x g x H)")
    print("Ft = Water density x nozzle area x V^2")
    print("Fa = Weight (kg) x (L1 / L2) x g")
    print("Ci = Fa / Ft")

    # --------------------------------------------------------
    # 7. GRAPH: ACTUAL FORCE VS THEORETICAL FORCE
    # --------------------------------------------------------

    vane_types = list(dict.fromkeys(
        r["vane"] for r in results
    ))

    plt.figure(figsize=(8, 6))

    for vane in vane_types:

        selected = [
            r for r in results if r["vane"] == vane
        ]

        theoretical_values = [
            r["theoretical_force"] for r in selected
        ]

        actual_values = [
            r["actual_force"] for r in selected
        ]

        plt.scatter(
            theoretical_values,
            actual_values,
            label=vane,
            s=60
        )

    plt.xlabel("Theoretical Force, Ft (N)")
    plt.ylabel("Actual Force, Fa (N)")
    plt.title("Actual Force vs Theoretical Force")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "impact_force_comparison.png",
        dpi=300
    )

    plt.show()

    # --------------------------------------------------------
    # 8. GRAPH: COEFFICIENT OF IMPACT VS DISCHARGE
    # --------------------------------------------------------

    plt.figure(figsize=(8, 6))

    for vane in vane_types:

        selected = sorted(
            [r for r in results if r["vane"] == vane],
            key=lambda r: r["Q"]
        )

        discharge_values = [
            r["Q"] for r in selected
        ]

        coefficient_values = [
            r["coefficient"] for r in selected
        ]

        plt.plot(
            discharge_values,
            coefficient_values,
            marker="o",
            label=vane
        )

    plt.xlabel("Actual Discharge, Q (m^3/s)")
    plt.ylabel("Coefficient of Impact, Ci")
    plt.title("Coefficient of Impact vs Discharge")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "coefficient_of_impact_vs_discharge.png",
        dpi=300
    )

    plt.show()

    print("\nExperiment calculations completed successfully.")
    print("Both graphs have been saved in the current working directory.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
