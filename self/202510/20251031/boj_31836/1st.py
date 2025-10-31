import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())

    first = []
    second = []

    if N%3 == 1:
        for i in range(2, N+1, 3):
            first.append(i)
            first.append(i+1)

            second.append(i+2)

    elif N%3 == 2:
        first.append(1)
        second.append(2)

        for i in range(3, N+1, 3):
            first.append(i)
            first.append(i+1)

            second.append(i+2)

    else:
        for i in range(1, N+1, 3):
            first.append(i)
            first.append(i+1)

            second.append(i+2)

    print(len(first))
    print(*first)
    print(len(second))
    print(*second)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()