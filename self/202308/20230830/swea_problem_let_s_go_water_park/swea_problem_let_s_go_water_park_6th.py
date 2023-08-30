import sys
sys.stdin = open('input.txt')
from collections import deque


def what_the():
    while start_idx:
        x, y = start_idx.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and check_arr[nx][ny] == -1:
                check_arr[nx][ny] = check_arr[x][y] + 1
                start_idx.append([nx, ny])


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    start_idx = deque([])
    check_arr = [[-1] * M for _ in range(N)]
    for i in range(N):
        swimming_pool = list(input())
        for j in range(M):
            if swimming_pool[j] == 'W':
                start_idx.append([i, j])
                check_arr[i][j] = 0


    # for i in range(N):
    #     for j in range(M):
    #         if swimming_pool[i][j] == 'W':
    #             start_idx.append([i, j])
    #             check_arr[i][j] = 0

    what_the()
    ans = 0
    for inner in check_arr:
        ans += sum(inner)
    print(f'#{test+1} {ans}')