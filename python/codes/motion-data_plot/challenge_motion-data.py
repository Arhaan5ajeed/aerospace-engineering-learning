
import numpy as np
import matplotlib.pyplot as plt

print("========== MOTION DATA CHALLENGE ==========")
print()

# Initial conditions
initial_position = 10.0  # metres
initial_velocity = 5.0   # m/s
acceleration = 2.0       # m/s^2

# Generate time data from 0 to 8 seconds
time = np.linspace(0, 8, 81)

# Calculate position and velocity
position = (
    initial_position
    + initial_velocity * time
    + 0.5 * acceleration * time**2
)

velocity = initial_velocity + acceleration * time

# Display the final results
print(f"Initial Position: {initial_position:.2f} m")
print(f"Initial Velocity: {initial_velocity:.2f} m/s")
print(f"Acceleration: {acceleration:.2f} m/s^2")
print(f"Final Time: {time[-1]:.2f} s")
print(f"Final Position: {position[-1]:.2f} m")
print(f"Final Velocity: {velocity[-1]:.2f} m/s")

# Plot 1: Position vs Time
plt.figure(figsize=(8, 5))
plt.plot(
    time,
    position,
    marker=".",
    markevery=10,
    label="Position"
)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Velocity vs Time
plt.figure(figsize=(8, 5))
plt.plot(
    time,
    velocity,
    marker=".",
    markevery=10,
    label="Velocity"
)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()