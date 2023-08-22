import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze(N, M): # 미로를 탐험하는 함수를 정의합니다.

    start_x = start_y = 0 # 시작 좌표를 정합니다. 이 값은 일정합니다.
    end_x = N - 1
    end_y = M - 1 # 탐색을 끝낼 지점을 정합니다.
    que = deque([]) # 방문가능한 지점을 저장할 큐를 만듭니다.
    que.append([start_x, start_y]) # 탐험 시작 좌표를 넣습니다.
    while que: # 큐에 값이 있는 동안 반복하겠습니다.
        x, y = que.popleft() # 현재 탐험할 위치를 지정합니다.
        for dx, dy in delta: # 델타 탐색할 값을 받아옵니다.
            if 0 <= (x + dx) < N and 0 <= (y + dy) < M and matrix[x + dx][y + dy] and not checker[x+dx][y+dy]: # 탐색할 좌표가 미로 안에 있는 좌표이고, 해당 좌표의 미로 값이 1이며, 방문기록이 없다면,
                    que.append([x + dx, y + dy]) # 해당 좌표를 큐에 넣습니다.
                    checker[x+dx][y+dy] = 1 # 해당 좌표의 방문기록을 남깁니다.
                    matrix[x + dx][y + dy] = matrix[x][y] + 1 # 해당 좌표에 현재 좌표보다 1을 더한 값을 남깁니다.
            if x+dx == end_x and y+dy == end_y: # 만약 해당 좌표가 탐색을 종료할 지점이라면
                return matrix[end_x][end_y] # 해당 좌표가 가지고 있는 값을 반환합니다. 이 값이 최소 탐색 기록이 됩니다.


N, M = map(int, input().split()) # 미로의 크기를 받아옵니다.

matrix = [] # 미로의 정보를 받아올 리스트를 선언합니다.

for _ in range(N): # 미로를 생성합니다.
    matrix.append(list(map(int, input().rstrip())))
delta = [[1, 0], [0, -1], [-1, 0], [0, 1]] # 델타탐색 범위를 지정합니다.
checker = [[0] * M for _ in range(N)] # 미로의 방문 기록을 체크할 리스트를 만듭니다.
checker[0][0] = 1 # 미로의 시작지점에 방문체크를 합니다.

print(maze(N, M))