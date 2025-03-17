import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
src, sink, trash = N*M+1, N*M+2, N*M+3

B = [list(input().rstrip()) for _ in range(N)]

G = [[] for _ in range(N*M+4)]
C = [[0] * (N*M+4) for _ in range(N*M+4)]
D = [[0] * (N*M+4) for _ in range(N*M+4)]
F = [[0] * (N*M+4) for _ in range(N*M+4)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
grades = [(10, 8, 7, 5, 1), (8, 6, 4, 3, 1), (7, 4, 3, 2, 1), (5, 3, 2, 2, 1), (1, 1, 1, 1, 0)]
T = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
ans = 0

for i in range(N):
    for j in range((i+1)%2, M, 2):
        v = i * M + j + 1

        G[v].append(sink)
        G[sink].append(v)
        C[v][sink] = 1

    for j in range(i%2, M, 2):
        u = i * M + j + 1

        G[src].append(u)
        G[u].append(src)
        G[u].append(sink)
        G[sink].append(u)
        C[u][sink] = 1
        C[src][u] = 1

        for di, dj in delta:
            xi, xj = i+di, j+dj
            if xi >= 0 and xi < N and xj >= 0 and xj < M:
                v = xi * M + xj + 1
                G[u].append(v)
                G[v].append(u)
                C[u][v] = 1
                D[u][v] = -grades[T[B[i][j]]][T[B[xi][xj]]]
                D[v][u] = -D[u][v]

while True:
    pre, dist, checker = [-1] * (N*M+4), [float("inf")] * (N*M+4), [0] * (N*M+4)
    q = deque([src])
    checker[src] = 1
    dist[src] = 0

    while q:
        n = q.popleft()
        checker[n] = 0

        for x in G[n]:
            if C[n][x] > F[n][x] and dist[x] > dist[n] + D[n][x]:
                dist[x] = dist[n] + D[n][x]
                pre[x] = n

                if not checker[x]:
                    checker[x] = 1
                    q.append(x)

    if pre[sink] == -1: break

    n = sink
    while n != src:
        F[pre[n]][n] += 1
        F[n][pre[n]] -= 1
        ans += D[pre[n]][n]

        n = pre[n]

print(-ans)