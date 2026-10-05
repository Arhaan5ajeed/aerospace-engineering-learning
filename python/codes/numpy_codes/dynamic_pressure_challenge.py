import numpy as np

print("========== DYNAMIC PRESSURE CHALLENGE ==========")
print()

# Get air density from the user
rho = float(input("Enter air density in kg/m^3: "))

# Get multiple velocities from the user
velocity_input = input("Enter velocities in m/s separated by spaces: ")

# Convert the input into a NumPy array
velocity = np.array([float(value) for value in velocity_input.split()])

# Calculate dynamic pressure
# q = 0.5 * rho * V^2
dynamic_pressure = 0.5 * rho * velocity ** 2

# Display results
print()
print("Velocity:", velocity, "m/s")
print("Dynamic Pressure:", dynamic_pressure, "Pa")

print()

# Find maximum and minimum dynamic pressure
maximum_pressure = np.max(dynamic_pressure)
minimum_pressure = np.min(dynamic_pressure)

print("Maximum Dynamic Pressure:", maximum_pressure, "Pa")
print("Minimum Dynamic Pressure:", minimum_pressure, "Pa")