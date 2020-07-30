# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Simple numerical counting logic based on constraints - learning to use arrays (lists)

#!/bin/python

import sys

def solve(n, s, d, m):
    # Define the variables
    tmp_sum = 0
    ch_cnt = 0
    
    for i in range(len(s)):
        tmp_sum = 0
        for j in range(m):
            if(j+i < len(s)):
                tmp_sum = tmp_sum+s[j+i]
        if(tmp_sum == d):
            ch_cnt += 1
     
    return ch_cnt
            

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
