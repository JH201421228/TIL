import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(n, cur, D, dp, N):
    if n == N: return 0
    
    if dp[n][cur] != -1: return dp[n][cur]
    
    dp[n][cur] = float("inf")
    
    for i in range(N):
        if cur & (1<<i): continue
        
        dp[n][cur] = min(dp[n][cur], dfs(n+1, cur | (1<<i), D, dp, N) + D[n][i])
    
    return dp[n][cur]


def solve():
    N = int(input())
    D = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[-1] * (1<<N) for _ in range(N)]
    
    print(dfs(0, 0, D, dp, N))
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
    