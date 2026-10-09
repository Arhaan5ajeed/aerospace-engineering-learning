import numpy as np
import matplotlib.pyplot as plt

print("========== MOTION DATA VISUALISATION ==========")

# Time data in seconds
time = np.array([0, 1, 2, 3, 4, 5, 6])

# Velocity data in m/s
velocity = np.array([0, 5, 10, 15, 20, 25, 30])

# Position data in metres
position = np.array([0, 2.5, 10, 22.5, 40, 62.5, 90])

# Plot velocity against time
plt.figure(figsize=(8, 5))
plt.plot(time, velocity, marker="o", label="Velocity")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot position against time
plt.figure(figsize=(8, 5))
plt.plot(time, position, marker="o", label="Position")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()