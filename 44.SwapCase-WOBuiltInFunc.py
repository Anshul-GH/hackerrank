# https://www.hackerrank.com/challenges/swap-case/problem
# Swap the case of string without using built in functions

def swap_case(s):
    swp_s = list(s)
    for i in range(len(swp_s)):
        if 65 <= ord(swp_s[i]) <= 90:
            swp_s[i] = chr(ord(swp_s[i]) + 32)
        elif 97 <= ord(swp_s[i]) <= 122:
            swp_s[i] = chr(ord(swp_s[i]) - 32)
    swp_s = ''.join(swp_s)
    # print(swp_s)
    return swp_s
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
