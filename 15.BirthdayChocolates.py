# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Simple numerical counting logic based on constraints - learning to use arrays (lists)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, s, d, m):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
