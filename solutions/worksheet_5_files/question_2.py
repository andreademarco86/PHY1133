from numpy.random import random

with open("vectors.txt", 'w') as f:
    for i in range(100):
        x = random() * 10
        y = random() * 10
        z = random() * 10

        f.write("{} {} {}\n".format(x, y, z))