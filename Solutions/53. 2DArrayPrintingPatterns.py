'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

https://www.hackerrank.com/challenges/alphabet-rangoli/problem

'''


# def print_rangoli(size):
#     # # ASCII starter for alphabets
#     # start = 97
#     # chrct = chr(start + size - 1)
#     # # print(chrct)

#     # length = 4*size - 3
    
#     # for i in range(2*size - 1):        
#     #     for j in range(length):            
#     #         if j == 2*size/2+1:
#     #             print(chr(start + size - 1 - i), end='')
#     #         else:
#     #             print('-', end='')
#     #     print()

#     width = 4*size - 3
#     start = 97
#     chrct = chr(start + size - 1)
      
#     # Print the pattern having a top triangle 
#     for i in range (0, int (size - 1)): 
#         pattern = ('-' + chr(start + size - 1 - i) + '-') * ((2 * i) + 1) 
#         print (pattern.center (width, '-')) 
      
#     # # Print GeeksforGeeks in the center 
#     # print ("GeeksforGeeks".center (width, '-')) 
      
#     # Print the pattern having  
#     # an inverted triangle 
#     i = int (size - 1) 
#     while i > 0: 
#         pattern = ('-' + chr(start + size - 1 - i) + '-') * ((2 * i) - 1) 
#         print (pattern.center (width, '-')) 
#         i = i-1
#     return



# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    print(data)
    
    items = list(range(n))
    print(items)

    print(items[:-1], items[::-1])

    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

n = int(input())
print_rangoli(n)