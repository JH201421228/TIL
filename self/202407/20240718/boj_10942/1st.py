import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]
di, dj = -1, 1

for i in range(N):
    dp[i][i] = 1
    if i+1 < N and nums[i] == nums[i+1]:
        dp[i][i+1] = 1
    n = 1
    while i+n*di >= 0 and i+n*dj < N:
        if not dp[i+(n-1)*di][i+(n-1)*dj]:
            break
        elif nums[i+n*di] == nums[i+n*dj]:
            dp[i+n*di][i+n*dj] = 1

        n += 1

    n = 1
    while i + n * di >= 0 and i + n * dj + 1 < N:
        if not dp[i+(n-1)*di][i+(n-1)*dj+1]:
            break
        elif nums[i + n * di] == nums[i + n * dj + 1]:
            dp[i + n * di][i + n * dj + 1] = 1

        n += 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])