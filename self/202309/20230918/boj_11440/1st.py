import sys
sys.stdin = open('input.txt')


divide = 1_000_000_007


def gogo(mat, N):
    if N == 1:
        return mat
    elif N == 2:
        return multi(mat, mat)
    elif N % 2:
        return multi(gogo(multi(mat, mat), N // 2), mat)
    else:
        return gogo(multi(mat, mat), N // 2)

def multi(mat1, mat2):
    length = len(mat1)
    return_mat = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                return_mat[i][j] += mat1[i][k] * mat2[k][j]
            return_mat[i][j] %= divide
    return return_mat

N = int(input())
# sum(fibo_n ** 2) = fibo_n+1 ** 2 - fibo_n ** 2 +-1
matrix = [[1, 1], [1, 0]]
fibo = gogo(matrix, N)
print(((fibo[0][0] ** 2) % divide - (fibo[0][1] ** 2) % divide + divide + (-1) ** (N-1)) % divide)
