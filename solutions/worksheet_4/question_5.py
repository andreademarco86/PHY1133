# Implement factorial function using recursion
def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)


# Get input from user
n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))

# Check that n > r
if n <= r:
    print("n must be greater than r!")
    exit()

# Calculate answer
answer = factorial(n) / (factorial(r) * factorial(n - r))

# Print output
print(f"nCr for n={n} and r={r} = {answer}")
