import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
maxv = 1_000_001
arr = [0] * maxv
dp = [0] * maxv

for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

if K < maxv:
    dp[0] = sum(arr[:K+1])
else:
    print(sum(arr))
    exit(0)

for idx in range(1, maxv-K):
    l, r = idx-K-1, idx+K
    if l >= 0:
        dp[idx] = dp[idx-1] - arr[l]
    else:
        dp[idx] = dp[idx-1]
    dp[idx] = dp[idx] + arr[r]

print(max(dp))