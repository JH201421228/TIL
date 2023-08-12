import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze_runner(jump_point, N, M):

    if N == 1 and M == 1:
        return 1

    que = deque([])
    que.append([0, 0])
    delat = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ans = []

    for break_x, break_y in jump_point:
        maze_dup = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if maze[i][j]:
                    maze_dup[i][j] = 1  # 시험용 미로 만듦, 0은 갈 수 있음, 1은 막힘

        maze_dup[break_x][break_y] = 0 # 벽을 부숨
        maze_dup[0][0] = 1
        cnt = 0
        while que:
            x, y = que.popleft()
            for dx, dy in delat:
                if 0 <= x+dx < N and 0 <= y+dy < M and not maze_dup[x+dx][y+dy]:
                    que.append([x+dx, y+dy])
                    cnt = maze_dup[x][y] + 1
                    maze_dup[x+dx][y+dy] = cnt
        if maze_dup[N-1][M-1]:
            ans.append(cnt)

    if not ans:
        return -1
    else:
        return min(ans)

N, M = map(int, input().split())
input_list = []
for _ in range(N):
    input_list.append(input())

maze = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        maze[i][j] = (int(input_list[i][j]))

jump_point = []

for i in range(N):
    for j in range(M):
        if maze[i][j]:
            jump_point.append([i, j])

print(maze_runner(jump_point, N, M))
