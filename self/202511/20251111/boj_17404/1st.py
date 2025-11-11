import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def min_cost(start, costs):
    dp = [[float("inf")] * 3 for _ in range(len(costs))]
    dp[0][start] = costs[0][start]

    for idx in range(1, len(costs)):
        dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + costs[idx][0]
        dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + costs[idx][1]
        dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + costs[idx][2]

    dp[-1][start] = float("inf")

    return min(dp[-1])


def solve():
    N = int(input())

    costs = [tuple(map(int, input().split())) for _ in range(N)]

    print(min(min_cost(0, costs), min_cost(1, costs), min_cost(2, costs)))

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()