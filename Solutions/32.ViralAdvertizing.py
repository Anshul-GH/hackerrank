# https://www.hackerrank.com/challenges/strange-advertising/problem
# Multiplying patterns, cumulative addition etc

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cnt_liked = 0
    # d1_cnt = 5
    # tmp_like = 0
    tmp_shr = 5
    
    while n > 0:
        tmp_like = (int(tmp_shr/2))
        tmp_shr = 3 * tmp_like
        cnt_liked += tmp_like
        n -= 1
        
    return cnt_liked   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
