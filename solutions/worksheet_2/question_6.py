from math import factorial, exp, fabs

# Ask user for value of x
x = float(input("Enter value of x: "))

# Compute analytic value of e^x
analytic_value = exp(x)

# Loop until minimum error is reached
iterations = 0
value = 0.0

while fabs(value - analytic_value) > 0.0001:
    value += x ** iterations / factorial(iterations)
    iterations += 1

# Output result and number of iterations
print(f"Computed value is {value:.5} in {iterations} iterations with error {fabs(value - analytic_value):.2e} ")