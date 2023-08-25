import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)


def sudoku_okay(n, idx_x, idx_y):
    for idx in range(9):
        if idx != idx_y:
            if sudoku[idx_x][idx] == n:
                return False

    for idx in range(9):
        if idx != idx_x:
            if sudoku[idx][idx_y] == n:
                return False

    for i in range(idx_x//3 * 3, idx_x//3 * 3 + 3):
        for j in range(idx_y//3 * 3, idx_y//3 * 3 + 3):
            if i != idx_x and j != idx_y:
                if sudoku[i][j] == n:
                    return False

    return True


def fxxk_sudoku(start):
    if start == len(zero_idx):
        for inner in sudoku:
            print(*inner)
        exit(0) # 조건 맞으면 강제 종료

    x, y = zero_idx[start]
    for num in range(1, 10):
        sudoku[x][y] = num # 1 부터 넣어보고
        if sudoku_okay(num, x, y):  # 가로 세로 33에서 없는 값임을 확인하면
            fxxk_sudoku(start + 1) # 다음 스타트 포인트에서 시작, 근데 다음 스타트 포인트에서 넣은 값이 모두 불가능하면 다시 돌아옴(재귀)
        sudoku[x][y] = 0 # 들여쓰기 조심...

sudoku = [list(map(int, input().split())) for _ in range(9)]
zero_idx = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            zero_idx.append([i, j])
fxxk_sudoku(0)
# print(sudoku)