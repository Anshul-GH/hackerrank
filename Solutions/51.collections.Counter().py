# https://www.hackerrank.com/challenges/collections-counter/problem
# 51.collections.Counter().py

from collections import Counter

if __name__ == '__main__':
    shoe_cnt = int(input())
    shoe_list = list(map(int, input().split()))
    # list(map(int, input().rstrip().split()))
    # print(shoe_cnt)
    # print(shoe_list)
    shoe_dict = dict()
    
    shoe_dict = Counter(shoe_list)
    shoe_dict = dict(shoe_dict)
    # print(shoe_dict) 
    cust_cnt = int(input())
    amt_made = 0
    for i in range(cust_cnt):
        size_amt = input().split()
        size = int(size_amt[0])
        amt = int(size_amt[1])
        if shoe_dict.get(size, -1) > 0:
            amt_made += amt
            shoe_dict[size] -= 1
            
    print(amt_made)
