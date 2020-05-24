# https://www.hackerrank.com/challenges/staircase/problem
# Keywords: print pattern of a staircase on screen.

#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print('#', end='')
        print('\n', end='')    
    
            

if __name__ == '__main__':
    n = int(input())

    staircase(n)
