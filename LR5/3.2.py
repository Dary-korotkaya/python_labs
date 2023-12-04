import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем диапазон значений x и y
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)

# Создаем сетку значений x и y
x, y = np.meshgrid(x_values, y_values)

# Задаем функции
z1 = np.power(x, 0.25) + np.power(y, 0.25)
z2 = np.power(x, 2) - np.power(y, 2)
z3 = 2 * x + 3 * y
z4 = np.power(x, 2) + np.power(y, 2)
z5 = 2 + 2 * x + 2 * y - np.power(x, 2) - np.power(y, 2)

# Создаем 3D-графики
fig = plt.figure(figsize=(18, 6))

# График 1
ax1 = fig.add_subplot(151, projection='3d')
ax1.plot_surface(x, y, z1, cmap='viridis')
ax1.set_title('z = x**0.25 + y**0.25')

# График 2
ax2 = fig.add_subplot(152, projection='3d')
ax2.plot_surface(x, y, z2, cmap='plasma')
ax2.set_title('z = x**2 - y**2')

# График 3
ax3 = fig.add_subplot(153, projection='3d')
ax3.plot_surface(x, y, z3, cmap='magma')
ax3.set_title('z = 2*x + 3*y')

# График 4
ax4 = fig.add_subplot(154, projection='3d')
ax4.plot_surface(x, y, z4, cmap='inferno')
ax4.set_title('z = x**2 + y**2')

# График 5
ax5 = fig.add_subplot(155, projection='3d')
ax5.plot_surface(x, y, z5, cmap='plasma')
ax5.set_title('z = 2 + 2*x + 2*y - x**2 - y**2')

plt.show()
