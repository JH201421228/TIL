import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1)]

def solve(src, sink):
    pre, dist, checker, indx = [-1] * (sink+1), [float("inf")] * (sink+1), [0] * (sink+1), [-1] * (sink+1)
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

    if dist[sink] == float("inf"): return 0

    n = sink
    while n != src:
        edge = G[pre[n]][indx[n]]
        edge.c -= 1
        G[n][edge.inv].c += 1

        n = pre[n]

    return dist[sink]


def set_edge(u, v, c, d):
    G[u].append(Edge(v, c, -d, len(G[v])))
    G[v].append(Edge(u, 0, d, len(G[u])-1))
    return

class Edge:
    def __init__(self, x, c, d, inv):
        self.x = x
        self.c = c
        self.d = d
        self.inv = inv

N, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
G = [[] for _ in range((N**2+1)<<1)]
src, sink = 2, (N**2)<<1|1

for n in range(1, N**2+1):
    set_edge(n<<1, n<<1|1, 1, maze[(n-1)//N][(n-1)%N])
    set_edge(n<<1, n<<1|1, float("inf"), 0)

for i in range(N):
    for j in range(N):
        u = N*i+j+1
        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii >= 0 and ii < N and jj >= 0 and jj < N:
                v = N*ii+jj+1
                set_edge(u<<1|1, v<<1, float("inf"), 0)

ans = 0
for _ in range(K):
    ans += solve(src, sink)

print(-ans)