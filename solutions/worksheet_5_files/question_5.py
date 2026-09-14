from matplotlib import pyplot as plt
import numpy as np

n_max = 50
threshold = 50
units = 1000

def mandelbrot(c):
    z = 0
    for i in range(n_max):
        z = z*z + c
    return z

x = np.linspace(-2, 1, units)
y = np.linspace(-1.5, 1.5, units)
grid = np.zeros((units, units))

for x_i in range(units):
    for y_i in range(units):
        value = mandelbrot(x[x_i] + y[y_i] * 1j)
        if abs(value) < threshold:
            grid[x_i, y_i] = 1
        else:
            grid[x_i, y_i] = 0

plt.imshow(grid)
plt.show()