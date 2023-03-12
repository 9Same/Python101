import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x,y, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=2)

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('My Graph')

plt.show()