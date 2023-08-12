

matrix = [list(map(int, input().split())) for _ in range(9)]
max_num = matrix[0][0]
max_index_N = 0
max_index_M = 0

for i in range(9):

    for j in range(9):
        if matrix[i][j] >= max_num:
            max_num = matrix[i][j]
            max_index_N = i + 1
            max_index_M = j + 1

print(max_num)
print(max_index_N, max_index_M)