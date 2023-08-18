# import sys
from collections import deque
# sys.stdin = open('input.txt')

def maze_runner():
    que = deque([[1, 1]])
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < 15 and 0 <= y+dy < 16:
                if maze[x+dx][y+dy] == 3:
                    return 1
                if not maze[x+dx][y+dy]:
                    maze[x+dx][y+dy] = 1
                    que.append([x+dx, y+dy])
    return 0

for _ in range(10):
    test_num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{test_num} {maze_runner()}')