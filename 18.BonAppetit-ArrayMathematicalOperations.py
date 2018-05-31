# https://www.hackerrank.com/challenges/bon-appetit/problem
# Mathematical operations within array - selective summation etc

# Enter your code here. Read input from STDIN. Print output to STDOUT
def refundOrFair(dishCosts, alrgDish, splAmtChrgd):
    totAmt = sum(dishCosts)
    # print(totAmt)
    # print(dishCosts[alrgDish])
    eligAmt = int((totAmt - dishCosts[alrgDish])/2)
    # print(eligAmt)
    if(eligAmt == splAmtChrgd):
        print('Bon Appetit')
    else:
        print(str(splAmtChrgd - eligAmt))
    

if __name__ == '__main__':
    dishPref = input().split()
    totDishes = int(dishPref[0])
    alrgDish = int(dishPref[1])
    
    dishCosts = list(map(int, input().rstrip().split()))
    splAmtChrgd = int(input())
    # print(totDishes)
    # print(alrgDish)
    # print(dishCosts)
    # print(splAmtChrgd)
    refundOrFair(dishCosts, alrgDish, splAmtChrgd)
