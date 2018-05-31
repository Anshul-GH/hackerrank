# https://www.hackerrank.com/challenges/diagonal-difference/problem
# Keywords: Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    # Define the diagonal variables
    diag_1 = 0
    diag_2 = 0
    
    # Define the diff variable
    diff = 0
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                diag_1 += a[i][j]
            if i+j == (len(a[i])-1):
                diag_2 += a[i][j]
    diff = abs(diag_1 - diag_2)
    return diff
                
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
