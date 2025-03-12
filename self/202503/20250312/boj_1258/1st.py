import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
src, sink = 2*N+1, 2*N+2

temp = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(sink+1)]
F = [[0] * (sink+1) for _ in range(sink+1)]
D = [[0] * (sink+1) for _ in range(sink+1)]
C = [[0] * (sink+1) for _ in range(sink+1)]

for u in range(1, N+1):
    G[src].append(u)
    G[u].append(src)
    C[src][u] = 1

    G[sink].append(u+N)
    G[u+N].append(sink)
    C[u+N][sink] = 1

for i in range(N):
    u = i+1
    for j in range(N):
        v = j+N+1

        G[u].append(v)
        G[v].append(u)

        C[u][v] = 1

        D[u][v], D[v][u] = temp[i][j], -temp[i][j]

ans = 0

while True:
    pre, dist, checker = [-1] * (sink+1), [float("inf")] * (sink+1), [0] * (sink+1)
    q = deque([src])
    dist[src], checker[src] = 0, 1

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

print(ans)