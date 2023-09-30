import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
housing = [list(map(int, input().split())) for _ in range(N)]
fxxk_dp = [[[0] * N for _ in range(N)] for _ in range(3)]
fxxk_dp[0][0][1] = 1
for idx in range(2, N):
    if not housing[0][idx]:
        fxxk_dp[0][0][idx] = fxxk_dp[0][0][idx-1]
        # if not fxxk_dp[0][0][idx]:
        #     break

for i in range(1, N):
    for j in range(1, N):
        if not housing[i][j] and not housing[i-1][j] and not housing[i][j-1]:
            fxxk_dp[2][i][j] = fxxk_dp[0][i-1][j-1] + fxxk_dp[1][i-1][j-1] + fxxk_dp[2][i-1][j-1]
        if not housing[i][j]:
            fxxk_dp[0][i][j] = fxxk_dp[0][i][j-1] + fxxk_dp[2][i][j-1]
            fxxk_dp[1][i][j] = fxxk_dp[1][i-1][j] + fxxk_dp[2][i-1][j]
print(fxxk_dp[0][N-1][N-1] + fxxk_dp[1][N-1][N-1] + fxxk_dp[2][N-1][N-1])
