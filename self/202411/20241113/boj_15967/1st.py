import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if s == e:
        tree[tree_idx] = arr[s]
        return arr[s]

    mid = (s + e) // 2

    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)

    return tree[tree_idx]

def lazy_U(s, e, tree_idx):
    if lazy[tree_idx]:
        tree[tree_idx] += (e-s+1) * lazy[tree_idx]
        if s != e:
            lazy[tree_idx*2] += lazy[tree_idx]
            lazy[tree_idx*2+1] += lazy[tree_idx]
        lazy[tree_idx] = 0

def S(s, e, l, r, tree_idx):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return 0

    if (s >= l and e <= r):
        return tree[tree_idx]

    mid = (s + e) // 2

    return S(s, mid, l, r, tree_idx*2) + S(mid+1, e, l, r, tree_idx*2+1)

def U(s, e, l, r, tree_idx, v):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return

    if (s >= l and e <= r):
        lazy[tree_idx] += v
        lazy_U(s, e, tree_idx)
        return

    mid = (s + e) // 2

    U(s, mid, l, r, tree_idx*2, v)
    U(mid+1, e, l, r, tree_idx*2+1, v)
    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]


N, Q1, Q2 = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

I(1, N, 1)

for _ in range(Q1+Q2):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        print(S(1, N, temp[1], temp[2], 1))
    else:
        U(1, N, temp[1], temp[2], 1, temp[3])