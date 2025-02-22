import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    V[x][y] = 1
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            if xx >= 0 and xx < N and yy >= 0 and yy < M and not V[xx][yy] and MAP[xx][yy] != 1:
                if MAP[xx][yy] != 0:
                    print("TAK")
                    print(V[x][y])
                    exit(0)
                V[xx][yy] = V[x][y] + 1
                q.append((xx, yy))

N, M = map(int, input().split())

MAP = [list(map(int, input().rstrip())) for _ in range(N)]

V = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            bfs(i, j)
            print("NIE")
            break