# import sys
from collections import deque
# sys.stdin = open('input.txt')

def maze_runner(N, start):
    que = deque([start])
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cnt = 1
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if maze[x+dx][y+dy] == 2:
                    return maze[x][y] - 3
                if not maze[x+dx][y+dy]:
                    que.append([x+dx, y+dy])
                    maze[x + dx][y + dy] = maze[x][y] + 1

    return False



Test = int(input())
for test in range(Test):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                start = [i, j]
                break

    ans = maze_runner(N, start)
    if ans:
        print(f'#{test+1} {ans}')
    else:
        print(f'#{test + 1} 0')