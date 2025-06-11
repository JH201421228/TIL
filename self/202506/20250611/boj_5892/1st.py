import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 전체 흙 양과, 목표 흙 양의 차를 통해 구매량과 매각량을 구해서 초기값 설정
# 현재 상태와 타겟 상태를 연결할 때, 버리고 사는게 싸면, 버리고 사는 비용으로 연결


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
    N, X, Y, Z = map(int, input().split())

    src, sink, cur, tar = (N+1)<<1, (N+1)<<1|1, 0, 0
    G = [[] for _ in range(sink+1)]

    for i in range(1, N+1):
        a, b = map(int, input().split())
        cur += a
        tar += b
        set_edge(src, i<<1, a, 0, G)
        set_edge(i<<1|1, sink, b, 0, G)

    ans = 0
    if tar > cur: ans += (tar-cur)*X
    else: ans += (cur-tar)*Y

    fee = X+Y
    for u in range(1, N+1):
        for v in range(1, N+1):
            base = abs(u-v) * Z
            charge = min(fee, base)
            set_edge(u<<1, v<<1|1, float("inf"), charge, G)

    while True:
        pre = [-1] * (sink+1)
        indx = [-1] * (sink+1)
        checker = [0] * (sink+1)
        dist = [float("inf")] * (sink+1)
        q = deque([src])
        dist[src] = 0
        checker[src] = 1

        while q:
            n = q.popleft()
            checker[n] = 0

            for idx in range(len(G[n])):
                edge = G[n][idx]

                if edge.c and dist[edge.x] > dist[n] + edge.d:
                    dist[edge.x] = dist[n]  + edge.d
                    pre[edge.x] = n
                    indx[edge.x] = idx

                    if not checker[edge.x]:
                        checker[edge.x] = 1
                        q.append(edge.x)

        if pre[sink] == -1: break

        n = sink
        flow = float("inf")
        while n != src:
            edge = G[pre[n]][indx[n]]
            flow = min(flow, edge.c)

            n = pre[n]

        n = sink
        while n != src:
            edge = G[pre[n]][indx[n]]
            edge.c -= flow
            G[n][edge.inv].c += flow

            n = pre[n]

        ans += dist[sink] * flow

    print(ans)

    return


if __name__ == "__main__":
    solve()