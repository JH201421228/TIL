import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(1, Test_Case + 1):
    input_num = int(input())
    alpha_list = []
    for _ in range(input_num):
        alpha_list.append(list(input().split()))

    ans_list = []

    for inner_list in alpha_list:
        ans_list.extend([inner_list[0]] * int(inner_list[1]))

    length_of_list = len(ans_list)

    print(f'#{test_case}')
    for index in range(length_of_list):
        print(ans_list[index], end='')
        if (index + 1) % 10 == 0 or index == length_of_list - 1:
            print()
