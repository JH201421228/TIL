import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

C = [[0] * 203 for _ in range(203)]
D = [[0] * 203 for _ in range(203)]
F = [[0] * 203 for _ in range(203)]

G = [[] for _ in range(203)]

src, sink = 201, 202

temp = list(map(int, input().split()))
for u in range(101, 101+N):
    G[u].append(sink)
    G[sink].append(u)
    C[u][sink] = temp[u-101]

temp = list(map(int, input().split()))
for v in range(1, 1+M):
    G[v].append(src)
    G[src].append(v)
    C[src][v] = temp[v-1]

for u in range(1, M+1):
    temp = list(map(int, input().split()))
    for v in range(101, 101+N):
        D[u][v], D[v][u] = temp[v-101], -temp[v-101]
        C[u][v] = float("inf")
        G[u].append(v)
        G[v].append(u)

ans = 0

while True:
    pre, dist, checker = [-1] * 203, [float("inf")] * 203, [0] * 203
    q = deque([src])
    dist[src] = 0
    checker[src] = 1

    while q:
        n = q.popleft()
        checker[n] = 0

        for x in G[n]:
            if (C[n][x] - F[n][x] > 0 and dist[x] > dist[n] + D[n][x]):
                dist[x] = dist[n] + D[n][x]
                pre[x] = n

                if not checker[x]:
                    q.append(x)
                    checker[x] = 1

    if pre[sink] == -1:
        break

    flow = float("inf")

    n = sink
    while n != src:
        flow = min(flow, C[pre[n]][n] - F[pre[n]][n])
        n = pre[n]

    n = sink

    while n != src:
        ans += (flow * D[pre[n]][n])
        F[pre[n]][n] += flow
        F[n][pre[n]] -= flow

        n = pre[n]

print(ans)