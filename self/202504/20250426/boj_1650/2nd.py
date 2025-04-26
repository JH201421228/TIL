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


def set_edge(u, v, c, d):
    G[u].append(Edge(v, c, d, len(G[v])))
    G[v].append(Edge(u, 0, -d, len(G[u])-1))


def solve():
    src, sink = 2, (N<<1)|1
    pre, checker, dist, idx = [-1] * (sink+1), [0] * (sink+1), [float("inf")] * (sink+1), [-1] * (sink+1)
    q = deque([src])
    checker[src] = 1
    dist[src] = 0

    while q:
        n = q.popleft()
        checker[n] = 0

        for i, edge in enumerate(G[n]):
            if edge.c and dist[edge.x] > dist[n] + edge.d:
                dist[edge.x] = dist[n] + edge.d
                pre[edge.x] = n
                idx[edge.x] = i

                if not checker[edge.x]:
                    checker[edge.x] = 1
                    q.append(edge.x)

    n = sink
    while n != src:
        edge = G[pre[n]][idx[n]]
        edge.c -= 1
        G[n][edge.inv].c += 1

        n = pre[n]

    return dist[sink]

def main():
    for i in range(1, N+1):
        set_edge(i<<1, (i<<1)|1, float("inf"), 0)

    for _ in range(M):
        u, v, d = map(int, input().split())
        set_edge((u<<1)|1, v<<1, 1, d)
        set_edge((v<<1)|1, u<<1, 1, d)

    ans = 0

    for _ in range(2):
        ans += solve()

    print(ans)

N, M = map(int, input().split())
G = [[] for _ in range((N+1)<<1)]


if __name__ == "__main__":
    main()