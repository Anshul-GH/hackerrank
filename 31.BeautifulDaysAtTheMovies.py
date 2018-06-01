# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Identify unique numbers from a set that satisfy a mathematical pattern.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    # Count of beautiful days
    cnt_bd = 0

    while i <= j:
        i_rev = reverseNumber(i)
        if abs(i - i_rev) % k == 0:
            cnt_bd += 1
        i += 1
            
    return cnt_bd
    # Step 1: Reverse the numbers

    
def reverseNumber(n):
    n_rev = 0
    while n > 0:
        n_rev = (n_rev * 10) + (n % 10)
        n = n // 10
    
    return n_rev
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
