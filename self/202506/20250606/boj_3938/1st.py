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


def spfa(src, sink, G):
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
        while n != src:
            edge = G[pre[n]][indx[n]]
            edge.c -= 1
            G[n][edge.inv].c += 1

            n = pre[n]

        ans += dist[sink]

    return ans


def solve():
    while True:
        N = int(input())
        if not N: break

        src, sink = 366<<1, 366<<1|1
        G = [[] for _ in range(sink+1)]
        set_edge(src, 1<<1, 2, 0, G)
        set_edge(365<<1|1, sink, 2, 0, G)
        for i in range(1, 366): set_edge(i<<1, i<<1|1, float("inf"), 0, G)
        for u in range(1, 365): set_edge(u<<1|1, (u+1)<<1, float("inf"), 0, G)

        for _ in range(N):
            i, j, w = map(int, input().split())
            set_edge(i<<1, j<<1|1, 1, w, G)

        print(-spfa(src, sink, G))

    return


if __name__ == "__main__":
    solve()