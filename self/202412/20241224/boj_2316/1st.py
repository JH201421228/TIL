import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline


def set_edge(i, j):
    G[i].append(j)
    G[j].append(i) #반례2
    C[(i, j)] = 1
    C[(j, i)] = 0 #반례2

def bfs(src, sink, n):
    L = [-1] * (2*n+1) #여기 반례
    L[src] = 0
    q = deque([src])

    while q:
        u = q.popleft()
        for v in G[u]:
            if L[v] == -1 and C[(u, v)] > 0:
                L[v] = L[u] + 1
                q.append(v)

    if L[sink] != -1:
        return L
    else:
        return []

def dfs(u, sink, L):
    if u == sink:
        return 1

    for v in G[u]:
        if L[v] == L[u]+1 and C[(u, v)] > 0:
            k = dfs(v, sink, L)
            if k:
                C[(u, v)] -= k
                C[(v, u)] += k #반례2
                return k

    return 0

def max_flow(src, sink):
    total = 0
    while True:
        L = bfs(src, sink, N)
        if L:
            while True:
                flow = dfs(src, sink, L)
                if not flow:
                    break
                total += flow
        else:
            return total


N, P = map(int, input().split())

G = [[] for _ in range(2*N+1)]
C = defaultdict(int)

for i in range(3, N+1):
    set_edge(i, i+N)


for _ in range(P):
    u, v = map(int, input().split())

    if u > 2:
        set_edge(u+N, v)
    else:
        set_edge(u, v)

    if v > 2:
        set_edge(v+N, u)
    else:
        set_edge(v, u)

print(max_flow(1, 2))