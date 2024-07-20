import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())

dp = [0] * (K+1)

for _ in range(N):
    c = int(input())

    if c <= K:
        dp[c] = 1

        for i in range(c+1, K+1):
            if dp[i-c]:
                if dp[i]:
                    dp[i] = min(dp[i], dp[i-c]+1)
                else:
                    dp[i] = dp[i-c]+1

if dp[-1]:
    print(dp[-1])
else:
    print(-1)