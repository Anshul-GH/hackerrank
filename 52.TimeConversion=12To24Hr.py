# https://www.hackerrank.com/challenges/time-conversion/problem
# 52.TimeConversion=12To24Hr.py


#!/bin/python3
from datetime import datetime
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Using datetime library to convert time to military standard
    tmp_time = str(s[:-2] + ' ' + s[-2:])
    tmp_time = datetime.strptime(tmp_time,'%I:%M:%S %p')
    tmp_time = str(tmp_time.time())
    
    return tmp_time
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

