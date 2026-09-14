
# Initialise variables
total = 0
max_number = 0
min_number = 9e10

# Loop 10 times
for i in range(10):
    # Get new number from user
    num = float(input(f"Enter number {i+1}: "))

    # Add to total
    total += num

    # Check if number is greater than current maximum,
    # and if so set maximum to number
    if max_number < num:
        max_number = num

    # Or: max_number = max(max_number, num)

    # Check if number is less than current minimum,
    # and if so set minimum to number
    if min_number > num:
        min_number = num

    # Or: min_number = min(max_number, num)

# Print result
print(f"Sum is: {total}, average: {total/10.0}, minimum: {min_number}, maximum: {max_number}")