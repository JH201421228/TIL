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
    G[u].append(Edge(v ,c, -d, len(G[v])))
    G[v].append(Edge(u, 0, d, len(G[u])-1))

    return

def solve():
    N, M = map(int, input().split())
    horizontal, vertical = [], []

    for _ in range(N):
        horizontal.append(tuple(map(int, input().split())))

    for _ in range(M):
        vertical.append(tuple(map(int, input().split())))

    src, sink = N+M+1, N+M+2
    G = [[] for _ in range(N+M+3)]

    for u in range(1, N+1):
        set_edge(src, u, 1, 0, G)
        u_x1, u_y1, u_x2, u_y2, u_w = horizontal[u-1]

        for v in range(N+1, N+M+1):
            v_x1, v_y1, v_x2, v_y2, v_w = vertical[v-N-1]

            if v_x1 > min(u_x1, u_x2) and v_x1 < max(u_x1, u_x2) and u_y1 > min(v_y1, v_y2) and u_y1 < max(v_y1, v_y2):
                set_edge(u, v, 1, u_w*v_w, G)

    for v in range(N+1, N+M+1):
        set_edge(v, sink, 1, 0, G)

    cnt = 0
    ans = 0

    while True:
        checker, pre, indx, dist = [0] * (sink + 1), [-1] * (sink + 1), [-1] * (sink + 1), [float("inf")] * (sink + 1)
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

        cnt += 1

        n = sink

        while n != src:
            edge = G[pre[n]][indx[n]]
            edge.c -= 1
            G[n][edge.inv].c += 1
            n = pre[n]

        ans += dist[sink]

    return cnt, -ans

if __name__ == "__main__":

    for _ in range(int(input())):
        print(*solve())