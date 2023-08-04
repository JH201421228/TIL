# 백만 장자 프로젝트

import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    list_length = int(input())
    total_money = 0
    money_info = list(map(int, input().split()))

    while money_info:
        max_index = money_info.index(max(money_info))
        max_val = max(money_info)

        for i in money_info[:max_index]:
            total_money += (max_val - i)

        money_info = money_info[max_index + 1:]

    print(f'#{test_case + 1} {total_money}')