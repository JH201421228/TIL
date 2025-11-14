import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_003


def solve():
    N = int(input())
    K = int(input())

    dp = [[0] * (K+1) for _ in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = 1
        dp[i][1] = i

    for n in range(2, N):
        for k in range(2, K+1):
            dp[n][k] = (dp[n-2][k-1] + dp[n-1][k]) % MOD

    print((dp[N-3][K-1] + dp[N-1][K]) % MOD)

    for d in dp:
        print(d)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()