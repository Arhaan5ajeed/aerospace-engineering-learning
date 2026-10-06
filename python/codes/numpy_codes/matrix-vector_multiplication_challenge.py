import numpy as np

print("========== MATRIX-VECTOR MULTIPLICATION CHALLENGE ==========")
print()

# Create matrix A
A = np.array([
    [2, 4],
    [1, 3]
])

# Create vector x
x = np.array([10, 20])

# Perform matrix-vector multiplication
result = A @ x

# Display the inputs
print("Matrix A:")
print(A)

print()

print("Vector x:")
print(x)

print()

# Display the result
print("A @ x:")
print(result)