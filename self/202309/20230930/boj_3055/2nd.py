import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def water_field():
    que = deque(water)
    water_list = [[0] * C for _ in range(R)]
    # if not water:
    #     return [[float('inf')] * C for _ in range(R)]
    for i, j in water:
        water_list[i][j] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < R and 0 <= y+dy < C and field[x+dx][y+dy] not in 'XD' and not water_list[x+dx][y+dy]:
                water_list[x+dx][y+dy] = water_list[x][y] + 1
                que.append((x+dx, y+dy))
    return water_list


def animal_field():
    que = deque([animal])
    animal_list = [[0] * C for _ in range(R)]
    animal_list[animal[0]][animal[1]] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < R and 0 <= y+dy < C and field[x+dx][y+dy] != 'X' and not animal_list[x+dx][y+dy]:
                if field[x+dx][y+dy] == 'D':
                    return animal_list[x][y]
                if water_list[x+dx][y+dy] > animal_list[x][y] + 1 or not water_list[x+dx][y+dy]:
                    animal_list[x+dx][y+dy] = animal_list[x][y] + 1
                    que.append((x+dx, y+dy))
    return "KAKTUS"


# . 빈곳, * 물이 차있는 곳, X 돌, 비버의 굴 D, 고슴도치 S
# 물이 먼저 차고, 고슴도치가 이동
# 물이 찰것으로 예상되는 지점에 고슴도치가 미리 가 있을 수 없다.
R, C = map(int, input().split())
field = [list(input().rstrip()) for _ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if field[i][j] == '*':
            water.append((i, j))
        elif field[i][j] == 'S':
            animal = (i, j)
water_list = water_field()
# print(water_list)
print(animal_field())
# animal_list = animal_field()
# print(animal_list)
# for inner in water_list:
#     print(inner)
# print('---------------')
# for inner in animal_list:
#     print(inner)
