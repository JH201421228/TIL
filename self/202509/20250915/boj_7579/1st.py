import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    bites = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    dp = [[0] * (sum(cost)+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, sum(cost)+1):
            if j >= cost[i-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-cost[i-1]] + bites[i-1])
            dp[i][j] = max(dp[i][j], dp[i-1][j])

    for idx in range(1, sum(cost) + 1):
        if dp[-1][idx] >= M:
            print(idx)
            break

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()