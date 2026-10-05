import numpy as np

print("========== DYNAMIC PRESSURE CALCULATOR ==========")
print()

# Air density
rho = 1.225  # kg/m^3

# Multiple aircraft velocities
velocity = np.array([50, 100, 150, 200, 250])

# Dynamic pressure equation:
# q = 0.5 * rho * V^2

dynamic_pressure = 0.5 * rho * velocity ** 2

print("Air density:", rho, "kg/m^3")
print("Velocity:", velocity, "m/s")
print()

print("Dynamic Pressure:", dynamic_pressure, "Pa")