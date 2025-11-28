import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    test = 111111111111111111111111111111111111111111111111111111111111111

    print(len(str(test)))
    print(test % 15)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()