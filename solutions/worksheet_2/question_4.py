# Ask user for number
number = int(input("Enter number: "))

# Loop until value of number is 1
iterations = 0
while number != 1:

    # If number is even, divide it by 2
    if number % 2 == 0:
        number /= 2

    # If number is odd, multiply it by three and add 1
    else:
        number = number * 3 + 1

    # Increment number of iterations
    iterations += 1

# Output number of iterations
print(f"Reached 1 in {iterations} iterations")