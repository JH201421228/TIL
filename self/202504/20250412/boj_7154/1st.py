import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


satisfaction = [(4, 3, 2, 1), (8, 7, 6, 5), (12, 11, 10, 9)]

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break

    ans, src, sink = 0, N+M+1, N+M+2
    G = [[] for _ in range(sink+1)]
    F = [[0] * (sink+1) for _ in range(sink+1)]
    C = [[0] * (sink+1) for _ in range(sink+1)]
    D = [[0] * (sink+1) for _ in range(sink+1)]

    for i in range(N):
        C[i+M+1][sink] = int(input())
        G[i+M+1].append(sink)
        G[sink].append(i+M+1)

    for i in range(M):
        u = i+1

        C[src][u] = 1
        G[src].append(u)
        G[u].append(src)

        temp = list(map(int, input().split()))
        grade = temp[0]
        for idx in range(1, 5):
            v = temp[idx]+1+M
            G[u].append(v)
            G[v].append(u)
            D[u][v] = -satisfaction[grade-1][idx-1]
            D[v][u] = satisfaction[grade-1][idx-1]
            C[u][v] = 1

    while True:
        pre, dist, checker = [-1] * (sink+1), [float("inf")] * (sink+1), [0] * (sink+1)
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
                        q.append(x)
                        checker[x] = 1

        if pre[sink] == -1: break

        n = sink
        while n != src:
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D[pre[n]][n]

            n = pre[n]

    print(-ans)