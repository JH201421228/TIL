import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday():
    ans = []
    cnt = 0
    x_num = 0
    while start_point:

        x, y, num = start_point.popleft()
        if num != x_num:
            ans.append(cnt)
            cnt = 0
            x_num = num
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and cheeze[x+dx][y+dy] == 1:
                cheeze[x+dx][y+dy] = 0
                start_point.append((x+dx, y+dy, num + 1))
                cnt += 1
    return num, ans

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
# 치즈의 가장자리가 조사 시작 지점
# 근처의 치르를 녹여가며 녹인 부분을 조사지점으로 교체
# 한번 while을 돌 떄 녹이는 횟수를 저장
# 마지막 녹인 횟수를 반환
start_point = deque([])
start_point_set = set()
que = deque([(0, 0)])
cheeze[0][0] = -1
while que:
    x, y = que.popleft()
    for dx, dy in delta:
        if 0 <= x+dx < N and 0 <= y+dy < M:
            if not cheeze[x+dx][y+dy]:
                cheeze[x+dx][y+dy] = -1
                que.append((x+dx, y+dy))
            elif cheeze[x+dx][y+dy] == 1:
                start_point_set.add((x, y, 0))
for inner in cheeze:
    print(inner)
# for i in range(N):
#     for j in range(M):
#         if not cheeze[i][j]:
#             for di, dj in delta:
#                 if 0 <= i+di < N and 0 <= j+dj < M and cheeze[i+di][j+dj]:
#                     start_point_set.add((i+di, j+dj, 0))
start_point.extend(list(start_point_set))
# print(start_point)
print(holiday())