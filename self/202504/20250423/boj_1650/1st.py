import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def set_edge(u, v, c, n, G, C, D):
    G[u].append(v)
    G[v].append(u)
    C[u][v] += n
    D[u][v], D[v][u] = c, -c


def solve():
    N, M = map(int, input().split())
    ans, src, sink = 0, 1, 2*N

    G = [[] for _ in range(2*N+1)]
    C = [[0] * (2*N+1) for _ in range(2*N+1)]
    D = [[0] * (2*N+1) for _ in range(2*N+1)]
    F = [[0] * (2*N+1) for _ in range(2*N+1)]

    for u in range(1, N+1):
        set_edge(u, u+N, 0, float("inf"), G, C, D)

    set_edge(1, N+1, 0, float("inf"), G, C, D)
    set_edge(N, 2*N, 0, float("inf"), G, C, D)

    for _ in range(M):
        P, Q, L = map(int, input().split())
        set_edge(P+N, Q, L, 1, G, C, D)
        set_edge(Q+N, P, L, 1, G, C, D)

    for _ in range(2):
        pre, dist, checker = [-1] * (2*N+1), [float("inf")] * (2*N+1), [0] * (2*N+1)
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

    print(ans)


if __name__ == "__main__":
    solve()