import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
inventory = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = inventory[i-1][0]
        value = inventory[i-1][1]
        if j < weight:
            matrix[i][j] = matrix[i-1][j]
        else:
            matrix[i][j] = max(matrix[i-1][j], value + matrix[i-1][j-weight])
print(matrix[-1][-1])