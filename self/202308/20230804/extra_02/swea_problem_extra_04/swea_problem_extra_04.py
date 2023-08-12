import sys
sys.stdin = open('input.txt')


def sudoku_checker(sudoku):
    for row in sudoku:
        if sum(row) != 45 or len(set(row)) != 9:
            return 0

    for i in range(9):
        col_list = []
        for j in range(9):
            col_list.append(sudoku[j][i])
        if sum(col_list) != 45 or len(set(col_list)) != 9:
            return 0

    for i in range(3):
        for j in range(3):
            rec_list = []
            for k in range(3*i, 3*(i+1)):
                for l in range(3*j, 3*(j+1)):
                    rec_list.append(sudoku[k][l])
            if sum(rec_list) != 45 or len(set(rec_list)) != 9:
                return 0

    return 1


Test_Case = int(input())

for test_case in range(Test_Case):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case + 1} {sudoku_checker(sudoku)}')
