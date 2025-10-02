import sys
sys.setrecursionlimit(20_000)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(n, G, V, dp):

    for x in G[n]:
        if not V[x]:
            V[x] = 1
            bfs(x, G, V, dp)
            dp[n][0] += max(dp[x][0], dp[x][1])
            dp[n][1] += dp[x][0]

    return


def solve():
    N = int(input())
    populations = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    dp = [[0]*2 for _ in range(N+1)]
    for i, p in enumerate(populations):
        dp[i+1][1] = p

    V = [0] * (N+1)
    V[1] = 1

    bfs(1, G, V, dp)

    print(max(dp[1]))

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()