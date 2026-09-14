# Get input from user
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

# Calculate quotient, integer part of quotient and remainder
quotient = num1 / num2
integer_quotient = num1 // num2
remainder = num1 % num2

# Print result
print(f"Quotient: {quotient:.3f}, integer part: {integer_quotient}, remainder: {remainder}")