# =========================================================
# Formative Assessment No. 1
# Calculating Distance Between Two Points
# Using Math and I/O Libraries
# =========================================================

# We import the math library so we can use its built-in
# functions instead of writing the square root and power
# formulas ourselves from scratch.
import math


def get_point(point_label):
    """
    Ask the user for the x and y coordinates of one point.
    float() is used so the program accepts decimal values too.
    Returns the coordinates as a tuple: (x, y).
    """
    x = float(input(f"Enter x{point_label}: "))
    y = float(input(f"Enter y{point_label}: "))
    return x, y


def calculate_distance(point_a, point_b):
    """
    Calculate the Euclidean distance between two points.

    Euclidean Distance Formula:
    d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

    math.pow(base, exponent) raises a number to a power.
    math.sqrt(number) calculates the square root of a number.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance


def main():
    # ---- INPUT ----
    # Ask the user for the coordinates of the two points.
    point_1 = get_point(1)
    point_2 = get_point(2)

    # ---- PROCESS ----
    distance = calculate_distance(point_1, point_2)

    # ---- OUTPUT ----
    # round(distance, 2) keeps the output to 2 decimal places,
    # matching the expected output format.
    print()
    print(f"The distance between the two points is: {round(distance, 2)}")


if __name__ == "__main__":
    main()


# =========================================================
# REFLECTION
# =========================================================
# Using a library is more practical than writing calculations
# from scratch because it saves time and reduces errors. In
# this activity, math.sqrt() and math.pow() handled the square
# root and exponent steps of the distance formula instantly,
# instead of me having to write extra loops or formulas to
# compute them manually. This let me focus on solving the
# problem (getting the right input and applying the formula)
# rather than worrying about how square roots are calculated
# internally.
#
# Guide Questions:
# 1. How did the math library help simplify your program?
#    - It provided ready-made functions (sqrt, pow) so I didn't
#      have to write my own algorithms to compute square roots
#      or exponents. This let me apply the distance formula in
#      just one line instead of building the math logic myself.
#
# 2. What functions were easier to use because of the library?
#    - math.sqrt() made finding the square root simple, and
#      math.pow() made squaring the differences (x2 - x1) and
#      (y2 - y1) straightforward. Both functions let me plug in
#      values directly instead of writing separate calculations.
#
# 3. How would the program be more difficult without sqrt()
#    and pow()?
#    - I would need to write a custom loop or formula (like
#      Newton's method or repeated approximation) just to get a
#      square root, and manually multiply numbers repeatedly to
#      raise them to a power. This adds more code, more chances
#      for bugs, and makes the program harder to read and
#      maintain compared to just calling one library function.
