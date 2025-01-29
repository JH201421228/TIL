import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def U(s, e, idx, tar):
    if s == e and s == tar:
        T[idx] += 1
        return T[idx]

    if s > tar or e < tar:
        return T[idx]

    mid = (s+e) >> 1
    T[idx] = U(s, mid, idx<<1, tar) + U(mid+1, e, idx<<1|1, tar)

    return T[idx]

def D(s, e, idx, v):
    if s == e:
        T[idx] -= 1
        return s

    mid = (s+e) >> 1

    if T[idx<<1] >= v:
        res = D(s, mid, idx<<1, v)
    else:
        res = D(mid+1, e, idx<<1|1, v-T[idx<<1])

    T[idx] = T[idx<<1] + T[idx<<1|1]

    return res


T = [0] * (4 * 2_000_001 + 1)

for _ in range(int(input())):
    t, x = map(int, input().split())

    if t == 1:
        U(1, 2_000_001, 1, x)
    else:
        print(D(1, 2_000_001, 1, x))