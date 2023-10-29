import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 한칸 이동시 1의 연료 소모
# 고객을 태우고 이동한 거리의 2배만큼 충전


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def taxi_driver(i, j, status):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    q = deque([(i, j, 0)])
    temp = []
    flag = 0
    while q:
        x, y, dist = q.popleft()
        if flag and dist >= flag:
            temp.sort()
            # print(temp)
            return temp
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy] and MAP[x+dx][y+dy] != 1:
                visited[x+dx][y+dy] = 1
                q.append((x+dx, y+dy, dist + 1))
                if not status and MAP[x+dx][y+dy] > 1:
                    temp.append((x+dx, y+dy, dist + 1))
                    flag = dist + 1
                if status and MAP[x+dx][y+dy] == destination:
                    return x+dx, y+dy, dist + 1

    if temp:
        temp.sort()
        # print(temp)
        return temp

    return False


N, M, F = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

s_i, s_j = map(int, input().split())

customer_num = 0
for num in range(M):
    c_s_i, c_s_j, c_e_i, c_e_j = map(int, input().split())
    # drive.append((c_s_i, c_s_j, c_e_i, c_e_j))
    MAP[c_s_i - 1][c_s_j - 1] = num + 2
    MAP[c_e_i - 1][c_e_j - 1] = -(num + 2)
    customer_num += 1

destination = 0
idx_x = s_i-1
idx_y = s_j-1
while customer_num > 0:

    value = taxi_driver(idx_x, idx_y, 0)
    if not value:
        print(-1)
        exit(0)

    idx_x, idx_y, expend = value[0]
    F -= expend
    destination = (-MAP[idx_x][idx_y])
    MAP[idx_x][idx_y] = 0

    if F <= 0:
        print(-1)
        exit(0)

    value = taxi_driver(idx_x, idx_y, 1)
    if not value:
        print(-1)
        exit(0)
    # print(value)
    idx_x, idx_y, expend = value
    F -= expend

    if F < 0:
        print(-1)
        exit(0)

    F += expend*2
    customer_num -= 1

print(F)

