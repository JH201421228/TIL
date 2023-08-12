

N, M = map(int, input().split())

# matrix_1st = []
# matrix_2nd = []
matrix_sum = [[0] * M for _ in range(N)]
matrix_1st = [list(map(int, input().split())) for i in range(N)]
matrix_2nd = [list(map(int, input().split())) for i in range(N)]

for i in range(N):

    for j in range(M):
        sum_int = matrix_1st[i][j] + matrix_2nd[i][j]
        matrix_sum[i][j] = (sum_int)

for i in range(N):

    for j in range(M):
        print(matrix_sum[i][j], end = ' ')

    print()
