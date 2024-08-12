import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, idx):
    if (s == e):
        tree[idx] = nums[s]
        return tree[idx]

    mid = (s+e) // 2
    tree[idx] = (I(s, mid, idx*2) * I(mid+1, e, idx*2+1)) % 1_000_000_007
    return tree[idx]


def S(s, e, l, r, idx):
    if (s > r or e < l):
        return 1

    if (s >= l and e <= r):
        return tree[idx]

    mid = (s+e) // 2
    val = (S(s, mid, l, r, idx*2) * S(mid+1, e, l, r, idx*2+1)) % 1_000_000_007
    return val


def U(s, e, nums_idx, tree_idx, change):
    if (s == e and s == nums_idx):
        tree[tree_idx] = change
        return change

    if (nums_idx > e or nums_idx < s):
        return tree[tree_idx]

    if (nums_idx >= s and nums_idx <= e):
        mid = (s+e) // 2
        tree[tree_idx] = (U(s, mid, nums_idx, tree_idx*2, change) * U(mid+1, e, nums_idx, tree_idx*2+1, change)) % 1_000_000_007
        return tree[tree_idx]


N, M, K = map(int, input().split())
nums = [0]
tree = [1] * (4*N)

for _ in range(N):
    nums.append(int(input()))

I(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b] = c
        U(1, N, b, 1, c)

    else:
        print(S(1, N, b, c, 1))
