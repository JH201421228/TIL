import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
dp = [0] * 1001
dp[2] = 1
dp[4] = 1
dp[5] = 1

for idx in range(6, 1001):
    if not dp[idx-1] * dp[idx-3] * dp[idx-4]:
        dp[idx] = 1

if dp[N]:
    print("SK")
else:
    print("CY")