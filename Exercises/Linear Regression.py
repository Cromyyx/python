import statistics

x = [203, 437, 579, 342, 448]
y = [9.1, 8.6, 8.4, 9.4, 8.1]

linear_regression = statistics.linear_regression(x, y)

print(linear_regression)

# LinearRegression(slope=-0.0026425823286777574, intercept=9.781789579662723)


import numpy as np

x = [203, 437, 579, 342, 448]
y = [9.1, 8.6, 8.4, 9.4, 8.1]

# Perform quadratic regression (polynomial of degree 2)
coefficients = np.polyfit(x, y, 2)

# The coefficients are in the order of highest degree first
a, b, c = coefficients

print(f"Quadratic Regression Equation: y = {a}x^2 + {b}x + {c}")
