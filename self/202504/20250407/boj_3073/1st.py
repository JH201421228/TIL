import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


while True:
    N, M = map(int, input().split())

    if not N and not M:
        break

    maps = [input().rstrip() for _ in range(N)]
    homes, children = [], []

    for n in range(N*M):
        i, j = n // M, n % M

        if maps[i][j] == 'H':
            homes.append((i, j))
        elif maps[i][j] == 'm':
            children.append((i, j))

    n, m = len(homes), len(children)
    src, sink = n+m+1, n+m+2
    G = [[] for _ in range(sink+1)]
    F = [[0] * (sink+1) for _ in range(sink+1)]
    C = [[0] * (sink+1) for _ in range(sink+1)]
    D = [[0] * (sink+1) for _ in range(sink+1)]

    for i in range(n):
        u = i+1
        G[src].append(u)
        G[u].append(src)
        C[src][u] = 1

    for i in range(m):
        u = i+1+n
        G[sink].append(u)
        G[u].append(sink)
        C[u][sink] = 1

    for i in range(n):
        h = homes[i]
        u = i+1
        for j in range(m):
            c = children[j]
            v = j+1+n

            G[u].append(v)
            G[v].append(u)
            C[u][v] = 1
            D[u][v] = abs(h[0]-c[0]) + abs(h[1]-c[1])
            D[v][u] = -D[u][v]

    ans = 0
    while True:
        pre = [-1] * (sink+1)
        dist = [float("inf")] * (sink+1)
        checker = [0] * (sink+1)
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

        if pre[sink] == -1:
            break

        n = sink
        while n != src:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D[pre[n]][n]

            n = pre[n]

    print(ans)