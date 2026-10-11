
import numpy as np
import matplotlib.pyplot as plt

print("========== ORIFICEMETER DISCHARGE CALCULATOR ==========")
print()

# --------------------------------------------------
# 1. INPUT: PIPE, ORIFICE AND COLLECTING TANK
# --------------------------------------------------

d1_mm = float(input("Enter pipe internal diameter d1 (mm): "))
do_mm = float(input("Enter orifice diameter do (mm): "))
tank_area = float(input("Enter collecting tank area (m^2): "))

# Relative densities
rho1 = float(
    input("Enter manometer fluid relative density [13.6]: ") or 13.6
)
rho2 = float(
    input("Enter flowing fluid relative density [1.0]: ") or 1.0
)

g = 9.81  # m/s^2
rise = 0.10  # 10 cm rise in collecting tank, in metres

# --------------------------------------------------
# 2. VALIDATE INPUTS AND CONVERT UNITS
# --------------------------------------------------

if d1_mm <= 0 or do_mm <= 0:
    raise ValueError("Diameters must be greater than zero.")

if do_mm >= d1_mm:
    raise ValueError(
        "Orifice diameter must be smaller than pipe diameter."
    )

if tank_area <= 0:
    raise ValueError("Collecting tank area must be greater than zero.")

if rho1 <= rho2 or rho2 <= 0:
    raise ValueError(
        "For this formula, the manometer fluid must be denser "
        "than the flowing fluid, and both densities must be positive."
    )

d1 = d1_mm / 1000  # mm to m
do = do_mm / 1000  # mm to m

# Cross-sectional areas
A1 = np.pi * d1**2 / 4
Ao = np.pi * do**2 / 4

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

    # Convert cm to m
    hm_m = hm_cm / 100

    # Equivalent head in metres of flowing fluid
    H = hm_m * (rho1 / rho2 - 1)

    # Actual discharge (m^3/s)
    Qa = (tank_area * rise) / time

    # Theoretical discharge (m^3/s)
    Qt = Ao * np.sqrt(
        (2 * g * H) / (1 - (Ao / A1)**2)
    )

    # Coefficient of discharge
    Cd = Qa / Qt if Qt > 0 else float("nan")

    hm_values.append(hm_cm)
    H_values.append(H)
    Qa_values.append(Qa)
    Qt_values.append(Qt)
    Cd_values.append(Cd)

    print("\nRESULTS")
    print(f"Differential reading, hm = {hm_cm:.2f} cm")
    print(f"Manometer head, H = {H:.6f} m")
    print(f"Actual discharge, Qa = {Qa:.8f} m^3/s")
    print(f"Theoretical discharge, Qt = {Qt:.8f} m^3/s")
    print(f"Coefficient of discharge, Cd = {Cd:.4f}")

# --------------------------------------------------
# 4. DISPLAY SUMMARY
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
# 5. PLOT Qt AGAINST Qa
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(Qa_values, Qt_values, label="Experimental trials")

plt.xlabel("Actual Discharge, Qa (m^3/s)")
plt.ylabel("Theoretical Discharge, Qt (m^3/s)")
plt.title("Theoretical Discharge vs Actual Discharge - Orificemeter")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("orificemeter_discharge_graph.png", dpi=300)
plt.show()
