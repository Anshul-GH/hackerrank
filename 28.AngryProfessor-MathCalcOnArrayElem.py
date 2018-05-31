# https://www.hackerrank.com/challenges/angry-professor/problem
# Simple mathematical calc based on array elements

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    cnt_lt = 0
    for i in a:
        if i <= 0:
            cnt_lt += 1
    # print('Cnt:', cnt_lt)
    if cnt_lt < k:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
