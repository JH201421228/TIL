import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 판은 4방향으로 기울일 수 있다.
# 가는 경로에 O가 있으면 빠져나옴
# 두 구슬의 x, y좌표가 같을 때는 기울일 때 생각하고 하기
# 10번 이내로 통과 못하면 실패
# 몇트만에 통과하는지 출력


# 우 하 좌 상
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    cnt = 0
    while True:
        if cnt == 10:
            return -1
        x_b, y_b = q_b.popleft()
        x_r, y_r = q_r.popleft()
        for dx, dy in delta:
            if x_b != x_r and y_b != y_r:
                
    
    
    
        cnt += 1

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            q_b = deque([(i, j)]) # 수정 필요
            vi_b = [[0] * M for _ in range(N)]
            vi_b[i][j] = 1
        elif board[i][j] == 'R':
            q_r = deque([(i, j)]) # 수정 필요
            vi_r = [[0] * M for _ in range(N)]
            vi_r[i][j] = 1

