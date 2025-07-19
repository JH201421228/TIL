import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    P = [[] for _ in range(N)]

    for _ in range(M):
        p = list(map(int, input().split()))
        for idx in range(N):
            P[idx].append(p[idx])

    res = []
    ans = 0
    for idx in range(N):
        P[idx].sort()

        if not M % 2:
            mid = round((P[idx][M//2 - 1] + P[idx][M//2]) / 2)
            res.append(mid)
            for p in P[idx]:
                ans += abs(p - mid)

        else:
            mid = P[idx][M//2]
            res.append(mid)
            for p in P[idx]:
                ans += abs(p - mid)

    print(ans)
    print(*res)

    return


if __name__ == "__main__":
    solve()