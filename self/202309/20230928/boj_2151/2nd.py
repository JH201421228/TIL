import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday(start, end):
    ans_list = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    que = deque([])
    start_x, start_y = start
    end_x, end_y = end
    for i in range(4):
        dx, dy = delta[i]
        if 0 <= start_x+dx < N and 0 <= start_y+dy < N and house[start_x+dx][start_y+dy] != '*':
            ans_list[start_x+dx][start_y+dy][i] = 0
            que.append((start_x+dx, start_y+dy, i))
        # print(que)
    while que:
        x, y, idx = que.popleft()
        dx, dy = delta[idx]

        if not (0 <= x+dx < N and 0 <= y+dy < N and house[x+dx][y+dy] != '*'):
            continue

        if house[x+dx][y+dy] == '.':
            if ans_list[x+dx][y+dy][idx] > ans_list[x][y][idx]:
                ans_list[x + dx][y + dy][idx] = ans_list[x][y][idx]
                que.append((x+dx, y+dy, idx))
        elif house[x+dx][y+dy] == '!':
            if ans_list[x+dx][y+dy][idx] > ans_list[x][y][idx]:
                ans_list[x + dx][y + dy][idx] = ans_list[x][y][idx]
                que.append((x+dx, y+dy, idx))
            if ans_list[x+dx][y+dy][(idx+1) % 4] > ans_list[x][y][idx] + 1:
                ans_list[x + dx][y + dy][(idx + 1) % 4] = ans_list[x][y][idx] + 1
                que.append((x+dx, y+dy, (idx + 1) % 4))
            if ans_list[x + dx][y + dy][(idx + 3) % 4] > ans_list[x][y][idx] + 1:
                ans_list[x + dx][y + dy][(idx + 3) % 4] = ans_list[x][y][idx] + 1
                que.append((x + dx, y + dy, (idx + 3) % 4))
    return min(ans_list[end_x][end_y])
N = int(input())
house = [list(input().rstrip()) for _ in range(N)]
# !를 지나면 방향이 전환됨과 동시에 cnt 증가
point = []
for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            point.append((i, j))
            house[i][j] = '.'
ans = holiday(point[0], point[1])
# for inner in ans:
#     print(inner)
print(ans)