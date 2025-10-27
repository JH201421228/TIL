import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    ans = [0] * 2 * (N//2)

    for i in range(2 * (N//2)):
        idx = (2 * (N//2) - 1 + ((-1)**(i+1))*(2 * (N//2)-1))//2 + ((-1)**i)*2*(i//2)
        value = N//2 + ((-1)**(i+1)) * ((i+1)//2)
        ans[idx] = value

    if N%2:
        print(N, *ans)
    else:
        print(*ans)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()