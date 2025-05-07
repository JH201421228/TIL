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
    G[u].append(Edge(v, c, -d, len(G[v])))
    G[v].append(Edge(u, 0, d, len(G[u])-1))

    return


def solve():
    ans = 0

    while True:
        pre, indx, dist, checker = [-1] * (sink+1), [-1] * (sink+1), [float("inf")] * (sink+1), [0] * (sink+1)
        q = deque([src])
        dist[src] = 0
        checker[src] = 1

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

    return -ans - 3_000_000


N = int(input())
stories = list(map(int, input().split()))

src, sink = N+5, N+6
G = [[] for _ in range(sink+1)]

for v in range(1, 4):
    set_edge(src, v, 1, 1_000_000)
    set_edge(src, v, stories[v-1]-1, 0)

set_edge(src, 4, float("inf"), 0)

for u in range(5, src):
    temp = list(map(int, input().split()))

    set_edge(u, sink, 1, 0)

    for v in range(1, 4):
        set_edge(v, u, 1, temp[v-1])

    set_edge(4, u, 1, 0)

print(solve())