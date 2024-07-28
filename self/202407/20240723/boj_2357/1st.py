import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I1(s, e, idx):
    if s >= e:
        tree1[idx] = nums[s]
        return tree1[idx]

    mid = (s+e) // 2
    tree1[idx] = min(I1(s, mid, idx*2), I1(mid+1, e, idx*2+1))
    return tree1[idx]


def I2(s, e, idx):
    if s >= e:
        tree2[idx] = nums[s]
        return tree2[idx]

    mid = (s+e) // 2
    tree2[idx] = max(I2(s, mid, idx*2), I2(mid+1, e, idx*2+1))
    return tree2[idx]


def S1(s, e, l, r, idx):
    if s > r or e < l:
        return float('inf')

    if s >= l and e <= r:
        return tree1[idx]

    mid = (s+e) // 2
    v = min(S1(s, mid, l, r, idx*2), S1(mid+1, e, l, r, idx*2+1))
    return v


def S2(s, e, l, r, idx):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return tree2[idx]

    mid = (s+e) // 2
    v = max(S2(s, mid, l, r, idx*2), S2(mid+1, e, l, r, idx*2+1))
    return v


N, M = map(int, input().split())
nums = [0]
tree1 = [[0, 0] for _ in range(4*N)]
tree2 = [[0, 0] for _ in range(4*N)]

for _ in range(N):
    nums.append(int(input()))

I1(1, N, 1)
I2(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(S1(1, N, a, b, 1), S2(1, N, a, b, 1))