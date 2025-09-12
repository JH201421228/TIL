import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(i, j, M, N, G, V):
    if i == M-1 and j == N-1: return 1
    if V[i][j] != -1: return V[i][j]

    V[i][j] = 0

    for di, dj in delta:
        ii, jj = i+di, j+dj

        if ii >= 0 and jj >= 0 and ii < M and jj < N:
            if G[ii][jj] < G[i][j]:
                V[i][j] += dfs(ii, jj, M, N, G, V)

    return V[i][j]


def solve():
    M, N = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(M)]
    V = [[-1] * N for _ in range(M)]

    print(dfs(0, 0, M, N, G, V))

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()