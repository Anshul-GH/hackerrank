# https://www.hackerrank.com/challenges/time-conversion/problem
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#!/bin/python3

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s_split = s.split(':')
    
    # Validate the time attributes meet the constraints
    s_split[0]
    
    s_join = ''
    if (int(s_split[0]) in range(1,13)) and (int(s_split[1]) in range(0,60)) and (int(s_split[2][:-2]) in range(0,60)):
        if "PM" in s:
            if s_split[0] != '12':
                s_split[0] = str(int(s_split[0]) + 12)
            s_split[-1] = s_split[-1][:-2]
            s_join = ':'.join(s_split)        
        elif "AM" in s:
            if s_split[0] == '12':
                s_split[0] = '00'
            s_split[-1] = s_split[-1][:-2]
            s_join = ':'.join(s_split)        
        else:
            s_join = s
    
    return s_join

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
