import numpy as np
import matplotlib.pyplot as plt

print("========== AIRCRAFT MOTION SIMULATION ==========")

# Initial conditions
initial_position = 0.0       # m
initial_velocity = 0.0       # m/s
acceleration = 5.0           # m/s^2

# Time from 0 to 10 seconds, with 101 data points
time = np.linspace(0, 10, 101)

# Equations of motion for constant acceleration
position = (
    initial_position
    + initial_velocity * time
    + 0.5 * acceleration * time**2
)

velocity = initial_velocity + acceleration * time

# Position vs time
plt.figure(figsize=(8, 5))
plt.plot(time, position, label="Position", marker=".", markevery=10)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Velocity vs time
plt.figure(figsize=(8, 5))
plt.plot(time, velocity, label="Velocity", marker=".", markevery=10)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Display final values
print("Final time:", time[-1], "s")
print("Final position:", position[-1], "m")
print("Final velocity:", velocity[-1], "m/s")