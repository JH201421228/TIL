import sys
sys.stdin = open('input.txt')
from collections import deque


def bavocado1031(N):
    que = deque([[0, 0]]) # 시작값을 넣음
    delta = [[1, 0], [0, 1]] # 갈 수 있는 곳


    while que:
        x, y = que.popleft() # 좌표 받아오기

        for dx, dy in delta:
            if x+dx < N and y+dy < N: # 범위안에 있으면
                if not ans_graph[x+dx][y+dy] or ans_graph[x+dx][y+dy] > ans_graph[x][y] + graph[x+dx][y+dy]:
                       # 방문 기록이 없고,        기존의 합보다 작다면
                    ans_graph[x + dx][y + dy] = ans_graph[x][y] + graph[x + dx][y + dy] # 해당 값을 교체
                    que.append([x+dx, y+dy]) # 해당 좌표를 삽입

T = int(input()) # 총 테스트 케이스 횟수
for test in range(T):
    N = int(input()) # 받아올 리스트의 크기
    graph = [list(map(int, input().split())) for _ in range(N)] # 리스트 받아오기
    ans_graph = [[0] * N for _ in range(N)] # 방문 및 합을 기록할 그래프 생성
    ans_graph[0][0] = graph[0][0] # 시작 좌표값은 미리 넣음
    # for inner in graph:
    #     print(inner)
    # print('----------------')
    bavocado1031(N)
    print(f'#{test+1} {ans_graph[-1][-1]}') # 마지막 좌표 출력