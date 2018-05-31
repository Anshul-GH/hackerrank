# https://www.hackerrank.com/challenges/picking-numbers/problem
# A good problem based on choosing subsets within an array/list based on a mathematical constraint (a-b <= 1)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    max_cnt = 0
    a.sort()
    b = list(set(a))
    b.sort()
    c = [1]*len(b)
    '''
    for i in range(len(b)):
        c.append(1)
    '''    
    cnt_num = 0
    j = 0
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            cnt_num += 1
        elif j < len(c):
            c[j] = c[j] + cnt_num
            cnt_num = 0
            j += 1
    
    # Assigning the count for the last value in the set
    if a[-1] == a[-2]:
        c[-1] += cnt_num
    else:
        c[-1] = 1
        
    if len(c) - 1 > 0:
        max_cnt = max(c)
        for i in range(len(c) - 1):
            if abs(b[i+1] - b[i]) == 1:
                if (c[i+1]+c[i]) > max_cnt:
                    max_cnt = c[i+1]+c[i]
    elif len(c) - 1 == 0:
        max_cnt = c[0]
    
    # print(max_cnt)
    # print(a)
    # print(b)
    # print(c)
    
    return max_cnt
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

