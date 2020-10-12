'''
Print all combinations of balanced parentheses

  Input : n=1
  Output: {}

  Input : n=2
  Output:
  {}{}
  {{}}

    n = 3
    {}{}{}
    {{}}{}
    {}{{}}
    {{{}}}

   f(n){}
   {}f(n)
   {f(n)}


{{}}}{{}
    
'''

# br_open = '{'
# counter += 1

# br_close = '}'
# counter -= 1


# count = int(input())

# for i in ran


def print_patterns(inpt, pattern):
    f1 = '{}'
    if inpt == 1:
        if pattern == '':
            pattern = f1
        else:
            for val in pattern:
                pattern.append(f1 + str(val))
                pattern.append(str(val) + f1)
                pattern.append('{' + str() + '}')


            # pattern += f1
            # pattern = f1 + pattern
            # pattern = '{' + pattern + '}'
            #print(pattern)
    else:
        pattern.append(f1)
        print_patterns(inpt - 1, pattern)
    
    # return pattern



if __name__ == "__main__":    
    inpt = int(input())
    pattern = []
    # pattern = 
    print_patterns(inpt, pattern)

    print(pattern)

