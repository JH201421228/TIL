import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def dfs(n):
    global cnt
    A[n] = cnt = cnt+1
    for x in G[n]:
        dfs(x)
    E[n] = cnt

def U(s, e, idx, i, v):
    if s > i or e < i:
        return

    if s == e:
        tree[idx] += v
        return

    mid = (s+e) >> 1

    U(s, mid, idx*2, i, v)
    U(mid+1, e, idx*2+1, i, v)
    tree[idx] = tree[idx*2] + tree[idx*2+1]

def S(s, e, idx, l, r):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return tree[idx]

    mid = (s+e) >> 1

    return S(s, mid, idx*2, l, r) + S(mid+1, e, idx*2+1, l, r)


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
A = [0] * (N+1)
E = [0] * (N+1)
cnt = 0
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

temp = list(map(int, input().split()))
for i in range(1, N):
    G[temp[i]].append(i+1)

dfs(1)

for _ in range(M):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        U(1, N, 1, A[temp[1]], temp[2])
    else:
        print(S(1, N, 1, A[temp[1]], E[temp[1]]))