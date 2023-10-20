import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 빙산은 1년이 지날 때 마다 인접한 바다 칸의 개수만큼 줄어듦
# 빙산이 2 조각 이상이 되면 끝
# 빙산이 2 조각이 안되면 0을 출력


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(qq):
    q = deque(qq)
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i, j in q:
        visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy]:
                if not iceberg[x+dx][y+dy]:
                    visited[x+dx][y+dy] = 1
                    q.append((x+dx, y+dy))
                else:
                    iceberg[x+dx][y+dy] -= 1
                    if not iceberg[x+dx][y+dy]:
                        visited[x+dx][y+dy] = 1
                        cnt += 1
    return cnt


def ice_bfs(iceberg_num):
    qqq = deque([])
    visited = [[0] * M for _ in range(N)]
    flag = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if iceberg[i][j]:
                qqq.append((i, j))
                visited[i][j] = 1
                flag = 1
                break
        if flag:
            break

    count = 1
    while qqq:
        x, y = qqq.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy] and iceberg[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                count += 1
                qqq.append((x+dx, y+dy))
    if count != iceberg_num:
        return True
    else:
        return False


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
iceberg_num = 0
qq = []
for i in range(N):
    for j in range(M):
        if not iceberg[i][j]:
            qq.append((i, j))
        else:
            iceberg_num += 1
year = 0
check = 0
while True:
    year += 1
    cnt = bfs(qq)
    # for inner in iceberg:
    #     print(inner)
    # print(iceberg_num)
    # print(cnt)
    iceberg_num -= cnt
    if not iceberg_num:
        print(0)
        break
    if ice_bfs(iceberg_num):
        print(year)
        check = 1
        break
# if not iceberg_num and not check:
#     print(0)
