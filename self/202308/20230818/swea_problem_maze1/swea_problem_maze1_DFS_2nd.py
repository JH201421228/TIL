import sys
sys.stdin = open('input.txt')


def maze_runner(x, y):

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dx, dy in delta:
        if 0 <= x+dx < 16 and 0 <= y+dy < 16:
            if maze[x+dx][y+dy] == 3:
                ans.append([x+dx, y+dy])
            if not maze[x+dx][y+dy]:
                maze[x+dx][y+dy] = 1
                maze_runner(x+dx, y+dy)

    return


for _ in range(10):
    test_num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    ans = []
    maze_runner(1, 1)
    if ans:
        print(f'#{test_num} 1')
    else:
        print(f'#{test_num} 0')