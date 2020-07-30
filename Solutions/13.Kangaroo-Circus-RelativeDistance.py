# https://www.hackerrank.com/challenges/kangaroo/problem
# Simple logic of relative motion of two moving objects

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    dist_rel = x2 - x1
    jmp_cnt = 0
    met = False
    dist_trv = v2 - v1
    
    if dist_rel > 0 and dist_trv < 0:
        abs_dis_trv = abs(dist_trv)
        while(abs_dis_trv * jmp_cnt <= dist_rel):
            if abs_dis_trv * jmp_cnt == dist_rel:
                return 'YES'
                met = True
                break
            else:
                jmp_cnt += 1        
            
    if jmp_cnt == 0 or met == False:
        return 'NO'
    
    
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
