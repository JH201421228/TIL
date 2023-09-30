import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday():
    que1 = deque([water])
    que2 = deque([animal])
    check = [[0] * C for _ in range(R)]
    check[water[0]][water[1]] = float('inf')
    check[animal[0]][animal[1]] = 1

    while que1 and que2:
        w_x, w_y = que1.popleft()
        a_x, a_y = que2.popleft()
        for dx, dy in delta:
            if 0 <= w_x+dx < R and 0 <= w_y+dy < C and field[w_x+dx][w_y+dy] not in 'XD' and check[w_x+dx][w_y+dy] != float('inf'):
                check[w_x+dx][w_y+dy] = float('inf')
                que1.append((w_x+dx, w_y+dy))
        for dx, dy in delta:
            if 0 <= a_x+dx < R and 0 <= a_y+dy < C and field[a_x+dx][a_y+dy] != 'X' and (not check[a_x+dx][a_y+dy] or check[a_x+dx][a_y+dy] != float('inf')):
                if field[a_x + dx][a_y + dy] == 'D':
                    return check[a_x][a_y]
                check[a_x+dx][a_y+dy] = check[a_x][a_y] + 1
                que2.append((a_x+dx, a_y+dy))
    return "KAKTUS"

# . 빈곳, * 물이 차있는 곳, X 돌, 비버의 굴 D, 고슴도치 S
# 물이 먼저 차고, 고슴도치가 이동
R, C = map(int, input().split())
field = [list(input().rstrip()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if field[i][j] == '*':
            water = (i, j)
        elif field[i][j] == 'S':
            animal = (i, j)
print(holiday())