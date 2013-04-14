#!/usr/bin/env python3

import re

l, d, n = map(int, input().split())

words = []
for i in range(d):
    words.append(input())

for i in range(n):
    case = i + 1
    pattern = input().replace('(', '[').replace(')', ']')
    matches = 0
    for word in words:
        if re.match(pattern, word):
            matches += 1
    print('Case #{0}: {1} '.format(case, matches))
