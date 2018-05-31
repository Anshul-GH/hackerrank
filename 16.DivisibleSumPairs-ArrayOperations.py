# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    val_cnt = 0
    for i in range(len(ar)):
        j = (len(ar) - 1)
        while(j > i):
            if((ar[i]+ar[j]) % k == 0):
                val_cnt += 1
            j -= 1
    return val_cnt

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
