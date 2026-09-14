from math import exp, sqrt, pi

# Segment the area into 10 trapezoids
integral = 0
for i in range(10):
    x1 = i * 0.1
    x2 = (i + 1) * 0.1

    # Calculate area of current segment and add to integral sum
    integral += ((exp(-x1 * x1 / 2.0) + exp(-x2 * x2 / 2.0)) / 2.0) * (x2 - x1)

# Multiply result by factor
integral *= 1.0 / sqrt(2 * pi)

# Output result
print(f"Integral is: {integral:.4}")