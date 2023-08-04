# 어디에 단어가 들아갈 수 있을까?
# 1이 빈칸

import sys
sys.stdin = open('input.txt')


def str_checker(matrix, str_size):
    ans = 0
    str_str = [str(1) for _ in range(str_size)]
    str_str.insert(0, '0')
    str_str.append('0')
    str_for_ans = ''.join(str_str)
    for matrix_list in matrix:
        matrix_list_str = [str(i) for i in matrix_list]
        matrix_list_str.insert(0, '0')
        matrix_list_str.append('0')
        matrix_str = ''.join(matrix_list_str)
        start = 0
        while True:
            index = matrix_str.find(str_for_ans, start)
            if index != -1:
                start += index + 1
                ans += 1
            else:
                break
    return ans


Test_Case = int(input())

for test_case in range(Test_Case):
    matrix_size, str_size = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    trans_matrix = [[0]*matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        for j in range(matrix_size):
            trans_matrix[i][j] = matrix[j][i]

    print(f'#{test_case + 1} {str_checker(matrix, str_size)+ str_checker(trans_matrix, str_size)}')
    # print(f'#{test_case + 1} ')
