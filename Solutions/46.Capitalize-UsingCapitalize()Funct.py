# https://www.hackerrank.com/challenges/capitalize/problem
# UsingCapitalize()Funct to convert the string to just first letter capital for each word

#!/bin/python3

import math
import os
import random
import re
import sys

def capitalize(string):
    spl_str = list(string.split(' '))
    ret_str = ''
    for i in range(len(spl_str)):
        ret_str += spl_str[i].capitalize() + ' '
        
    return ret_str
