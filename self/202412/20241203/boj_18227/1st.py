import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(400_000)
input = sys.stdin.readline


def dfs(n):
    global cnt, order
    A[n] = cnt = cnt+1
    W[n] = order = order+1
    for x in G[n]:
        if not A[x]:
            dfs(x)
    E[n] = cnt
    order -= 1

def U(idx):
    while idx < N+1:
        tree[idx] += 1
        idx += (idx & -idx)

def S(idx):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= (idx & -idx)
    return res

N, C = map(int, input().split())

G = [[] for _ in range(N+1)]
A = [0] * (N+1)
E = [0] * (N+1)
W = [0] * (N+1)
cnt = 0
order = 0

tree = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs(C)

for _ in range(int(input())):
    u, v = map(int, input().split())

    if u == 1:
        U(A[v])
    else:
        print(W[v] * (S(E[v]) - S(A[v]-1)))