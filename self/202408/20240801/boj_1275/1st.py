import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]

    mid = (s+e) // 2
    tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1)
    return tree[idx]


def S(s, e, l, r, idx):
    if (s > r or e < l):
        return 0

    if (s >= l and e <= r):
        return tree[idx]

    mid = (s+e) // 2
    val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1)
    return val


def U(s, e, nums_idx, tree_idx, v):
    if nums_idx > e or nums_idx < s:
        return

    tree[tree_idx] += v

    if s == e:
        return

    mid = (s+e) // 2
    U(s, mid, nums_idx, tree_idx*2, v)
    U(mid+1, e, nums_idx, tree_idx*2+1, v)


N, Q = map(int, input().split())
nums = [0]
tree = [0] * (4*N)

nums.extend(list(map(int, input().split())))

I(1, N, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(S(1, N, min(x, y), max(x, y), 1))
    U(1, N, a, 1, b-nums[a])
    nums[a] = b