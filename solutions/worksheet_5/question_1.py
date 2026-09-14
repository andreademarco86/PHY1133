import numpy as np

# Generate a 1D array from 1 to 15
data = np.arange(1, 16)

# Transform this into a 2D 5x3 array and transpose it
data = np.reshape(data, (3, 5)).T

# Create new array containing 2nd and 4th rows
new_array = data[(1, 3), :]

# Print out new array
print(new_array)