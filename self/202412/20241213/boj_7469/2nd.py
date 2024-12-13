import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def merge(X, Y):
    res = []
    i, j, x, y = 0, 0, len(X), len(Y)

    while i < x and j < y:
        if X[i] > Y[j]:
            res.append(Y[j])
            j += 1
        else:
            res.append(X[i])
            i += 1

    while i < x:
        res.append(X[i])
        i += 1

    while j < y:
        res.append(Y[j])
        j += 1

    return res

def I(s, e, idx):
    if s == e:
        T[idx].append(arr[s])
        return T[idx]

    mid = (s+e) >> 1

    T[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))
    return T[idx]

def count(X, k):
    s, e = 0, len(X)-1

    while s <= e:
        mid = (s+e) >> 1

        if X[mid] >= k:
            e = mid-1
        else:
            s = mid+1

    return s


def S(s, e, idx, l, r, k):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return count(T[idx], k)

    mid = (s+e) >> 1

    return S(s, mid, idx<<1, l, r, k) + S(mid+1, e, idx<<1|1, l, r, k)


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
T = [[] for _ in range(4*N+1)]

I(1, N, 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    s, e = -10**9, 10**9

    while s <= e:
        mid = (s+e) >> 1

        if S(1, N, 1, i, j, mid) >= k:
            e = mid-1
        else:
            s = mid+1

    print(e)