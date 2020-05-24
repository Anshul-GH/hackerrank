# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# 49.itertools.combinations_with_replacement().py

from itertools import combinations_with_replacement

if __name__ == '__main__':
    inp_list = input().split()
    # print(inp_list)
    
    str_inp= inp_list[0]
    str_list = list(str_inp)
    str_list.sort()
    # print(str_list)
    
    str_len = int(inp_list[1])
    # print(str_list)
    # print(str_len)
    str_perm = [''.join(p) for p in combinations_with_replacement(str_list, str_len)] 
    for i in range(len(str_perm)):
        print(str_perm[i])
