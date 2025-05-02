import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

delta = [(1, 0), (0, 1)]

def solve(N, src, sink):
    pre, dist, checker, indx = [-1] * (N**2+1), [-float("inf")] * (N**2+1), [0] * (N**2+1), [-1] * (N**2+1)
    q = deque([src])
    dist[src] = 0
    checker[src] = 1

    while q:
        n = q.popleft()
        checker[n] = 0

        for idx in range(len(G[n])):
            edge = G[n][idx]
            i, j = (n-1)//N, (n-1)%N
            if edge.c:
                if edge.c == float("inf") and dist[edge.x] < dist[n] + maze[i][j]:
                    dist[edge.x] = dist[n] + maze[i][j]
                    pre[edge.x] = n
                    indx[edge.x] = idx
                    if not checker[edge.x]:
                        checker[edge.x] = 1
                        q.append(edge.x)
                elif dist[edge.x] < dist[n] - D[n][edge.x]:
                    dist[edge.x] = dist[n] - D[n][edge.x]
                    pre[edge.x] = n
                    indx[edge.x] = idx
                    if not checker[edge.x]:
                        checker[edge.x] = 1
                        q.append(edge.x)
                # D[n][edge.x], maze[i][j] = maze[i][j], D[n][edge.x]




    if dist[sink] == -float("inf"): return 0

    n = sink
    while n != src:
        G[pre[n]][indx[n]].c -= 1
        G[n][G[pre[n]][indx[n]].inv].c += 1
        i, j = (n-1)//N, (n-1)%N
        D[n][pre[n]], maze[i][j] = maze[i][j], D[n][pre[n]]

        n = pre[n]

    return dist[sink]

def set_G(N):
    for i in range(N):
        for j in range(N):
            u = i*N+j+1
            for di, dj in delta:
                if verification(N, i+di, j+dj):
                    v = (i+di)*N+(j+dj)+1
                    G[u].append(Edge(v, float("inf"), len(G[v])))
                    G[v].append(Edge(u, 0, len(G[u])-1))

def verification(N, x, y):
    if x >= 0 and x < N and y >= 0 and y < N: return True
    return False

class Edge:
    def __init__(self, x, c, inv):
        self.x = x
        self.c = c
        self.inv = inv


N, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
src, sink = 1, N**2

ans = maze[0][0] + maze[-1][-1]
maze[0][0], maze[-1][-1] = 0, 0

G = [[] for _ in range(N**2+1)]
D = [[0] * (N**2+1) for _ in range(N**2+1)]

set_G(N)


print(solve(N, src, sink))

print(solve(N, src, sink))



print(solve(N, src, sink))



print(solve(N, src, sink))