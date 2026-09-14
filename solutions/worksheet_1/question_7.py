# Get input from user
hours = float(input("Enter time in decimal hours: "))

# Convert to hours, minutes and seconds
hour = int(hours)
minutes = int((hours - hour) * 60)
seconds = ((hours - hour) * 60 - minutes) * 60

print(f"Time is {hour}:{minutes}:{seconds}")
