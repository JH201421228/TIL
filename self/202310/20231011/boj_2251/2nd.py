import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dua_lipa(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        que.append((x, y))


def anne_marie():
    while que:
        x, y = que.popleft()
        z = c - x - y
        if not x:
            ans.append(z)
        # x -> y
        water = min(x, b - y)
        dua_lipa(x - water, y + water)
        # x -> z
        water = min(x, c - z)
        dua_lipa(x - water, y)
        # y -> x
        water = min(y, a - x)
        dua_lipa(x + water, y - water)
        # y -> z
        water = min(y, c - z)
        dua_lipa(x, y - water)
        # z -> x
        water = min(z, a - x)
        dua_lipa(x + water, y)
        # z -> y
        water = min(z, b - y)
        dua_lipa(x, y + water)


a, b, c = map(int, input().split())
que = deque([(0, 0)])

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True
ans = []

anne_marie()
ans.sort()
print(*ans)