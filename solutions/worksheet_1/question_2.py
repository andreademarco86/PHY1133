from math import sqrt

# Get input from user
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

# Calculate z
z = sqrt(x*x + y*y)

# or
# z = sqrt(x**2 + y**2)

# Print result
print(f"Value of z is: {z}")