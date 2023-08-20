import sys
sys.stdin = open('input.txt')

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # print(t, N, M, grid)

    min_pang = 0

    for i in range(N):
        for j in range(M):
            sum_pang = grid[i][j]
            for dx, dy in direction:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    sum_pang += grid[ni][nj]
            if min_pang < sum_pang:
                min_pang = sum_pang

    print(min_pang)