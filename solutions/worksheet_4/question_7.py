# Implement fibonacci as a recursive function
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# Get input from user
number = int(input("Enter number: "))

# Call function
answer = fibonacci(number)

# Print result
print(f"fibonacci({number}) = {answer}".format(number, answer))
