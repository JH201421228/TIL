import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
matrixes = []
for _ in range(N):
    matrixes.append(tuple(map(int, input().split())))
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    dp[1][i+1] = (matrixes[i][0], matrixes[i][1], 0)
# print(dp)
for i in range(2, N+1): # i는 범위
    for j in range(1, N-i+2): # j는 시작점
        dp[i][j] = (0, 0, float('inf'))
        # print('-----------------')
        # print(i, j)
        for k in range(j, j+i-1): # k는 분할지점
            # print(-j+k+1, j, '|', i+j-k-1, k+1)
            if dp[-j+k+1][j][0] * dp[-j+k+1][j][1] * dp[i+j-k-1][k+1][1] + dp[-j+k+1][j][2] + dp[i+j-k-1][k+1][2] < dp[i][j][2]:
                dp[i][j] = (dp[-j+k+1][j][0], dp[i+j-k-1][k+1][1], dp[-j+k+1][j][0] * dp[-j+k+1][j][1] * dp[i+j-k-1][k+1][1] + dp[-j+k+1][j][2] + dp[i+j-k-1][k+1][2])
# print(dp)
print(dp[N][1][2])
