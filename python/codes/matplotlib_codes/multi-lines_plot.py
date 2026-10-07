import numpy as np
import matplotlib.pyplot as plt

# Velocity data
velocity = np.array([50, 100, 150, 200, 250])

# Aircraft masses
mass_1 = 1000
mass_2 = 1500

# Calculate kinetic energy
kinetic_energy_1 = 0.5 * mass_1 * velocity ** 2
kinetic_energy_2 = 0.5 * mass_2 * velocity ** 2

# Plot both datasets
plt.plot(velocity, kinetic_energy_1, label="Mass = 1000 kg")
plt.plot(velocity, kinetic_energy_2, label="Mass = 1500 kg")

# Labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

# Title
plt.title("Kinetic Energy for Different Aircraft Masses")

# Grid
plt.grid()

# Legend
plt.legend()

# Display
plt.show()