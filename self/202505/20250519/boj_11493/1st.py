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


def solve(src, sink):
    ans = 0

    while True:
        pre = [-1] * (sink+1)
        dist = [float("inf")] * (sink+1)
        checker = [0] * (sink+1)
        indx = [0] * (sink+1)
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


for _ in range(int(input())):
    N, M = map(int, input().split())
    src, sink = 2*N+2, 2*N+3

    G = [[] for _ in range(sink+1)]

    for u in range(1, N+1):
        set_edge(u<<1, u<<1|1, float("inf"), 0)

    for _ in range(M):
        x, y = map(int, input().split())
        set_edge(x<<1|1, y<<1, float("inf"), 1)
        set_edge(y<<1|1, x<<1, float("inf"), 1)

    temp = list(map(int, input().split()))
    for u in range(1, N+1):
        if not temp[u-1]: set_edge(u<<1|1, sink, 1, 0)

    temp = list(map(int, input().split()))
    for v in range(1, N+1):
        if not temp[v-1]: set_edge(src, v<<1, 1, 0)

    print(solve(src, sink))