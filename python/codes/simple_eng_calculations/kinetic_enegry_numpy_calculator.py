import numpy as np

print("========== NUMPY KINETIC ENERGY CALCULATOR ==========")
print()

# Get aircraft mass
mass = float(input("Enter aircraft mass in kg: "))

# Get multiple velocities
velocity_input = input(
    "Enter velocities in m/s separated by spaces: "
)

# Convert user input into a NumPy array
velocity = np.array([float(v) for v in velocity_input.split()])

# Calculate kinetic energy using vectorisation
kinetic_energy = 0.5 * mass * velocity ** 2

# Display results
print()
print("Velocity values:", velocity)
print("Kinetic Energy:", kinetic_energy, "J")