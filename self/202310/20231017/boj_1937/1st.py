import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(30000)

# 갔다가 돌아오면서 길 더하기


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    if visited[x][y]:
        return visited[x][y]
    visited[x][y] = 1
    for dx, dy in delta:
        if 0 <= x+dx < N and 0 <= y+dy < N and woods[x+dx][y+dy] > woods[x][y]:
            visited[x][y] = max(visited[x][y], bfs(x+dx, y+dy)+1)
    return visited[x][y]



N = int(input())
woods = [list(map(int, input().split())) for _ in range(N)]
# print(woods)
visited = [[0] * N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(bfs(i, j), ans)
print(ans)