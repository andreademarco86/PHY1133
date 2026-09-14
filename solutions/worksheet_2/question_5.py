from math import factorial, exp

# Ask user for value of x
x = float(input("Enter value of x: "))

# Evaluate series up to 10 terms
value = 0
for i in range(10):
    value += x**i / factorial(i)

# Output result and comparison
print(f"Computed value is {value:.3}, analytic value is {exp(x):.3}")