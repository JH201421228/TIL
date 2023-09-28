import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday(start, end):
    start_x, start_y = start
    end_x, end_y = end
    ans_list = [[float('inf')] * W for _ in range(H)]
    pq = [(0, 0, start_x, start_y)]
    # cnt, status, x, y
    ans_list[start_x][start_y] = 0

    while pq:
        cnt, status, x, y = heapq.heappop(pq)
        for dx, dy in delta:
            if 0 <= x+dx < H and 0 <= y+dy < W:
                if (not dx and status == 1) or (not dy and status == -1): # 방향전환시 cnt 증가 및 상태 변환
                    next_cnt = cnt + 1
                    next_status = status * -1
                else:
                    next_cnt = cnt
                    next_status = status
                if not status:
                    if not dx:
                        next_status = -1
                    else:
                        next_status = 1
                if razor[x+dx][y+dy] != '*' and ans_list[x+dx][y+dy] > next_cnt:
                    # if x+dx == end_x and y+dy == end_y:
                    #     return next_cnt
                    ans_list[x+dx][y+dy] = next_cnt
                    heapq.heappush(pq, (next_cnt, next_status, x+dx, y+dy))
    return ans_list[end_x][end_y]

W, H = map(int, input().split())
razor = [list(input().rstrip()) for _ in range(H)]
C_point = []
for i in range(H):
    for j in range(W):
        if razor[i][j] == 'C':
            C_point.append((i, j))
# 방향전환에 가중치 1
# 방향전환 횟수를 가장 적게해서 다른 포인트에 도착하면 답
# 수직으로 움직이는 status 1, 수평으로 움직이는 상황 status -1


ans1 = holiday(C_point[0], C_point[1])
ans2 = holiday(C_point[1], C_point[0])
# for inner in ans:
#     print(inner)
# print(ans[6][1])
print(min(ans1, ans2))