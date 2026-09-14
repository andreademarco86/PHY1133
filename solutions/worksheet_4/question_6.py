# Implement collatz conjecture function
def collatz(number):
    # Print number
    print(number)

    # If number ==  1 we have finished
    if number == 1:
        return 0

    # If number is even, divide by two and continue
    elif number % 2 == 0:
        return 1 + collatz(number / 2)

    # If number is odd, multiply by 3, add 1 and continue
    else:
        return 1 + collatz(number * 3 + 1)


# Ask user for number
number = int(input("Enter number: "))

# Call function
iterations = collatz(number)

# Output number of iterations
print(f"Reached 1 in {iterations} iterations")