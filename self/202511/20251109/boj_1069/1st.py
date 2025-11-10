import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    X, Y, D, T = map(int, input().split())

    dist = (X**2 + Y**2) ** .5

    if D / T > 1:
        temp = dist // D
        ans = temp * T
        cur = dist - temp * D

        if temp:
            print(ans + min(T, cur, T+D-cur))
        else:
            print(ans + min(2*T, cur, T+D-cur))

    else:
        print(dist)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()