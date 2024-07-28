import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, i):
    if s == e:
        tree[i] = nums[s-1]
        return tree[i]

    mid = (s+e) // 2
    tree[i] = I(s, mid, i*2) + I(mid+1, e, i*2+1)
    return tree[i]

def S(s, e, l, r, idx):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return tree[idx]

    mid = (s+e) // 2
    val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1)
    return val

def U(s, e, idx, cidx, val):
    if s > cidx or e < cidx:
        return

    tree[idx] += val

    if s == e:
        return

    mid = (s+e) // 2
    U(s, mid, idx*2, cidx, val)
    U(mid+1, e, idx*2+1, cidx, val)


N, M, K = map(int, input().split())

nums = []
tree = [0] * (N*4)

for _ in range(N):
    nums.append(int(input()))

I(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        v = c - nums[b-1]
        nums[b-1] = c
        U(1, N, 1, b, v)
    else:
        print(S(1, N, b, c, 1))