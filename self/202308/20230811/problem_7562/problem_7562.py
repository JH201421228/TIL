import sys
from collections import deque
# sys.stdin = open('input.txt')


def night_move(start_x, start_y, end_x, end_y, I):
    que = deque([])
    que.append([start_x, start_y])
    chess_board[start_x][start_y] = 1

    delta = [[2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2]]

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < I and 0 <= y+dy < I and not chess_board[x+dx][y+dy]:
                que.append([x+dx, y+dy])
                chess_board[x+dx][y+dy] = chess_board[x][y] + 1
                if x+dx == end_x and y+dy == end_y:
                    return chess_board[x+dx][y+dy] - 1


Test_Case = int(input())

for _ in range(Test_Case):

    I = int(input()) # chess board s size
    start_x, start_y = map(int, input().split())
    end_X, end_y = map(int, input().split())
    chess_board = [[0] * I for _ in range(I)]

    ans = night_move(start_x, start_y, end_X, end_y, I)

    if ans:
        print(ans)
    else:
        print(0)