# Get input from user
temp_f = float(input("Enter temperature in Fahrenheit: "))

# Calculate temperature in Celsius
temp_c = temp_f - 32 * 5/9

# Print result
print(f"{temp_f} in Fahrenheit is {temp_c:.3f} in Celsius")
