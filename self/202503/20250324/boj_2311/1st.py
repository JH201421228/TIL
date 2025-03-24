import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

src, sink, ans = N*2+1, N*2+2, 0

G = [[] for _ in range(N*2+3)]
C = [[0] * (N*2+3) for _ in range(N*2+3)]
F = [[0] * (N*2+3) for _ in range(N*2+3)]
D = [[0] * (N*2+3) for _ in range(N*2+3)]

G[src].append(1)
G[1].append(src)
C[src][1] = 2
C[1][1+N] = 1

G[2*N].append(sink)
G[sink].append(2*N)
C[2*N][sink] = 2
C[N][2*N] = 1

for i in range(1, N+1):
    u_i, u_o = i, i+N

    G[u_i].append(u_o)
    G[u_o].append(u_i)
    C[u_i][u_o] += 1

for _ in range(M):
    a, b, c = map(int, input().split())
    u_i, u_o, v_i, v_o = a, a+N, b, b+N

    G[u_o].append(v_i)
    G[v_i].append(u_o)
    C[u_o][v_i] = 1
    D[u_o][v_i], D[v_i][u_o] = c, -c

    G[v_o].append(u_i)
    G[u_i].append(v_o)
    C[v_o][u_i] = 1
    D[v_o][u_i], D[u_i][v_o] = c, -c

for _ in range(2):
    pre, dist, checker = [-1] * (2*N+3), [float("inf")] * (2*N+3), [0] * (2*N+3)
    q = deque([src])
    dist[src] = 0
    checker[src] = 1

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