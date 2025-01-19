import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

N, K, X = map(int, input().split())
A = [0] * 333
O = [0] * 333
C = [0] * 333
P = [0] * 333
T = [0] * 333
G = defaultdict(list)

def dfs(v):
    for i in G[v]:
        if C[i]:
            continue
        C[i] = 1
        if not P[i] or dfs(P[i]):
            P[i] = v
            return True
    return False

for i in range(1, N + 1):
    s, *groups = map(int, input().split())
    for t in groups:
        for k in range(1, X + 1):
            G[i].append((t - 1) * X + k - 1)

A[1:N + 1] = list(map(int, input().split()))
O[1:N + 1] = range(1, N + 1)
O[1:N + 1] = sorted(O[1:N + 1], key=lambda u: -A[u])

for i in range(1, N + 1):
    C = [0] * len(C)
    T = P[:]
    if not dfs(O[i]):
        P = T[:]

for i in range(1, K + 1):
    assigned = [j for j in range((i - 1) * X, i * X) if P[j]]
    print(len(assigned), *assigned)
