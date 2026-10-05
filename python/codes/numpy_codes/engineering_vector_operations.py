import numpy as np

print("========== ENGINEERING VECTOR CALCULATIONS ==========")
print()

# Aircraft velocity components
velocity = np.array([100, 50, 20])

print("Velocity vector:", velocity, "m/s")

# Calculate velocity magnitude
velocity_magnitude = np.linalg.norm(velocity)

print("Velocity magnitude:", velocity_magnitude, "m/s")

print()

# Aircraft acceleration components
acceleration = np.array([2, 1, 0.5])

print("Acceleration vector:", acceleration, "m/s^2")

# Calculate acceleration magnitude
acceleration_magnitude = np.linalg.norm(acceleration)

print("Acceleration magnitude:", acceleration_magnitude, "m/s^2")

print()

# Calculate momentum
mass = 1000  # kg

momentum = mass * velocity

print("Aircraft mass:", mass, "kg")
print("Momentum vector:", momentum, "kg·m/s")

print()

# Calculate kinetic energy for each velocity component
kinetic_energy_components = 0.5 * mass * velocity ** 2

print("Kinetic energy components:", kinetic_energy_components, "J")