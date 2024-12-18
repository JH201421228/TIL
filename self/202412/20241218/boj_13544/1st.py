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


def count(X, v):
    s, e = 0, len(X)-1

    while s <= e:
        mid = (s+e) >> 1

        if X[mid] > v:
            e = mid-1
        else:
            s = mid+1

    return len(X)-e-1


def S(s, e, idx, l, r, v):
    if s > r or e < l:
        return 0

    if s >= l and e <= r:
        return count(T[idx], v)

    mid = (s+e) >> 1

    return S(s, mid, idx<<1, l, r, v) + S(mid+1, e, idx<<1|1, l, r, v)


N = int(input())
arr = [0] + list(map(int, input().split()))
T = [[] for _ in range(4*N+1)]

I(1, N, 1)

last_ans = 0

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a ^= last_ans
    b ^= last_ans
    c ^= last_ans

    last_ans = S(1, N, 1, a, b, c)
    print(last_ans)