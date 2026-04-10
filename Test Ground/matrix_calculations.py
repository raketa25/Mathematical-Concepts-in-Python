import numpy as np

# Function to multiply two matrices

def mat_multiply(A, B):
    """
    Multiplies two matrices A and B.

    Parameters:
    A (list of list of floats): First matrix.
    B (list of list of floats): Second matrix.

    Returns:
    list of list of floats: Resultant matrix after multiplication.
    """
    # return np.dot(A, B).tolist()
    nligsA, ncolsA = len(A), len(A[0])             # Dimensions of A
    nligsB, ncolsB = len(B), len(B[0])             # Dimensions of B
    res = [[0] * ncolsB for i in range(nligsA)]    # Initialize result matrix with zeros

    for i in range(0, nligsA):
        for j in range(0, ncolsB):
            res[i][j] = 0
            for k in range(0, ncolsA):
                res[i][j] += A[i][k] * B[k][j]
    return res

# Example usage
A = [
    [15.2, 41, 51],
    [7.2, 0, 43],
    [10.2, 44, 63],
    [8.2, 0, 12],
    [5.2, 54, 43]
]

B = [[480.0], [100.0], [30.0]]

result = mat_multiply(A, B)
# print(f"The result of multiplying matrix A with matrix B is: {result}")

# Using numpy for verification
np_result = np.array(A).dot(np.array([row[0] for row in B]))
print(f"The result using numpy is: {np_result}")

