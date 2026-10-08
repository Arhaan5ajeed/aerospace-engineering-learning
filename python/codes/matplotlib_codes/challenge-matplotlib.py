import numpy as np
import matplotlib.pyplot as plt

print("========== KINETIC ENERGY VS VELOCITY ==========")
print()

# Aircraft mass
mass = 1200  # kg

# Velocity values
velocity = np.array([50, 100, 150, 200, 250, 300])  # m/s

# Calculate kinetic energy
# KE = 0.5 * m * V^2
kinetic_energy = 0.5 * mass * velocity ** 2

# Display calculated values
print("Aircraft Mass:", mass, "kg")
print()
print("Velocity (m/s):")
print(velocity)

print()
print("Kinetic Energy (J):")
print(kinetic_energy)

# Create the plot
plt.figure(figsize=(8, 5))

plt.plot(
    velocity,
    kinetic_energy,
    marker="o",
    label="Kinetic Energy"
)

# Add labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")

# Add title
plt.title("Aircraft Kinetic Energy vs Velocity")

# Add grid
plt.grid()

# Add legend
plt.legend()

# Save the figure
plt.savefig("kinetic_energy_vs_velocity.png", dpi=300)

# Display the figure
plt.show()