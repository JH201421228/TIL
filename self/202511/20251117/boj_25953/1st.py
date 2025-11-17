import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, T, M = map(int, input().split())
    S, E = map(int, input().split())

    G = [[] for _ in range(T)]
    for idx in range(T):
        for _ in range(M):
            G[idx].append(tuple(map(int, input().split())))

    # dp[i][j]: i 시간에 j까지의 최소 비용

    # dp[i][j] = min(dp[i][j], min(dp[i-1][j] 이번 시간에 갈 수 있는 k to j를 고려))

    dp = [[float("inf")] * N for _ in range(T)]

    for u, v, k in G[0]:
        if u == S:
            dp[0][v] = min(dp[0][v], k)
        if v == S:
            dp[0][u] = min(dp[0][u], k)

    for i in range(1, T):
        for j in range(N):
            dp[i][j] = dp[i-1][j]

        for u, v, k in G[i]:
            if u == S:
                dp[i][v] = min(dp[i][v], k)
                continue

            if v == S:
                dp[i][u] = min(dp[i][u], k)
                continue

            if dp[i-1][u] != float("inf"):
                dp[i][v] = min(dp[i][v], dp[i-1][u] + k)

            if dp[i-1][v] != float("inf"):
                dp[i][u] = min(dp[i][u], dp[i-1][v] + k)

    if dp[-1][E] == float("inf"): print(-1)
    else: print(dp[-1][E])
            
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()