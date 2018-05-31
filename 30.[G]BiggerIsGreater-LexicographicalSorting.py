# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# This is an awesome problem that utilizes the following algorithm:
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# Superb learning !!!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # Step 1: Convert string to numeric array
    num_w = [0] * len(w)
    for i in range(len(w)):
        num_w[i] = ord(w[i]) - 97
    
    # Step 2: Find the longest non-increasing suffix
    i = len(num_w) - 1
    while i > 0 and num_w[i - 1] >= num_w[i]:
        i -= 1 
        # This finds the longest increasing sequence from the back
    
    if i <= 0:
        # The string in question is already the maximum in the sequence.
        return 'no answer'
    
    # Step 3: Choose num_w[i -1] as the pivot
    # Find the righmost index j that exceeds the pivot.
    j = (len(num_w) - 1)
    while num_w[j] <= num_w[i - 1]:
        j -= 1
        
    # Step 4: Now num_w[j] will be the new pivot
    tmp_num = num_w[i - 1]
    num_w[i - 1] = num_w[j]
    num_w[j] = tmp_num
    
    # Step 5: Reverse the suffix
    j = (len(num_w) - 1)
    while i < j:
        tmp_num = num_w[i]
        num_w[i] = num_w[j]
        num_w[j] = tmp_num
        i += 1
        j -= 1 
    
    # Step 6: Convert the number to string and return
    chr_w = []
    for i in range(len(num_w)):
        chr_w.append(chr(num_w[i] + 97))
    
    return ''.join(chr_w)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
