import sys
sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def solve_dp(N, matrix):
    dp = [[float('inf')] * (N) for _ in range(N)]
    dp[0][0] = matrix[0][0]

    for i in range(N):
        for j in range(N):
            for dx, dy in delta:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + matrix[ni][nj])

    return dp[N-1][N-1]

T = int(input())
for test in range(T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    ans = solve_dp(N, matrix)
    print(ans)
