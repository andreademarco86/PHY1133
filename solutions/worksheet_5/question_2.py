import matplotlib.pyplot as plt
import numpy as np

# Generate x axis
x = np.arange(1000) * 0.01

# Generate the two lines
line_1 = x**4 * np.exp(-2*x)
line_2 = (x**2*np.exp(-x)*np.sin(x**2))**2

# Show the lines
plt.plot(x, line_1, label='Line 1')
plt.plot(x, line_2, label='Line 2')
plt.xlabel('X axis')
plt.xlabel('Y axis')
plt.title("Cool plot")
plt.show()
