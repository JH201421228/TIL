import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, tree_idx):
    if (s == e):
        tree[tree_idx] = arr[s]
        return arr[s]

    mid = (s + e) // 2

    tree[tree_idx] = I(s, mid, tree_idx*2) ^ I(mid+1, e, tree_idx*2+1)

    return tree[tree_idx]

def lazy_U(s, e, tree_idx):
    if(lazy[tree_idx]):
        if ((e-s+1)%2):
            tree[tree_idx] ^= lazy[tree_idx]
        if (s != e):
            lazy[tree_idx*2] ^= lazy[tree_idx]
            lazy[tree_idx*2+1] ^= lazy[tree_idx]
        lazy[tree_idx] = 0

def S(s, e, tree_idx, l, r):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return 0

    if (s >= l and e <= r):
        return tree[tree_idx]

    mid = (s + e) // 2

    return S(s, mid, tree_idx*2, l, r) ^ S(mid+1, e, tree_idx*2+1, l, r)

def U(s, e, tree_idx, l, r, val):
    lazy_U(s, e, tree_idx)

    if (s > r or e < l):
        return

    if (s >= l and e <= r):
        if((e-s+1) % 2):
            tree[tree_idx] ^= val
        if (s != e):
            lazy[tree_idx*2] ^= val
            lazy[tree_idx*2+1] ^= val
        return

    mid = (s + e) // 2

    U(s, mid, tree_idx*2, l, r, val)
    U(mid+1, e, tree_idx*2+1, l, r, val)
    tree[tree_idx] = tree[tree_idx*2] ^ tree[tree_idx*2+1]


N = int(input())

arr = [0] + list(map(int, input().split()))
tree = [0] * (4*N+1)
lazy = [0] * (4*N+1)

I(1, N, 1)

M = int(input())

for _ in range(M):
    temp = list(map(int, input().split()))

    if (temp[0] == 1):
        U(1, N, 1, temp[1]+1, temp[2]+1, temp[3])
    else:
        print(S(1, N, 1, temp[1]+1, temp[2]+1))