from numpy.random import random
from math import pi


# Function to throw a random dart. Return 1 if the dart falls
# within the circle, 0 otherwise
def throw_dart():
    x = random()
    y = random()

    if (x ** 2 + y ** 2) ** 0.5 < 1:
        return 1
    else:
        return 0


# Check how many iterations required for 2 significant digits
# Note that we kickstart the calculation with the first thrown
# to avoid a divide by 0 error when calculating pi
total_throws = 1
total_in = throw_dart()
my_pi = 4 * (total_in / float(total_throws))

# Keep looping until we reach the required error
while abs(my_pi - pi) > 0.001:
    total_throws += 1
    total_in += throw_dart()
    my_pi = 4 * (total_in / float(total_throws))

# Applying Monte Carlo's Method to estimate Pi
print(f"{my_pi:.4f} = {pi:.4f} with 2 significant figures in {total_throws} iterations")
