# https://www.hackerrank.com/challenges/utopian-tree/problem
# Concept of applying alternate constraints to even and odd array elements.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    ht = 1
    for i in range(n):
        if (i+1) % 2 == 1:
            ht *= 2
        else:
            ht += 1
            
    return ht
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
