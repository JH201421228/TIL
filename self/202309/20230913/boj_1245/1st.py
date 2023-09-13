import sys
from collections import deque
sys.stdin = open('input.txt')

delta = [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]

def find_mountain_top(cor_x, cor_y):
    temp_list = [[cor_x, cor_y]]
    que = deque([[cor_x, cor_y]])
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and [x+dx, y+dy] not in temp_list:
                if farm_info[x+dx][y+dy] > farm_info[x][y]:
                    return False
                elif farm_info[x+dx][y+dy] == farm_info[x][y]:
                    que.append([x+dx, y+dy])
                    temp_list.append([x+dx, y+dy])
    top_info.extend(temp_list)
    return True

N, M = map(int, input().split())
farm_info = [list(map(int, input().split())) for _ in range(N)]
# 주변에 자기보다 큰 값이 있으면 산봉우리 아님
# 주변에 자기보다 큰 값이 없으면 산봉우리임
# 주변에 자기보다 큰 값이 없고 같은 값만 있다면 탐사를 진행함
top_info = []
ans = 0
for idx_i in range(N):
    for idx_j in range(M):
        if [idx_i, idx_j] not in top_info:
            if find_mountain_top(idx_i, idx_j):
                ans += 1
print(ans)
