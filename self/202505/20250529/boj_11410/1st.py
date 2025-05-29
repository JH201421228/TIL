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
    G[u].append(Edge(v, c, -d, len(G[v])))
    G[v].append(Edge(u, 0, d, len(G[u])-1))

    return


def solve():
    N, P = map(int, input().split())
    G = [[] for _ in range(N+3)]
    src, sink = N+1, N+2

    set_edge(src, 1, P, 0, G)
    set_edge(N, sink, P, 0, G)
    for u in range(1, N): set_edge(u, u+1, float("inf"), 0, G)

    clients = [list(map(int, input().split())) for _ in range(N-1)]
    fees = [list(map(int, input().split())) for _ in range(N-1)]

    for u in range(1, N):
        for v in range(u+1, N+1): set_edge(u, v, clients[u-1][v-u-1], fees[u-1][v-u-1], G)

    ans = 0
    while True:
        pre = [-1] * (sink+1)
        dist = [float("inf")] * (sink+1)
        indx = [-1] * (sink+1)
        checker = [0] * (sink+1)
        q = deque([src])
        checker[src] = 1
        dist[src] = 0

        while q:
            n = q.popleft()
            checker[n] = 0

            for idx in range(len(G[n])):
                edge = G[n][idx]

                if edge.c and dist[edge.x] > dist[n] + edge.d:
                    dist[edge.x] = dist[n] + edge.d
                    pre[edge.x] = n
                    indx[edge.x] = idx

                    if not checker[edge.x]:
                        checker[edge.x] = 1
                        q.append(edge.x)

        if pre[sink] == -1: break

        n = sink
        flow = float("inf")
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

        ans += dist[sink] * flow

    return -ans

if __name__ == "__main__":
    print(solve())