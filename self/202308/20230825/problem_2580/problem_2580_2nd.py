import sys
sys.stdin = open('input.txt')


def sudoku_okay(n, idx_x, idx_y):
    pass


def fxxk_sudoku(start):


    x, y = zero_idx[i]
    for num in range(1, 10):
        sudoku[x][y] = num # 1 부터 넣어보고
        if sudoku_okay(num, x, y): # 가로 세로 33에서 없는 값임을 확인하면
            fxxk_sudoku(i+1) # 다음 스타트 포인트에서 시작, 근데 1




sudoku = [list(map(int, input().split())) for _ in range(9)]
zero_idx = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            zero_idx.append([i, j])
zero_length = len(zero_idx)
