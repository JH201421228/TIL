import sys
from collections import deque
# sys.stdin = open('input.txt')


def worm(start_x, start_y, M, N):
    que = deque([[start_x, start_y]])
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    global cnt

    while que:
        x, y = que.popleft()
        farm[x][y] = 0
        for dx, dy in delta:
            if 0 <= x+dx < M and 0 <= y+dy < N and farm[x+dx][y+dy]:
                que.append([x+dx, y+dy])
                farm[x+dx][y+dy] = 0
    cnt += 1

Test_Case = int(input())
for _ in range(Test_Case):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    cnt = 0
    point = []
    for _ in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1
        point.append([x, y])

    for i, j in point:
        if farm[i][j]:
            worm(i, j, M, N)

    print(cnt)

