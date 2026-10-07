import matplotlib.pyplot as plt

# Data
velocity = [50, 100, 150, 200, 250]
distance = [100, 200, 300, 400, 500]

# Create plot
plt.plot(velocity, distance)

# Add labels
plt.xlabel("Velocity (m/s)")
plt.ylabel("Distance (m)")

# Add title
plt.title("Distance vs Velocity")

# Display grid
plt.grid()

# Display plot
plt.show()