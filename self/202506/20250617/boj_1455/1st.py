import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def flipper(x, y, coins):
    for i in range(x):
        for j in range(y):
            coins[i][j] = 1-coins[i][j]

    return coins


def solve():
    N, M = map(int, input().split())
    coins = [list(map(int, input().rstrip())) for _ in range(N)]

    ans = 0
    for j in range(M-1, -1, -1):
        i = N-1
        while i >= 0 and j < M:
            if coins[i][j]:
                ans += 1
                coins = flipper(i+1, j+1, coins)

            i -= 1
            j += 1

    for i in range(N-2, -1, -1):
        j = 0
        while i >= 0 and j < M:
            if coins[i][j]:
                ans += 1
                coins = flipper(i+1, j+1, coins)

            i -= 1
            j += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()