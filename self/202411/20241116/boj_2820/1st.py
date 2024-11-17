import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(50_000)
input = sys.stdin.readline


def dfs(n):
    global cnt
    A[n] = cnt = cnt+1

    for x in G[n]:
        dfs(x)

    E[n] = cnt

def I(s, e, idx):
    if s == e:
        tree[idx] = F[s]
        return

    mid = (s+e) >> 1

    I(s, mid, idx*2)
    I(mid+1, e, idx*2+1)

def lazy_U(s, e, idx):
    if lazy[idx]:
        if s == e:
            tree[idx] += lazy[idx]
        else:
            lazy[idx*2] += lazy[idx]
            lazy[idx*2+1] += lazy[idx]
        lazy[idx] = 0

def S(s, e, idx, i):
    lazy_U(s, e, idx)

    if i > e or i < s:
        return 0

    if s == e:
        return tree[idx]

    mid = (s+e) >> 1

    return S(s, mid, idx*2, i) + S(mid+1, e, idx*2+1, i)

def U(s, e, idx, l, r, v):
    lazy_U(s, e, idx)

    if s > r or e < l:
        return

    if s >= l and e <= r:
        lazy[idx] += v
        lazy_U(s, e, idx)
        return

    mid = (s+e) >> 1

    U(s, mid, idx*2, l, r, v)
    U(mid+1, e, idx*2+1, l, r, v)
    tree[idx] = tree[idx*2] + tree[idx*2+1]


N, M = map(int, input().split())
F = [0] * (N+1)
G = [[] for _ in range(N+1)]
A = [0] * (N+1)
E = [0] * (N+1)
cnt = 0
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

F[1] = int(input())
for i in range(N-1):
    temp = list(map(int, input().split()))
    F[i+2] = temp[0]
    G[temp[1]].append(i+2)

dfs(1)

I(1, N, 1)

for _ in range(M):
    temp = list(map(str, input().split()))

    if temp[0] == "p":
        U(1, N, 1, A[int(temp[1])], E[int(temp[1])], int(temp[2]))
        U(1, N, 1, A[int(temp[1])], A[int(temp[1])], -int(temp[2]))
    else:
        print(S(1, N, 1, A[int(temp[1])]))