import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_009

dp = [[0] * 1_001 for _ in range(1_001)]
dp[1][1], dp[1][2], dp[1][3] = 1, 1, 1

for i in range(1, 1001):
    for j in range(1, 1001):
        if i - 1 > 0:
            if j - 1 > 0:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= MOD
            if j - 2 > 0:
                dp[i][j] += dp[i - 1][j - 2]
                dp[i][j] %= MOD
            if j - 3 > 0:
                dp[i][j] += dp[i - 1][j - 3]
                dp[i][j] %= MOD

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[M][N])