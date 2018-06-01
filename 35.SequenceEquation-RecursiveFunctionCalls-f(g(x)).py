# https://www.hackerrank.com/challenges/permutation-equation/problem
# recursive functionc alls - f(g(x)) etc

#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the permutationEquation function below.
def permutationEquation(p):    
    tmp_p = copy.deepcopy(p)
    tmp_p.sort()
    # print(p)
    # print(tmp_p)
    
    retn_val = [0]*len(p)
    idx_val = [0]*len(p)
    
    # 1. Find the indexes of relevant values
    for i in range(len(tmp_p)):
        for j in range(len(p)):
            if tmp_p[i] == p[j]:
                idx_val[i] = j+1
    
    # print(idx_val)        
    
    # 2. Final indexes that are relevant
    for i in range(len(p)):
        for j in range(len(idx_val)):
            if idx_val[i] == p[j]:
                retn_val[i] = j+1
    
    # print(retn_val) 
    
    return retn_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
