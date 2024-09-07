import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def lazy_U(s, e, tree_idx):
    if lazy[tree_idx]:
        if (s == e):
            arr[s] ^= lazy[tree_idx]
        else:
            lazy[tree_idx*2] ^= lazy[tree_idx]
            lazy[tree_idx*2+1] ^= lazy[tree_idx]
        lazy[tree_idx] = 0


def S(s, e, tree_idx, idx):
    lazy_U(s, e, tree_idx)

    if (idx > e or idx < s):
        return 0

    if (s == e):
        if (s == idx):
            return arr[idx]
        else:
            return 0

    mid = (s + e) // 2

    return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx)


def U(s, e, tree_idx, l, r, val):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return

    if (s >= l and e <= r):
        if (s == e):
            arr[s] ^= val
        else:
            lazy[tree_idx*2] ^= val
            lazy[tree_idx*2+1] ^= val

        return

    mid = (s + e) // 2

    U(s, mid, tree_idx*2, l, r, val)
    U(mid+1, e, tree_idx*2+1, l, r, val)

N = int(input())
arr = [0] + list(map(int, input().split()))
lazy = [0] * (4*N+1)

M = int(input())

for _ in range(M):
    temp = list(map(int, input().split()))

    if (temp[0] == 1):
        U(1, N, 1, temp[1]+1, temp[2]+1, temp[3])
    else:
        print(S(1, N, 1, temp[1]+1))