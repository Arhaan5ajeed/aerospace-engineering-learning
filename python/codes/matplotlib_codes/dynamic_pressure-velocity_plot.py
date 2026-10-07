import numpy as np
import matplotlib.pyplot as plt

# Air density
rho = 1.225  # kg/m^3

# Velocity range
velocity = np.array([50, 100, 150, 200, 250])

# Dynamic pressure
dynamic_pressure = 0.5 * rho * velocity ** 2

# Plot
plt.plot(velocity, dynamic_pressure)

# Labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Dynamic Pressure (Pa)")

# Title
plt.title("Dynamic Pressure vs Velocity")

# Grid
plt.grid()

# Display
plt.show()