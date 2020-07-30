# https://www.hackerrank.com/challenges/plus-minus/problem
# Keywords: Given an array of integers, calculate the fractions of its elements that are 
# positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    # Define the three collection variables
    num_pos = 0.0
    num_neg = 0.0
    num_zero = 0.0
    
    
    for i in arr:
        if i > 0:
            num_pos+=1
        elif i < 0:
            num_neg+=1
        else:
            num_zero+=1
    
    print (num_pos/len(arr))
    print (num_neg/len(arr))
    print (num_zero/len(arr))
  

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
