import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if (s == e):
        fake_tree[tree_idx] = 1
        return 1

    mid = (s+e) // 2
    fake_tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)
    return fake_tree[tree_idx]


def lazy_U(s, e, tree_idx):
    if lazy[tree_idx]:
        tree[tree_idx] = fake_tree[tree_idx] - tree[tree_idx]
        if (s != e):
            lazy[tree_idx*2] = 1 - lazy[tree_idx*2]
            lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1]
        lazy[tree_idx] = 0


def S(s, e, tree_idx, l, r):
    lazy_U(s, e, tree_idx)

    if (l > e or r < s):
        return 0

    if (s >= l and e <= r):
        return tree[tree_idx]

    mid = (s+e) // 2
    return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)


def U(s, e, tree_idx, l, r):
    lazy_U(s, e, tree_idx)

    if (l > e or r < s):
        return

    if (s >= l and e <= r):
        tree[tree_idx] = fake_tree[tree_idx] - tree[tree_idx]
        if (s != e):
            lazy[tree_idx * 2] = 1 - lazy[tree_idx * 2]
            lazy[tree_idx * 2 + 1] = 1 - lazy[tree_idx * 2 + 1]
        return

    mid = (s+e) // 2
    U(s, mid, tree_idx*2, l, r)
    U(mid+1, e, tree_idx * 2+1, l, r)

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]


N, M = map(int, input().split())
arr = [0] * (N+1)
fake_tree = [0] * (4*N+1)
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

I(1, N, 1)

for _ in range(M):
    O, F, T = map(int, input().split())

    if not O:
        U(1, N, 1, F, T)
    else:
        print(S(1, N, 1, F, T))