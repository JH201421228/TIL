import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(M)]
print(board)
b_board = [[0] * N for _ in range(M)]
w_board = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if (i+j) % 2:
            if board[i][j] == 'B':
                if j:
                    b_board[i][j] = b_board[i][j-1] + 1
                    w_board[i][j] = w_board[i][j-1]
                else:
                    b_board[i][j] = 1
                    w_board[i][j] = 0
            else:
                if j:
                    b_board[i][j] = b_board[i][j-1]
                    w_board[i][j] = w_board[i][j-1] + 1
                else:
                    b_board[i][j] = 0
                    w_board[i][j] = 1
        else:
            if board[i][j] == 'B':
                if j:
                    b_board[i][j] = b_board[i][j - 1]
                    w_board[i][j] = w_board[i][j - 1] + 1
                else:
                    b_board[i][j] = 0
                    w_board[i][j] = 1
            else:
                if j:
                    b_board[i][j] = b_board[i][j - 1] + 1
                    w_board[i][j] = w_board[i][j - 1]
                else:
                    b_board[i][j] = 1
                    w_board[i][j] = 0
print(w_board)
print(b_board)