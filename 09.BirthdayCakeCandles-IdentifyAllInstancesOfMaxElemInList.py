# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Keywords: Identify All Instances Of Max Elem In List

#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    # Define the array to hold sorted values
    # ar_desc = sorted(ar, reverse=True)
    ar_desc = ar
    ar_desc.sort(reverse = True)
    
    # Counter to blow out new candles. Counting 1 for the max value by default
    cnt_candles = 1
    
    # Logic to count
    for i in range(n-1):
        if ar_desc[i+1] == ar_desc[0]:
            cnt_candles += 1
        else:
            break
            
    return cnt_candles

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
