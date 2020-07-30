'''
https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
    # binary equivalent of n
    binary = bin(number).lstrip("0b")
    binLen = len(str(binary))

    for i in range(1, number+1):
        print(str(i).rjust(binLen, " "), end=' ')
        print(str(oct(i).lstrip("0o")).rjust(binLen, " "), end=' ')
        print(str(hex(i).lstrip("0x")).upper().rjust(binLen, " "), end=' ')
        print(str(bin(i).lstrip("0b")).rjust(binLen, " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)