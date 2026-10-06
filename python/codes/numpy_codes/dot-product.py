import numpy as np

print("========== NUMPY DOT PRODUCT ==========")
print()

# Define two vectors
A = np.array([2, 3, 4])
B = np.array([5, 6, 7])

print("Vector A:", A)
print("Vector B:", B)

print()

# Calculate dot product
dot_product = np.dot(A, B)

print("Dot Product:", dot_product)

print("========== DOT PRODUCT USING @ ==========")
print()

A = np.array([2, 3, 4])
B = np.array([5, 6, 7])

dot_product = A @ B

print("Vector A:", A)
print("Vector B:", B)

print()

print("Dot Product:", dot_product)