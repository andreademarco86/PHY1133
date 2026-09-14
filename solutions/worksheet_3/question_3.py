from numpy.random import random

# Create random list from 1 to 500
mylist = random(100) * 499 + 1

# Find maximum, minimum and number of
# elements between 200 and 250
counter = 1
curr_max = 1
curr_min = 500
for num in mylist:
    if curr_max < num:
        curr_max = num
    if curr_min > num:
        curr_min = num

    if 200 <= num <= 250:
        counter += 1

# Print results
print(f"Maximum: {curr_max}, minimum: {curr_min}, number of elements between 200 and 250: {counter}")
