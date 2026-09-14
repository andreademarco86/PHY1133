from math import sin


# Implement equation for sinc(x)
def equation(x):
    if x == 0:
        print("x cannot be zero")
    else:
        print(f"sinc({x}) = {sin(x) / x}")


# Get input from user
value = float(input("Enter value for x: "))

# Call function
equation(value)
