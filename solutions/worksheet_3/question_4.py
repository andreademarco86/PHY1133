from numpy.random import random

# Initialise empty list
my_list = []

# Generate 10 numbers in a for loop and print them one by one
for i in range(10):
    num = random(1)
    my_list.append(num[0])
    print(num)

# Reverse the list:
my_list = my_list[::-1]

# Print reversed list
print(my_list)
