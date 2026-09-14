from math import sqrt

# Get input from user
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

# Compute b^2-4ac
temp = b*b - 4 * a * c

# Calculate solution based on value of temp
if temp > 0:
    # Two real solutions
    solution_1 = (-b + sqrt(temp)) / (2 * a)
    solution_2 = (-b - sqrt(temp)) / (2 * a)
    print(f"Two solutions: {solution_1:.3} and {solution_2:.3}")

elif temp == 0:
    # One real solution
    solution = (-b + sqrt(temp)) / (2 * a)
    print(f"One solution: {solution:.3}")

else:
    # Complex solutions
    print("Negative discriminant, solutions are complex")