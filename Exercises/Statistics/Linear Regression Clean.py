import matplotlib.pyplot as plt
import numpy as np

# Data points
x_data = [1, 2, 3, 4, 5]
y_data = [4, 5.25, 6, 7.5, 7.75]

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
#population_covariance = float(np.cov(x_data, y_data, bias=True)[0, 1])  # float: array -> float
plt.text(1, 7, f"R²: {round(correlation, 3)}")
#plt.text(1, 6.75, f"Covariance: {round(population_covariance, 3)}")

# Set graph title and labels
plt.title("Hours Studied vs. Exam Grade")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Grade")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
