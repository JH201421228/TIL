import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline


def set_edge(u, v, w):
    G[u].append(v)
    G[v].append(u)
    C[(u, v)] = 1
    C[(v, u)] = 0
    W[(u, v)] = w
    W[(v, u)] = -w

def bfs(src, sink):
    L = [-1] * (sink+1)
    q = deque([src])
    L[src] = 0

    while q:
        u = q.popleft()

        for v in G[u]:
            if L[v] == -1 and C[(u, v)] > 0:
                L[v] = L[u]+1
                q.append(v)

    if L[sink] == -1:
        return []
    else:
        return L

def dfs(u, sink, flow, L):
    if u == sink:
        return flow

    for v in G[u]:
        if L[v] == L[u]+1 and C[(u, v)] > 0:
            flow =


N, M = map(int, input().split())

G = [[] for _ in range(N+M+3)]
# N+1 src, N+2 sink

C = defaultdict(int)
W = defaultdict(int)

for i in range(N):
    temp = list(map(int, input().split()))

    for idx in range(temp[0]):
        G[i+1].append(N+temp[2*idx+1])
        G[N+temp[2*idx+1]].append(i+1)
        C[(i+1, N+temp[2*idx+1])] = 1
        C[(N+temp[2*idx+1], i+1)] = 0
        W[(i+1, N+temp[2*idx+1])] = temp[2*idx+2]
        W[(N+temp[2*idx+1], i+1)] = -temp[2*idx+2]