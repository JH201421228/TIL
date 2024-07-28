import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())

if N == 1 and M == 1:
    print(1)
    exit(0)

G = []

for _ in range(N):
    G.append(list(map(int, map(str, input().rstrip()))))

V = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
V[0][0][0] = 1

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque([(0, 0, 0)])

while q:
    i, j, k = q.popleft()

    for di, dj in delta:
        ii, jj = i+di, j+dj
        if ii >= 0 and ii < N and jj >= 0 and jj < M:
            if not G[ii][jj] and not V[ii][jj][k]:
                V[ii][jj][k] = V[i][j][k] + 1
                q.append((ii, jj, k))
                if ii == N-1 and jj == M-1:
                    print(V[ii][jj][k])
                    exit(0)

            elif G[ii][jj] and k < K and not V[ii][jj][k+1]:
                V[ii][jj][k+1] = V[i][j][k] + 1
                q.append((ii, jj, k+1))
                if ii == N-1 and jj == M-1:
                    print(V[ii][jj][k+1])
                    exit(0)

print(-1)