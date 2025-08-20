import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())

    ans = [0, 0]

    tmp = N
    while tmp > 1:
        tmp //= 2
        ans[0] += 1

    tmp = N
    while tmp >= 3:
        tmp //= 3
        ans[1] += 2

    k = ans[1]//2
    if N >= 2*(3**k):
        ans[1] += 1

    print(*ans)

    return


def init():
    for _ in range(int(input())):
        solve()


if __name__ == "__main__":
    init()