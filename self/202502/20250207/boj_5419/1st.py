import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def U(idx):
    while idx < N+1:
        T[idx] += 1
        idx += (idx & -idx)


def S(idx):
    res = 0
    while idx > 0:
        res += T[idx]
        idx -= (idx & -idx)

    return res


for _ in range(int(input())):
    N = int(input())
    islands = []
    xs, ys = [], []
    xd, yd = {}, {}

    for _ in range(N):
        x, y = map(int, input().split())
        islands.append([x, -y])
        xs.append(x)
        ys.append(-y)

    xs.sort()
    ys.sort()

    prex = 1
    prey = 1
    for idx in range(N):
        xd[xs[idx]] = xd.get(xs[idx], prex)
        yd[ys[idx]] = yd.get(ys[idx], prey)
        prex += 1
        prey += 1

    for idx in range(N):
        x, y = islands[idx]
        islands[idx] = (xd[x], yd[y])

    islands.sort()

    T = [0] * (N+1)

    ans = 0
    for x, y in islands:
        ans += S(y)
        U(y)

    print(ans)