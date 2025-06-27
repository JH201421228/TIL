import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    strs = [' ' + input().rstrip() for _ in range(3)]

    dp = [[[0]*len(strs[2]) for _ in range(len(strs[1]))] for _ in range(len(strs[0]))]

    for i in range(1, len(strs[0])):
        for j in range(1, len(strs[1])):
            for k in range(1, len(strs[2])):
                if strs[2][k] == strs[1][j] and strs[2][k] == strs[0][i]:
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    print(dp[-1][-1][-1])

    return


if __name__ == "__main__":
    solve()