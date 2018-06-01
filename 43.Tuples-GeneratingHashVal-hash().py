# https://www.hackerrank.com/challenges/python-tuples/problem
# GeneratingHashVal-hash()

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_tuple = tuple(integer_list)
    hash_tuple = hash(int_tuple)
    
    print(hash_tuple)
    # print(int_tuple)
