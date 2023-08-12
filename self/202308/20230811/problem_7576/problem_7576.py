import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def rotten_tomato(start_point, M, N):
    cnt = 0
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    if not start_point:
        return -1

    que = deque([])
    que.extend(start_point)

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not tomato[x+dx][y+dy]:
                que.append([x+dx, y+dy])
                cnt = tomato[x][y]
                tomato[x+dx][y+dy] = cnt + 1

    for inner_list in tomato:
        if 0 in inner_list:
            return - 1

    return cnt

M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))

start_point = [] # 시작점에 대한 정보를 저장

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start_point.append([i, j])

print(rotten_tomato(start_point, M, N))