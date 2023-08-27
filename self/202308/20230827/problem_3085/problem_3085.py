import sys
sys.stdin = open('input.txt')

N = int(input())
candy = [list(map(str, input())) for _ in range(N)]
# print(candy)
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(N):
    for j in range(N):
        for di, dj in delta:
            if 0 <= i+di < N and 0 <= j+dj < N:
                candy[i][j], candy[i+di][j+dj] = candy[i+di][j+dj], candy[i][j]
                for k in range(N):
                    for l in range(N)

