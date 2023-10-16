import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def maze_runner(x, y, where):
    if where == 1:
        if maze[x+1][y] == 'U':
            s = [(x+1, y)]
        else:
            return
    elif where == 2:
        if maze[x][y+1] == 'L':
            s = [(x, y+1)]
        else:
            return
    elif where == 3:
        if maze[x][y-1] == 'R':
            s = [(x, y-1)]
        else:
            return
    else:
        if maze[x-1][y] == 'D':
            s = [(x-1, y)]
        else:
            return

    while s:
        x, y = s.pop()
        if not visited[x][y]:
            visited[x][y] = 1

            if maze[x+1][y] == 'U':
                s.append((x+1, y))

            if maze[x][y-1] == 'R':
                s.append((x, y-1))

            if maze[x-1][y] == 'D':
                s.append((x-1, y))

            if maze[x][y+1] == 'L':
                s.append((x, y+1))

    return


N, M = map(int, input().split())
maze = []
maze.append([1] * (M+2))
for _ in range(N):
    temp = list(input().rstrip())
    maze.append([1] + temp + [1])
maze.append([1] * (M+2))
visited = [[0] * (M+2) for _ in range(N+2)]
# print(maze)
# print(visited)

for i in range(1, M+1):
    if not visited[0][i]:
        visited[0][i] = 1
        maze_runner(0, i, 1)

for i in range(1, M+1):
    if not visited[N+1][i]:
        visited[N+1][i] = 1
        maze_runner(N+1, i, 4)

for j in range(1, N+1):
    if not visited[j][0]:
        visited[j][0] = 1
        maze_runner(j, 0, 2)

for j in range(1, N+1):
    if not visited[j][M+1]:
        visited[j][M+1] = 1
        maze_runner(j, M+1, 3)

ans = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if visited[i][j]:
            ans += 1
# for inner in visited:
#     print(inner)
print(ans)