#!/usr/bin/env python3

class Case(object):

    def __init__(self):
        self.path = []
        self.count = 0

    def dfs(self, chests, keys):

        self.count += 1
        print(self.count, self.path)

        if not chests: return True

        if not keys: return False

        required = []
        available = keys[:]
        for chest in chests:
            required.append(chest[1])
            available.extend(chest[3:])

        for key in required:
            if key in available:
                available.remove(key)
            else:
                return False

        for i, chest in enumerate(chests):
            key = chest[1]
            if key in keys:
                keys.remove(key)
                keys.extend(chest[3:])
                chests.pop(i)

                self.path.append(chest[0])
                if self.dfs(chests, keys):
                    return self.path

                self.path.pop()
                keys.append(key)
                chests.insert(i, chest)
                for key in chest[3:]:
                    keys.remove(key)

T = int(input())
for case in range(T):
    K, N = map(int, input().split())
    keys = list(map(int, input().split()))

    chests = []
    for i in range(N):
        chest = [str(i + 1)] # Ci
        chest.extend(map(int, input().split()))
        chests.append(chest)

    res = Case().dfs(chests, keys)
    if res:
        status = ' '.join(res)
    else:
        status = 'IMPOSSIBLE'
    print('Case #{0}: {1}'.format(case + 1, status))

