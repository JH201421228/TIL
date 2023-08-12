# 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    matrix_size, str_length = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    trans_matrix = [[0] * matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        for j in range(matrix_size):
            trans_matrix[i][j] = matrix[j][i]

    total1 = total2 = 0

    for inner_list in matrix:
        cnt = 0
        for i in range(matrix_size - str_length + 1):
            ans = 0
            if (i == 0 or inner_list[i - 1] == 0) and (i + str_length == matrix_size or inner_list[i + str_length] == 0):
                for num in range(i, i + str_length):
                    if inner_list[num] == 0:
                        ans = -1
                if ans == 0:
                    cnt += 1
        total1 += cnt


    for inner_list in trans_matrix:
        cnt = 0
        for i in range(matrix_size - str_length + 1):
            ans = 0
            if (i == 0 or inner_list[i - 1] == 0) and (i + str_length == matrix_size or inner_list[i + str_length] == 0):
                for num in range(i, i + str_length):
                    if inner_list[num] == 0:
                        ans = -1
                if ans == 0:
                    cnt += 1
        total2 += cnt

    print(f'#{test_case + 1} {total1 + total2}')
