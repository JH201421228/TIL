import sys
sys.stdin = open('input.txt')

matrix = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j]:
            cnt += 1
print(cnt)