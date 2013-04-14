#!/usr/bin/env python3

groups = [
        [' '],
        [],
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
        ]


def get_code(c):
    result = ""
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            if groups[i][j] == c:
                for k in range(j + 1):
                    result += str(i)
                return result


def solve_case(case):
    message = input()
    result = []
    for i in range(len(message)):
        c = message[i]
        next = get_code(c)
        if len(result) > 0 and result[-1:] == [next[:1]]:
            result += " "
        result += next
        
    print("Case #{0}: {1}".format(case, "".join(result)))


n = int(input())
for i in range(n):
    solve_case(i + 1)
