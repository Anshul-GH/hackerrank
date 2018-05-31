# https://www.hackerrank.com/challenges/electronics-shop/problem
# Simple logic of numeric counting

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # This will store the max amount that could be spent
    max_amt = 0
    
    keyboards.sort()
    drives.sort(reverse = True)
    
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if((keyboards[i] + drives[j] > b) and (max_amt == 0)):
                max_amt = -1
            elif((keyboards[i] + drives[j] <= b) and (keyboards[i] + drives[j] > max_amt)):
                max_amt = keyboards[i] + drives[j]
    
    return max_amt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
