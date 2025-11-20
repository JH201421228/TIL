import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MAX = 1_000_000_000


def solve():
    cur = int(input())

    ans = 0
    n = 5

    while True:
        if n > cur: break

        ans += cur//n

        n *= 5

    print(ans)

    return


def main():
    for _ in range(int(input())):
        solve()

    return


if __name__ == "__main__":
    main()