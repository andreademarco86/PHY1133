from math import sqrt, pi

g = 9.81

# Part 1

# Get input from user
length = float(input("Enter length: "))

# Calculate period
period = 2 * pi * sqrt(length / g)

# Output result
print(f"Period is {period:.3}")

# Part 2

# Get input from user
period = float(input("Enter period: "))

# Calculate period
length = g * ((period / (2 * pi)) ** 2)

# Output result
print(f"Length is {length:.3}")
