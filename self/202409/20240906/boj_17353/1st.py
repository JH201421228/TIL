import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if (s == e):
        tree[tree_idx] = arr[s]
        return arr[s]

    mid = (s + e) // 2

    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)
    return tree[tree_idx]


def lazy_U(s, e, tree_idx):
    if checker[tree_idx]:
        tree[tree_idx] += ((e-s+1) * lazy[tree_idx] + dp[e-s+1])

        mid = (s + e) // 2

        if (s != e):
            lazy[tree_idx*2] += lazy[tree_idx]
            checker[tree_idx*2] = 1
            lazy[tree_idx*2+1] += (lazy[tree_idx] + (mid-s+1))
            checker[tree_idx*2+1] = 1
        lazy[tree_idx] = 0
        checker[tree_idx] = 0


def S(s, e, tree_idx, idx):
    lazy_U(s, e, tree_idx)

    if (idx > e or idx < s):
        return 0

    if (s == e):
        if (s == idx):
            return tree[tree_idx]
        else:
            return 0

    mid = (s + e) // 2

    return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx)


def U(s, e, tree_idx, l, r, val):
    lazy_U(s, e, tree_idx)

    if (l > e or r < s):
        return

    mid = (s + e) // 2

    if (l <= s and e <= r):
        tree[tree_idx] += ((e - s + 1) * val + dp[e - s + 1])
        if (s != e):
            lazy[tree_idx*2] += val
            checker[tree_idx*2] = 1
            lazy[tree_idx*2+1] += (val + (mid-s+1))
            checker[tree_idx*2+1] = 1
        return

    U(s, mid, tree_idx*2, l, r, val)
    if mid >= l:
        U(mid+1, e, tree_idx*2+1, l, r, val + (mid-l+1))
    else:
        U(mid + 1, e, tree_idx * 2 + 1, l, r, val)

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]


N = int(input())

arr = [0] + list(map(int, input().split()))

tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)
checker = [0] * (4*N+1)

dp = [i for i in range(N+1)]

for i in range(1, N+1):
    dp[i] += dp[i-1]

print(dp)
I(1, N, 1)

M = int(input())

for _ in range(M):
    temp = list(map(int, input().split()))

    if (temp[0] == 1):
        U(1, N, 1, temp[1], temp[2], 0)
        print(tree)
        print(lazy)
        print(checker)
    else:
        print(S(1, N, 1, temp[1]))
        print(tree)
        print(lazy)
        print(checker)