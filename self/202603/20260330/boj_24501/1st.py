import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def solve():
    N, M = map(int, input().split())
    
    maps = [list(input().rstrip()) for _ in range(N)]
    
    dp = [[[0]*3 for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j][0] - dp[i-1][j-1][0]
            dp[i][j][1] = dp[i][j-1][1] + dp[i-1][j][1] - dp[i-1][j-1][1]
            dp[i][j][2] = dp[i][j-1][2] + dp[i-1][j][2] - dp[i-1][j-1][2]
            
            if maps[i-1][j-1] == "E":
                dp[i][j][0] += 1
            elif maps[i-1][j-1] == "S":
                dp[i][j][1] += dp[i][j-1][0] + dp[i-1][j][0] - dp[i-1][j-1][0]
            else:
                dp[i][j][2] += dp[i][j-1][1] + dp[i-1][j][1] - dp[i-1][j-1][1]

            dp[i][j][0] %= MOD
            dp[i][j][1] %= MOD
            dp[i][j][2] %= MOD
                
    
    print(dp[-1][-1][-1])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()