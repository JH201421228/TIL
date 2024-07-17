import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
dp = [0] * (N+1)
D, C = [], []

for i in range(N):
    d, c = map(int, input().split())

    if i+d < N+1:
        dp[i+d] = max(dp[i+d], dp[i] + c)

    dp[i+1] = max(dp[i], dp[i+1])

print(max(dp))