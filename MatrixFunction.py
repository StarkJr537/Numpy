import numpy as np

# Step 1: Create two random matrices (3x3)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Step 2: Addition
print("\nA + B:\n", A + B)

# Step 3: Subtraction
print("\nA - B:\n", A - B)

# Step 4: Matrix Multiplication (dot product)
print("\nA dot B:\n", np.dot(A, B))

# Step 5: Transpose
print("\nTranspose of A:\n", A.T)

# Step 6: Inverse (only works if matrix is invertible)
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:\n", A_inv)
except np.linalg.LinAlgError:
    print("\nMatrix A is not invertible.")