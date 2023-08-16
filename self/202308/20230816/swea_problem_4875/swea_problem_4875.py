import sys
from collections import deque
# sys.stdin = open('input.txt')

def maze_runner(start, end, N):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que = deque([start])


    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if [x+dx, y+dy] == end:
                    return True
                if not maze[x+dx][y+dy]:
                    maze[x + dx][y + dy] = 1
                    que.append([x+dx, y+dy])
    return False


Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]

    for i in range(N):
        for j in range(N):

            if maze[i][j] == 3:
                start = [i, j]
            if maze[i][j] == 2:
                end = [i, j]
    if maze_runner(start, end, N):
        print(f'#{test_case + 1} 1')
    else:
        print(f'#{test_case + 1} 0')
