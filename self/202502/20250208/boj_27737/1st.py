import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(i, j):
    q = deque([(i, j)])
    V[i][j] = 1
    res = 1

    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii >= 0 and ii < N and jj >= 0 and jj < N and not V[ii][jj] and not farm[ii][jj]:
                V[ii][jj] = 1
                q.append((ii, jj))
                res += 1

    return res


N, M, K = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
V = [[0] * N for _ in range(N)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
afford = []

for i in range(N):
    for j in range(N):
        if not V[i][j] and not farm[i][j]:
            afford.append(bfs(i, j))

ans = 0
for aff in afford:
    ans += (aff // K)
    if aff % K:
        ans += 1

if ans > M or not ans:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M-ans)