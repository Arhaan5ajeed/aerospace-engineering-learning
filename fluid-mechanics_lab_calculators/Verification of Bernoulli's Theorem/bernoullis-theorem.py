
import numpy as np
import matplotlib.pyplot as plt

print("=" * 65)
print("       GENERAL BERNOULLI'S THEOREM VERIFICATION")
print("=" * 65)
print()

# --------------------------------------------------
# 1. CONSTANTS AND GENERAL INPUTS
# --------------------------------------------------

g = 9.81                 # Gravitational acceleration (m/s^2)
datum_head = 0.0         # Assumed datum elevation (m)

tank_area = float(input("Enter measuring tank area (m^2): "))

# Generalise the tank rise; default is the manual's 10 cm
rise_input = input("Enter tank water-level rise (cm) [default 10]: ")
tank_rise_cm = float(rise_input) if rise_input.strip() else 10.0

# Distance between adjacent measurement sections
spacing_cm = float(
    input("Enter distance between adjacent tubes (cm): ")
)

# Collection time
time = float(
    input("Enter time for the tank water-level rise (s): ")
)

# Number of measurement sections
n = int(input("Enter the number of measurement tubes/sections: "))

# --------------------------------------------------
# 2. VALIDATE GENERAL INPUTS
# --------------------------------------------------

if tank_area <= 0:
    raise ValueError("Measuring tank area must be greater than zero.")

if tank_rise_cm <= 0:
    raise ValueError("Tank water-level rise must be greater than zero.")

if spacing_cm <= 0:
    raise ValueError("Distance between sections must be greater than zero.")

if time <= 0:
    raise ValueError("Time must be greater than zero.")

if n < 1:
    raise ValueError("Number of sections must be at least 1.")

tank_rise = tank_rise_cm / 100
spacing = spacing_cm / 100

# --------------------------------------------------
# 3. INPUT SECTION DIMENSIONS AND PIEZOMETER READINGS
# --------------------------------------------------

heights_mm = []
breadths_mm = []
pressure_readings_cm = []

print("\nEnter dimensions and piezometer readings for each section.")
print("Dimensions h and b are entered in mm.")
print("Piezometer pressure-head readings are entered in cm.")
print()

for i in range(n):
    print(f"---------- SECTION {i + 1} ----------")

    h = float(input(f"Enter section height h{i + 1} (mm): "))
    b = float(input(f"Enter section breadth b{i + 1} (mm): "))
    pressure = float(
        input(f"Enter piezometer reading at section {i + 1} (cm): ")
    )

    if h <= 0 or b <= 0:
        raise ValueError("Section height and breadth must be positive.")

    if pressure < 0:
        raise ValueError("Piezometer readings must not be negative.")

    heights_mm.append(h)
    breadths_mm.append(b)
    pressure_readings_cm.append(pressure)

# Convert input lists to NumPy arrays
heights_mm = np.array(heights_mm, dtype=float)
breadths_mm = np.array(breadths_mm, dtype=float)
pressure_readings_cm = np.array(pressure_readings_cm, dtype=float)

# --------------------------------------------------
# 4. CONVERT UNITS AND CALCULATE CROSS-SECTIONAL AREAS
# --------------------------------------------------

# Dimensions entered in mm: multiply by 10^-3 to convert to m
heights = heights_mm * 1e-3
breadths = breadths_mm * 1e-3

# Rectangular flow passage area at each section
areas = heights * breadths

# Piezometer readings entered in cm: multiply by 10^-2 to convert to m
pressure_heads = pressure_readings_cm * 1e-2

# --------------------------------------------------
# 5. CALCULATE DISCHARGE
# --------------------------------------------------

# Actual volumetric discharge from the measuring tank
Q = (tank_area * tank_rise) / time

# --------------------------------------------------
# 6. CALCULATE VELOCITY AND VELOCITY HEAD
# --------------------------------------------------

# Continuity equation: Q = A * V
velocity = Q / areas

# Velocity head = V^2 / (2g)
velocity_head = velocity**2 / (2 * g)

# --------------------------------------------------
# 7. CALCULATE HGL AND TOTAL ENERGY HEAD
# --------------------------------------------------

# Common datum elevation is assumed to be zero
# HGL = datum elevation + pressure head
HGL = datum_head + pressure_heads

# TEL = datum elevation + pressure head + velocity head
TEL = datum_head + pressure_heads + velocity_head

# --------------------------------------------------
# 8. DISPLAY RESULTS
# --------------------------------------------------

print("\n" + "=" * 120)
print("             BERNOULLI'S THEOREM — RESULTS")
print("=" * 120)

print(f"Measuring tank area       : {tank_area:.5f} m^2")
print(f"Tank water-level rise     : {tank_rise:.5f} m")
print(f"Collection time           : {time:.3f} s")
print(f"Calculated discharge      : {Q:.8f} m^3/s")
print(f"Assumed datum elevation   : {datum_head:.3f} m")
print()

print(
    f"{'Tube':<7}"
    f"{'Distance(m)':<14}"
    f"{'Area(m^2)':<15}"
    f"{'Pressure(m)':<15}"
    f"{'Velocity(m/s)':<16}"
    f"{'Vel.Head(m)':<15}"
    f"{'HGL(m)':<13}"
    f"{'TEL(m)':<13}"
)

print("-" * 108)

# Location 1 is taken as x = 0
distance = np.arange(n) * spacing

for i in range(n):
    print(
        f"{i + 1:<7}"
        f"{distance[i]:<14.4f}"
        f"{areas[i]:<15.7f}"
        f"{pressure_heads[i]:<15.5f}"
        f"{velocity[i]:<16.5f}"
        f"{velocity_head[i]:<15.5f}"
        f"{HGL[i]:<13.5f}"
        f"{TEL[i]:<13.5f}"
    )

print("-" * 108)

print(f"\nMean pressure head : {np.mean(pressure_heads):.5f} m")
print(f"Mean velocity head : {np.mean(velocity_head):.5f} m")
print(f"Mean HGL           : {np.mean(HGL):.5f} m")
print(f"Mean TEL           : {np.mean(TEL):.5f} m")
print(f"TEL variation      : {np.ptp(TEL):.5f} m")

# --------------------------------------------------
# 9. PLOT HGL AND TEL AGAINST DISTANCE
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    distance,
    HGL,
    marker="o",
    linestyle="-",
    label="Hydraulic Gradient Line (HGL)"
)

plt.plot(
    distance,
    TEL,
    marker="s",
    linestyle="-",
    label="Total Energy Line (TEL)"
)

plt.xlabel("Distance Along Flow Passage (m)")
plt.ylabel("Head (m)")
plt.title("Verification of Bernoulli's Theorem")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bernoulli_theorem_verification.png", dpi=300)
plt.show()
