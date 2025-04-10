import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


coin = float(input())
freeze = 0
if coin >= 1.98:
    freeze += 2
elif coin >= 0.99:
    freeze += 1

N = int(input())
days = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(freeze)]

for idx in range(N):
    if days[idx]:
        dp[0][idx+1] = dp[0][idx]+1

print(dp)