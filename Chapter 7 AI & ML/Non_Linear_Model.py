# Modelling a non linear Model

# Libraries
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Parameters calculation using the least squares method
def fit(X, Y):
    return inv(X.T.dot(X)).dot(X.T).dot(Y)

# Eoline Radius
R = 50         # Eoline blade radius in [m]
pi = 3.1415    # Pi parameter
rho = 1.292    # Air density 
# The flow surface become
S = 2 * pi * R**2

# Wind velocity taken between 0 and 30 in  [m/s]
V = np.linspace(0, 30, 50)
V_3 = 8.0/27.0 * S * np.array([[v**3] for v in V])

# Power calculation according to Betz law

P = np.array([rho * (V_3 + np.random.normal())])

# For this exercise, the least squares method is used to compute the air density rho
rho = fit(V_3, P)
print(rho, "\n\n")

# plot
plt.figure(figsize=(10, 6))
plt.plot(V,
         [p[0] for p in P[0]],
         label='Betz Law')
plt.xlabel('Velocity in [m/s]')
plt.ylabel('Power in Joule')
plt.title('Eoline power output vs wind velocity')
plt.legend()
plt.grid(True)
plt.show()