# https://www.hackerrank.com/challenges/grading/problem
# Basic rounding off mathematical implementation

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    # Define the relevant variables
        
    # Logic
    for idx, val in enumerate(grades):
        val_mod = val % 5
        if (val > 37) and (val_mod > 2):
            grades[idx] = val + (5 - val_mod)

    return grades
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
