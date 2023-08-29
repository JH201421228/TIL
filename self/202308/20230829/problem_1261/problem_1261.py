import sys
from collections import deque
# sys.stdin = open('input.txt')


def maze_runner(N, M): # 부순 벽이 적으면 덮어쓰기 가능
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque([[0, 0, 0]])

    while que:
        x, y, break_num = que.popleft()

        for dx, dy in delta:
            if 0 <= x+dx < M and 0 <= y+dy < N:
                if not maze[x+dx][y+dy]: # 미로에 길이 있으면
                    if (not maze_check[x+dx][y+dy][0] and not maze_check[x+dx][y+dy][1]) or maze_check[x+dx][y+dy][1] > break_num: # 미로 체크 배열에서 방문한적 없는 길이거나, 벽을 더 적게 부수고 갈 수 있다면
                        maze_check[x+dx][y+dy][0] = maze_check[x][y][0] + 1
                        maze_check[x+dx][y+dy][1] = break_num
                        que.append([x+dx, y+dy, break_num])
                else: # 미로에 길이 없으면
                    if (not maze_check[x + dx][y + dy][0] and not maze_check[x + dx][y + dy][1]) or maze_check[x + dx][y + dy][1] > break_num + 1:
                        maze_check[x + dx][y + dy][0] = maze_check[x][y][0] + 1
                        maze_check[x + dx][y + dy][1] = break_num + 1
                        que.append([x+dx, y+dy, break_num + 1])

N, M = map(int, input().split())
maze = [list(map(int, map(str, input()))) for _ in range(M)]
maze_check = [[[0] * 2 for _ in range(N)] for _ in range(M)] # [i, j] i : 이동 거리, j : 부순 벽의 개수

# print(maze)
maze_check[0][0][0] = 1
maze_runner(N, M)
# for inner in maze_check:
#     print(inner)
print(maze_check[M-1][N-1][1])

