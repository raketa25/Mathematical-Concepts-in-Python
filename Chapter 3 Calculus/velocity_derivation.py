# Caomputation of the position at a given time t, if the displacement happens at a constant velocity v, and the initial position is given by x0.

def position_at_time_t(initial_position, velocity, time):
    """
    Calculate the position at time t given an initial position, constant velocity, and time.

    Parameters:
    initial_position (float): The initial position at time t=0.
    velocity (float): The constant velocity of the object.
    time (float): The time at which to calculate the position.

    Returns:
    float: The position of the object at time t.
    """
    P = initial_position + velocity * time
    return P
  
#   Generic function to compute the derivation(differentiation) of a function f at a point x, using the definition of the derivative as a limit by taking a small delta value h.
def derivative_at_point(f, x, h=1e-3):
    """
    Compute the derivative of a function f at a point x using the definition of the derivative.

    Parameters:
    f (function): The function to differentiate.
    x (float): The point at which to compute the derivative.
    h (float): A small value for delta x.

    Returns:
    float: The derivative of f at point x.
    """
    # d = (f(x + h) - f(x - h)) / (2 * h)
    d = (f(x + h) - f(x)) / h
    return d  

# Application:
# Let's compute the instant velocity of an object at a specific time t, given its position function f(x) = x^2, and we want to find the velocity at t = 15 seconds. 
# 
# For a constant velocity v = 5 m/s and x0 = 0, the position function can be defined as f(x) = x0 + v * t, where x0 is the initial position. 
initial_position = 0
velocity_const = 5
t = 15

velocity_inst = derivative_at_point(lambda x: position_at_time_t(initial_position, velocity_const, x), t)
print(f"The instantaneous velocity at time t={t} seconds is approximately: {velocity_inst:.4f} m/s")

# print(derivative_at_point(lambda x: position_at_time_t(initial_position, velocity_const, x), t))

# Plotting the position function and its derivative to visualize the velocity at different time points. f(x) = x**2, x in [0.5, 1.5], and linearized around x = 1.

print("\n\n")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 1.5, 100)
y1 = x**2
y2= 1 + 2*(x - 1)                               # Linearized function around 1

plt.figure(figsize=(10,8))
plt.plot(x, y1, label= 'x^2 (Exact Function)', color='blue')
plt.plot(x, y2, label='1 + 2(x - 1) (Linear approximation)', color='red')

plt.title('Function vs Linear Approximation around x=1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.show()


