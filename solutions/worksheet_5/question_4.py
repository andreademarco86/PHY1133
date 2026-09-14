import matplotlib.pyplot as plt
import numpy as np

# Load the data from file
frequency, mic1, mic2 = np.loadtxt('microphones.txt', unpack=True)

# Show plot
plt.plot(frequency, mic1, label='Mic 1')
plt.plot(frequency, mic2, label='Mic 2')
plt.plot(frequency, mic1 / mic2, label='Ratio')
plt.ylabel('Power')
plt.xlabel('Frequency (kHz)')
plt.legend()
plt.show()
