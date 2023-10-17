import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def fire_bfs():
    while fire:
        x, y = fire.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < h and 0 <= y+dy < w and not fire_status[x+dx][y+dy] and maze[x+dx][y+dy] != '#':
                fire_status[x+dx][y+dy] = fire_status[x][y] + 1
                fire.append((x+dx, y+dy))


def human_bfs():
    while human:
        x, y = human.popleft()
        if not x or not y or x == h-1 or y == w-1:
            return human_status[x][y]
        for dx, dy in delta:
            if 0 <= x + dx < h and 0 <= y + dy < w and not human_status[x+dx][y+dy] and maze[x+dx][y+dy] != '#' and (fire_status[x+dx][y+dy] > human_status[x][y] + 1 or not fire_status[x+dx][y+dy]):
                human_status[x+dx][y+dy] = human_status[x][y] + 1
                human.append((x+dx, y+dy))
    return 'IMPOSSIBLE'


for _ in range(int(input())):
    w, h = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(h)]
    fire = deque([])
    human = deque([])
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '*':
                fire.append((i, j))
            elif maze[i][j] == '@':
                human.append((i, j))
    fire_status = [[0] * w for _ in range(h)]
    human_status = [[0] * w for _ in range(h)]
    for i, j in fire:
        fire_status[i][j] = 1
    for i, j in human:
        human_status[i][j] = 1
    fire_bfs()
    print(human_bfs())
    # for inner in fire_status:
    #     print(inner)
    # for inner in human_status:
    #     print(inner)


