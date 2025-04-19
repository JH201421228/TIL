import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_009

N = int(input())

dp = [[0] * 3 for _ in range(N+1)]
dp[1] = [1, 0, 0]

if N > 1:
    for idx in range(2, N+1):
        dp[idx] = [(dp[idx-1][0]+dp[idx-1][1]) % MOD, dp[idx-2][2], (dp[idx-1][0]+dp[idx-1][1]) % MOD]

    print(dp[idx][0] + dp[idx][1] + dp[idx-1][2])

else:
    print(1)