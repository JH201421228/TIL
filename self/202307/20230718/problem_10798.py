

matrix = [str(input()) for _ in range(5)]
max_num = 0

for i in range(5):
    if len(matrix[i]) > max_num:
        max_num = len(matrix[i])

for i in range(max_num):

    for j in range(5):
        try:
            print(matrix[j][i], end = '')

        except IndexError:
            pass
