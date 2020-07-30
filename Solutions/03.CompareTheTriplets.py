# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Keywords: compare elements in two int lists/arrays

#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    # Define the score variables for Alice and Bob and the return list
    score_a = 0
    score_b = 0
    ret_set = []
    
    # Comparision Logic for 0th element
    if a0 > b0:
        score_a += 1
    elif a0 < b0:
        score_b += 1
        
    # Comparision Logic for 1st element
    if a1 > b1:
        score_a += 1
    elif a1 < b1:
        score_b += 1
    
    # Comparision Logic for 2nd element
    if a2 > b2:
        score_a += 1
    elif a2 < b2:
        score_b += 1
    
    # Append the score values to the list
    ret_set.append(score_a)
    ret_set.append(score_b)
    
    return ret_set

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
