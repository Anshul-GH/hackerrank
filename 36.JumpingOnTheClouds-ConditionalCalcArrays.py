# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Conditional calculations on arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    idx = 0
    enrg = 100
    
    while True:
        idx = (idx + k) % len(c)
        if c[idx] == 1:
            enrg -= 3
        else:
            enrg -= 1
        if idx == 0:
            break
    
    return enrg       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
