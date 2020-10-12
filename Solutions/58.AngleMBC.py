# https://www.hackerrank.com/challenges/find-angle/problem

import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())

    # hypotenuse
    AC = math.sqrt((AB*AB) + (BC*BC))

    # mid-point of hypotenuse
    MC = AC / 2

    # cosine formula
    angle1 = math.degrees(math.acos())

