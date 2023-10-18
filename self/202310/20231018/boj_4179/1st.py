import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def fire_bfs():
    while fire:
        x, y = fire.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < R and 0 <= y+dy < C and not fire_maze[x+dx][y+dy] and maze[x+dx][y+dy] != '#':
                fire_maze[x+dx][y+dy] = fire_maze[x][y] + 1
                fire.append((x+dx, y+dy))


def human_bfs():
    while human:
        x, y = human.popleft()
        if not x or x == R-1 or not y or y == C-1:
            return human_maze[x][y]
        for dx, dy in delta:
            if 0 <= x + dx < R and 0 <= y + dy < C and not human_maze[x+dx][y+dy] and (fire_maze[x+dx][y+dy] > human_maze[x][y] + 1 or not fire_maze[x+dx][y+dy]) and maze[x+dx][y+dy] != '#':
                human_maze[x+dx][y+dy] = human_maze[x][y] + 1
                human.append((x+dx, y+dy))
    return 'IMPOSSIBLE'


R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
fire = deque([])
human = deque([])
fire_maze = [[0] * C for _ in range(R)]
human_maze = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            human.append((i, j))
        elif maze[i][j] == 'F':
            fire.append((i, j))
for i, j in fire:
    fire_maze[i][j] = 1
for i, j in human:
    human_maze[i][j] = 1
fire_bfs()
# for inner in fire_maze:
#     print(inner)
print(human_bfs())
# for inner in human_maze:
#     print(inner)