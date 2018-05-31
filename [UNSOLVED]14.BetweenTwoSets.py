# https://www.hackerrank.com/challenges/between-two-sets/problem
# The problem statement is confusing. I was not able to solve this
'''
You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:
- The elements of the first array are all factors of the integer being considered
- The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
'''

# Approach 1:
#!/bin/python3
from copy import deepcopy
import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    ret_cnt = 0
    # Starting with the numbers themselves being factors already
    fact_a = deepcopy(a)
    # print(a)
    for i in range(len(a)):        
        for j in range(len(a)):
            if j >= i:
                fact_a.append(a[i] * a[j])
                
    # Ignoring the duplicates
    fact_a = list(set(fact_a))
    print(fact_a)
                
    '''fact_b = []
    for i in range(len(b)):        
        for j in range(len(b)):
            if j >= i:
                fact_b.append(b[i] * b[j])
    '''
            
    # print(fact_a)
    # print(fact_b)
    fact_flg = False
    
    for i in range(len(fact_a)):
        for j in range (len(b)):
            # print('b[j]: ', b[j], 'fact_a[i]: ', fact_a[i])
            if b[j] % fact_a[i] == 0:
                fact_flg = True
            else:
                fact_flg = False
                break
        if fact_flg == True:
            ret_cnt += 1
            fact_flg = False
    
    return ret_cnt
                
                

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()


########################################################################################


# Approach 2:
#!/bin/python3

import os
import sys
# from math import gcd

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    # Define the return count variable
    cnt_ret = 0
    
    # Defining the function for gcd
    def gcd (a,b):
        if (b == 0):
            return a
        else:
            return gcd (b, a % b)
    
    # Step1: Find the LCM of list1
    lcm_l1 = a[0]
    for i in a[1:]:
        lcm_l1 = lcm_l1*i/gcd(lcm_l1, i)
        
    # Step2: Find the GCD of list2
    gcd_l2 = b[0]
    for j in b[1:]:
        gcd_l2 = gcd(gcd_l2, j)
    
    if gcd_l2 % lcm_l1 == 0:
        return len(b)
    else:
        return 0
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    total = getTotalX(a, b)
    f.write(str(total) + '\n')
    f.close()

