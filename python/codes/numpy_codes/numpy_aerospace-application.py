import numpy as np

print("========== WORK DONE USING DOT PRODUCT ==========")
print()

# Force vector in Newtons
force = np.array([100, 50, 20])

# Displacement vector in metres
displacement = np.array([10, 5, 2])

print("Force:", force, "N")
print("Displacement:", displacement, "m")

print()

# Work = F . s
work = np.dot(force, displacement)

print("Work Done:", work, "J")

print("========== VECTOR PROJECTION ==========")
print()

# Vector A
A = np.array([6, 8])

# Reference vector
B = np.array([1, 0])

print("Vector A:", A)
print("Reference vector B:", B)

print()

# Projection of A onto B
projection_scalar = np.dot(A, B) / np.linalg.norm(B)

projection_vector = projection_scalar * (B / np.linalg.norm(B))

print("Scalar Projection:", projection_scalar)
print("Vector Projection:", projection_vector)