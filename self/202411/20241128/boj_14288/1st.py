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

def lazy_U(s, e, idx, lazy, tree):
    if lazy[idx]:
        tree[idx] += (e-s+1) * lazy[idx]
        if s != e:
            lazy[idx*2] += lazy[idx]
            lazy[idx*2+1] += lazy[idx]
        lazy[idx] = 0

def S(s, e, idx, l, r, lazy, tree):
    lazy_U(s, e, idx, lazy, tree)

    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return tree[idx]

    mid = (s+e) >> 1

    return S(s, mid, idx*2, l, r, lazy, tree) + S(mid+1, e, idx*2+1, l, r, lazy, tree)

def U(s, e, idx, l, r, v, lazy, tree):
    lazy_U(s, e, idx, lazy, tree)

    if s > r or e < l:
        return

    if s >= l and e <= r:
        lazy[idx] += v
        lazy_U(s, e, idx, lazy, tree)
        return

    mid = (s+e) >> 1

    U(s, mid, idx*2, l, r, v, lazy, tree)
    U(mid+1, e, idx*2+1, l, r, v, lazy, tree)
    tree[idx] = tree[idx*2] + tree[idx*2+1]


N, M = map(int, input().split())

A = [0] * (N+1)
E = [0] * (N+1)
cnt = 0
G = [[] for _ in range(N+1)]
tree1 = [0] * (4*N+1)
tree2 = [0] * (4*N+1)
lazy1 = [0] * (4*N+1)
lazy2 = [0] * (4*N+1)

temp = list(map(int, input().split()))
for i in range(1, N):
    G[temp[i]].append(i+1)

dfs(1)

is_down_direction = True

for _ in range(M):
    temp = list(map(int, input().split()))

    if temp[0] == 3:
        is_down_direction = not is_down_direction
    elif temp[0] == 1:
        if is_down_direction:
            U(1, N, 1, A[temp[1]], E[temp[1]], temp[2], lazy1, tree1)
        else:
            U(1, N, 1, A[temp[1]], A[temp[1]], temp[2], lazy2, tree2)
    else:
        print(S(1, N, 1, A[temp[1]], A[temp[1]], lazy1, tree1) + S(1, N, 1, A[temp[1]], E[temp[1]], lazy2, tree2))