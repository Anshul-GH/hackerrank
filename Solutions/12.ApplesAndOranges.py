# https://www.hackerrank.com/challenges/apple-and-orange/problem
# Simple logic of relative distance on the number line

#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Variables to hold valid counts
    cnt_apples = 0
    cnt_oranges = 0
    
    # Logic
    for idx, val in enumerate(apples):
        dist = val + a
        if s <= dist <= t:
            cnt_apples += 1
            
    for idx, val in enumerate(oranges):
        dist = val + b
        if s <= dist <= t:
            cnt_oranges += 1

    print(cnt_apples)
    print(cnt_oranges)
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
