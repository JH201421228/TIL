import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):

    N, M = map(int, input().split())

    N_matrix = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for x in range(N - M + 1):
        for y in range(N - M + 1):
            total = 0
            for x_index in range(x, x + M):
                for y_index in range(y, y + M):
                    total += N_matrix[x_index][y_index]

            if total > max_val:
                max_val = total

    print(f'#{test_case + 1} {max_val}')