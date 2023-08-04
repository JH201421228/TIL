# 쇠막대 자르기
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    status = input()
    num = 0
    total = 0
    while len(status):
        if status[:2] == '()':
            status = status[2:]
            total += num
        elif status[0] == '(':
            status = status[1:]
            num += 1
        elif status[0] == ')':
            status = status[1:]
            num -= 1
            total += 1

    print(f'#{test_case + 1} {total}')
