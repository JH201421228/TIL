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


def init():
    for t in range(int(input())):
        print(f"Case #{t+1}: {solve()}")

    return


def spfa(src, sink, G):
    res = 0

    while True:
        pre = [-1] * (sink+1)
        indx = [-1] * (sink+1)
        checker = [0] * (sink+1)
        dist = [float("inf")] * (sink+1)
        q = deque([src])
        checker[src] = 1
        dist[src] = 0

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

        if pre[sink] == -1: break;

        flow = float("inf")
        n = sink
        while n != src:
            edge = G[pre[n]][indx[n]]
            flow = min(flow, edge.c)

            n = pre[n]

        n = sink
        while n != src:
            edge = G[pre[n]][indx[n]]
            edge.c -= flow
            G[n][edge.inv].c += flow

            n = pre[n]

        res -= dist[sink]*flow

    return res


def solve():
    N, A, B, C, D, E, F = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(3)]

    src, sink = 7, 8
    G = [[] for _ in range(9)]

    set_edge(src, 1, A, 0, G)
    set_edge(src, 2, B, 0, G)
    set_edge(src, 3, C, 0, G)

    set_edge(4, sink, D, 0, G)
    set_edge(5, sink, E, 0, G)
    set_edge(6, sink, F, 0, G)

    for u in range(3):
        for v in range(3):
            set_edge(u+1, v+4, N, -arr[u][v], G)


    return spfa(src, sink, G)


if __name__ == "__main__":
    init()