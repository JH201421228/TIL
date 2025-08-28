import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_007


def solve():
    N = int(input())
    res = [[0]*2 for _ in range(1_000_001)]

    res[1] = [2, 3]
    res[2] = [7, 10]
    res[3] = [22, 32]

    for idx in range(4, 1_000_001):
        res[idx][0] = (res[idx-1][0]*2 + res[idx-2][0]*3 + res[idx-3][1]*2) % MOD
        res[idx][1] = (res[idx][0] + res[idx-1][1]) % MOD

    print(res[N][0])
    return


if __name__ == "__main__":
    solve()