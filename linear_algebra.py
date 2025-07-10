import numpy as np

# Addition of vectors
def vector_add(a, b):
    sum_vector = a + b
    print(f"Sum of vectors a and b: {sum_vector}")

# Subtraction of vectors
def vector_diff(a, b):
    diff_vector = a - b
    print(f"Difference of vectors a and b: {diff_vector}")

# Dot product of vectors
def vector_dot_product(a, b):
    dot_product = np.dot(a, b)
    print(f"Dot product of vectors a and b: {dot_product}")

# Addition of matrices
def matrix_sum(A, B):
    sum_matrix = A + B
    print(f"Sum of matrices A and B: {sum_matrix}")

# Subtraction of matrices
def matrix_diff(A, B):
    diff_matrix = A - B
    print(f"Difference of matrices A and B: {diff_matrix}")

# Scalar multiplication of vectors
def scalar_mult_vector(c, a):
    scalar_mult_vector = c * a
    print(f"Scalar multiplication of vector a by {c}: {scalar_mult_vector}")

# Scalar multiplication of matrices
def scalar_mult(c, A):
    scalar_mult_matrix = c * A
    print(f"Scalar multiplication of matrix A by {c}: {scalar_mult_matrix}")

# Matrix multiplication
def multiply_matrices(A, B):
    product_matrix = np.dot(A, B)
    print(f"Product of matrices A and B: {product_matrix}")

# Transpose of a matrix
def find_transpose(A):
    transpose_matrix = A.T
    print(f"Transpose of matrix A: {transpose_matrix}")

# Magnitude of a matrix
def find_magnitude (a):
    magnitude = np.linalg.norm(a)
    print(f"Magnitude of vector a: {magnitude}")

# Create vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
f = np.array([1, 1, 2])

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

vector_add(a, b)
vector_diff(a, b)

matrix_sum(A, B)
matrix_diff(A, B)

vector_dot_product(a, b)

multiply_matrices(C, D)

find_magnitude(f)

find_transpose(A)