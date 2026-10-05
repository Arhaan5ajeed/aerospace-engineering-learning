import numpy as np

print("========== NUMPY VECTOR OPERATIONS ==========")
print()

# Create two velocity vectors
velocity_a = np.array([50, 100, 150])
velocity_b = np.array([10, 20, 30])

print("Velocity A:", velocity_a)
print("Velocity B:", velocity_b)

print()

# Vector addition
velocity_sum = velocity_a + velocity_b
print("Vector Addition:", velocity_sum)

# Vector subtraction
velocity_difference = velocity_a - velocity_b
print("Vector Subtraction:", velocity_difference)

# Scalar multiplication
scaled_velocity = velocity_a * 2
print("Scalar Multiplication:", scaled_velocity)

# Element-wise multiplication
elementwise_product = velocity_a * velocity_b
print("Element-wise Multiplication:", elementwise_product)

# Element-wise division
elementwise_division = velocity_a / velocity_b
print("Element-wise Division:", elementwise_division)

# Squaring every element
squared_velocity = velocity_a ** 2
print("Squared Velocity:", squared_velocity)

# Square root of every element
sqrt_velocity = np.sqrt(velocity_a)
print("Square Root:", sqrt_velocity)

print()

# Basic statistics
print("Maximum value:", np.max(velocity_a))
print("Minimum value:", np.min(velocity_a))
print("Average value:", np.mean(velocity_a))
print("Sum:", np.sum(velocity_a))