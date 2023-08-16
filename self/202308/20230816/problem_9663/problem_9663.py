import sys
sys.stdin = open('input.txt')


def NQ(N,start_x, start_y):
    if len(ans_list) == N:
        # print(ans_list)
        global cnt
        cnt += 1
        return
    global num
    for i in range(start_x, N):
        for j in range(start_y, N):
            if not chess_board[i][j]:
                num += 1 # 몇번째 퀸인지 명시
                # 퀸의 공격범위를 모두 채울 예정
                for k in range(N):
                    if not chess_board[i][k]:
                        chess_board[i][k] = num
                    if not chess_board[k][j]:
                        chess_board[k][j] = num
                dx = dy = 1
                for k in range(1, N):
                    if 0 <= i+k*dx < N and 0 <= j+k*dy < N:
                        if not chess_board[i+k*dx][j+k*dy]:
                            chess_board[i + k * dx][j + k * dy] = num
                    if 0 <= i-k*dx < N and 0 <= j-k*dy < N:
                        if not chess_board[i-k*dx][j-k*dy]:
                            chess_board[i - k * dx][j - k * dy] = num
                    if 0 <= i+k*dx < N and 0 <= j-k*dy < N:
                        if not chess_board[i+k*dx][j-k*dy]:
                            chess_board[i + k * dx][j - k * dy] = num
                    if 0 <= i-k*dx < N and 0 <= j+k*dy < N:
                        if not chess_board[i-k*dx][j+k*dy]:
                            chess_board[i - k * dx][j + k * dy] = num
                ans_list.append([i, j])
                NQ(N, i+1, 0)
                ans_list.pop()
                for k in range(N):
                    for l in range(N):
                        if chess_board[k][l] == num:
                            chess_board[k][l] = 0
                num -= 1

N = int(input())
chess_board = [[0] * N for _ in range(N)]
ans_list = []
cnt = 0
num = 0
NQ(N, 0, 0)
print(cnt)