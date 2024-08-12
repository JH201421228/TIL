import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

MOD = 1_000_000_007

def I(s, e, idx):
    if s == e:
        tree[idx] = nums[s]
        return tree[idx]

    mid = (s + e) // 2
    tree[idx] = (I(s, mid, idx*2) * I(mid+1, e, idx*2+1)) % MOD
    return tree[idx]


def S(s, e, l, r, idx):
    if s > r or e < l:
        return 1

    if s >= l and e <= r:
        return tree[idx]

    mid = (s + e) // 2
    val = (S(s, mid, l, r, idx*2) * S(mid+1, e, l, r, idx*2+1)) % MOD
    return val


def U(s, e, nums_idx, tree_idx, change):
    if s == e:
        tree[tree_idx] = change
        return tree[tree_idx]

    mid = (s + e) // 2
    if nums_idx <= mid:
        left_val = U(s, mid, nums_idx, tree_idx*2, change)
        right_val = tree[tree_idx*2+1]
    else:
        left_val = tree[tree_idx*2]
        right_val = U(mid+1, e, nums_idx, tree_idx*2+1, change)

    tree[tree_idx] = (left_val * right_val) % MOD
    return tree[tree_idx]


N, M, K = map(int, input().split())
nums = [0]
tree = [1] * (4 * N)

for _ in range(N):
    nums.append(int(input()))

I(1, N, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b] = c
        U(1, N, b, 1, c)
    else:
        print(S(1, N, b, c, 1))
