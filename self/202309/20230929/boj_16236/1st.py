import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]



def holiday():
    x, y = start
    que = deque([(x, y, 2, 0, 1, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    time = 0

    while que:
        x, y, size, hunger, check, temp_time = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] < check and matrix[x+dx][y+dy] <= size:
                visited[x+dx][y+dy] = check
                temp_list = []
                if matrix[x+dx][y+dy] and matrix[x+dx][y+dy] < size:
                    matrix[x+dx][y+dy] = 0
                    hunger += 1
                    check += 1
                    time = temp_time + 1
                    que.clear()
                    if size == hunger:
                        size += 1
                        hunger = 0
                    temp_list.append((x+dx, y+dy))
                    # que.append((x + dx, y + dy, size, hunger, check, temp_time + 1))
                    break
                else:
                    que.append((x + dx, y + dy, size, hunger, check, temp_time + 1))

                if temp_list:

    return time


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N**2):
    if matrix[i // N][i % N] == 9:
        start = (i//N, i%N)
        break
# 물고기를 잡아먹을 수 있는 시간을 출력
print(holiday())