import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def path_finder(si, N, M):
    sj = 0
    res = 1
    while sj < N-1:
        res += 1
        if M[si][sj+1] == '.': sj += 1
        else: si = 1 - si

    return res


def solve():
    N = int(input())
    M = [list(input().rstrip()) for _ in range(2)]

    cnt = 0
    for m in M:
        for n in m:
            if n == '.': cnt += 1

    count = float("inf")
    if M[0][0] == '.': count = min(count, path_finder(0, N, M))
    if M[1][0] == '.': count = min(count, path_finder(1, N, M))

    print(cnt - count)
    return


if __name__ == "__main__":
    solve()