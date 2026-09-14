from math import sqrt, atan2, acos

# Open output file
with open("spherical.txt", 'w') as output_file:

    # Open input file
    with open("vectors.txt") as input_file:

        # Loop forever
        while True:

            # Read the next line
            line = input_file.readline()

            # If the length of the line is 0, we have reached the end, so break
            if len(line) == 0:
                break

            # A line contains three values separated by a white line. Split
            # this line
            values = line.split(' ')

            # We should have three value, convert each to a float
            x, y, z = float(values[0]), float(values[1]), float(values[2])

            # Compute spherical coordinates
            p = sqrt(x*x + y*y + z*z)
            theta = atan2(y, x)
            phi = acos(x / p)

            # Write to file
            output_file.write(f"{p} {theta} {phi}\n")
