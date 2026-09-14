from math import exp, pi, sqrt


# Implement equation
def equation(x):
    return (1 / sqrt(2 * pi)) * exp(x**2 / 2)


# Loop from 0 to 40 in steps of 0.5
for x in range(0, 9):
    print(f"f({x * 0.5}) = {equation(x * 0.5)}")