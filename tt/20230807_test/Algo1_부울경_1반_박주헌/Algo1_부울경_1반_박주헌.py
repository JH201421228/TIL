import sys
sys.stdin = open('input.txt')

# ############절취선#################

Test_Case = int(input())

for test_case in range(Test_Case):
    matrix_size = int(input())
    x_start, y_start, x_end, y_end = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
    total = 0
    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            total += matrix[x][y]
    # 값이 있는 잔디를 순회하며 total값을 구함.

    avg_num = total // ((x_end - x_start + 1)*(y_end - y_start + 1))
    # 평균값을 구함.

    work_num = 0
    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            while matrix[x][y] != avg_num:
                if matrix[x][y] > avg_num:
                    matrix[x][y] -= 1
                    work_num += 1
                else:
                    matrix[x][y] += 1
                    work_num += 1
    # 잔디를 돌며 일을 얼마나 해야하는지 구함

    print(f'#{test_case + 1} {work_num}')