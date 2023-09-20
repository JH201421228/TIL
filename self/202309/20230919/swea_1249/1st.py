import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    # print(matrix)
    for i in range(N):
        for j in range(N):
            if not i and not j:
                pass
            elif not i:
                matrix[i][j] += matrix[i][j-1]
            elif not j:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])
    print(matrix[-1][-1])
    # for inner in matrix:
    #     print(inner)
