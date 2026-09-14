from math import exp, fabs

# Ask user to input required error
req_error = float(input("Enter required error: "))

# Initialise variables
iterations = 0
error = 1e9
x1 = 1.0
x2 = 2.0

# Loop while error is greater than required error
while error > req_error:
    # Calculate mid-point
    xnew = (x1 + x2) / 2.0
    error = fabs((x1 - x2) / 2)

    # Evaluate at new point
    f_xnew = exp(-xnew) + 4*xnew**3 - 5

    # Update x1 or x2 to xnew accordingly
    if f_xnew > 0:
        x2 = xnew
    else:
        x1 = xnew

    iterations += 1

# Print out root and number of iterations
print(f"Root at {x1} (after {iterations} iterations)")
