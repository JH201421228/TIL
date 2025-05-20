import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 10**9 + 7


# 모듈러 역원: b^(-1) mod MOD
def modinv(x):
    return pow(x, MOD - 2, MOD)


# (n(n+1)) // 2 mod MOD
def sum_k(n):
    n %= MOD
    return n * (n + 1) % MOD * modinv(2) % MOD


# S(n) = n(n+1)(n+2)/6
def S(n):
    n %= MOD
    a = sum_k(n)        # (n(n+1))//2
    b = (n + 1 - (2 * n + 1) * modinv(3) % MOD + MOD) % MOD
    return a * b % MOD


def solve(H, W):
    a = S(H)
    b = S(W)
    numerator = 9 * a % MOD * b % MOD
    denominator = (sum_k(H) * sum_k(W)) % MOD
    return numerator * modinv(denominator) % MOD


H, W = map(int, input().split())
print(solve(H, W))
