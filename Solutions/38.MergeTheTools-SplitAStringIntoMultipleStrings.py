# https://www.hackerrank.com/challenges/merge-the-tools/problem
# SplitAStringIntoMultipleStrings

def merge_the_tools(string, k):
    str_list = []
    str_list_cpy = []
    # str_tmp = ''
    cnt = 0
    for i in range(int(len(string)/k)):
        # print('i: ', i)
        str_tmp = ''
        while cnt < (k * (i + 1)):
            str_tmp += string[cnt]
            # print('str_tmp: ', str_tmp)
            # print('cnt before: ', cnt)
            cnt += 1
            # print('cnt after: ', cnt)
        str_list.append(str_tmp)
    
    
    for i in range(len(str_list)):
        str_tmp = ''
        for j in range(len(str_list[i])):
            if str_tmp.find(str_list[i][j]) == -1:
                str_tmp += str_list[i][j]
        str_list_cpy.append(str_tmp)
        
    for i in str_list_cpy:
        print(i)
