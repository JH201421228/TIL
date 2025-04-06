import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(n, x, y):
    V = [[0] * (n+1) for _ in range(n+1)]
    q = deque([(x, y)])
    V[x][y] = 1

    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ii, jj = i+di, j+dj
            if ii > 0 and ii <= n and jj > 0 and jj <= n and not V[ii][jj]:
                q.append((ii, jj))
                V[ii][jj] = V[i][j] + 1

    ans_list = []
    for i, j in target:
        ans_list.append(V[i][j]-1)

    print(*ans_list)

    return


delta = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

N, M = map(int, input().split())
x, y = map(int, input().split())
target = [tuple(map(int, input().split())) for _ in range(M)]

bfs(N, x, y)