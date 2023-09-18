import sys
sys.stdin = open('input.txt')


def let_s_go(mat, n):
    if n == 1:
        return mat
    elif n == 2:
        return work_hard(mat, mat)
    elif n % 2:
        return work_hard(let_s_go(work_hard(mat, mat), n//2), mat)
    else:
        return let_s_go(work_hard(mat, mat), n//2)


def work_hard(mat1, mat2):
    length = len(mat1)
    return_mat = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                return_mat[i][j] += mat1[i][k] * mat2[k][j]
            return_mat[i][j] %= 1_000_000_000

    return return_mat



a, b = map(int, input().split())
divide = 1_000_000_000
# A_ab = A_b+2 - A_a+1
matrix = [[1, 1], [1, 0]]
print((let_s_go(matrix, b+1)[0][0] % divide - let_s_go(matrix, a)[0][0] % divide + divide) % divide)

