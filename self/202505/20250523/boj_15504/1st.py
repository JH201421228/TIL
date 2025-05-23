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


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    H = list(map(int, input().split()))
    L = list(map(int, input().split()))

    src, sink = 2*N+2, 2*N+3
    G = [[] for _ in range(sink+1)]

    arr = []
    for idx in range(N):
        arr.append((A[idx], H[idx], L[idx]))

    arr.sort(reverse=True)

    set_edge(src, 1<<1, arr[0][2], arr[0][1], G)
    for v in range(2, N+1):
        set_edge(src, v<<1, arr[v-1][2]-1, arr[v-1][1], G)

    for u in range(2, N+1):
        set_edge(u<<1|1, sink, 1, arr[u-1][1], G)

    for u in range(1, N+1):
        for v in range(u+1, N+1):
            set_edge(u<<1, v<<1|1, 1, -(arr[u-1][0]^arr[v-1][0]), G)

    ans = 0
    while True:
        pre = [-1] * (sink+1)
        dist = [float("inf")] * (sink+1)
        checker = [0] * (sink+1)
        indx = [-1] * (sink+1)
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

    print(-ans)


if __name__ == "__main__":
    solve()