import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n, k, v, pre):
    global ans

    if n == k:
        ans = max(ans, v)
        return

    if pre >= N*M:
        return

    for x in range(pre, N*M):
        i, j = x // M, x % M

        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii >= 0 and ii < N and jj >= 0 and jj < M and not checker[ii][jj] or (ii < 0 or ii >= N or jj < 0 or jj >= M):
                continue
            else:
                break
        else:
            checker[i][j] = 1
            dfs(n+1, k, v+B[i][j], i*M+j+1)
            checker[i][j] = 0
    return


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M, K = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]
checker = [[0] * M for _ in range(N)]
ans = -float("inf")

dfs(0, K, 0, 0)

print(ans)