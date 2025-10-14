import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def set_dp(n, dp, V, G):
    V[n] = 1
    dp[n][1] = 1

    for x in G[n]:
        if not V[x]:
            set_dp(x, dp, V, G)
            dp[n][0] += dp[x][1]
            dp[n][1] += min(dp[x][0], dp[x][1])

    return


def solve():
    N = int(input())
    G = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    dp = [[0] * 2 for _ in range(N+1)]
    V = [0] * (N+1)

    set_dp(1, dp, V, G)

    print(min(dp[1]))

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()