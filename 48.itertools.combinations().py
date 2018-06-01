# https://www.hackerrank.com/challenges/itertools-combinations/submissions/code/73964900
# 48.itertools.combinations().py

from itertools import combinations

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
    str_perm = []
      
    
    for i in range(str_len):
        temp_list = [''.join(p) for p in combinations(str_list, i + 1)]
        # print(temp_list)
        # temp_list.sort()
        str_perm.extend(temp_list)
    # str_perm.sort(key=len)
    
    for i in range(len(str_perm)):
        print(str_perm[i])
