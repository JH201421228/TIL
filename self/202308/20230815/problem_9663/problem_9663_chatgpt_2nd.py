import sys

sys.stdin = open('input.txt')


def is_safe(chess_board, row, col, N):
    # Check if it's safe to place a queen at the given position
    for i in range(row):
        if chess_board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chess_board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if chess_board[i][j] == 1:
            return False

    return True


def N_Q(N, chess_board, row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        if is_safe(chess_board, row, col, N):
            chess_board[row][col] = 1
            N_Q(N, chess_board, row + 1)
            chess_board[row][col] = 0


N = int(input())
chess_board = [[0] * N for _ in range(N)]
cnt = 0
N_Q(N, chess_board, 0)
print(cnt)
