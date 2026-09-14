from math import sqrt


def newton_raphson(guess, value):
    fx = guess * guess - value
    df = 2 * guess
    return guess - fx / df


# Get inputs from user
value = int(input("Root of C to find: "))
guess = float(input("Initial guess: "))

# Calculate correct value
correct = sqrt(value)

# Loop until we reach the required accuracy and print number of iterations
iterations = 0
while (guess - correct) > 0.0001:
    guess = newton_raphson(guess, value)
    iterations += 1

# Print result
print(f"Reached {guess - correct} difference in {iterations} iterations")