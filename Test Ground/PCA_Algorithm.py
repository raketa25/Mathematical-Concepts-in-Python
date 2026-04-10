# ============= Scientific implementations =================
'''
Here is the implementation of the PCA (Principal Component Analysis) algorithm in Python.
The variance plays a major role in PCA as it helps to identify the directions (principal components) along which the data varies the most.
By projecting the data onto these principal components, PCA reduces the dimensionality of the dataset while retaining most of the variance(with higher values).
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import multivariate_normal

plt.style.use('grayscale')
plt.gca().set_aspect('equal', adjustable='box')

# PCA Function
def PCA(X):

    # Step 1: Means calcuation for each dimension(feature)
    means = np.matrix([np.mean(X[:, col]) for col in range(0, X.shape[1])])

    # Step 2: Centering the data around the mean
    X_centered = X - np.ones((X.shape[0], 1)) * means

    # Step 3: Covariance matrix calculation
    covariance_matrix = 1 / (X.shape[0] - 1) * X_centered.T * X_centered

    # Step 4: Eigen decomposition of the covariance matrix
    ei_vals, ei_vecs = np.linalg.eig(covariance_matrix)

    # Step 5: Sorting eigenvalues and corresponding eigenvectors
    sorted_indices = np.argsort(ei_vals)[::-1] # Indices for sorting in descending order
    ei_vals = ei_vals[sorted_indices]         # Sorted eigenvalues
    ei_vecs = ei_vecs[:, sorted_indices]      # Sorted eigenvectors

    return covariance_matrix, ei_vals, ei_vecs, means

# Example usage
data = np.matrix(multivariate_normal([7, 8], [[5, 1], [1, 1]], 500))
cov_matrix, ei_vals, ei_vecs, means = PCA(data)

# Displaying results
print("Covariance Matrix:\n", cov_matrix)
print("Eigenvalues:\n", ei_vals)
print("Eigenvectors:\n", ei_vecs)

# Plotting the data and principal components

plt.scatter(list(data[:, 0]),
            list(data[:, 1]),
            label='cloud of Initial data points')

plt.scatter(list(cov_matrix[:, 0]),
            list(cov_matrix[:, 1]),
            label='cloud of recentered data points')

plt.quiver(0, 0, ei_vecs[0, 0], ei_vecs[1, 0],
           scale=1 / ei_vals[0],
           scale_units='x',
           color='r',
           label='First Principal Component')

plt.quiver(0, 0, ei_vecs[0, 1], ei_vecs[1, 1],
           scale=1 / ei_vals[1],
           scale_units='x',
           color='g',
           label='First Principal Component')

plt.legend()
plt.show()
