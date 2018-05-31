# https://www.hackerrank.com/challenges/a-very-big-sum/submissions/code/72024475
# Keywords: Handling sum of large integers - 0<= n <= 10^10

#!/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    # Define the variable to hold the sum
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
