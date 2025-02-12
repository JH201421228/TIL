import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Sieve(L):
    res = [L[0]]
    order = [0]
    cur = L[0]
    l = len(L)
    cnt = 1

    for idx in range(l):
        if L[idx] > cur:
            cur = L[idx]
            res.append(L[idx])
            order.append(idx)
            cnt += 1

    return res, order, cnt


def binary_search(n):
    s, e = 0, cnt-1

    while s <= e:
        mid = (s+e) >> 1

        if sieve[mid] < n:
            s += 1
        else:
            e -= 1

    return s


N = int(input())
H = list(map(int, input().split()))

H = [H[i]+i for i in range(N)]

sieve, order, cnt = Sieve(H)

Q = int(input())
S = list(map(int, input().split()))

ans = []

for n in S:
    ans.append(order[binary_search(n)]+1)

print(*ans)