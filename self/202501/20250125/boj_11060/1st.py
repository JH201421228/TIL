import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
M = list(map(int, input().split()))
dp = [float("inf")] * N
dp[0] = 0

for i in range(N):
    u = M[i]
    for j in range(i+1, i+1+u):
        if j < N:
            dp[j] = min(dp[j], dp[i]+1)

if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])