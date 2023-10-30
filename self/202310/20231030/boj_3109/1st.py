import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(x, y):
    global flag
    if y == C-1:
        flag = 1
        return

    for dx, dy in delta:
        if 0 <= x+dx < R and 0 <= y+dy < C and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy]
            bfs(x+dx, y+dy)
            if flag:
                break
            else:
                visited[x+dx][y+dy] = 0


R, C = map(int, input().split())
MAP = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
for idx in range(R):
    visited[idx][0] = 1
    bfs(idx, 0)
# print(MAP)