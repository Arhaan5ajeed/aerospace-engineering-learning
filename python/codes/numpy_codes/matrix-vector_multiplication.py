import numpy as np

print("========== MATRIX-VECTOR MULTIPLICATION ==========")
print()

# Define a matrix
A = np.array([
    [2, 1],
    [1, 3]
])

# Define a vector
x = np.array([10, 20])

print("Matrix A:")
print(A)

print()

print("Vector x:")
print(x)

print()

# Matrix-vector multiplication
result = A @ x

print("A @ x:")
print(result)