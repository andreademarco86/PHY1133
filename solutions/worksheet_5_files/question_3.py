from math import sqrt

with open("vectors.txt") as f:
    # Loop forever
    while True:

        # Read the next line
        line = f.readline()

        # If the length of the line is 0, we have reached the end, so break
        if len(line) == 0:
            break

        # A line contains three values separated by a white line. Split
        # this line
        values = line.split(' ')

        # We should have three value, convert each to a float
        x, y, z = float(values[0]), float(values[1]), float(values[2])

        # Compute distance
        r = sqrt(x*x + y*y + z*z)

        print(f"x{x:.2f}, y={y:.2f}, z={z:.2f}, r={r:.2f}")
