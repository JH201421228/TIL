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
print(dp)
for i in range(2, N+1):
    for j in range(1, N-i+2):
        dp[i][j] = (0, 0, float('inf'))
        print('-----------------')
        print(i, j)
        for k in range(j, j+i-1):
            print(i-k, j, '|', k, i+j-k)
#             if dp[i-k][j][0] * dp[i-k][j][1] * dp[k][i+j-k][1] + dp[i-k][j][2] + dp[k][i+j-k][2] < dp[i][j][2]:
#                 dp[i][j] = (dp[i-k][j][0], dp[k][i+j-k][1], dp[i-k][j][0] * dp[i-k][j][1] * dp[k][i+j-k][1] + dp[i-k][j][2] + dp[k][i+j-k][2])
# print(dp)
