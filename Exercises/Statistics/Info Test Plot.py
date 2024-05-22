import matplotlib.pyplot as plt
import numpy as np

# Data points
x_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y_data = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Perform linear regression
slope, intercept = np.polyfit(x_data, y_data, 1)  # 1 = linear (one polynom)

# Display the slope and intercept
print(f"Slope: {slope}, Intercept: {intercept}")

# Define two points based on the slope and intercept for the line equation
point_one = (0, intercept)
point_two = (1, slope * 1 + intercept)  # y = kx+d

# Plot the original data points
plt.plot(x_data, y_data, color='blue', marker='o', linestyle='', label='Data points')

# Plot the regression line
plt.axline(point_one, point_two, color='r', linestyle='dashed', label='Regression Line')

# Calculate and display R-squared and population covariance
correlation = float(np.corrcoef(x_data, y_data)[0, 1] ** 2)
# Bias = Population, Unbias = Sample
population_covariance = float(np.cov(x_data, y_data, bias=True)[0, 1])  # float: array -> float
population_variance_x = float(np.var(x_data, ddof=0))
population_variance_y = float(np.var(y_data, ddof=0))
plt.text(0, 90, f"R²: {round(correlation, 3)}")
plt.text(0, 88, f"Variance x: {round(population_variance_x, 3)}")
plt.text(0, 86, f"Variance y: {round(population_variance_y, 3)}")
plt.text(0, 84, f"Regression Equation: {round(slope), 3} x + {round(intercept, 3)}")

# Set graph title and labels
plt.title("Hours Studied vs. Exam Points")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Points")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
