import sys
sys.stdin = open('input.txt')


def mat_cal(mat1, mat2):
    ans_mat = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans_mat[i][j] += mat1[i][k] * mat2[k][j]
            ans_mat[i][j] %= 1_000_000_007
    return ans_mat


def linear_algebra(num, mat):
    if num == 1:
        return mat
    elif num == 2:
        return mat_cal(mat, mat)
    elif num % 2:
        return mat_cal(linear_algebra(num // 2, mat_cal(mat, mat)), mat)
    else:
        return linear_algebra(num // 2, mat_cal(mat, mat))


n = int(input())
matrix = [[1, 1], [1, 0]]
print(linear_algebra(n, matrix)[-1][0])