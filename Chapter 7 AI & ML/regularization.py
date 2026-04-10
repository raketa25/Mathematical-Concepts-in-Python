import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Definition of x values
x = np.linspace(-20, 20, 200)

# absolute value of x
y = np.abs(x)

# Let's calculate the approximated value of x using the log(cosh(x)) function
y_logcosh = np.log(np.cosh(x))

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Absolute error', color='blue')
plt.plot(x, y_logcosh, label=f'Log(cosh(x)) approximation', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Absolute Error and Log(cosh(x)) Regularization')
plt.legend()
plt.grid(True)
plt.show()

# Let's perform some tests of the function at some key points
test_points = [-10.0, -5.0, 0.0, 5.0, 10.0]
for point in test_points:
    abs_value = np.abs(point)
    logcosh_value = np.log(np.cosh(point))
    print(f"x: {point}, |x|: {abs_value:.4f}, log(cosh(x)): {logcosh_value:.4f}")

# at zero, both functions should yield the same value
zero_point = 0.0
print("At x = 0:", "\n")
print(np.abs(zero_point), "\n")
print(np.log(np.cosh(zero_point)))

# For large and positive x, log(cosh(x)) should approximate to x - log(2)
large_positive_x = 10.0
print("At large positive x:", "\n")
print(np.abs(large_positive_x), "\n")
print(np.log(np.cosh(large_positive_x)) - (large_positive_x) + np.log(2), "\n")
print(large_positive_x - np.log(2))

# For large and negative x, log(cosh(x)) should approximate to -x - log(2)
large_negative_x = -10.0
print("At large negative x:", "\n")
print(np.abs(large_negative_x), "\n")
print(np.log(np.cosh(large_negative_x)) - (- large_negative_x) + np.log(2), "\n")
print(-large_negative_x - np.log(2))
