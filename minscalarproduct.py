#!/usr/bin/env python3

def solve_case(case):
    n = int(input())
    v1 = sorted(map(int, input().split()))
    v2 = sorted(map(int, input().split()))

    product = 0
    for i in range(n):
        product += v1[i] * v2[n - i - 1]

    print('Case #{0}: {1}'.format(case, product))

T = int(input())
for i in range(T):
    solve_case(i + 1)
