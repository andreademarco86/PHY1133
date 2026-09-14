# Initialise list

mylist = []

# Loop forever
while True:
    # Ask user to enter a number
    num = int(input("Enter a number: "))

    # If number is -999, break from loop
    if num == -999:
        break

    # Add number to list
    mylist.append(num)

# Print list
print(mylist)
