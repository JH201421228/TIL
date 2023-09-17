import sys
sys.stdin = open('input.txt')
read = sys.stdin.readline

N, M = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(N)]
for i in range(N):
    for j in range(1, N):
        matrix[i][j] += matrix[i][j-1]
# print(matrix)
for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    ans = 0
    if y1 > 1:
        for idx_x in range(x1-1, x2):
            ans += (matrix[idx_x][y2-1] - matrix[idx_x][y1-2])


    else:
        for idx_x in range(x1-1, x2):
            ans += matrix[idx_x][y2-1]


    print(ans)