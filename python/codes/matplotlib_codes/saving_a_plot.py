import numpy as np
import matplotlib.pyplot as plt

velocity = np.array([50, 100, 150, 200, 250])

rho = 1.225

dynamic_pressure = 0.5 * rho * velocity ** 2

plt.plot(velocity, dynamic_pressure)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Dynamic Pressure (Pa)")
plt.title("Dynamic Pressure vs Velocity")

plt.grid()

# Save the figure
plt.savefig("dynamic_pressure_vs_velocity.png", dpi=300)

# Display the figure
plt.show()