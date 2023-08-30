import sys
sys.stdin = open('input.txt')

from collections import deque

delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]

def what_the(N, M):

    while start_idx:
        x, y = start_idx.popleft()
        # for dx, dy in delta:
        for i in range(4):
            dx = delta_x[i]
            dy = delta_y[i]
            if 0 <= x+dx < N and 0 <= y+dy < M and check_arr[x+dx][y+dy] == -1:
                check_arr[x+dx][y+dy] = check_arr[x][y] + 1
                start_idx.append([x+dx, y+dy])


T = int(input())
for test in range(T):
    N, M = map(int, input().split())

    start_idx = deque([])
    check_arr = [[-1] * M for _ in range(N)]
    for i in range(N):
        swimming_pool = input()
        for j in range(M):
            if swimming_pool[j] == 'W':
                start_idx.append([i, j])
                check_arr[i][j] = 0

    what_the(N, M)
    ans = 0
    for inner in check_arr:
        ans += sum(inner)
    print(f'#{test+1} {ans}')