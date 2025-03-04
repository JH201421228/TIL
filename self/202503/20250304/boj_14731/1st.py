import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_007

def DQ(n):
    if not n:
        return 1
    elif n == 1:
        return 2

    return (DQ(n//2)**2 * DQ(n%2)) % MOD

ans = 0

for _ in range(int(input())):
    C, K = map(int, input().split())
    if not K:
        continue
    ans += (C*K*DQ(K-1) % MOD)

print(ans % MOD)