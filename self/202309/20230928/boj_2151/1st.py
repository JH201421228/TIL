import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday(start, end):
    start_x, start_y = start
    end_x, end_y = end
    ans_list = [[float('inf')] * N for _ in range(N)]
    ans_list[start_x][start_y] = 0
    pq = []
    for dx, dy in delta:
        if 0 <= start_x+dx < N and 0 <= start_y+dy < N and house[start_x+dx][start_y+dy] != '*':
            if house[start_x+dx][start_y+dy] == '#':
                return 0
            elif house[start_x+dx][start_y+dy] == '!':
                ans_list[start_x + dx][start_y + dy] = 0
                heapq.heappush(pq, (0, dx, dy, start_x + dx, start_y + dy))
                heapq.heappush(pq, (1, dy, dx, start_x + dx, start_y + dy))
                heapq.heappush(pq, (1, dy * -1, dx * -1, start_x + dx, start_y + dy))
            else:
                ans_list[start_x+dx][start_y+dy] = 0
                heapq.heappush(pq, (0, dx, dy, start_x+dx, start_y+dy))

    while pq:
        cnt, dx, dy, x, y = heapq.heappop(pq)
        if not dx:
            while True:
                y += dy
                if 0 <= y < N:
                    if house[x][y] == '.' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                    elif house[x][y] == '!' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                        heapq.heappush(pq, (cnt + 1, 1, 0, x, y))
                        heapq.heappush(pq, (cnt + 1, -1, 0, x, y))
                    elif house[x][y] == '#' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                        break
                    else:
                        break
        else:
            while True:
                x += dx
                if 0 <= x < N:
                    if house[x][y] == '.' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                    elif house[x][y] == '!' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                        heapq.heappush(pq, (cnt + 1, 0, 1, x, y))
                        heapq.heappush(pq, (cnt + 1, 0, -1, x, y))
                    elif house[x][y] == '#' and ans_list[x][y] > cnt:
                        ans_list[x][y] = cnt
                        break
                    else:
                        break
    return ans_list[end_x][end_y]


N = int(input())
house = [list(input().rstrip()) for _ in range(N)]
# !를 지나면 방향이 전환됨과 동시에 cnt 증가
point = []
for i in range(N):
    for j in range(N):
        if house[i][j] == '#':
            point.append((i, j))
ans = holiday(point[0], point[1])
# for inner in ans:
#     print(inner)
print(ans)
