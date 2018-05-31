#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar_set = list(set(ar))
    ar_count = []
    ar_count = [0] * len(ar_set)
    '''
    for i in range(len(ar_set)):
        ar_count.append(0)
    '''
    ar.sort()
    cnt_pair_sold = 0
    
    
    for i in range(len(ar_set)):
        for j in range(len(ar)):
            if ar[j] == ar_set[i]:
                ar_count[i] += 1
    
    # print(ar_set)
    # print(ar_count)

    for k in range(len(ar_count)):
        if ar_count[k] >= 2:
            cnt_pair_sold += int(ar_count[k] / 2)
            # print(ar_set[k], ar_count[k], cnt_pair_sold)            
            
    return cnt_pair_sold

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
