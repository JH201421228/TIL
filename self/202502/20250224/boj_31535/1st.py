import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(i, j):
    q = deque([(i, j)])
    V[i][j] = 0

    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii >= 0 and ii <= H and jj >= 0 and jj <= W and V[ii][jj] > V[i][j] + max(pool[i][j], pool[ii][jj]):
                V[ii][jj] = V[i][j] + max(pool[i][j], pool[ii][jj])
                q.append((ii, jj))

    return


W, H = map(int, input().split())
N, D = map(int, input().split())

L = list(map(int, input().split()))
P = list(map(int, input().split()))

delta = [(1, 0), (-1, 0), (0, 1)]

pool = []
V = [[float("inf")] * (W+1) for _ in range(H+1)]
idx = 0

for i in range(H):
    if i == L[idx]:
        idx += 1
    pool.append([P[idx]] * (W+1))
pool.append([P[-1]] * (W+1))

bfs(0, 0)

print(V[D][W])
