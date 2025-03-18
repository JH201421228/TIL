import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]

delta = [(1, 0), (0, 1)]

for i in range(N):
    for j in range(M):
        for di, dj in delta:
            xi, xj = i+di, j+dj
            if xi >= 0 and xi < N and xj >= 0 and xj < M:
                ans[xi][xj] = max(ans[xi][xj], MAP[xi][xj] + ans[i][j])

print(ans[-1][-1])