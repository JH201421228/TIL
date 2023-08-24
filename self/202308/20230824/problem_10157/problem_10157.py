import sys
sys.stdin = open('input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
C, R = map(int, input().split())
who = int(input())
matrix = [[0] * C for _ in range(R)]
# start_cordinate = []
num = 1
x = R - 1
y = 0
matrix[x][y] = num
delta_idx = 0
while num < C*R:
    dx, dy = delta[delta_idx]
    if 0 <= x+dx < R and 0 <= y+dy < C and not matrix[x+dx][y+dy]:
        x = x+dx
        y = y+dy

        num += 1
        matrix[x][y] = num
    else:
        delta_idx = (delta_idx + 1) % 4

if who > C*R:
    print(0)

for i in range(R):
    for j in range(C):
        if matrix[i][j] == who:
            print(j + 1, R - i)
            break

