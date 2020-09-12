'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    
    https://www.hackerrank.com/challenges/designer-door-mat/problem
    
    '''




# M = 3 * N

# center = int(M/2)

# for i in range(N):
#     # for j in range(M - center - i - 1):
#     #     print("-", end='')
#     # print('.|.')
#     # for j in range(M - center - i - 1):
#     #     print("-", end='')
#     # print()

#     for j in range(0, M-2*(i+1)-1, 2):
#         if j == (center-i-1):
#             for k in range(0, i+1, 2):
#                 print('.|.', end='')
#         print('-', end='')
#     print()

def print_rangoli(N, M):
    # Print the pattern having a top triangle 
    for i in range (0, int(N/2)): 
        pattern = '.|.' * ((2 * i) + 1) 
        print (pattern.center (M, '-')) 
        
    # Print Welcome in the center 
    print ("WELCOME".center (M, '-')) 
        
    # Print the pattern having  
    # an inverted triangle 
    i = int(N/2) 
    while i > 0: 
        pattern = '.|.' * ((2 * i) - 1) 
        print (pattern.center (M, '-')) 
        i = i-1
    
    return


if __name__ == '__main__':
    N, M = 0, 0
    try:
        values = input().split(' ')
        N = int(values[0])
        M = int(values[1])
    except ValueError as e:
        print(e)
    print_rangoli(N, M)