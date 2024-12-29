import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(src, sink, n):
    L = [-1] * (n+1)
    L[src] = 0
    q = deque([src])

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

def dfs(u, sink, L):
    if u == sink:
        return 1

    for v in G[u]:
        if L[v] == L[u]+1 and C[(u, v)] > 0:
            k = dfs(v, sink, L)
            if k:
                C[(u, v)] = 0
                C[(v, u)] = 1
                return 1

    return 0

def get_ans(src, sink, n):
    ans = 0

    while True:
        L = bfs(src, sink, n)

        if L:
            while True:
                flow = dfs(src, sink, L)
                if not flow:
                    break
                ans += flow
        else:
            break

    return ans

N, P = map(int, input().split())

G = [[] for _ in range(N+1)]
C = defaultdict(int)

for _ in range(P):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    C[(u, v)] = 1
    C[(v, u)] = 0

print(get_ans(1, 2, N))