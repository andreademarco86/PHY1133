# Function to provide rounded truncation
def rounded_truncation(number):
    if (number - int(number)) < 0.5:
        return int(number)
    else:
        return int(number + 1)


# Get number from user
number = float(input("Enter number: "))

# Calculate rounded value
rounded = rounded_truncation(number)

# Output result
print(f"{number} was rounded to {rounded}")
