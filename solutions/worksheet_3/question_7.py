# Define acceleration
a = -9.8

# Ask user to input initial height and velocity
height = float(input("Enter initial height: "))
v0 = float(input("Enter initial velocity: "))

# Create time array using list comprehension
time = [i * 0.1 for i in range(50)]

# Initialise position list
position = []

# For each time step, calculate position
for t in time:
    position.append(height + v0 * t + 0.5 * a * t ** 2)

# Print position list, nicely using list comprehension and the join function
print(''.join([f'{i}: {p}\n' for i, p in enumerate(position)]))

