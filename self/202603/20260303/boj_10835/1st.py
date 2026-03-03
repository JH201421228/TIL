import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    dp = [[0] * (N+1) for _ in range(N+1)]
    V = [[0] * (N+1) for _ in range(N+1)]

    V[0][0] = 1

    for i in range(N):
        for j in range(N):
            if V[i][j]:
                dp[i+1][j+1] = max(dp[i][j], dp[i+1][j+1])
                dp[i+1][j] = max(dp[i][j], dp[i+1][j])
                V[i+1][j+1] = 1
                V[i+1][j] = 1
                if L[i] > R[j]:
                    dp[i][j+1] = max(dp[i][j] + R[j], dp[i][j+1])
                    V[i][j+1] = 1
    
    ans = 0
    
    for i in range(N+1):
        ans = max(ans, dp[-1][i], dp[i][-1])
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()