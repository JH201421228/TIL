import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday():
    start_x, start_y = C_point[0]
    end_x, end_y = C_point[1]
    ans_list1 = [[float('inf')] * W for _ in range(H)]
    ans_list2 = [[float('inf')] * W for _ in range(H)]
    pq = [(0, 0, start_x, start_y)]
    # cnt, status, x, y
    ans_list1[start_x][start_y] = 0
    ans_list2[start_x][start_y] = 0

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
                if razor[x+dx][y+dy] != '*':
                    if status == 1 and  ans_list1[x+dx][y+dy] > next_cnt:
                        # if x+dx == end_x and y+dy == end_y:
                        #     return next_cnt
                        ans_list1[x+dx][y+dy] = next_cnt
                        heapq.heappush(pq, (next_cnt, next_status, x+dx, y+dy))

                    if status == -1 and  ans_list2[x+dx][y+dy] > next_cnt:
                        # if x+dx == end_x and y+dy == end_y:
                        #     return next_cnt
                        ans_list2[x+dx][y+dy] = next_cnt
                        heapq.heappush(pq, (next_cnt, next_status, x+dx, y+dy))

    return min(ans_list1[end_x][end_y], ans_list2[end_x][end_y])

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


ans = holiday()
# for inner in ans:
#     print(inner)
# print(ans[6][1])
print(ans)