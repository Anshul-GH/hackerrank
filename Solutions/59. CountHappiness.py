# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == "__main__":
    n,m = input().split(' ')
    # m = int(input())

    arr = input().split(' ')
    # converting str values to int
    # arr = [int(val) for val in arr]

    a = input().split(' ')
    # converting str values to int
    # a = [int(val) for val in a]

    b = input().split(' ')
    # converting str values to int
    # b = [int(val) for val in b]

    
    # happiness count
    happiness = 0


    for num in arr:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1

    # print("happiness:", happiness)
    print(happiness)

