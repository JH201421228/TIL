import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
dp = []

for _ in range(N):
    dp.append(list(map(int, map(str, input().rstrip()))))

ans = max(dp[0])

for i in range(1, N):
    if dp[i][0]:
        ans = 1
        break

for i in range(1, N):
    for j in range(1, M):
        if dp[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans**2)