import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 상어는 자기보다 작거나 같은 물고기가 있는 공간만 이동 가능
# 상어는 자기 크기와 같은 수의 물고기를 먹으면 크기가 1 증가한다


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(position, siz, stat):
    i, j = position
    q = deque([(i, j, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[position[0]][position[1]] = 1
    temp = []
    flag = 0

    while q:
        x, y, dist = q.popleft()
        if flag and dist >= flag:
            # print(temp)
            return temp

        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy]:
                if shark[x+dx][y+dy] == siz or not shark[x+dx][y+dy]:
                    visited[x+dx][y+dy] = 1
                    q.append((x+dx, y+dy, dist+1))
                elif shark[x+dx][y+dy] < siz:
                    visited[x+dx][y+dy] = 1
                    temp.append((x+dx, y+dy, dist+1))
                    flag = dist+1
    if temp:
        # print(temp)
        return temp
    return False


N = int(input())
shark = [list(map(int, input().split())) for _ in range(N)]

flag = 0
for i in range(N):
    for j in range(N):
        if shark[i][j] == 9:
            shark[i][j] = 0
            pos = (i, j)
            flag = 1
            break
    if flag:
        break

# 함수에는 상어의 위치, 크기, 상태 가 입력되어야 함
# 함수는 먹이를 먹을 수 있는지,
# 먹을 수 있다면 거리값 및 같은 거리에 있는 물고기 좌표 반환
size = 2 # 상어 크기
status = 0 # 상어가 먹은 물고기 개수
total_time = 0

while True: # 더이상 물고기를 먹지 못할 떄 까지 반복
    value = bfs(pos, size, status)
    if not value:
        print(total_time)
        break
    value.sort()
    inner = value[0]
    status += 1
    if size == status:
        size += 1
        status = 0
    shark[inner[0]][inner[1]] = 0
    pos = (inner[0], inner[1])
    total_time += inner[2]