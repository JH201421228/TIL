import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze(N, M):

    start_x = start_y = 0
    end_x = N - 1
    end_y = M - 1
    delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    que = deque([])
    que.append([start_x, start_y])
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= (x + dx) < N and 0 <= (y + dy) < M and matrix[x + dx][y + dy] and not checker[x+dx][y+dy]:
                    que.append([x + dx, y + dy])
                    checker[x+dx][y+dy] = 1
                    matrix[x + dx][y + dy] = matrix[x][y] + 1
            if x+dx == end_x and y+dy == end_y:
                return matrix[end_x][end_y]


N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().rstrip())))

checker = [[0] * M for _ in range(N)]
checker[0][0] = 1

print(maze(N, M))






