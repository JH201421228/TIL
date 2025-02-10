import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def nCr(n, c):
    res = 1

    for i in range(c):
        res *= (n-i)

    for i in range(c):
        res //= (i+1)

    return res % MOD


MOD = 1_000_000_007

N, M = map(int, input().split())
ans = 0
cnt = 0

while N >= 0:
    if N >= (N+cnt) // 2:
        ans += nCr(N+cnt, cnt)
    else:
        ans += nCr(N+cnt, N)

    ans %= MOD

    N -= M
    cnt += 1

print(ans)