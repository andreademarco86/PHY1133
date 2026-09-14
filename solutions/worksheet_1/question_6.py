# Part 1

# Get input from user
distance = float(input("Enter distance: "))
duration = float(input("Enter duration in seconds: "))

# Calculate speed
speed = distance / duration

# Print result
print(f"Speed is {speed:.3}")

# Part 2

distance = float(input("Enter distance: "))
hours = float(input("Enter duration hours : "))
minutes = float(input("Enter duration minutes : "))
seconds = float(input("Enter duration seconds : "))

# Calculate speed
speed = distance / (hours * 3600 + minutes * 60 + seconds)

# Print result
print(f"Speed is {speed:.3}")