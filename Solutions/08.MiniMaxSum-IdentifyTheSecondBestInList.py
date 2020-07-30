# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Keywords: Identify the second best in the list

#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    # Create the variables to hold values
    sum_min = 0
    sum_max = 0
    arr_asc = []
    arr_desc = []
    
    # Create sorted array holders
    arr_asc = sorted(arr, reverse = False)
    # print(arr_asc)
    arr_desc = sorted(arr, reverse = True)
    # print(arr_desc)
    
    for i in range(len(arr) - 1):
        sum_min += arr_asc[i]
        sum_max += arr_desc[i]
        
    # Print results
    print(sum_min, sum_max)
        
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
