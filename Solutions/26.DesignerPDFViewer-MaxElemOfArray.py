# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Simple logic to map text/char to mathematical height and hence the area of rectangular block.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    wrd_lst = list(word)
    wrd_pos = [0]*len(wrd_lst)
    wrd_ht = [0]*len(wrd_pos)
    
    # print(wrd_lst)
    # print(wrd_pos)
    
    for i in range(len(wrd_lst)):
        wrd_pos[i] = ord(wrd_lst[i]) - 97
        
    for i in range(len(wrd_pos)):
        wrd_ht[i] = h[wrd_pos[i]]
    
    # print(wrd_ht)
    
    return (len(wrd_lst) * max(wrd_ht))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
