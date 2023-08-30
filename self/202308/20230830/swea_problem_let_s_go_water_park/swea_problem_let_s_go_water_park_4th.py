import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
from collections import deque


def landing_project(N, M):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque(start_idx)
    ans = 0
    while que:
        x, y, val = que.popleft()
        for dx, dy in delta:
            # if 0 <= x+dx < N and 0 <= y+dy < M and swimming_pool[x+dx][y+dy] == 'L' and not check_arr[x+dx][y+dy]:
            if 0 <= x + dx < N and 0 <= y + dy < M and swimming_pool[x+dx][y+dy] == 'L':
                swimming_pool[x+dx][y+dy] = 1
                val += 1
                que.append([x+dx, y+dy, val])
                ans += val
    return ans

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    swimming_pool = [list(map(str, input())) for _ in range(N)]
    # check_arr = [[-1] * M for _ in range(N)]

    start_idx = []
    for i in range(N):
        for j in range(M):
            if swimming_pool[i][j] == 'W':
                start_idx.append([i, j, 0])
                swimming_pool[i][j] = 0
                # check_arr[i][j] = 0
    # print(start_idx)
    # ans = 0
    # print(landing_project(N, M))
    # print(check_arr)

    # for inner in check_arr:
    #     ans += sum(inner)
    print(f'#{test+1} {landing_project(N, M)}')
    # print('-------------')