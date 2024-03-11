import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def i_want_rest():
    ans = 0
    check = 0
    while q:
        now = q.popleft()
        for dx in delta:
            if now + dx not in checker:
                checker[now + dx] = checker[now] + 1
                ans += checker[now] + 1
                check += 1
                q.append(now + dx)
                if check == K:
                    return ans


N, K = map(int, input().split())
sams = list(map(int, input().split()))
checker = dict()
delta = (-1, 1)
for sam in sams:
    checker[sam] = 0
q = deque([*sams])
# print(q)
# print(checker)
print(i_want_rest())
