# Define function to convert fahrenheit to celsius
def fahrenheit_to_celsius(temperature):
    return temperature - 32 * 5.0 / 9.0


# Get input from user
temp_f = float(input("Enter temperature in Fahrenheit: "))

# Calculate temperature in Celsius
temp_c = fahrenheit_to_celsius(temp_f)

# Print result
print(f"{temp_f} in Fahrenheit is {temp_c:.3f} in Celsius")
