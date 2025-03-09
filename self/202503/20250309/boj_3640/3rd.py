import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


while True:
    try:
        V, E = map(int, input().split())
    except:
        break

    ans = 0
    G = [[] for _ in range(2*V+1)]
    F = [[0] * (2*V+1) for _ in range(2*V+1)]
    C = [[0] * (2*V+1) for _ in range(2*V+1)]
    D = [[0] * (2*V+1) for _ in range(2*V+1)]

    for u in range(1, V+1):
        v = u+V
        G[u].append(v)
        G[v].append(u)
        C[u][v] = 1
    C[1][1+V] += 1
    C[V][2*V] += 1

    for _ in range(E):
        a, b, c = map(int, input().split())
        G[a+V].append(b)
        G[a].append(b+V)
        G[b+V].append(a)
        G[b].append(a+V)
        C[a+V][b] = 1
        D[a+V][b] = c

    for _ in range(2):
        pre, dist, chercker = [-1] * (2*V+1), [float("inf")] * (2*V+1), [0] * (2*V+1)
        q = deque([1])
        chercker[1], dist[1] = 1, 0

        while q:
            n = q.popleft()
            chercker[n] = 0

            for x in G[n]:
                if C[n][x] > F[n][x] and dist[x] > dist[n] + D[n][x]:
                    dist[x] = dist[n] + D[n][x]
                    pre[x] = n

                    if not chercker[x]:
                        q.append(x)
                        chercker[x] = 1

        n = 2*V
        while n != 1:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            D[n][pre[n]] = -D[pre[n]][n]
            ans += D[pre[n]][n]

            n = pre[n]

    print(ans)