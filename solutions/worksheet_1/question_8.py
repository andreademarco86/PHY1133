# Newton–Raphson one-step update for sqrt(c)

# Get input from user
c = float(input("Enter value of c: "))
x0 = float(input("Enter initial guess: "))

# Compute f(x) = x^2 - c and f'(x) = 2x
fx = x0**2 - c
df = 2 * x0

# Newton–Raphson update
x1 = x0 - fx / df

print(f"Next best guess for sqrt({c}) is {x1:.5f}")