
import numpy as np
import matplotlib.pyplot as plt

print("========== VENTURIMETER DISCHARGE CALCULATOR ==========")
print()

# --------------------------------------------------
# 1. INPUT: VENTURIMETER AND COLLECTING TANK
# --------------------------------------------------

d1_mm = float(input("Enter inlet diameter d1 (mm): "))
d2_mm = float(input("Enter throat diameter d2 (mm): "))
tank_area = float(input("Enter collecting tank area A (m^2): "))

# Relative densities: mercury = 13.6, water = 1.0
rho1 = float(input("Enter manometer fluid relative density [13.6]: ") or 13.6)
rho2 = float(input("Enter flowing fluid relative density [1.0]: ") or 1.0)

g = 9.81  # m/s^2
rise = 0.10  # 10 cm rise in collecting tank, in metres

# --------------------------------------------------
# 2. VALIDATE INPUTS AND CONVERT UNITS
# --------------------------------------------------

if d1_mm <= 0 or d2_mm <= 0:
    raise ValueError("Diameters must be greater than zero.")

if d2_mm >= d1_mm:
    raise ValueError("Throat diameter d2 must be smaller than inlet diameter d1.")

if tank_area <= 0:
    raise ValueError("Collecting tank area must be greater than zero.")

if rho1 <= rho2 or rho2 <= 0:
    raise ValueError(
        "For this formula, manometer fluid density must exceed "
        "flowing fluid density, and both must be positive."
    )

d1 = d1_mm / 1000  # Convert mm to m
d2 = d2_mm / 1000  # Convert mm to m

# Cross-sectional areas
A1 = np.pi * d1**2 / 4
A2 = np.pi * d2**2 / 4

# --------------------------------------------------
# 3. INPUT EXPERIMENTAL READINGS
# --------------------------------------------------

n = int(input("\nEnter the number of experimental trials: "))

if n <= 0:
    raise ValueError("Number of trials must be greater than zero.")

hm_values = []
H_values = []
Qa_values = []
Qt_values = []
Cd_values = []

for i in range(n):
    print(f"\n---------- TRIAL {i + 1} ----------")

    h1 = float(input("Enter manometer reading h1 (cm): "))
    h2 = float(input("Enter manometer reading h2 (cm): "))
    time = float(input("Enter time for 10 cm tank rise (s): "))

    if time <= 0:
        raise ValueError("Time must be greater than zero.")

    # Differential manometer reading
    hm_cm = abs(h1 - h2)

    # Convert differential head from cm to m
    hm_m = hm_cm / 100

    # Manometer head in metres of flowing fluid
    H = hm_m * (rho1 / rho2 - 1)

    # Actual discharge (m^3/s)
    Qa = (tank_area * rise) / time

    # Theoretical discharge (m^3/s)
    Qt = A2 * np.sqrt(
        (2 * g * H) / (1 - (A2 / A1)**2)
    )

    # Coefficient of discharge
    if Qt == 0:
        Cd = float("nan")
    else:
        Cd = Qa / Qt

    hm_values.append(hm_cm)
    H_values.append(H)
    Qa_values.append(Qa)
    Qt_values.append(Qt)
    Cd_values.append(Cd)

    # Display trial results
    print("\nRESULTS")
    print(f"Differential reading, hm = {hm_cm:.2f} cm")
    print(f"Manometer head, H = {H:.6f} m")
    print(f"Actual discharge, Qa = {Qa:.8f} m^3/s")
    print(f"Theoretical discharge, Qt = {Qt:.8f} m^3/s")
    print(f"Coefficient of discharge, Cd = {Cd:.4f}")

# --------------------------------------------------
# 4. SUMMARY OF ALL TRIALS
# --------------------------------------------------

print("\n========== EXPERIMENTAL SUMMARY ==========")
print(
    f"{'Trial':<8}{'hm (cm)':<12}{'H (m)':<14}"
    f"{'Qa (m^3/s)':<18}{'Qt (m^3/s)':<18}{'Cd':<10}"
)

for i in range(n):
    print(
        f"{i + 1:<8}"
        f"{hm_values[i]:<12.2f}"
        f"{H_values[i]:<14.6f}"
        f"{Qa_values[i]:<18.8f}"
        f"{Qt_values[i]:<18.8f}"
        f"{Cd_values[i]:<10.4f}"
    )

# --------------------------------------------------
# 5. PLOT: THEORETICAL DISCHARGE VS ACTUAL DISCHARGE
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    Qa_values,
    Qt_values,
    label="Experimental trials"
)

plt.xlabel("Actual Discharge, Qa (m^3/s)")
plt.ylabel("Theoretical Discharge, Qt (m^3/s)")
plt.title("Theoretical Discharge vs Actual Discharge")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("venturimeter_discharge_graph.png", dpi=300)
plt.show()
