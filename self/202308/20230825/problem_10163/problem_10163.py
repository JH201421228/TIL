import sys
sys.stdin = open('input.txt')

N = int(input())
matrix = [[0] * 1002 for _ in range(1002)]
for num in range(N):
    s_x, s_y, l_x, l_y = map(int, input().split())
    for i in range(s_x, s_x + l_x):
        for j in range(s_y, s_y + l_y):
            matrix[i][j] = num + 1

ans = [0] * 101
for i in range(1002):
    for j in range(1002):
        if matrix[i][j]:
            ans[matrix[i][j]] += 1

for idx in range(1, N+1):
    print(ans[idx])
