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

    return


def solve():
    pre, dist, checker, indx = [-1] * (2*N+2), [float("inf")] * (2*N+2), [0] * (2*N+2), [-1] * (2*N+2)
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

    if pre[sink] == -1: return dist[sink]

    n = sink
    while n != src:
        edge = G[pre[n]][indx[n]]
        edge.c -= 1
        G[n][edge.inv].c += 1

        n = pre[n]

    return dist[sink]


N, M = map(int, input().split())

G = [[] for _ in range(2*N+2)]

for u in range(1, N+1): set_edge(u<<1, u<<1|1, 1, 0)

for _ in range(M):
    a, b, c = map(int, input().split())
    set_edge(b<<1|1, c<<1, 1, a)
    set_edge(c<<1|1, b<<1, 1, a)

a, b = map(int, input().split())
src, sink = a<<1, b<<1|1
set_edge(a<<1, a<<1|1, 1, 0)
set_edge(b<<1, b<<1|1, 1, 0)

ans = 0
for _ in range(2):
    ans += solve()

if ans == float("inf"): print(-1)
else: print(ans)
