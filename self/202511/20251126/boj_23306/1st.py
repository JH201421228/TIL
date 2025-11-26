import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    res = []

    print(f"? {1}", flush=True)
    res.append(int(input()))

    print(f"? {N}", flush=True)
    res.append(int(input()))

    if res[0] == res[1]:
        print(0)
    elif res[0] < res[1]:
        print(1)
    else:
        print(-1)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()