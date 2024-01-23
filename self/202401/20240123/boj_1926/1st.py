import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(i, j):

    ans = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy] and graph[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                q.append((x+dx, y+dy))
                ans += 1
    return ans


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

ans_list = []
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]:
            visited[i][j] = 1
            ans_list.append(bfs(i, j))

if ans_list:
    print(len(ans_list))
    print(max(ans_list))
else:
    print(0)
    print(0)