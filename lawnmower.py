#!/usr/bin/env python3

T = int(input())
N, M = map(int, input().split())

print(T, N, M)

for case in range(T):
    lawn = []
    for i in range(N):
        lawn.append(map(int, input().split()))

    for x in range(N):
        for y in range(M):
            val = lawn[x][y]

            if is_row_min(lawn[x][y], lawn)

    test = [[0 for y in range(M)] for x in range(N)]

    print('Case #{0}: {1}'.format(case + 1, matches))
