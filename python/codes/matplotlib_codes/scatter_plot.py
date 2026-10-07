import numpy as np
import matplotlib.pyplot as plt

# Experimental velocity data
velocity = np.array([50, 80, 110, 140, 170, 200])

# Example measured drag data
drag = np.array([120, 190, 310, 480, 700, 950])

# Create scatter plot
plt.scatter(velocity, drag)

# Labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")

# Title
plt.title("Measured Drag vs Velocity")

# Grid
plt.grid()

# Display
plt.show()