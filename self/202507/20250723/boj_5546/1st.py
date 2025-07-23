import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    dp = [[[0] * 2 for _ in range(N+1)] for _ in range(3)]
    fix = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        fix[a] = b

    if not fix[1]:
        dp[0][1][0], dp[1][1][0], dp[2][1][0] = 1, 1, 1
    else:
        dp[fix[1]-1][1][0] = 1

    isFixed = False
    for j in range(1, N):
        if not fix[j+1]:
            isFixed = False
        else:
            isFixed = True

        if not isFixed:
            for i in range(3):
                for k in range(3):
                    if i == k:
                        dp[i][j+1][1] += dp[i][j][0]
                        dp[i][j+1][1] %= 10_000
                    else:
                        dp[i][j+1][0] += (dp[k][j][0] + dp[k][j][1])
                        dp[i][j+1][0] %= 10_000

        else:
            for k in range(3):
                if fix[j+1]-1 == k:
                    dp[k][j+1][1] += dp[k][j][0]
                    dp[k][j+1][1] %= 10_000
                else:
                    dp[fix[j+1]-1][j+1][0] += (dp[k][j][0] + dp[k][j][1])
                    dp[fix[j+1]-1][j+1][0] %= 10_000

    ans = sum(dp[0][-1]) + sum(dp[1][-1]) + sum(dp[2][-1])
    print(ans % 10_000)

    return


if __name__ == "__main__":
    solve()