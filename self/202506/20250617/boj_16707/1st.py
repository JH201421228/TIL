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


def spfa(src, sink, length, G):
    pre = [-1] * length
    indx = [-1] * length
    dist = [float("inf")] * length
    checker = [0] * length

    q = deque([src])
    dist[src] = 0
    checker[src] = 1

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

    n = sink
    while n != src:
        edge = G[pre[n]][indx[n]]
        edge.c -= 1
        G[n][edge.inv].c += 1

        n = pre[n]

    return dist[sink]


def solve():
    N, M = map(int, input().split())

    G = [[] for _ in range((N+1)<<1)]

    for n in range(1, N+1):
        set_edge(n<<1, n<<1|1, float("inf"), 0, G)

    for _ in range(M):
        u, v, d = map(int, input().split())
        set_edge(u<<1|1, v<<1, 1, d, G)
        set_edge(v<<1|1, u<<1, 1, d, G)

    print(spfa(2<<1, 1<<1|1, (N+1)<<1, G) + spfa(2<<1, N<<1|1, (N+1)<<1, G))

    return


if __name__ == "__main__":
    solve()