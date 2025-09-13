import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fibo():
    res = [1, 2]

    while True:
        temp = res[-1] + res[-2]
        if temp < 1e18:
            res.append(temp)
        else:
            break

    return res


def solve(fibo_seq):
    N = int(input())

    ans = []
    idx = len(fibo_seq)-1
    while idx >= 0:
        if N >= fibo_seq[idx]:
            ans.append(fibo_seq[idx])
            N -= fibo_seq[idx]
        idx -= 1

    ans.sort()

    print(len(ans))
    print(*ans)

    return


def main():
    solve(fibo())
    return


if __name__ == "__main__":
    main()