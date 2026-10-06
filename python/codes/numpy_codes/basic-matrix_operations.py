import numpy as np

print("========== NUMPY MATRIX OPERATIONS ==========")
print()

# Create two 2x2 matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print()

print("Matrix B:")
print(B)

print()

# Matrix addition
addition = A + B

print("A + B:")
print(addition)

print()

# Matrix subtraction
subtraction = A - B

print("A - B:")
print(subtraction)

print()

# Scalar multiplication
scalar = 3
scalar_multiplication = scalar * A

print("3A:")
print(scalar_multiplication)

print()

# Element-wise multiplication
elementwise_multiplication = A * B

print("A * B (element-wise multiplication):")
print(elementwise_multiplication)

print()

# Matrix multiplication
matrix_multiplication = A @ B

print("A @ B (matrix multiplication):")
print(matrix_multiplication)

print()

# Transpose
transpose_A = A.T

print("Transpose of A:")
print(transpose_A)