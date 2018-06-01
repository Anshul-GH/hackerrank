# https://www.hackerrank.com/challenges/itertools-permutations/problem
# 47.itertools.permutations().py

from itertools import permutations

if __name__ == '__main__':
    inp_list = input().split()
    # print(inp_list)
    
    # input list
    str_list = inp_list[0]
    
    # Need to identify all possible permutations of lenght 'str_len'
    str_len = int(inp_list[1])
    # print(str_list)
    # print(str_len)
    
    str_perm = [''.join(p) for p in permutations(str_list, str_len)]
    str_perm.sort()
    
    for i in range(len(str_perm)):
        print(str_perm[i])
