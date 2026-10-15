import numpy as np
import matplotlib.pyplot as plt


def get_positive_float(prompt):
    """Read a positive numerical value from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Value must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(prompt):
    """Read a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("Value must be at least 1.")

        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("=" * 72)
    print("       DETERMINATION OF PIPE FRICTION MAJOR LOSS")
    print("=" * 72)

    # --------------------------------------------------
    # 1. CONSTANTS AND GENERAL APPARATUS INPUTS
    # --------------------------------------------------

    g = 9.81  # Gravitational acceleration (m/s^2)

    print("\n--- APPARATUS DETAILS ---")

    tank_area = get_positive_float(
        "Enter collecting tank area (m^2): "
    )

    rise_input = input(
        "Enter tank water-level rise in cm [default 10]: "
    ).strip()

    if rise_input == "":
        tank_rise_cm = 10.0
    else:
        try:
            tank_rise_cm = float(rise_input)
        except ValueError:
            raise ValueError(
                "Tank water-level rise must be a valid number."
            )

        if tank_rise_cm <= 0:
            raise ValueError(
                "Tank water-level rise must be greater than zero."
            )

    pipe_diameter_mm = get_positive_float(
        "Enter internal pipe diameter (mm): "
    )

    pipe_length = get_positive_float(
        "Enter distance between pressure taps (m): "
    )

    # Relative densities are dimensionless.
    print("\n--- FLUID PROPERTIES ---")

    sm_input = input(
        "Enter manometric-fluid relative density "
        "[default 13.6 for mercury]: "
    ).strip()

    sf_input = input(
        "Enter flowing-fluid relative density "
        "[default 1.0 for water]: "
    ).strip()

    try:
        sm = float(sm_input) if sm_input else 13.6
        sf = float(sf_input) if sf_input else 1.0
    except ValueError:
        raise ValueError("Relative densities must be numerical.")

    if sm <= 0 or sf <= 0:
        raise ValueError("Relative densities must be positive.")

    if sm <= sf:
        raise ValueError(
            "This version assumes a manometric fluid denser "
            "than the flowing fluid. Enter Sm > Sf."
        )

    # --------------------------------------------------
    # 2. UNIT CONVERSIONS AND PIPE GEOMETRY
    # --------------------------------------------------

    tank_rise = tank_rise_cm * 1e-2
    diameter = pipe_diameter_mm * 1e-3

    pipe_area = np.pi * diameter**2 / 4

    # --------------------------------------------------
    # 3. COLLECT EXPERIMENTAL TRIALS
    # --------------------------------------------------

    n = get_positive_integer(
        "\nEnter number of experimental trials: "
    )

    times = []
    h1_readings = []
    h2_readings = []

    print("\n--- EXPERIMENTAL READINGS ---")
    print("Enter manometer readings in cm.")
    print("Enter the time for the specified tank rise in seconds.")

    for i in range(n):
        print(f"\nTRIAL {i + 1}")

        h1 = float(
            input("Enter manometer reading h1 (cm): ")
        )

        h2 = float(
            input("Enter manometer reading h2 (cm): ")
        )

        t = get_positive_float(
            "Enter collection time (s): "
        )

        if h1 < 0 or h2 < 0:
            raise ValueError(
                "Manometer readings must be non-negative."
            )

        h1_readings.append(h1)
        h2_readings.append(h2)
        times.append(t)

    # Convert lists to NumPy arrays.
    times = np.array(times, dtype=float)
    h1_readings = np.array(h1_readings, dtype=float)
    h2_readings = np.array(h2_readings, dtype=float)

    # --------------------------------------------------
    # 4. CALCULATE MANOMETER HEAD AND MAJOR HEAD LOSS
    # --------------------------------------------------

    # Difference in manometer readings, initially in cm.
    hm_cm = np.abs(h1_readings - h2_readings)

    # Convert the difference to metres.
    hm = hm_cm * 1e-2

    # Equivalent head loss in the flowing fluid.
    # Relative densities are used, so their ratio is sufficient.
    hf = hm * (sm / sf - 1)

    # --------------------------------------------------
    # 5. CALCULATE DISCHARGE AND VELOCITY
    # --------------------------------------------------

    # Actual volumetric discharge from the collecting tank.
    Q = (tank_area * tank_rise) / times

    # Mean velocity in a circular pipe flowing full.
    velocity = Q / pipe_area

    # --------------------------------------------------
    # 6. CALCULATE FRICTION FACTORS
    # --------------------------------------------------

    # Darcy-Weisbach equation:
    # hf = f_D * (L / D) * (V^2 / 2g)
    #
    # Rearranging gives the Darcy friction factor.
    darcy_factor = (
        hf * 2 * g * diameter
        / (pipe_length * velocity**2)
    )

    # Manual equation:
    # hf = 4 * f_F * (L / D) * (V^2 / 2g)
    #
    # The manual's factor f is the Fanning friction factor.
    fanning_factor = darcy_factor / 4

    # --------------------------------------------------
    # 7. DISPLAY RESULTS
    # --------------------------------------------------

    print("\n" + "=" * 150)
    print("                    PIPE FRICTION EXPERIMENT RESULTS")
    print("=" * 150)

    print(f"Collecting tank area        : {tank_area:.5f} m^2")
    print(f"Tank water-level rise       : {tank_rise:.5f} m")
    print(f"Pipe internal diameter      : {diameter:.5f} m")
    print(f"Distance between taps       : {pipe_length:.4f} m")
    print(f"Pipe cross-sectional area   : {pipe_area:.8f} m^2")
    print(f"Manometric relative density : {sm:.4f}")
    print(f"Flowing-fluid relative density: {sf:.4f}")
    print()

    header = (
        f"{'Trial':<7}"
        f"{'hm(cm)':<11}"
        f"{'hf(m)':<13}"
        f"{'Time(s)':<12}"
        f"{'Q(m^3/s)':<16}"
        f"{'V(m/s)':<13}"
        f"{'Fanning f':<15}"
        f"{'Darcy f':<13}"
    )

    print(header)
    print("-" * len(header))

    for i in range(n):
        print(
            f"{i + 1:<7}"
            f"{hm_cm[i]:<11.3f}"
            f"{hf[i]:<13.6f}"
            f"{times[i]:<12.3f}"
            f"{Q[i]:<16.8f}"
            f"{velocity[i]:<13.5f}"
            f"{fanning_factor[i]:<15.6f}"
            f"{darcy_factor[i]:<13.6f}"
        )

    print("-" * len(header))

    print("\n--- SUMMARY ---")
    print(f"Mean discharge, Q             : {np.mean(Q):.8f} m^3/s")
    print(f"Mean velocity, V              : {np.mean(velocity):.5f} m/s")
    print(f"Mean major head loss, hf      : {np.mean(hf):.6f} m")
    print(f"Mean Fanning friction factor  : {np.mean(fanning_factor):.6f}")
    print(f"Mean Darcy friction factor    : {np.mean(darcy_factor):.6f}")

    print("\nNote:")
    print("The manual's friction factor is the Fanning factor.")
    print("The Darcy friction factor is four times the Fanning factor.")
    print("Average factors are most meaningful when the same pipe")
    print("and pressure-tap spacing are used for all trials.")

    # --------------------------------------------------
    # 8. PLOT DISCHARGE AGAINST MAJOR HEAD LOSS
    # --------------------------------------------------

    # Sort the data by discharge to make the connecting line orderly.
    order = np.argsort(Q)

    Q_sorted = Q[order]
    hf_sorted = hf[order]

    plt.figure(figsize=(9, 6))

    plt.plot(
        Q_sorted,
        hf_sorted,
        marker="o",
        linestyle="-",
        label="Experimental data"
    )

    plt.xlabel("Discharge, Q (m³/s)")
    plt.ylabel("Major head loss, hf (m)")
    plt.title("Discharge vs Major Head Loss Due to Pipe Friction")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "pipe_friction_major_loss_graph.png",
        dpi=300
    )

    plt.show()


if __name__ == "__main__":
    main()