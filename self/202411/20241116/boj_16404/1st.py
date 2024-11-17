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
        if s == e:
            tree[idx] += lazy[idx]
        else:
            lazy[idx*2] += lazy[idx]
            lazy[idx*2+1] += lazy[idx]
        lazy[idx] = 0

def S(s, e, idx, i):
    lazy_U(s, e, idx)

    if s > i or e < i:
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
A = [0] * (N+1)
E = [0] * (N+1)
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

temp = list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for i in range(1, N):
    G[temp[i]].append(i+1)

cnt = 0

dfs(1)

for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        U(1, N, 1, A[temp[1]], E[temp[1]], temp[2])
    else:
        print(S(1, N, 1, A[temp[1]]))