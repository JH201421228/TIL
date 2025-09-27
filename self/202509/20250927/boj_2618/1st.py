import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline


def dist(i, j, d):
    return abs(d[i][0] - d[j][0]) + abs(d[i][1] - d[j][1])


def cal(n, m, dp, dp_trace, W, d):
    x = max(n, m) + 1
    if x == W+2: return 0
    if dp[n][m] != -1: return dp[n][m]

    first = cal(n, x, dp, dp_trace, W, d) + dist(m, x, d)
    second = cal(x, m, dp, dp_trace, W, d) + dist(n, x, d)

    if first > second:
        dp[n][m] = second
        dp_trace[n][m] = 1
    else:
        dp[n][m] = first
        dp_trace[n][m] = 2

    return dp[n][m]


def solve(N, W):
    tasks = [tuple(map(int, input().split())) for _ in range(W)]
    tasks = [(1, 1), (N, N)] + tasks

    dp = [[-1] * (W+2) for _ in range(W+2)]
    dp_trace = [[-1] * (W+2) for _ in range(W+2)]

    print(cal(0, 1, dp, dp_trace, W, tasks))

    n, m = 0, 1
    for i in range(2, W+2):
        print(dp_trace[n][m])
        if dp_trace[n][m] == 1:
            n = i
        else:
            m = i

    return


def main():
    N = int(input())
    W = int(input())

    solve(N, W)

    return


if __name__ == "__main__":
    main()