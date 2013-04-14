#!/usr/bin/env python3

def solve_case(case):
    words = input().split()
    count = len(words)
    reverse = [words[count - i] for i in range(1, count + 1)]
    print("Case #{0}: {1}".format(case, " ".join(reverse)))

n = int(input())
for i in range(n):
    solve_case(i + 1)
