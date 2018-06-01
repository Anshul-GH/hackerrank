# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Find2ndHeighestValArr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # This should sort the array descending
    arr.sort(reverse=True)
    # Variable to hold the runnerup score
    run_scr = arr[-1]
    max_scr = max(arr)    
    i = 0
    while i < len(arr):
        if arr[i] < max_scr:
            run_scr = arr[i]
            break
        i += 1
    print(run_scr)
