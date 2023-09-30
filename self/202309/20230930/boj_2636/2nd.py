import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def holiday(start):
    que = deque(start)
    return_set = set()

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if not cheeze[x+dx][y+dy]:
                    cheeze[x+dx][y+dy] = -1
                    que.append((x+dx, y+dy))
                elif cheeze[x+dx][y+dy] == 1:
                    cheeze[x+dx][y+dy] = -1
                    return_set.add((x+dx, y+dy))
    return return_set


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
# 치즈의 가장자리가 조사 시작 지점
# 근처의 치즈를 녹여가며 녹인 부분을 조사지점으로 교체
# 한번 while을 돌 떄 녹이는 횟수를 저장
# 마지막 녹인 횟수를 반환
cheeze[0][0] = -1
start_point = [(0, 0)]
ans_list = []
while True:
    start_point = list(holiday(start_point))
    length = len(start_point)
    if length:
        ans_list.append(len(start_point))
    else:
        break
print(len(ans_list))
print(ans_list[-1])