import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T, W = map(int, input().split())

vals = []
prev = 0
cnt = 0

for i in range(T):
    v = int(input())

    if not i and v == 1:
        vals.append(0)

    if prev and prev != v:
        vals.append(cnt)
        cnt = 0

    cnt += 1
    prev = v
vals.append(cnt)

L = len(vals) + 1
dp = [[0] * L for _ in range(W+1)]

for i in range(1, L):
    if i%2:
        dp[0][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1] + vals[i-1]

ans = dp[0][i]

for i in range(1, W+1):
    for j in range(i, L):
        if i%2:
            if j%2:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
        else:
            if j%2:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1]

    ans = max(dp[i][j], ans)

print(ans)