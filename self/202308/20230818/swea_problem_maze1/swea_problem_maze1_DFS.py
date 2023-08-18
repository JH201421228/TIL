import sys
sys.stdin = open('input.txt')


def maze_runner():
    stack = [[1, 1]]
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while stack:
        x, y = stack.pop()
        for dx, dy in delta:
            if 0 <= x+dx < 16 and 0 <= y+dy < 16:
                if maze[x+dx][y+dy] == 3:
                    return 1
                if not maze[x+dx][y+dy]:
                    stack.append([x+dx, y+dy])
                    maze[x + dx][y + dy] = 1
    return 0

for _ in range(10):
    test_num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{test_num} {maze_runner()}')
    # for i in range(16):
    #     for j in range(16):
