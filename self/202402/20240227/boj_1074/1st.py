import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def di_con(r, c):
    global N, ans
    N -= 1

    if N < 0:
        print(ans)
        exit(0)

    if r < 2**N and c < 2**N:
        di_con(r, c)
    elif r < 2**N and c >= 2**N:
        ans += (2**N)**2
        di_con(r, c - 2**N)
    elif r >= 2**N and c < 2**N:
        ans += ((2**N)**2) * 2
        di_con(r - 2**N, c)
    else:
        ans += ((2 ** N) ** 2) * 3
        di_con(r - 2**N, c - 2**N)

N, r, c = map(int, input().split())
ans = 0
di_con(r, c)

