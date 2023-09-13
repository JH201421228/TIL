import sys
from collections import deque
sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def what_the_game():
    que = deque([[0, 0]])
    checker = [[0, 0]]
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < R and 0 <= y+dy < R and board_info[x+dx][y+dy] not in trace and [x+dx, y+dy] not in checker:
                que.append([x+dx, y+dy])
                checker.append([x+dx, y+dy])
                trace.append(board_info[x+dx][y+dy])
                board_info[x+dx][y+dy] = board_info[x][y] + 1


R, C = map(int, input().split())
board_info = [list(input()) for _ in range(R)]
trace = [board_info[0][0]]
board_info[0][0] = 0
what_the_game()
print(board_info)
