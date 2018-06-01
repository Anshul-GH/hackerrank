# https://www.hackerrank.com/challenges/save-the-prisoner/problem
# I am not able to solve this yet.

#!/bin/python3

# import the cycle module that has been specifically created to handle circular lists
from itertools import cycle
import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # create a list of prisoners (each unique no denotes a prisoner)
    list_n = [(x+1) for x in range(n)]
    
    # create a circular list based on list_n
    cyc_n = cycle(list_n)
    '''
    cnt = 0
    for item in cyc_n:
        if cnt < 25:
            print(item)
            cnt += 1
        else:
            break
    print('----------------------')
    '''
          
    # calculate the actual leftover sweets that count
    act_m = m % n
    
    # cur_pos = s - 1, considering that the leftover distribution starts from 's'th position, 
    # we have to consider it in the count
    cur_pos = s - 1
    
    for i in range(act_m + cur_pos - 1):
        next(cyc_n)
        
    # printing the 'number' corresponding to the last prisoner
    print(next(cyc_n))
    
        
    # printing the 'number' corresponding to the last prisoner
    #print(cur_pos)
    # print(next(cyc_n))
    # next(cyc_n)
    # print(next(cyc_n))
    # next(cyc_n)
    # print(next(cyc_n))
    # next(cyc_n)
    # print(next(cyc_n))
    
    
    
    
    '''
    while act_m > 0:
        cur_pos += 1
        act_m -= 1
    '''
    # print cur_pos
    # print(list_n)
    
    # commenting the entire block
    '''
    act_m = m % n
    # print(act_m)
    
    # print(act_m + s)
    if act_m == 0:
        act_m = 1
    
    if (act_m + s) >= n:
        cur_pos = act_m + s - n
    else:
        cur_pos = act_m + s
    # print(cur_pos)
          
        
    return cur_pos
    ''' 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
