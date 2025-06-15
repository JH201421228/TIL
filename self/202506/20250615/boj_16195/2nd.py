import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_009


def solve():
    arr = [[0] * 1_001 for _ in range(1_001)]
    arr[0][0] = 1

    for i in range(1, 1_001):
        for j in range(1, 1_001):
            if j - 3 >= 0: arr[i][j] += arr[i - 1][j - 3]
            if j - 2 >= 0: arr[i][j] += arr[i - 1][j - 2]
            arr[i][j] += arr[i - 1][j - 1]

    for _ in range(int(input())):
        N, M = map(int, input().split())

        ans = 0
        for i in range(M+1): ans += arr[i][N]

        print(ans % MOD)

    return


if __name__ == "__main__":
    solve()