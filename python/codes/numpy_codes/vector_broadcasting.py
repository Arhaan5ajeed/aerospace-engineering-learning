import numpy as np

print("========== NUMPY BROADCASTING ==========")
print()

# Velocities of an aircraft at different conditions
velocity = np.array([50, 100, 150, 200])

print("Velocity:", velocity)

# One scalar is applied to every element
time = 2

distance = velocity * time

print("Time:", time, "s")
print("Distance:", distance, "m")

print()

# Add the same value to every element
temperature_change = 5

new_temperature = velocity + temperature_change

print("Temperature change:", temperature_change)
print("Result after broadcasting:", new_temperature)

print()

# Multiply every element by the same factor
scale_factor = 1.5

scaled_velocity = velocity * scale_factor

print("Scale factor:", scale_factor)
print("Scaled velocity:", scaled_velocity)