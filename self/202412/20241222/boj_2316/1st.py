from collections import deque, defaultdict

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.capacity = defaultdict(int)

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] += cap
        self.capacity[(v, u)] += 0

    def bfs(self, src, sink):
        self.level = [-1] * self.n
        self.level[src] = 0
        queue = deque([src])
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if self.level[v] == -1 and self.capacity[(u, v)] > 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[sink] != -1

    def dfs(self, u, sink, flow):
        if u == sink:
            return flow
        for v in self.graph[u]:
            if self.level[v] == self.level[u] + 1 and self.capacity[(u, v)] > 0:
                pushed = self.dfs(v, sink, min(flow, self.capacity[(u, v)]))
                if pushed > 0:
                    self.capacity[(u, v)] -= pushed
                    self.capacity[(v, u)] += pushed
                    return pushed
        return 0

    def max_flow(self, src, sink):
        total_flow = 0
        while self.bfs(src, sink):
            while True:
                flow = self.dfs(src, sink, float('inf'))
                if flow == 0:
                    break
                total_flow += flow
        return total_flow

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n, p = map(int, data[0].split())
    dinic = Dinic(2 * n)  # Each node is split into in-node and out-node.

    for i in range(1, n + 1):
        if i != 1 and i != 2:  # Split nodes for 3 <= i <= n
            dinic.add_edge(i, i + n, 1)

    for line in data[1:]:
        u, v = map(int, line.split())
        if u > 2:
            u += n  # Convert to out-node for intermediate cities.
        dinic.add_edge(u, v, 1)
        dinic.add_edge(v, u, 1)

    # Compute max flow
    print(dinic.max_flow(1, 2))

if __name__ == "__main__":
    solve()
