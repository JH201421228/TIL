import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    input()

    ans = "2000\n"
    ans += "1 " * 1000
    ans += "1000 " * 1000

    print(ans)

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()