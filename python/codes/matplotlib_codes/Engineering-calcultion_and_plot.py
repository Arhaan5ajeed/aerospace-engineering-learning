import numpy as np
import matplotlib.pyplot as plt

print("========== AIRCRAFT PERFORMANCE PLOT ==========")
print()

# Aircraft parameters
mass = 1000          # kg
rho = 1.225          # kg/m^3

# Velocity range
velocity = np.array([50, 75, 100, 125, 150, 175, 200, 225, 250])

# Kinetic energy
kinetic_energy = 0.5 * mass * velocity ** 2

# Dynamic pressure
dynamic_pressure = 0.5 * rho * velocity ** 2

# Display calculated values
print("Velocity (m/s):")
print(velocity)

print()

print("Kinetic Energy (J):")
print(kinetic_energy)

print()

print("Dynamic Pressure (Pa):")
print(dynamic_pressure)

# Create kinetic energy plot
plt.figure(figsize=(8, 5))

plt.plot(
    velocity,
    kinetic_energy,
    marker="o",
    label="Kinetic Energy"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Aircraft Kinetic Energy vs Velocity")

plt.grid()
plt.legend()

plt.show()

# Create dynamic pressure plot
plt.figure(figsize=(8, 5))

plt.plot(
    velocity,
    dynamic_pressure,
    marker="o",
    label="Dynamic Pressure"
)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Dynamic Pressure (Pa)")
plt.title("Dynamic Pressure vs Velocity")

plt.grid()
plt.legend()

plt.show()