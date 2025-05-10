import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, D = map(int, input().split())
monsters, items = [], []

for _ in range(N):
    A, X = map(int, input().split())
    if A == 1: monsters.append(X)
    else: items.append(X)

monsters.sort()
items.sort()

monsters, items = deque(monsters), deque(items)

ans = 0

while monsters:
    if monsters[0] < D:
        D += monsters.popleft()
        ans += 1
    else:
        if items:
            D *= items.popleft()
            ans += 1
        else:
            break

while items:
    items.popleft()
    ans += 1

print(ans)