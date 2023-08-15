import sys
sys.stdin = open('input.txt')

def NQ(N):
    if len(arr) == N:
        print(arr)
        global cnt
        cnt += 1
        return
    check_num = 0
    for i in range(N):
        for j in range(N):
            if not chess_board[i][j]:
                check_num += 1
                for k in range(N):
                    chess_board[i][k] = check_num


N = int(input())
arr = []
cnt = 0
chess_board = [[0] * N for _ in range(N)]
