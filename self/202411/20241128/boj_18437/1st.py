import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(200_000)
input = sys.stdin.readline


def dfs(n):
    global cnt
    A[n] = cnt = cnt+1
    for x in G[n]:
        dfs(x)
    E[n] = cnt

def lazy_U(s, e, idx):
    if lazy[idx]:
        if lazy[idx] == 1:
            tree[idx] = e-s+1
        else:
            tree[idx] = 0
        if s != e:
            lazy[idx*2] = lazy[idx]
            lazy[idx*2+1] = lazy[idx]
        lazy[idx] = 0

def U(s, e, idx, l, r, v):
    lazy_U(s, e, idx)

    if s > r or e < l:
        return

    if s >= l and e <= r:
        lazy[idx] = v
        lazy_U(s, e, idx)
        return

    mid = (s+e) >> 1
    U(s, mid, idx*2, l, r, v)
    U(mid+1, e, idx*2+1, l, r, v)
    tree[idx] = tree[idx*2] + tree[idx*2+1]

def S(s, e, idx, l ,r):
    lazy_U(s, e, idx)

    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return tree[idx]

    mid = (s+e) >> 1

    return S(s, mid, idx*2, l, r) + S(mid+1, e, idx*2+1, l, r)


N = int(input())

A = [0] * (N+1)
E = [0] * (N+1)
cnt = 0
G = [[] for _ in range(N+1)]
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

temp = list(map(int, input().split()))
for i in range(1, N):
    G[temp[i]].append(i+1)

dfs(1)

U(1, N, 1, A[1], E[1], 1)
for _ in range(int(input())):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        for x in G[temp[1]]:
            U(1, N, 1, A[x], E[x], 1)
    elif temp[0] == 2:
        for x in G[temp[1]]:
            U(1, N, 1, A[x], E[x], 2)
    else:
        ans = 0
        for x in G[temp[1]]:
            ans += S(1, N, 1, A[x], E[x])
        print(ans)