import statistics
import matplotlib.pyplot as plt
import numpy as np  # statistics has no population/biased covariance

x_old = [1, 2, 3, 4, 5]
y_old = [4, 5.25, 6, 7.5, 7.75]

slope, intercept = statistics.linear_regression(x_old, y_old)

print("slope: ", slope, "intercept: ", intercept)

# change slope + intercept into 2 points
point_one = {"x": 0, "y": intercept}
point_two = {"x": 1, "y": (slope * 1) + intercept}  # y = mx+b

plt.plot(x_old, y_old, color="blue", linestyle="solid")
# plt.plot([point_one["x"], point_two["x"]], [point_one["y"], point_two["y"]], "r--")
plt.axline((point_one["x"], point_one["y"]), (point_two["x"], point_two["y"]),
           color='r', linestyle='dashed')
correlation = statistics.correlation(x_old, y_old) ** 2  # R²
population_covariance = float(np.cov(x_old, y_old, bias=True)[0, 1])  # float because bef. array
# "0,1" because 0:0 = cov(x), 0:1 = cov(x,y), 1:0 = cov(y,x), 1:1 = cov(y) | matrix shit
# bias = True because population biased, sample unbiased

plt.title("Hours studied to Grade achieved")
plt.xlabel("Hours studied")
plt.ylabel("Exam Grade")
plt.text(1, 7, f"R²:{round(correlation, 3)}")
plt.text(1, 6, f"Variance:{round(population_covariance, 3)}")
plt.grid(True)
plt.show()
