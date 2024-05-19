import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4,], [1, 4, 9, 16], "b--", linewidth=2, markersize=12)
plt.axis((0, 6, 0, 20))
plt.ylabel('some numbers')
plt.show()
