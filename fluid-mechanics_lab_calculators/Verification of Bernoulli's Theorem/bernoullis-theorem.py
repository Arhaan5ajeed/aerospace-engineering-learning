
import numpy as np
import matplotlib.pyplot as plt

print("=" * 65)
print("       VERIFICATION OF BERNOULLI'S THEOREM")
print("=" * 65)
print()

# --------------------------------------------------
# 1. APPARATUS DATA FROM THE AFDL MANUAL
# --------------------------------------------------

g = 9.81                 # Gravitational acceleration (m/s^2)
tank_length = 0.3        # Collecting tank length (m)
tank_breadth = 0.3       # Collecting tank breadth (m)
tank_rise = 0.10         # Water-level rise (m)
datum_head = 0.0         # Common datum, as specified in manual

tank_area = tank_length * tank_breadth

# Channel heights at locations 1 to 7 (mm), as per manual
channel_heights_mm = np.array([
    35.0, 32.5, 30.0, 25.0, 22.5, 18.5, 14.0
])

# Common channel breadth (mm)
channel_breadth_mm = 20.0

# Convert dimensions from mm to m
channel_heights = channel_heights_mm / 1000
channel_breadth = channel_breadth_mm / 1000

# Cross-sectional area at each channel location (m^2)
section_areas = channel_heights * channel_breadth

# --------------------------------------------------
# 2. INPUT EXPERIMENTAL READINGS
# --------------------------------------------------

print("Enter the seven piezometer pressure-head readings.")
print("Enter readings in cm, as represented by the manual's")
print("tabulation unit of 10^-2 m.")
print()

pressure_readings_cm = []

for i in range(7):
    reading = float(
        input(f"Enter piezometer reading at location {i + 1} (cm): ")
    )

    if reading < 0:
        raise ValueError("Piezometer readings must not be negative.")

    pressure_readings_cm.append(reading)

pressure_readings_cm = np.array(pressure_readings_cm)

time = float(
    input("\nEnter time taken for 10 cm rise in collecting tank (s): ")
)

if time <= 0:
    raise ValueError("Collection time must be greater than zero.")

# Convert piezometer readings from cm to m
pressure_heads = pressure_readings_cm / 100

# --------------------------------------------------
# 3. CALCULATE DISCHARGE
# --------------------------------------------------

# Actual discharge Q = collecting tank area * rise / time
Q = (tank_area * tank_rise) / time

# --------------------------------------------------
# 4. CALCULATE VELOCITY AT EACH LOCATION
# --------------------------------------------------

# Continuity equation: V = Q / a
velocity = Q / section_areas

# --------------------------------------------------
# 5. CALCULATE VELOCITY HEAD
# --------------------------------------------------

# Velocity head = V^2 / (2g)
velocity_head = velocity**2 / (2 * g)

# --------------------------------------------------
# 6. CALCULATE HGL AND TEL
# --------------------------------------------------

# Hydraulic Gradient Line = datum head + pressure head
HGL = datum_head + pressure_heads

# Total Energy Line = datum + pressure head + velocity head
TEL = datum_head + pressure_heads + velocity_head

# --------------------------------------------------
# 7. DISPLAY RESULTS
# --------------------------------------------------

print("\n" + "=" * 105)
print("                 BERNOULLI'S THEOREM CALCULATION TABLE")
print("=" * 105)

print(f"Collecting tank area: {tank_area:.4f} m^2")
print(f"Time for 10 cm rise:  {time:.3f} s")
print(f"Actual discharge Q:   {Q:.8f} m^3/s")

print()
print(
    f"{'Loc.':<6}"
    f"{'Height (mm)':<14}"
    f"{'Area (m^2)':<15}"
    f"{'Velocity (m/s)':<17}"
    f"{'Vel. Head (m)':<16}"
    f"{'Pressure Head (m)':<20}"
    f"{'HGL (m)':<12}"
    f"{'TEL (m)':<12}"
)

print("-" * 105)

for i in range(7):
    print(
        f"{i + 1:<6}"
        f"{channel_heights_mm[i]:<14.2f}"
        f"{section_areas[i]:<15.7f}"
        f"{velocity[i]:<17.4f}"
        f"{velocity_head[i]:<16.5f}"
        f"{pressure_heads[i]:<20.5f}"
        f"{HGL[i]:<12.5f}"
        f"{TEL[i]:<12.5f}"
    )

print("-" * 105)

print("\nMean HGL:", f"{np.mean(HGL):.5f} m")
print("Mean TEL:", f"{np.mean(TEL):.5f} m")
print("TEL variation:", f"{np.ptp(TEL):.5f} m")

# --------------------------------------------------
# 8. PLOT HGL AND TEL
# --------------------------------------------------

locations = np.arange(1, 8)

plt.figure(figsize=(9, 6))

plt.plot(
    locations,
    HGL,
    marker="o",
    linestyle="-",
    label="Hydraulic Gradient Line (HGL)"
)

plt.plot(
    locations,
    TEL,
    marker="s",
    linestyle="-",
    label="Total Energy Line (TEL)"
)

plt.xticks(locations)
plt.xlabel("Channel Location (1–7)")
plt.ylabel("Head (m)")
plt.title("Verification of Bernoulli's Theorem")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bernoulli_theorem_verification.png", dpi=300)
plt.show()
