import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def set_dp(n, G, V, dp, weights):
    V[n] = 1
    dp[n][1] = weights[n-1]

    for x in G[n]:
        if not V[x]:
            set_dp(x, G, V, dp, weights)
            dp[n][1] += dp[x][0]
            dp[n][0] += max(dp[x])

    return


def find_node(n, G, V, dp, ans, pre_use):
    V[n] = 1

    if not dp[n][0] > dp[n][1]:
        ans.append(n)

    for x in G[n]:
        if not V[x]:
            if pre_use:
                find_node(x, G, V, dp, ans, False)
            else:
                if dp[n][0] > dp[n][1]:
                    find_node(x, G, V, dp, ans, False)
                else:
                    find_node(x, G, V, dp, ans, True)

    return


def solve():
    N = int(input())
    weights = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u, v = map(int, input().split())

        G[u].append(v)
        G[v].append(u)

    V = [0] * (N+1)
    dp = [[0] * 2 for _ in range(N+1)]

    set_dp(1, G, V, dp, weights)

    V = [0] * (N+1)
    ans = []

    print(max(dp[1]))

    find_node(1, G, V, dp, ans, False)

    ans.sort()
    print(*ans)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()