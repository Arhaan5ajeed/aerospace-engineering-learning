
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# INPUT VALIDATION
# ============================================================

def positive_float(prompt, default=None):
    """Read a finite positive number, optionally using a default."""
    while True:
        try:
            raw = input(
                f"{prompt} [default {default}]: "
                if default is not None
                else f"{prompt}: "
            ).strip()

            value = float(raw) if raw else default

            if value is not None and np.isfinite(value) and value > 0:
                return value

            print("Enter a finite number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a numerical value.")


def positive_integer(prompt):
    """Read a positive whole number."""
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Enter an integer greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def classify_flow(reynolds_number):
    """Classify pipe flow using approximate Reynolds-number limits."""
    if reynolds_number < 2000:
        return "Laminar"
    elif reynolds_number <= 4000:
        return "Transitional"
    else:
        return "Turbulent"


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 76)
    print("       EXPERIMENT 7: FLOW VISUALIZATION - REYNOLDS APPARATUS")
    print("=" * 76)

    # 1. CONSTANTS AND APPARATUS PARAMETERS
    print("\n--- APPARATUS PARAMETERS ---")

    collection_volume_litres = positive_float(
        "Volume of water collected (litres)", 1.0
    )

    pipe_diameter_mm = positive_float(
        "Internal pipe diameter (mm)", 20.0
    )

    kinematic_viscosity = positive_float(
        "Kinematic viscosity of fluid (m^2/s)", 1.01e-6
    )

    # Convert to SI units
    collection_volume = collection_volume_litres / 1000.0
    pipe_diameter = pipe_diameter_mm / 1000.0
    pipe_area = np.pi * pipe_diameter**2 / 4.0

    # 2. EXPERIMENTAL OBSERVATIONS
    print("\n--- EXPERIMENTAL OBSERVATIONS ---")

    number_of_observations = positive_integer(
        "Enter the number of observations: "
    )

    results = []

    print(
        "\nFor each observation, enter the time taken to collect "
        f"{collection_volume_litres:g} litre(s) of water."
    )

    for i in range(number_of_observations):
        print(f"\n--- Observation {i + 1} ---")

        time_s = positive_float("Collection time (seconds)")

        # Discharge: Q = collected volume / time
        discharge = collection_volume / time_s

        # Mean pipe velocity: V = Q / A
        velocity = discharge / pipe_area

        # Reynolds number: Re = V*D/nu
        reynolds_number = (
            velocity * pipe_diameter / kinematic_viscosity
        )

        flow_regime = classify_flow(reynolds_number)

        results.append({
            "observation": i + 1,
            "time": time_s,
            "discharge": discharge,
            "velocity": velocity,
            "reynolds": reynolds_number,
            "regime": flow_regime
        })

    # 3. DISPLAY RESULTS
    print("\n" + "=" * 104)
    print("                    REYNOLDS APPARATUS RESULTS")
    print("=" * 104)

    print(
        f"{'No.':<6}"
        f"{'Time (s)':<13}"
        f"{'Q (m^3/s)':<17}"
        f"{'Velocity (m/s)':<19}"
        f"{'Reynolds No.':<19}"
        f"{'Flow regime':<18}"
    )

    print("-" * 104)

    for r in results:
        print(
            f"{r['observation']:<6}"
            f"{r['time']:<13.3f}"
            f"{r['discharge']:<17.6e}"
            f"{r['velocity']:<19.5f}"
            f"{r['reynolds']:<19.2f}"
            f"{r['regime']:<18}"
        )

    print("-" * 104)

    # 4. EXPERIMENT SUMMARY
    print("\n--- CALCULATION SUMMARY ---")
    print(f"Collection volume      : {collection_volume:.6f} m^3")
    print(f"Pipe diameter          : {pipe_diameter:.5f} m")
    print(f"Pipe cross-sectional area: {pipe_area:.6e} m^2")
    print(f"Kinematic viscosity    : {kinematic_viscosity:.4e} m^2/s")

    print("\nEquations used:")
    print("Q  = Collected volume / Collection time")
    print("A  = pi * D^2 / 4")
    print("V  = Q / A")
    print("Re = V * D / nu")

    # 5. GRAPH: REYNOLDS NUMBER VS DISCHARGE
    sorted_results = sorted(results, key=lambda r: r["discharge"])

    discharges = [r["discharge"] for r in sorted_results]
    reynolds_values = [r["reynolds"] for r in sorted_results]

    plt.figure(figsize=(9, 6))
    plt.plot(
        discharges,
        reynolds_values,
        marker="o",
        label="Calculated Reynolds number"
    )

    plt.axhline(
        2000,
        linestyle="--",
        label="Approximate laminar limit (Re = 2000)"
    )
    plt.axhline(
        4000,
        linestyle="--",
        label="Approximate turbulent limit (Re = 4000)"
    )

    plt.xlabel("Discharge, Q (m^3/s)")
    plt.ylabel("Reynolds Number, Re")
    plt.title("Reynolds Number vs Discharge")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("reynolds_number_vs_discharge.png", dpi=300)
    plt.show()

    # 6. GRAPH: VELOCITY VS REYNOLDS NUMBER
    velocities = [r["velocity"] for r in sorted_results]

    plt.figure(figsize=(9, 6))
    plt.plot(
        reynolds_values,
        velocities,
        marker="o",
        label="Calculated mean velocity"
    )

    plt.xlabel("Reynolds Number, Re")
    plt.ylabel("Mean Velocity, V (m/s)")
    plt.title("Mean Velocity vs Reynolds Number")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("velocity_vs_reynolds_number.png", dpi=300)
    plt.show()

    print("\nCalculations completed successfully.")
    print("Saved graph: reynolds_number_vs_discharge.png")
    print("Saved graph: velocity_vs_reynolds_number.png")
    print(
        "\nImportant: use the dye filament's observed behaviour "
        "to record the experimental flow pattern separately."
    )


if __name__ == "__main__":
    main()
