import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 그냥 돌리다가 음수를 반환하면 stop
# 음수를 반환하면 하나도 안 들어간 스토리들만 1 남기고 돌리기

class Edge:
    def __init__(self, x, c, d, inv):
        self.x = x
        self.c = c
        self.d = d
        self.inv = inv

def set_edge(u, v, c, d):
    G[u].append(Edge(v, c, -d, len(G[v])))
    G[v].append(Edge(u, 0, d, len(G[u])-1))

def solve(isNegative):
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

    if pre[sink] == -1: return 0

    if dist[sink] > 0 and isNegative: return dist[sink]

    n = sink

    while n != src:
        edge = G[pre[n]][indx[n]]
        edge.c -= 1
        G[n][edge.inv].c += 1

        n = pre[n]

    return dist[sink]


N = int(input())
arr = list(map(int, input().split()))
src, sink = N+4, N+5
G = [[] for _ in range(sink+1)]

for idx in range(3):
    set_edge(src, idx+1, arr[idx], 0)

for v in range(4, src):
    temp = list(map(int, input().split()))
    set_edge(v, sink, 1, 0)
    for u in range(1, 4):
        set_edge(u, v, 1, temp[u-1])

ans = 0

for _ in range(N-3):
    tmp = solve(True)

    if tmp < 0: ans += tmp
    else: break

cnt = 0

for v in range(3):
    edge = G[src][v]
    if edge.c < arr[v]: edge.c = 0
    else:
        edge.c = 1
        cnt += 1

for _ in range(cnt):
    ans += solve(False)

print(-ans)