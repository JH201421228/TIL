import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    qs = list(map(float, input().split()))
    rs = list(map(float, input().split()))

    C = qs[N-1]/rs[N-1]
    for idx in range(N-1, 0, -1):
        rs[idx-1] += rs[idx]
        C += (qs[idx-1]/rs[idx-1])

    ans = []
    for idx in range(N):
        ans.append((qs[idx]/rs[idx])/C)

    print(*ans)

    return


if __name__ == "__main__":
    solve()