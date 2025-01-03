import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, idx):
    if s == e:
        T[idx] = arr[s]
        return arr[s]

    mid = (s+e) >> 1
    T[idx] = min(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))

    return T[idx]

def lazy_U(s, e, idx):
    if L[idx]:
        T[idx] += L[idx]
        if s != e:
            L[idx<<1] += L[idx]
            L[idx<<1|1] += L[idx]
        L[idx] = 0
    return

def U(s, e, idx, l, r, v):
    lazy_U(s, e, idx)

    if s > r or e < l:
        return T[idx]

    if s >= l and e <= r:
        L[idx] += v
        lazy_U(s, e, idx)
        return T[idx]

    mid = (s+e) >> 1

    T[idx] = min(U(s, mid, idx<<1, l, r, v), U(mid+1, e, idx<<1|1, l, r, v))
    return T[idx]


temp = list(input().rstrip())

N = len(temp)

T = [0] * (4*N+1)
L = [0] * (4*N+1)
arr = [0]

V = 0

for idx in range(N):
    if temp[idx] == '(':
        arr.append(arr[idx] + 1)
    else:
        arr.append(arr[idx] - 1)

I(1, N, 1)

V = arr[-1]

ans = 0

for _ in range(int(input())):
    idx = int(input())
    c = 0
    if temp[idx-1] == '(':
        temp[idx-1] = ')'
        V -= 2
        c = U(1, N, 1, idx, N, -2)
    else:
        temp[idx-1] = '('
        V += 2
        c = U(1, N, 1, idx, N, 2)

    if not V and c >= 0:
        ans += 1

print(ans)