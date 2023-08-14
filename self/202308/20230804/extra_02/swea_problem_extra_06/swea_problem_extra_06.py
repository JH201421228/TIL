# 간단한 압축 풀기

import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    input_num = int(input())
    alpha_list = []
    for _ in range(input_num):
        alpha_list.append(list(input().split()))
    # 입력 받기 끝

    ans_list = []

    for inner_list in alpha_list:
        ans_list.extend(inner_list[0] * int(inner_list[1]))

    length_of_list = len(ans_list)

    print(f'#{test_case + 1}')
    for index in range(length_of_list):
        print(ans_list[index], end= '')
        if not (index + 1) % 10 or index == length_of_list - 1:
            print()
            