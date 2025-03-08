import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

T, src, sink = N+M+3, N+M+1, N+M+2

G = [[] for _ in range(T)]
F = [[0] * T for _ in range(T)]
D = [[0] * T for _ in range(T)]
C = [[0] * T for _ in range(T)]

for u in range(1, N+1):
    G[src].append(u)
    G[u].append(src)
    C[src][u] = 1

for u in range(N+1, N+M+1):
    G[sink].append(u)
    G[u].append(sink)
    C[u][sink] = 1

for u in range(1, N+1):
    temp = list(map(int, input().split()))

    for idx in range(len(temp)//2):
        v, c = temp[idx*2+1]+N, temp[idx*2+2]

        G[u].append(v)
        G[v].append(u)

        C[u][v] = 1
        D[u][v] = -c
        D[v][u] = c

ans = 0

while True:
    pre, dist, checker = [-1] * T, [float("inf")] * T, [0] * T

    q = deque([src])
    dist[src] = 0
    checker[src] = 1

    while q:
        n = q.popleft()
        checker[n] = 0

        for x in G[n]:
            if C[n][x] - F[n][x] > 0 and dist[x] > dist[n] + D[n][x]:
                dist[x] = dist[n] + D[n][x]
                pre[x] = n

                if not checker[x]:
                    q.append(x)
                    checker[x] = 1

    if pre[sink] == -1:
        break

    n = sink
    while n != src:
        F[pre[n]][n] += 1
        F[n][pre[n]] -= 1

        ans += D[pre[n]][n]

        n = pre[n]

cnt = 0
for inner in F:
    if inner[sink]:
        cnt += 1

print(cnt)
print(-ans)