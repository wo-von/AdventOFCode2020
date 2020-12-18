#!/usr/bin/python3

import string

testcase1 = "2 * 3 + (4 * 5)" # becomes 26
testcase2 = "5 + (8 * 3 + 9 + 3 * 4 * 3)" # becomes 437
testcase3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))" # becomes 12240
testcase4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2" # becomes 13632

def parse_string_into_list(stg):
    result = list()
    for s in stg:
        if s in string.whitespace:
            continue
        else:
            result.append(s)
    return result

def do_the_math(strlst):
    '''
    gets a list with no whitespaces and paranthesis and  does the math from left to right with no
    prioritites
    '''
    if len(strlst) == 3:
        if strlst[1] == '*':
            return int(strlst[0]) * int(strlst[2])
        else:
            return int(strlst[0]) + int(strlst[2])
    else:
        temp = list()
        temp.append(str(do_the_math(strlst[:3])))
        temp = temp + strlst[3:]
        return do_the_math(temp)

def do_whole(lst):
    '''
    gets a list of strings, and starts putting it into a stack
    untill matching parens are found, then does the math and
    puts the result back into stack
    '''
    stack = list()
    if "(" and ")" not in lst:
        return do_the_math(lst)
    else:
        for e in lst:
            if e != ")":
                stack.append(e)
            else:
                temp = list()
                while True:
                    item = stack.pop()
                    if item == "(":
                        break
                    else:
                        temp.append(item)
                temp.reverse()
                result = str(do_the_math(temp))
                stack.append(result)
    return do_the_math(stack)

finalcount = list()
with open("input") as f:
    for line in f:
        listtemp = parse_string_into_list(line)
        finalcount.append(do_whole(listtemp))

print(sum(finalcount))
