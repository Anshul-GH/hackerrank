# https://www.hackerrank.com/challenges/drawing-book/problem
# Clarifies the concept of a 2D array and manipulate the even and odd occurances of pattern (pages of book)

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    idx_p = 0
    # Representing the book as a 2 dimensional array
    book_arr = [[i for i in range(2)] for k in range(int(n/2) + 1)]
    # print(book_arr)
    
    
    for i in range(int(n/2)+1):
        for j in range(2):
            book_arr[i][j] = 2 * i + j
            
    for i in range(int(n/2)+1):
        for j in range(2):
            if book_arr[i][j] == p:
                idx_p = i
    
    # print(idx_p)
    
    return (idx_p if p < (int(n/2)+1) else (int(n/2) - idx_p))
            
    
    # if p > (n/2):
        

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
