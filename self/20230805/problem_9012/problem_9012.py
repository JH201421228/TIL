import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

Test_Case = int(input())

for test_case in range(Test_Case):
    input_str = input().rstrip()
    input_stack = [i for i in input_str]

    check_num = 0

    for _ in range(len(input_stack)):

        plz_check = input_stack.pop()
        if plz_check == ')':
            check_num += 1
        elif plz_check == '(':
            check_num -= 1

        if check_num < 0:
            print('NO')

            break

    if check_num == 0:
        print('YES')
    elif check_num > 0:
        print('NO')