# https://www.hackerrank.com/challenges/exceptions/problem


test_case_count = int(input())

result = []

for i in range(test_case_count):
    inpt = input().split()
    a = inpt[0]
    b = inpt[1]
    
    try:
        # print(int(a) // int(b))
        result.append(int(a) // int(b))
    except ZeroDivisionError as e:
        # print("Error Code:", e)
        strg = "Error Code: " + str(e)
        result.append(strg)
    except ValueError as e:
        # print("Error Code:", e)
        strg = "Error Code: " + str(e)
        result.append(strg)

for strg in result:
    print(strg)