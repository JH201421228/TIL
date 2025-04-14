import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(u):
    for v in G[u]:
        if V[v] == -1:
            V[v] = V[u]+1
            dfs(v)

    return


N, M, R = map(int, input().split())

G = [[] for _ in range(N+1)]
V = [-1] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for idx in range(1, N+1):
    G[idx].sort(reverse=True)

V[R] = 0
dfs(R)

for n in V[1:]: print(n)