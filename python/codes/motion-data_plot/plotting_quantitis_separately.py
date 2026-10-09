import numpy as np
import matplotlib.pyplot as plt

# Time in seconds
time = np.array([0, 1, 2, 3, 4, 5, 6])

# Motion data
position = np.array([0, 2.5, 10, 22.5, 40, 62.5, 90])
velocity = np.array([0, 5, 10, 15, 20, 25, 30])

# Example constant acceleration
acceleration = np.array([5, 5, 5, 5, 5, 5, 5])

# Position vs time
plt.figure(figsize=(8, 5))
plt.plot(time, position, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Velocity vs time
plt.figure(figsize=(8, 5))
plt.plot(time, velocity, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Acceleration vs time
plt.figure(figsize=(8, 5))
plt.plot(time, acceleration, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()