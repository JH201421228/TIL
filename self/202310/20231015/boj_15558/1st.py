import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 시작 위치는 고정
# 같은 줄에서 한칸 앞 혹은 뒤로 이동 가능
# 옆줄로 이동할 때는 K칸 앞으로 이동 가능
# 마지막 칸을 넘어가면 끝
# 뒷칸이 하나씩 사라짐
# 0은 위험한 칸, 1은 안전한 칸


def bfs():
    q = deque([(0, 0)])
    visited = [[0] * N for _ in range(2)]
    visited[0][0] = 1
    cnt = -1
    while q:
        x, y = q.popleft()
        if y + 1 >= N or y + K >= N:
            return 1
        if not visited[x][y+1] and board[x][y+1]:
            visited[x][y+1] = 1
            q.append((x, y+1))
        if y-1 > cnt and not visited[x][y-1] and board[x][y-1]:
            visited[x][y-1] = 1
            q.append((x, y-1))
        if not visited[1-x][y+K] and board[1-x][y+K]:
            visited[1-x][y+K] = 1
            q.append((1-x, y+K))
        # board[0][cnt] = board[1][cnt] = 0
        cnt += 1
        # for inner in visited:
        #     print(inner)
        # print('-------------')
    return 0


N, K = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(2)]
# for inner in board:
#     print(inner)
print(bfs())