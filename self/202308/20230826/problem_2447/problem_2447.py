import sys
sys.stdin = open('input.txt')


def star(N, M):
    if not N:
        return

    for i in range(M):
        for j in range(M):
            if N//3 <= i % N < N//3 * 2  and N//3 <= j % N < N//3 * 2:
                star_matrix[i][j] = ' '
    star(N//3, M)

n = int(input())
star_matrix = [['*'] * n for _ in range(n)]
star(n, n)
for inner in star_matrix:
    print(''.join(inner))
