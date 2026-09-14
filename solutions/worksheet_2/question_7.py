from math import pi, exp

# Iterate five times for both the x and y values
for i in range(6):
    for j in range(6):
        # Evaluate function for current values of x and y
        x = i * 0.1
        y = j * 0.1
        value = 1/(2*pi)*exp(-(x*x+y*y)/2)

        # Output result for current x and y values
        print(f"Value for ({x}, {y}) is {value}")