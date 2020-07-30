# https://www.hackerrank.com/challenges/itertools-product/problem
# 50.itertools.product().py

from itertools import product

if __name__ == '__main__':
    inp_A = list(input().split())
    inp_B = list(input().split())
    
    inp_A = [int(i) for i in inp_A]
    inp_B = [int(i) for i in inp_B]
    
    for i in list(product(inp_A, inp_B)):
        print(i, end = ' ')
