import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

dp = [i for i in range(10_001)]

for i in range(1, 10_001):
    dp[i] += dp[i-1]

ans = sum(dp[:N+1])

for i in range(1, N+1):
    if 2*i <= N:
        ans += dp[N+1-2*i]
    else: break

print(ans)