import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def lazy_U(s, e, tree_idx):
    if (lazy[tree_idx]):
        tree[tree_idx] += (e-s+1) * lazy[tree_idx]
        if (s != e):
            lazy[tree_idx*2] += lazy[tree_idx]
            lazy[tree_idx*2+1] += lazy[tree_idx]
        lazy[tree_idx] = 0


def S(s, e, tree_idx, idx):
    lazy_U(s, e, tree_idx)

    if (idx > e or idx < s):
        return 0

    if (s == e):
        return tree[tree_idx]

    mid = (s + e) // 2

    return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx)


def U(s, e, tree_idx, l, r, v):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return

    if (s >= l and e <= r):
        lazy[tree_idx] += v
        lazy_U(s, e, tree_idx)
        return

    mid = (s + e) // 2

    U(s, mid, tree_idx*2, l, r, v)
    U(mid+1, e, tree_idx*2+1, l, r, v)

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]


N = int(input())
tree = [0] * (4*100_000+1)
lazy = [0] * (4*100_000+1)

for _ in range(N):
    a, b, = map(int, input().split())
    print(S(1, 100_000, 1, a) + S(1, 100_000, 1, b))
    U(1, 100_000, 1, a, b, 1)
    U(1, 100_000, 1, a, a, -S(1, 100_000, 1, a))
    U(1, 100_000, 1, b, b, -S(1, 100_000, 1, b))