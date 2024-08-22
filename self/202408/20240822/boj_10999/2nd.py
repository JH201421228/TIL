import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if (s == e):
        tree[tree_idx] = arr[s]
        return arr[s]

    mid = (s+e) // 2
    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)
    return tree[tree_idx]


def S(s, e, l, r, tree_idx):
    if (s > r or e < l):
        return 0

    if (l <= s and r >= e):
        return tree[tree_idx]

    mid = (s+e) // 2
    val = S(s, mid, l, r, tree_idx*2) + S(mid+1, e, l, r, tree_idx*2+1)
    return val


def U(s, e, l, r, tree_idx, c):
    if (s > r or e < l):
        return 0

    if (s == e):
        tree[tree_idx] += c
        return c

    mid = (s+e) // 2
    val = U(s, mid, l, r, tree_idx*2, c) + U(mid+1, e, l, r, tree_idx*2+1, c)
    tree[tree_idx] += val
    return val


N, M, K = map(int, input().split())
arr = [0]
tree = [0] * (4*N+1)

for _ in range(N):
    arr.append(int(input()))

I(1, N, 1)

for _ in range(M+K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        U(1, N, temp[1], temp[2], 1, temp[3])
    else:
        print(S(1, N, temp[1], temp[2], 1))
        print(tree)