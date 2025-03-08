import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

src, sink, nodes = N+M+1, N+M+2, N+M+3

G = [[] for _ in range(nodes)]
F = [[0] * nodes for _ in range(nodes)]
C = [[0] * nodes for _ in range(nodes)]
D = [[0] * nodes for _ in range(nodes)]

temp = list(map(int, input().split()))
for u in range(1, N+1):
    G[u].append(src)
    G[src].append(u)
    C[src][u] = temp[u-1]

temp = list(map(int, input().split()))
for u in range(N+1, N+M+1):
    G[sink].append(u)
    G[u].append(sink)
    C[u][sink] = temp[u-N-1]

for v in range(N+1, N+M+1):
    temp = list(map(int, input().split()))
    for u in range(1, N+1):
        G[u].append(v)
        G[v].append(u)
        C[u][v] = temp[u-1]

for v in range(N+1, N+M+1):
    temp = list(map(int, input().split()))
    for u in range(1, N+1):
        D[u][v] = temp[u-1]
        D[v][u] = -temp[u-1]

ans = 0

while True:
    pre, dist, checker = [-1] * nodes, [float("inf")] * nodes, [0] * nodes
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

    if pre[sink] == -1:
        break

    flow = float("inf")
    n = sink
    while n != src:
        flow = min(flow, C[pre[n]][n]-F[pre[n]][n])
        n = pre[n]

    n = sink
    while n != src:
        F[pre[n]][n] += flow
        F[n][pre[n]] -= flow
        ans += (D[pre[n]][n] * flow)
        n = pre[n]

cnt = 0

for idx in range(N+1, N+M+1):
    cnt += F[idx][sink]

print(cnt)
print(ans)