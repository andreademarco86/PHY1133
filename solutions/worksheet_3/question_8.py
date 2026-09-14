from numpy.random import rand

# Generate a 10x5 matrix of random numbers
numbers = rand(10, 5).tolist()

# Print out list
print(numbers)

# Print out value and position of largest number
maximum = -1
x, y = 0, 0
for i in range(10):
    for j in range(5):
        if maximum < numbers[i][j]:
            maximum = numbers[i][j]
            x, y = i, j

print(f"Max: {maximum} at {x},{y}".format(maximum, x, y))

# Print out average of each row
for i in range(10):
    print(f"Average of row {i} is {sum(numbers[i]) / 5}")