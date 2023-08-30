import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
from collections import deque


def landing_project(N, M):


    while start_idx:
        x, y = start_idx.popleft()
        for dx, dy in delta:
            # if 0 <= x+dx < N and 0 <= y+dy < M and swimming_pool[x+dx][y+dy] == 'L' and not check_arr[x+dx][y+dy]:
            if 0 <= x + dx < N and 0 <= y + dy < M and swimming_pool[x+dx][y+dy] == 'L':
                swimming_pool[x+dx][y+dy] = swimming_pool[x][y] + 1
                start_idx.append([x+dx, y+dy])


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    swimming_pool = [list(map(str, input())) for _ in range(N)]
    # check_arr = [[-1] * M for _ in range(N)]
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    start_idx = deque([])
    for i in range(N):
        for j in range(M):
            if swimming_pool[i][j] == 'W':
                start_idx.append([i, j])
                swimming_pool[i][j] = 0
                # check_arr[i][j] = 0
    # print(start_idx)
    ans = 0
    landing_project(N, M)
    # print(check_arr)

    for inner in swimming_pool:
        ans += sum(inner)
    print(f'#{test+1} {ans}')
    # print('-------------')