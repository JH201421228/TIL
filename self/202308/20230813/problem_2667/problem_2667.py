import sys
from collections import deque
# sys.stdin = open('input.txt')


def numbering(N, start_x, start_y):
    global check_num
    if mapping_list[start_x][start_y] != 1:
        return False
    trace[start_x][start_y] = 1
    cnt = 1
    check_num += 1
    que = deque([[start_x, start_y]])
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and mapping_list[x+dx][y+dy] and not trace[x+dx][y+dy]:
                trace[x+dx][y+dy] = 1
                que.append([x+dx, y+dy])
                cnt += 1
                mapping_list[x+dx][y+dy] = check_num
    ans.append(cnt)
    return True

N = int(input())

input_list = [input() for _ in range(N)]
mapping_list = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        mapping_list[i][j] = int(input_list[i][j])
trace = [[0] * N for _ in range(N)]
check_num = 1
ans = []
for i in range(N):
    for j in range(N):
        numbering(N, i, j)
ans.sort()
print(check_num - 1)
for i in ans:
    print(i)