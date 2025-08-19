import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def setting_G(val, grid, R, C):
    G = [[] for _ in range(R*C+1)]
    res = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] > val:
                res += 1
            if not (i+j)%2 and grid[i][j] > val:
                for di, dj in delta:
                    ii, jj = i+di, j+dj
                    if ii >= 0 and ii < R and jj >= 0 and jj < C and grid[ii][jj] > val:
                        G[i*C+j+1].append(ii*C+jj+1)

    return G, res


def B(n, V, C, G):
    for x in G[n]:
        if V[x]: continue
        V[x] = 1

        if not C[x] or B(C[x], V, C, G):
            C[x] = n
            return True

    return False


def solve():
    R, C, D, W = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(R)]

    Zs = set()
    for i in range(R):
        for j in range(C):
            Zs.add(grid[i][j])
    Zs = list(Zs)
    Zs.append(0)
    Zs.sort()

    ans = float("inf")

    print(Zs)

    for val in Zs:
        G, cnt = setting_G(val, grid, R, C)
        E = [0] * (R*C+1)

        count = 0
        for n in range(1, R*C+1):
            V = [0] * (R*C+1)
            if B(n, V, E, G):
                count += 1

        if count*2 == cnt:
            ans = min(ans, val*W + count*D)
            print(val*W + count*D)

    # print(ans)

    return


if __name__ == "__main__":
    solve()