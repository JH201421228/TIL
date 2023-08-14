import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    max_val = 0
    for x in range(N):
        for y in range(M):
            total = matrix[x][y]
            for dx, dy in delta:
                if 0 <= x+dx < N and 0<= y+dy < M:
                     total += matrix[x+dx][y+dy]
                     if total > max_val:
                         max_val = total
    print(f'#{test_case+1} {max_val}')