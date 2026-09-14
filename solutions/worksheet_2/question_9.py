from math import fabs

# Ask user for initial guess and tolerance
x1 = float(input("Enter initial guess: "))
tolerance = float(input("Enter tolerance value: "))

# Perform fixed-point iteration until convergence
# NOTE: This is for g(x) = x^2-2
x2 = 1e9
while fabs(x2 - x1) > tolerance:
    x2 = x1
    x1 = x2*x2 - 2

# Print out root
print(f"Found root at {x1:.6}")
