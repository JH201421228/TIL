import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def set_edge(u, v, G, C):
    G[u].append(v)
    G[v].append(u)
    C[u][v] = 1
    return


def solve():
    N, M = map(int, input().split())
    ans, src, sink = 0, 2*N+1, 2*N+2

    G = [[] for _ in range(sink+1)]
    C = [[0] * (sink+1) for _ in range(sink+1)]
    D = [[0] * (sink+1) for _ in range(sink+1)]
    F = [[0] * (sink+1) for _ in range(sink+1)]

    for i in range(1, N+1):
        set_edge(i, i+N, G, C)
        set_edge(src, i, G, C)
        set_edge(i+N, sink, G, C)
        D[i][i+N], D[i+N][i] = -1, 1

    for _ in range(M):
        u, v = map(int, input().split())
        set_edge(u+N, v, G, C)

    for _ in range(2):
        pre, dist, checker = [-1] * (sink+1), [float("inf")] * (sink+1), [0] * (sink+1)
        q = deque([src])
        checker[src] = 1
        dist[src] = 0

        while q:
            n = q.popleft()
            checker[n] = 0

            for x in G[n]:
                if C[n][x] > F[n][x] and dist[x] > dist[n] + D[n][x]:
                    pre[x] = n
                    dist[x] = dist[n] + D[n][x]

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


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()