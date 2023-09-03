import sys
sys.stdin = open('input.txt')


def checker(i, j, n):
    for idx in range(9):
        if idx != j:
            if sudoku[i][idx] == n:
                return False
        if idx != i:
            if sudoku[idx][j] == n:
                return False

    for x in range(i//3 * 3, i//3 * 3 + 3):
        for y in range(j//3 * 3, j//3 * 3 + 3):
            if x != i and y != j:
                if sudoku[x][y] == n:
                    return False
    return True


def this_game(start):
    if start == len(start_point):
        for inner in sudoku:
            print(*inner)
        # print(sudoku)
        exit(0)

    now_i, now_j = start_point[start]
    for num in range(9, 0, -1):
        sudoku[now_i][now_j] = num
        if checker(now_i, now_j, num):
            this_game(start+1)
        sudoku[now_i][now_j] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
start_point = []
for idx_i in range(9):
    for idx_j in range(9):
        if not sudoku[idx_i][idx_j]:
            start_point.append([idx_i, idx_j])
this_game(0)
# print(sudoku)