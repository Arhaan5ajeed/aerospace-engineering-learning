import numpy as np

print("========== 2D ROTATION MATRIX ==========")
print()

# Angle of rotation
angle_degrees = 90

# Convert degrees to radians
angle_radians = np.deg2rad(angle_degrees)

# 2D rotation matrix
rotation_matrix = np.array([
    [np.cos(angle_radians), -np.sin(angle_radians)],
    [np.sin(angle_radians),  np.cos(angle_radians)]
])

# Original vector
vector = np.array([1, 0])

# Rotate the vector
rotated_vector = rotation_matrix @ vector

print("Rotation angle:", angle_degrees, "degrees")

print()

print("Rotation Matrix:")
print(rotation_matrix)

print()

print("Original Vector:")
print(vector)

print()

print("Rotated Vector:")
print(rotated_vector)