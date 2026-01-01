import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    
    values = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[[-float("inf")] * 3 for _ in range(M)] for _ in range(N)]
    
    dp[0][0] = [values[0][0]] * 3
    
    for i in range(N):
        for j in range(M):
            if i:
                dp[i][j][0] = values[i][j] + max(dp[i-1][j])
        
        for j in range(M):
            if j:
                dp[i][j][1] = values[i][j] + max(dp[i][j-1][0], dp[i][j-1][1])
                dp[i][M-1-j][2] = values[i][M-1-j] + max(dp[i][M-j][0], dp[i][M-j][2])

    print(max(dp[-1][-1]))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()