# https://www.hackerrank.com/challenges/circular-array-rotation/problem
# Implementing the circular array without using the iterable.cycle module

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, m):
    rslt = [0]*len(m)
    for i in range(len(m)):
        rslt[i] = a[m[i]]
    return rslt
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    m = []

    for _ in range(q):
        m_item = int(input())
        m.append(m_item)
    
    # reduce k to nullify full rotations
    k %= n
    
    # max index value for a
    max_idx = len(a) - 1
    
    # a temp copy of a
    a_tmp = [0]*(max_idx + 1)
    
    # Here is the rotation logic
    for i in range(max_idx+1):
        if i + k > max_idx:
            a_tmp[i + k - max_idx - 1] = a[i]
        else:
            a_tmp[i + k] = a[i]
            
    # print(a)
    # print(a_tmp)
        
    result = circularArrayRotation(a_tmp, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
