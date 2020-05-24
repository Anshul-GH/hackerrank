# https://www.hackerrank.com/challenges/append-and-delete/problem
# This was a difficuly hit and try scenario where the solutionw as arrived using test case to test case fixing approach

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # Step 1: Fill the shorter string with buffer characters - '*' 
    # to match the length of the other string
    if len(s) > len(t):
        t_apnd = t + ('*'*(len(s) - len(t)))
        s_apnd = s
        # print(t)
    else:
        s_apnd = s + ('*'*(len(t) - len(s)))
        t_apnd = t
        # print(t)
    
    # max_idx = len(s) if len(s) > len(t) else len(t)
    # print(len(s), len(t))
    
    matched_pos = [i for i in range(len(s_apnd)) if s_apnd[i] != t_apnd[i]]
    # print(matched_pos)
    
    # Checking for the case when the two strings are exactly same
    # In that case, the matched position array will be null
    if len(matched_pos) > 0:
        # Min count of steps required
        min_stps = len(s) + len(t) - (2 * matched_pos[0])
    else:
        min_stps = 0
    
    # Case #1: The minm steps required exactly match with 'k'
    if k == min_stps:
        return 'Yes'
    # Case #2: Partial match with k > min_stps => k has to greater than 
    # min_stps + twice the length of smaller string
    elif (k - min_stps) > (2 * (len(s) if len(s) < len(t) else len(t))):
        return 'Yes'    
    elif k > min_stps and len(matched_pos) > 0:
        # Case #3: Case of totally distinct strings
        if matched_pos[0] == 0:
            return 'Yes'
        # Case #4: Partial match with k > min_stps but less than 
        # min_stps + twice the length of smaller string
        elif (k - min_stps) % 2 == 0:
            return 'Yes'
        # Case #5: The failure case
        else:
            return 'No'
    # Case #6: Case with exactly identical strings.
    # Here min_stps will be 0 but any even value of k would work 
    # as a combination deleting and adding values at the end in pairs
    # will result in the same string for each pair of operations
    elif k > min_stps and len(matched_pos) == 0:
        if k % 2 == 0:
            return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
