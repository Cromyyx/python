import matplotlib.pyplot as plt

labels = 'A', '0', 'B', 'AB'
sizes = [2/5, 2/5, 15/100, 5/100]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.show()
