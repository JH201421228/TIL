import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


class Edge:
    def __init__(self, x, c, d, inv):
        self.x = x
        self.c = c
        self.d = d
        self.inv = inv


def set_edge(u, v, c, d, G):
    G[u].append(Edge(v, c, d, len(G[v])))
    G[v].append(Edge(u, 0, -d, len(G[u])-1))

    return


def setting(i_s, i_e, j_s, j_e, d, G):
    for u in range(i_s, i_e):
        for v in range(j_s, j_e):
            set_edge(u, v, 1, d, G)


def batch_edge(A, B, C, D, E, F, N, arr, G):
    setting(1, A+1, N+1, N+D+1, -arr[0][0], G)
    setting(1, A+1, N+D+1, N+D+E+1, -arr[0][1], G)
    setting(1, A+1, N+D+E+1, 2*N+1, -arr[0][2], G)

    setting(A+1, A+B+1, N+1, N+D+1, -arr[1][0], G)
    setting(A+1, A+B+1, N+D+1, N+D+E+1, -arr[1][1], G)
    setting(A+1, A+B+1, N+D+E+1, 2*N+1, -arr[1][2], G)

    setting(A+B+1, N+1, N+1, N+D+1, -arr[2][0], G)
    setting(A+B+1, N+1, N+D+1, N+D+E+1, -arr[2][1], G)
    setting(A+B+1, N+1, N+D+E+1, 2*N+1, -arr[2][2], G)

    return


def init():
    N, A, B, C, D, E, F = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(3)]

    src, sink = 2*N+1, 2*N+2
    G = [[] for _ in range(sink+1)]

    for v in range(1, N+1):
        set_edge(src, v, 1, 0, G)
        set_edge(v+N, sink, 1, 0, G)

    batch_edge(A, B, C, D, E, F, N, arr, G)


    return spfa(src, sink, G)


def spfa(src, sink, G):
    ans = 0

    while True:
        pre = [-1] * (sink+1)
        indx = [-1] * (sink+1)
        checker = [0] * (sink+1)
        dist = [float("inf")] * (sink+1)
        dist[src] = 0
        checker[src] = 1
        q = deque([src])

        while q:
            n = q.popleft()
            checker[n] = 0

            for idx, edge in enumerate(G[n]):
                if edge.c and dist[edge.x] > dist[n] + edge.d:
                    dist[edge.x] = dist[n] + edge.d
                    pre[edge.x] = n
                    indx[edge.x] = idx

                    if not checker[edge.x]:
                        checker[edge.x] = 1
                        q.append(edge.x)

        if pre[sink] == -1: break

        n = sink
        while n != src:
            edge = G[pre[n]][indx[n]]
            edge.c -= 1
            G[n][edge.inv].c += 1

            n = pre[n]

        ans += dist[sink]

    return -ans


def solve():
    for t in range(int(input())):
        print(f"Case #{t+1}:", init())

    return


if __name__ == "__main__":
    solve()