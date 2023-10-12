import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def dfs():
    que = deque([start])

    while que:
        x, y, z = que.popleft()
        for dx, dy, dz in delta:
            if 0 <= x+dx < C and 0 <= y+dy < R and 0 <= z+dz < L and (building[x+dx][y+dy][z+dz] == '.' or building[x+dx][y+dy][z+dz] == 'E'):
                if building[x+dx][y+dy][z+dz] == 'E':
                    return f'Escaped in {building[x][y][z]} minute(s).'
                building[x + dx][y + dy][z + dz] = building[x][y][z] + 1
                que.append((x+dx, y+dy, z+dz))
    return 'Trapped!'


while True:
    C, R, L = map(int, input().split())
    if not C and not R and not L:
        break
    building = []
    for _ in range(C):
        building.append([list(input().rstrip()) for _ in range(R)])
        input()
    # print(building)
    for i in range(C):
        for j in range(R):
            for k in range(L):
                if building[i][j][k] == 'S':
                    building[i][j][k] = 1
                    start = tuple((i, j, k))
                    break


    print(dfs())
    # print(building)