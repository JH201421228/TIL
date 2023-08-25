import sys
sys.stdin = open('input.txt')

sudoku = [list(map(int, input().split())) for _ in range(9)]
# print(sudoku)
checker1 = [0] * 9 # 가로 줄에 0이 몇개 있는가
checker2 = [0] * 9 # 세로 줄에 0이 몇개 있는가
checker3 = [0] * 9 # 3 3 으로 나눈 공간에 0이 몇개 있는가
cor_idx = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            checker1[i] += 1
            checker2[j] += 1
            checker3[cor_idx.index([i//3, j//3])] += 1
# for inner in sudoku:
#     print(inner)
# print()
# print(checker1)
# print(checker2)
# print(checker3) # 스도쿠 내용물과 0이 있는 개수 출력 체크용도

# sum_ch1 = sum(checker1)
# sum_ch2 = sum(checker2)
# sum_ch3 = sum(checker3)
# print(sum_ch1, sum_ch2, sum_ch3)

# flag = sum(checker1)
# while flag:
#     ch1_idx = False
#     ch2_idx = False
#     ch3_idx = False
#
#     for zero_val_idx in range(9):
#         if checker1[zero_val_idx] == 1:
#             ch1_idx = zero_val_idx
#             break
#     if ch1_idx is not False
#
#     flag -= 1