import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    ans = 1

    while sharks:
        i, j = sharks.popleft()

        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii >= 0 and ii < N and jj >= 0 and jj < M and not grid[ii][jj]:
                grid[ii][jj] = grid[i][j] + 1
                sharks.append((ii, jj))
                ans = max(ans, grid[ii][jj])

    return ans-1


N, M = map(int, input().split())

delta = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]

grid = [list(map(int, input().split())) for _ in range(N)]

sharks = deque([])
for i in range(N):
    for j in range(M):
        if grid[i][j]: sharks.append((i, j))

print(solve())