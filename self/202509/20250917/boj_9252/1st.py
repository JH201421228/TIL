import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = list(input().rstrip())
    M = list(input().rstrip())

    dp = [[0] * (len(M)+1) for _ in range(len(N)+1)]

    for i in range(1, len(N)+1):
        for j in range(1, len(M)+1):
            if N[i-1] == M[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ans_length = dp[-1][-1]
    print(ans_length)

    ans_string = ''

    i, j = len(N), len(M)
    while ans_length:
        if N[i-1] == M[j-1]:
            ans_length -= 1
            ans_string = N[i-1] + ans_string
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

    print(ans_string)

    return


if __name__ == "__main__":
    solve()