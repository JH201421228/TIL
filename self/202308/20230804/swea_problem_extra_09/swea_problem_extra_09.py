# 간단한 소인수 분해

import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    input_num = int(input())

    a = b = c = d = e = 0

    while not input_num % 2:
        input_num //= 2
        a += 1

    while not input_num % 3:
        input_num //= 3
        b += 1

    while not input_num % 5:
        input_num //= 5
        c += 1

    while not input_num % 7:
        input_num //= 7
        d += 1

    while not input_num % 11:
        input_num //= 11
        e += 1

    print(f'#{test_case + 1} {a} {b} {c} {d} {e}')