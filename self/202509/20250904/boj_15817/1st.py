import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def main():
    N, x = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (x+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        l = info[i - 1][0]
        for j in range(x+1):
            for k in range(info[i-1][1]+1):
                if dp[i-1][j] and j + k*l < x+1:
                    dp[i][j+k*l] += dp[i-1][j]

    print(dp[-1][-1])

    return


if __name__ == "__main__":
    main()