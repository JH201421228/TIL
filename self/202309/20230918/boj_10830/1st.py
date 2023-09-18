import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def cla_matrix(A, B):
    length = len(A)
    C = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C


def sunday_morning_rain_is_falling(mat, power):

    if power == 1:
        return mat
    elif power == 2:
        return cla_matrix(mat, mat)
    elif not power % 2:
        return sunday_morning_rain_is_falling(cla_matrix(mat, mat), power // 2)
    else:
        return cla_matrix(sunday_morning_rain_is_falling(cla_matrix(mat, mat), power // 2), mat)


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix[i][j] %= 1000
for inner in sunday_morning_rain_is_falling(matrix, B):
    print(*inner)