import matplotlib.pyplot as plt

# Aircraft names
aircraft = ["Tejas", "Rafale", "Su-30MKI", "Mirage 2000"]

# Example maximum speeds in Mach
max_speed = [1.6, 1.8, 2.0, 2.2]

# Create bar chart
plt.bar(aircraft, max_speed)

# Labels
plt.xlabel("Aircraft")
plt.ylabel("Maximum Speed (Mach)")

# Title
plt.title("Maximum Speed Comparison")

# Grid
plt.grid(axis="y")

# Display
plt.show()