import numpy as np
import matplotlib.pyplot as plt

# Create velocity array
velocity = np.array([50, 100, 150, 200, 250])

# Aircraft mass
mass = 1000

# Calculate kinetic energy
kinetic_energy = 0.5 * mass * velocity ** 2

# Plot
plt.plot(velocity, kinetic_energy)

# Labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

# Title
plt.title("Kinetic Energy vs Velocity")

# Grid
plt.grid()

# Display
plt.show()