
import numpy as np
import matplotlib.pyplot as plt


def positive_float(prompt):
    """Read a positive floating-point value."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def positive_integer(prompt):
    """Read a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter an integer of at least 1.")
        except ValueError:
            print("Please enter a valid whole number.")


def choose_fitting():
    """Choose a fitting covered by the laboratory manual."""
    fittings = {
        "1": "Elbow",
        "2": "Bend",
        "3": "Sudden enlargement",
        "4": "Sudden contraction",
    }

    print("\nSelect the pipe fitting:")
    for number, name in fittings.items():
        print(f"{number}. {name}")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in fittings:
            return fittings[choice]
        print("Invalid choice. Enter a number from 1 to 4.")


def main():
    print("=" * 72)
    print("       DETERMINATION OF MINOR LOSSES DUE TO PIPE FITTINGS")
    print("=" * 72)

    # --------------------------------------------------
    # 1. GENERAL APPARATUS INPUTS
    # --------------------------------------------------

    g = 9.81  # Gravitational acceleration (m/s^2)

    print("\n--- COLLECTING TANK DETAILS ---")

    tank_area = positive_float(
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
            raise ValueError("Tank rise must be a valid number.")

        if tank_rise_cm <= 0:
            raise ValueError("Tank rise must be greater than zero.")

    tank_rise = tank_rise_cm / 100

    print("\n--- FLUID PROPERTIES ---")

    sm_input = input(
        "Manometric-fluid relative density [default 13.6]: "
    ).strip()

    sf_input = input(
        "Flowing-fluid relative density [default 1.0]: "
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
            "This program assumes the manometric liquid is denser "
            "than the flowing fluid. Enter Sm > Sf."
        )

    # --------------------------------------------------
    # 2. NUMBER OF EXPERIMENTAL TRIALS
    # --------------------------------------------------

    n = positive_integer(
        "\nEnter number of experimental observations: "
    )

    results = []

    print("\nFor each observation, enter the fitting, pipe diameters,")
    print("manometer readings, and collection time.")
    print("All diameters are internal diameters.")
    print("For enlargement: d1 = smaller upstream diameter,")
    print("                 d2 = larger downstream diameter.")
    print("For contraction: d1 = larger upstream diameter,")
    print("                 d2 = smaller downstream diameter.")
    print("For an elbow or bend, enter the same diameter for d1 and d2.")

    # --------------------------------------------------
    # 3. INPUT AND CALCULATE EACH OBSERVATION
    # --------------------------------------------------

    for i in range(n):
        print(f"\n{'-' * 24} OBSERVATION {i + 1} {'-' * 24}")

        fitting = choose_fitting()

        d1_mm = positive_float(
            "Enter upstream pipe diameter d1 (mm): "
        )

        d2_mm = positive_float(
            "Enter downstream pipe diameter d2 (mm): "
        )

        if fitting in ("Elbow", "Bend"):
            if not np.isclose(d1_mm, d2_mm):
                raise ValueError(
                    "For an elbow or bend, enter the same diameter "
                    "for d1 and d2."
                )

        elif fitting == "Sudden enlargement":
            if d2_mm <= d1_mm:
                raise ValueError(
                    "For sudden enlargement, d2 must be greater than d1."
                )

        elif fitting == "Sudden contraction":
            if d2_mm >= d1_mm:
                raise ValueError(
                    "For sudden contraction, d2 must be less than d1."
                )

        h1 = float(input("Enter manometer reading h1 (cm): "))
        h2 = float(input("Enter manometer reading h2 (cm): "))

        if h1 < 0 or h2 < 0:
            raise ValueError("Manometer readings must be non-negative.")

        time = positive_float(
            "Enter time for the specified tank rise (s): "
        )

        # Convert diameters from mm to m.
        d1 = d1_mm * 1e-3
        d2 = d2_mm * 1e-3

        # Cross-sectional areas.
        area1 = np.pi * d1**2 / 4
        area2 = np.pi * d2**2 / 4

        # Differential manometer reading.
        hm_cm = abs(h1 - h2)
        hm = hm_cm / 100

        # Actual head loss in the flowing fluid.
        hf = hm * (sm / sf - 1)

        # Actual volumetric discharge from collecting tank.
        Q = (tank_area * tank_rise) / time

        # Velocities upstream and downstream.
        V1 = Q / area1
        V2 = Q / area2

        # Theoretical/reference velocity head loss.
        if fitting in ("Elbow", "Bend"):
            # Manual formula for elbow and bend.
            hv = V1**2 / (2 * g)

            # Reference velocity head for conventional K.
            reference_velocity_head = V1**2 / (2 * g)

        elif fitting == "Sudden enlargement":
            # Manual formula: (V1 - V2)^2 / (2g).
            hv = (V1 - V2)**2 / (2 * g)

            # Conventional local-loss coefficient uses upstream
            # velocity head as its reference.
            reference_velocity_head = V1**2 / (2 * g)

        else:
            # Sudden contraction: manual uses velocity in the
            # smaller pipe, which is the downstream pipe here.
            hv = 0.5 * V2**2 / (2 * g)

            # Conventional local-loss coefficient uses downstream
            # smaller-pipe velocity head as the reference.
            reference_velocity_head = V2**2 / (2 * g)

        # Standard loss coefficient:
        # K = actual measured head loss / reference velocity head.
        K_standard = hf / reference_velocity_head

        # Additional comparison with the manual's printed ratio.
        # This is NOT the conventional loss-coefficient definition.
        manual_ratio = hv / hf if hf > 0 else np.nan

        # Ratio of actual loss to the manual's theoretical hv.
        actual_to_theoretical = hf / hv if hv > 0 else np.nan

        results.append({
            "fitting": fitting,
            "d1_mm": d1_mm,
            "d2_mm": d2_mm,
            "hm_cm": hm_cm,
            "hf": hf,
            "time": time,
            "Q": Q,
            "V1": V1,
            "V2": V2,
            "hv": hv,
            "K_standard": K_standard,
            "manual_ratio": manual_ratio,
            "actual_to_theoretical": actual_to_theoretical,
        })

    # --------------------------------------------------
    # 4. DISPLAY RESULTS
    # --------------------------------------------------

    print("\n" + "=" * 156)
    print("                    MINOR LOSSES — EXPERIMENTAL RESULTS")
    print("=" * 156)

    print(
        f"{'No.':<5}"
        f"{'Fitting':<23}"
        f"{'hm(cm)':<10}"
        f"{'hf(m)':<13}"
        f"{'Time(s)':<11}"
        f"{'Q(m^3/s)':<15}"
        f"{'V1(m/s)':<12}"
        f"{'V2(m/s)':<12}"
        f"{'hv(m)':<13}"
        f"{'K standard':<14}"
        f"{'hv/hf manual':<15}"
    )

    print("-" * 156)

    for i, r in enumerate(results, start=1):
        print(
            f"{i:<5}"
            f"{r['fitting']:<23}"
            f"{r['hm_cm']:<10.3f}"
            f"{r['hf']:<13.6f}"
            f"{r['time']:<11.3f}"
            f"{r['Q']:<15.8f}"
            f"{r['V1']:<12.5f}"
            f"{r['V2']:<12.5f}"
            f"{r['hv']:<13.6f}"
            f"{r['K_standard']:<14.5f}"
            f"{r['manual_ratio']:<15.5f}"
        )

    print("-" * 156)

    print("\n--- DEFINITIONS AND NOTES ---")
    print("Q             : Actual volumetric discharge (m^3/s)")
    print("V1, V2        : Upstream and downstream mean velocities (m/s)")
    print("hf            : Actual head loss from the manometer (m)")
    print("hv            : Theoretical/reference head loss from the manual (m)")
    print("K standard    : Actual head loss / reference velocity head")
    print("hv/hf manual  : Ratio printed in the manual; shown for comparison")

    # --------------------------------------------------
    # 5. PLOT DISCHARGE AGAINST ACTUAL HEAD LOSS
    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    fitting_names = list(dict.fromkeys(
        r["fitting"] for r in results
    ))

    for fitting in fitting_names:
        selected = [
            r for r in results if r["fitting"] == fitting
        ]

        Q_values = np.array([r["Q"] for r in selected])
        hf_values = np.array([r["hf"] for r in selected])

        order = np.argsort(Q_values)

        plt.plot(
            Q_values[order],
            hf_values[order],
            marker="o",
            linestyle="-",
            label=fitting
        )

    plt.xlabel("Discharge, Q (m³/s)")
    plt.ylabel("Actual Minor Head Loss, hf (m)")
    plt.title("Discharge vs Minor Head Loss for Pipe Fittings")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "minor_losses_pipe_fittings_graph.png",
        dpi=300
    )

    plt.show()


if __name__ == "__main__":
    main()
