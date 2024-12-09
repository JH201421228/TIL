import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, idx):
    if s == e:
        T[idx] = [arr[s]]
        return T[idx]

    mid = (s+e) >> 1

    T[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))
    return T[idx]

def merge(X, Y):
    res = []

    i, j, x, y = 0, 0, len(X), len(Y)
    while i < x or j < y:
        if i >= x:
            res.append(Y[j])
            j += 1
        elif j >= y:
            res.append(X[i])
            i += 1
        else:
            if X[i] >= Y[j]:
                res.append(Y[j])
                j += 1
            else:
                res.append(X[i])
                i += 1

    return res

def count(A, k):
    s, e = 0, len(A)-1

    while s <= e:
        mid = (s+e) >> 1

        if A[mid] <= k:
            s = mid+1
        else:
            e = mid-1

    return len(A)-s

def S(s, e, idx, l, r, k):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return count(T[idx], k)

    mid = (s+e) >> 1

    return S(s, mid, idx<<1, l, r, k) + S(mid+1, e, idx<<1|1, l, r, k)

N = int(input())
arr = [0] + list(map(int, input().split()))
T = [[] for _ in range (4*N+1)]

I(1, N, 1)

for _ in range(int(input())):
    i, j, k = map(int, input().split())
    print(S(1, N, 1, i, j, k))