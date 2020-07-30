# https://www.hackerrank.com/challenges/counting-valleys/problem
# Simple pattern tracking logic using numerical counter

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # print(s)
    # Integer Equivalent of String Input Array
    # int_s = []
    sum_s = 0
    sum_s_prev = 0
    cnt_val = 0
    
    for i in s:
        sum_s_prev = sum_s
        if i == 'U':
            # int_s[i] = 1
            sum_s += 1
        elif i == 'D':
            # int_s[i] = -1
            sum_s += -1
        
        if(sum_s_prev < 0 and sum_s == 0):
            cnt_val += 1
    
    return cnt_val
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
