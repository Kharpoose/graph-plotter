import matplotlib.pyplot as plt

x1 = [2, 4, 5, 9]
y2 = [2, 3, 6, 8]

plt.plot(x1, y2, label = 'Line 1')

x2 = [1, 2, 3, 5, 8]
y2 = [2, 3, 4, 6, 9]

plt.plot(x2, y2, label = 'Line 2')
plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Graph with two')
plt.legend()
plt.show()
