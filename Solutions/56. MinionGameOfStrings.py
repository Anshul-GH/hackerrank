# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # split the string into chars
    chrs = [chrr.lower() for chrr in string]
    # print(chrs)

    # initialize vowels 
    vowels = ['a', 'e', 'i', 'o', 'u']

    # kevin's score
    score_kevin = 0

    # stuart's score
    score_stuart = 0

    for idx, val in enumerate(chrs):
        if val in vowels:
            score_kevin += len(string) - idx
        else:
            score_stuart += len(string) - idx

    # print("Kevin: ", score_kevin)
    # print("Stuart: ", score_stuart)

    if score_kevin < score_stuart:
        print('Stuart', score_stuart)
    elif score_kevin > score_stuart:
        print('Kevin', score_kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)