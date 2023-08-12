import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze_runner(N, M):
    if N == 1 and M == 1:
        return 1

    que = deque([])
    que.append([0, 0, 0])
    mapping_list[0][0][0] = 1
    delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while que:
        x, y, z = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if not maze[x+dx][y+dy] and not mapping_list[x+dx][y+dy][z]:
                    que.append([x+dx, y+dy, z])
                    mapping_list[x+dx][y+dy][z] = mapping_list[x][y][z] + 1

                elif maze[x+dx][y+dy] and z == 0:
                    que.append([x+dx, y+dy, z+1])
                    mapping_list[x+dx][y+dy][z+1] = mapping_list[x][y][z] + 1


                if x+dx == N-1 and y+dy == M-1:
                    return mapping_list[x+dx][y+dy][z]
    return -1


N, M = map(int, input().split())

input_str = []
for _ in range(N):
    input_str.append(input())

maze = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        maze[i][j] = int(input_str[i][j])

mapping_list = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(maze_runner(N, M))
