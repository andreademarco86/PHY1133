import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T  # trick: columns to variables

# plt.axes([0.2, 0.1, 0.5, 0.8])
# plt.plot(year, hares, year, lynxes, year, carrots)
# plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
# plt.show()

# Compute mean and std of each population
print(f"Mean and std of hares: {np.mean(hares)}, {np.std(hares)}")
print(f"Mean and std of lynxes: {np.mean(lynxes)}, {np.std(lynxes)}")
print(f"Mean and std of carrots: {np.mean(carrots)}, {np.std(carrots)}")
print('')

# Which year each species had the largest population
print(f"Best hare year: {year[np.argmax(hares)]}")
print(f"Best lynx year: {year[np.argmax(lynxes)]}")
print(f"Best carrot year: {year[np.argmax(carrots)]}")
print('')

# Which species has the largest population for each year
together = np.array([hares, lynxes, carrots])
types = np.array(['hares', 'lynxes', 'carrots'])
largest = types[np.argmax(together, axis=0)]
for i, y in enumerate(year):
    print(f"Largest population in {int(y)} was {largest(i)}")
print('')

# Which year any of the populations is above 5000
print(year[np.any(together > 50000, axis=0)])
print('')

# The top 2 years for each species when they had the lowest populations
sorted_indices = np.argsort(hares)
print("Worst hares years: ", year[sorted_indices][:-3:-1])
sorted_indices = np.argsort(lynxes)
print("Worst lynxes years: ", year[sorted_indices][:-3:-1])
sorted_indices = np.argsort(carrots)
print("Worst carrots years: ", year[sorted_indices][:-3:-1])
print()

# Plot change in hare population and the number of lynxes
plt.figure()
plt.plot(year, np.gradient(hares), label='Hares gradient')
plt.plot(year, lynxes, label='Lynxes')
plt.show()
