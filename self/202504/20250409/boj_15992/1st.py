import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def nCr(n, r):
    if r > n//2:
        return nCr(n, n-r)

    res = 1

    for i in range(n, n-r, -1):
        res *= i

    for i in range(1, r+1):
        res //= i

    return res


for _ in range(int(input())):
    elements = []
    N, M = map(int, input().split())
    a, b, c = 2*M-N, N-M, 0

    if a < 0 or b < 0:
        print(0)
        continue

    elements.append((a, b, c))

    while b > 1:
        a += 1
        b -= 2
        c += 1
        elements.append((a, b, c))

    ans = 0
    for a, b, c in elements:
        temp = nCr(M, a) * nCr(M-a, b) * nCr(M-a-b, c)
        ans += temp
        ans %= 1_000_000_009

    print(ans)