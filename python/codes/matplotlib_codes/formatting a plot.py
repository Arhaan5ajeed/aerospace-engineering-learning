import numpy as np
import matplotlib.pyplot as plt

velocity = np.array([50, 100, 150, 200, 250])
mass = 1000

kinetic_energy = 0.5 * mass * velocity ** 2

# Create figure
plt.figure(figsize=(8, 5))

# Plot
plt.plot(
    velocity,
    kinetic_energy,
    marker="o",
    linestyle="-",
    label="Kinetic Energy"
)

# Labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

# Title
plt.title("Aircraft Kinetic Energy")

# Grid
plt.grid()

# Legend
plt.legend()

# Display
plt.show()