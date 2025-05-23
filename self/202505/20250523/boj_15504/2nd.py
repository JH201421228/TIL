import sys
sys.stdin = open('input.txt')
from collections import deque

INF = 10**9

class Edge:
    def __init__(self, to, cap, cost, rev):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev  # 역방향 엣지

def add_edge(graph, u, v, cap, cost):
    graph[u].append(Edge(v, cap, cost, len(graph[v])))
    graph[v].append(Edge(u, 0, -cost, len(graph[u]) - 1))

def bfs(graph, s, t, msize):
    dist = [INF] * msize
    in_queue = [False] * msize
    prev_node = [-1] * msize
    prev_edge = [-1] * msize

    q = deque()
    dist[s] = 0
    q.append(s)
    in_queue[s] = True

    while q:
        u = q.popleft()
        in_queue[u] = False
        for i, e in enumerate(graph[u]):
            if e.cap > 0 and dist[e.to] > dist[u] + e.cost:
                dist[e.to] = dist[u] + e.cost
                prev_node[e.to] = u
                prev_edge[e.to] = i
                if not in_queue[e.to]:
                    q.append(e.to)
                    in_queue[e.to] = True

    if dist[t] == INF:
        return INF, 0

    flow = INF
    v = t
    while v != s:
        u = prev_node[v]
        flow = min(flow, graph[u][prev_edge[v]].cap)
        v = u

    v = t
    cost_sum = 0
    while v != s:
        u = prev_node[v]
        e = graph[u][prev_edge[v]]
        e.cap -= flow
        graph[v][e.rev].cap += flow
        cost_sum += e.cost
        v = u

    return cost_sum * flow, flow

def main():
    n = int(sys.stdin.readline())
    v = []

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        v.append((a[i], (b[i], c[i])))

    v.sort()

    msize = n * 2 + 2
    s, t = n * 2, n * 2 + 1
    graph = [[] for _ in range(msize)]

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            cost = -(v[i][0] ^ v[j][0])
            add_edge(graph, i, j + n, 1, cost)
        cap = v[i][1][1] - (0 if i == n - 1 else 1)
        add_edge(graph, s, i, cap, v[i][1][0])
        add_edge(graph, i + n, t, 1, v[i][1][0])

    total_cost = 0
    tc = n - 1
    while tc > 0:
        cost, flow = bfs(graph, s, t, msize)
        if cost == INF:
            break
        total_cost += cost
        tc -= 1

    print(-total_cost)

if __name__ == '__main__':
    main()
