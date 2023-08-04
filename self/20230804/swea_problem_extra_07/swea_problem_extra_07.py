# 파리 퇴치
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    matrix_size, fly_kill_size = map(int, input().split())
    matrix_list = [list(map(int, input().split())) for _ in range(matrix_size)]
    max_val = 0

    for x in range(matrix_size):
        for y in range(matrix_size):
            total = 0
            for dx in range(fly_kill_size):
                for dy in range(fly_kill_size):
                    if x + dx < matrix_size and y + dy < matrix_size:
                        total += matrix_list[x + dx][y + dy]
            if total > max_val:
                max_val = total
    print(f'#{test_case + 1} {max_val}')