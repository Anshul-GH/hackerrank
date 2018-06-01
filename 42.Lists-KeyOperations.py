# https://www.hackerrank.com/challenges/python-lists/problem
# Key operations on lists:
'''
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

if __name__ == '__main__':
    N = int(input())
    # inp_D = dict()
    opList = []
    for i in range(N):
        
        inpList = input().split()
        
        # Case 1: insert
        if inpList[0] == 'insert':
            opList.insert(int(inpList[1]), int(inpList[2]))
        # Case 2: print
        elif inpList[0] == 'print':
            print(opList)
        # Case 3: remove
        elif inpList[0] == 'remove':
            opList.remove(int(inpList[1]))
        # Case 4: append          
        elif inpList[0] == 'append':
            opList.append(int(inpList[1]))
        # Case 5: sort
        elif inpList[0] == 'sort':
            opList.sort()
        # Case 6: pop
        elif inpList[0] == 'pop':
            opList.pop()
        # Case 7: pop
        elif inpList[0] == 'reverse':
            opList.reverse()
