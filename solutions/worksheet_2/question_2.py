# Set sum to 0 and ask user to enter first number
total = 0
num = int(input("Enter number: "))

# Loop until the value -999 is encountered
while num != -999:
    
    # Add number to current sum and print it out
    total += num
    print(f"Current sum is {total}")

    # Ask user for a new number
    num = int(input("Enter number: "))

print("All done")
