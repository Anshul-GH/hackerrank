# from collections import defaultdict

# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")

# for i in d.items():
#     print(i)


# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem



def get_freq(n, m, n_list, m_list):
    for strg in m_list:
        idx_pos = [(idx+1) for idx, val in enumerate(n_list) if val == strg]
        if not idx_pos:
            print('-1', end=' ')
        else:
            for val in idx_pos:
                print(val, end=' ')
        print()



if __name__ == '__main__':
    n, m = 0, 0
    inpt = input().split()
    n = int(inpt[0])
    m = int(inpt[1])

    n_list = []
    m_list = []

    for i in range(n):
        n_list.append(input())
    
    for i in range(m):
        m_list.append(input())

    get_freq(n, m, n_list, m_list)

