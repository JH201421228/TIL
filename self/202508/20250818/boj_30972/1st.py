import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def area(si, sj, ei, ej, arrs):
    res = arrs[ei][ej]
    res -= arrs[ei][sj-1] if sj > 0 else 0
    res -= arrs[si-1][ej] if si > 0 else 0
    res += arrs[si-1][sj-1] if si > 0 and sj > 0 else 0

    res -= 2 * (arrs[ei-1][ej-1] - arrs[ei-1][sj] - arrs[si][ej-1] + arrs[si][sj])

    return -res


def solve():
    N = int(input())
    arrs = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not i and not j: continue
            elif not i: arrs[i][j] += arrs[i][j-1]
            elif not j: arrs[i][j] += arrs[i-1][j]
            else: arrs[i][j] = arrs[i][j] + arrs[i-1][j] + arrs[i][j-1] - arrs[i-1][j-1]

    Q = int(input())
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        print(area(r1-1, c1-1, r2-1, c2-1, arrs))

    return


if __name__ == "__main__":
    solve()