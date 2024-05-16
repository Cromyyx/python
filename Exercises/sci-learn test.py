import matplotlib.pyplot as plt
from sklearn import datasets

# Load an example dataset
iris = datasets.load_iris()
data = iris.data

# Select the feature you want to make a histogram for
# For instance, the first feature of the Iris dataset
feature_index = 0
feature_values = data[:, feature_index]

# Create the histogram
plt.hist(feature_values, bins=20, edgecolor='black')

# Add a title and labels
plt.title('Histogram of Feature Values')
plt.xlabel('Feature Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
