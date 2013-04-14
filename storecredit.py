#!/usr/bin/env python3

def solve_case(case):
    c = int(input())
    i = int(input())
    items = [int(x) for x in input().split(' ')]

    cases = [(x, y) for x in range(i) for y in range(i) if x < y]
    sums = [items[x] + items[y] for (x, y) in cases]
    result = max([x for x in sums if x <= c])

    for y in range(1, i):
        for x in range(i - 1):
            if x >= y:
                continue

            if items[x] + items[y] == result:
                print("Case #{0}: {1} {2}".format(case, x + 1, y + 1))

n = int(input())
for i in range(n):
    solve_case(i + 1)
