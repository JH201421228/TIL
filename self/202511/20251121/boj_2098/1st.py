import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(pre, cur, dp, C, N):
    if cur == (1<<N)-1:
        if C[pre][0]: 
            return C[pre][0]
        else:
            return float("inf")
    
    if dp[pre][cur] != -1: return dp[pre][cur]
    
    dp[pre][cur] = float("inf")
    
    for x in range(N):
        if C[pre][x] and not cur & (1<<x):
            dp[pre][cur] = min(dp[pre][cur], dfs(x, cur | (1<<x), dp, C, N) + C[pre][x])
    
    return dp[pre][cur]


def solve():
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[-1] * (1<<N) for _ in range(N)]
    
    print(dfs(0, 1, dp, C, N))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()