import statistics
import matplotlib.pyplot as plt

x=[203,437,579,342,448]
y=[9.1,8.6,8.4,9.4,8.1]

answer = statistics.linear_regression(x, y)

print(answer)

#LinearRegression(slope=-0.0026425823286777574, intercept=9.781789579662723)

plt.scatter(x, y,color='g')
plt.plot(x, y,color='k')

plt.show()