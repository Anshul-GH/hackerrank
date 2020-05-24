# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# AvgOfDictElemReadAsList

# from decimal import *
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    value = list(student_marks[query_name])
    # print(value)
    # getcontext().prec = 4
    avg = float(sum(value)/len(value))
    print("{0:.2f}".format(avg))
