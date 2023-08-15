import sys
sys.stdin = open('input.txt')

def N_Q(N, arr, start_x):
    if len(arr) == N:
        global cnt
        cnt += 1
        return

    for i in range(start_x, N):
        # 수정 1: 열의 시작점을 항상 0으로 설정
        for j in range(N):
            if not chess_board[i][j]:
                row_ck = sum(chess_board[i])
                col_ck = 0
                diagonal1 = 0
                diagonal2 = 0
                for k in range(N):
                    if chess_board[k][j]:
                        col_ck = 1
                        break
                dx = 1
                dy = 1
                for k in range(1, N):
                    if 0 <= i + k*dx < N and 0 <= j + k*dy < N:
                        if chess_board[i + k*dx][j + k*dy]:
                            diagonal1 = 1
                            break
                    if 0 <= i - k*dx < N and 0 <= j - k*dy < N:
                        if chess_board[i - k*dx][j - k*dy]:
                            diagonal1 = 1
                            break

                dx = 1
                dy = -1
                for k in range(1, N):
                    if 0 <= i + k * dx < N and 0 <= j + k * dy < N:
                        if chess_board[i + k * dx][j + k * dy]:
                            diagonal2 = 1
                            break
                    if 0 <= i - k * dx < N and 0 <= j - k * dy < N:
                        if chess_board[i - k * dx][j - k * dy]:
                            diagonal2 = 1
                            break

                if not row_ck and not col_ck and not diagonal1 and not diagonal2:
                    chess_board[i][j] = 1
                    arr.append([i, j])
                    # 수정 2: 행과 열의 시작점을 i+1, 0으로 설정
                    N_Q(N, arr, i + 1)
                    arr.pop()
                    chess_board[i][j] = 0

N = int(input())
chess_board = [[0] * N for _ in range(N)]
arr = []
cnt = 0
N_Q(N, arr, 0)
print(cnt)