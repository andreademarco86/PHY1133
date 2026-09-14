import matplotlib.pyplot as plt
import numpy as np

n = 5000
threshold = 50.0

M = np.zeros([n, n], np.uint8)
x_values = np.linspace(-2, 1, n)
y_values = np.linspace(-1.5, 1.5, n)

for u, x in enumerate(x_values):
    for v, y in enumerate(y_values):
        z = 0
        c = complex(x, y)
        for i in range(n):
            z = z*z + c
            if abs(z) > threshold:
                M[v, u] = 1
                break

plt.imshow(M, aspect='auto', cmap='gray')
plt.show()
