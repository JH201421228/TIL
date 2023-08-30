import sys
sys.stdin = open('input.txt')
from collections import deque


def landing_project(N, M):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque(start_idx)
    ans = 0
    while que:
        x, y, distance = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and swimming_pool[x+dx][y+dy] == 'L' and [x+dx, y+dy] not in check_idx:
                check_idx.append([x+dx, y+dy])
                distance += 1
                que.append([x+dx, y+dy, distance])
                ans += distance
    return ans


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    swimming_pool = [list(map(str, input())) for _ in range(N)]
    # check_arr = [[0] * M for _ in range(N)]

    start_idx = []
    check_idx = []
    for i in range(N):
        for j in range(M):
            if swimming_pool[i][j] == 'W':
                start_idx.append([i, j, 0])
                check_idx.append([i, j])

    # print(start_idx)

    # print(landing_project(N, M))
    # print(check_arr)

    # for inner in check_arr:
    #     ans += sum(inner)
    print(f'#{test+1} {landing_project(N, M)}')
    # print('-------------')