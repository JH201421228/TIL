import sys
from collections import deque
# sys.stdin = open('input.txt')


def rotten_tomato(start_info, M, N, H):
    que = deque([])
    que.extend(start_info)
    delta = [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, -1], [0, 0, 1]]
    cnt = 0

    if not start_info:
        return -1

    while que:
        x, y, z = que.popleft()
        for dx, dy, dz in delta:
            if 0 <= x+dx < H and 0 <= y+dy < N and 0 <= z+dz < M and not tomato_box[x+dx][y+dy][z+dz]:
                cnt = tomato_box[x][y][z]
                tomato_box[x+dx][y+dy][z+dz] = cnt + 1
                que.append([x+dx, y+dy, z+dz])

    for matrix in tomato_box:
        for inner_list in matrix:
            if 0 in inner_list:
                return -1

    return cnt


M, N, H = map(int, input().split())
tomato_box = []
for i in range(H):
    tomato = []
    for j in range(N):
        tomato.append(list(map(int, input().split())))
    tomato_box.append(tomato)

start_info = []
for x in range(H):
    for y in range(N):
        for z in range(M):
            if tomato_box[x][y][z] == 1:
                start_info.append([x, y, z])

print(rotten_tomato(start_info, M, N, H))