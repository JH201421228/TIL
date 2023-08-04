# [S/W 문제해결 기본] 10일차 - 비밀번호

import sys
sys.stdin = open('input.txt')

# def password_maker(arr):
#     while True

for test_case in range(10):
    num_of_int, numbers = map(str, input().split())

    numbers_list = [i for i in numbers]
    # print(numbers_list)
    out_signal = 0
    while True:
        if out_signal:
            break
        for index in range(len(numbers_list) - 1):

            if index == len(numbers_list) - 2:
                out_signal = 1
            if numbers_list[index] == numbers_list[index + 1]:
                del numbers_list[index:index+2]
                # del numbers_list[index]
                break

    # ans_list = [str(i) for i in numbers_list]
    print(f'#{test_case + 1}', end= ' ')
    for i in numbers_list:
        print(i, end='')
    print()
    # print(*numbers_list)