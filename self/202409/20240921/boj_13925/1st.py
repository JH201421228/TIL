import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if (s == e):
        tree[tree_idx] = arr[s]
        return arr[s]

    mid = (s + e) // 2

    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)
    tree[tree_idx] %= MOD

    return tree[tree_idx]


def lazy_U(s, e, tree_idx):
    if (lazy[tree_idx][0] != 1 or lazy[tree_idx][1]):
        tree[tree_idx] = (tree[tree_idx] * lazy[tree_idx][0] + (e-s+1) * lazy[tree_idx][1]) % MOD
        if (s != e):
            lazy[tree_idx*2][0] = (lazy[tree_idx*2][0] * lazy[tree_idx][0]) % MOD
            lazy[tree_idx*2+1][0] = (lazy[tree_idx*2+1][0] * lazy[tree_idx][0]) % MOD
            lazy[tree_idx*2][1] = (lazy[tree_idx*2][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD
            lazy[tree_idx*2+1][1] = (lazy[tree_idx*2+1][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD
        lazy[tree_idx] = [1, 0]


def S(s, e, tree_idx, l, r):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return 0

    if (s >= l and e <= r):
        return tree[tree_idx]

    mid = (s + e) // 2

    return (S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)) % MOD


def U(s, e, tree_idx, l, r, v1, v2):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return

    if (s >= l and e <= r):
        lazy[tree_idx][0] = (lazy[tree_idx][0] * v1) % MOD
        lazy[tree_idx][1] = (lazy[tree_idx][1] * v1) % MOD
        lazy[tree_idx][1] = (lazy[tree_idx][1] + v2) % MOD
        lazy_U(s, e, tree_idx)
        return

    mid = (s + e) // 2

    U(s, mid, tree_idx*2, l, r, v1, v2)
    U(mid+1, e, tree_idx*2+1, l, r, v1, v2)

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]


MOD = 1_000_000_007

N = int(input())

arr = [0] + list(map(int, input().split()))
lazy = [[1, 0] for _ in range(4*N+1)]
tree = [0] * (4*N+1)

I(1, N, 1)

M = int(input())

for _ in range(M):
    temp = list(map(int, input().split()))

    if (temp[0] == 1):
        U(1, N, 1, temp[1], temp[2], 1, temp[3])
    elif (temp[0] == 2):
        U(1, N, 1, temp[1], temp[2], temp[3], 0)
    elif (temp[0] == 3):
        U(1, N, 1, temp[1], temp[2], 0, temp[3])
    else:
        print(S(1, N, 1, temp[1], temp[2]))