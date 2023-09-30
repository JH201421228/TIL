import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday(x, y, val):
    # for inner in visited:
    #     print(inner)
    # print('-------------')
    if x == M - 1 and y == N - 1:
        return 1

    if visited[x][y] >= 0:
        return visited[x][y]

    visited[x][y] = 0

    for dx, dy in delta:
        if 0 <= x+dx < M and 0 <= y+dy < N and map_list[x+dx][y+dy] < val:
            visited[x][y] += holiday(x+dx, y+dy, map_list[x+dx][y+dy])
    return visited[x][y]

M, N = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(M)]
# print(map_list)
ans = 0
visited = [[-1] * N for _ in range(M)]
print(holiday(0, 0, map_list[0][0]))
# print(visited)
