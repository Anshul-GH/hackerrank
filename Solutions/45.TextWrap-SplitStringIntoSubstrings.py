# https://www.hackerrank.com/challenges/text-wrap/problem
# SplitStringIntoSubstrings

def wrap(string, max_width):
    splt_string = ''
    ret_string = ''
    padding = max_width - (len(string) % max_width)
    # print(len(string))
    for i in range(padding):
        string += ' '
    # print(len(string))
    # splt_cnt = (len(str) + max_width - (len(str) % max_width)) / max_width
    iter_cnt = 0
    
    while iter_cnt < len(string):
        for i in range(max_width):
            splt_string += string[i + iter_cnt]
        ret_string += (str(splt_string)).strip() + '\n'
        iter_cnt += max_width
        splt_string = ''
    
    return ret_string
