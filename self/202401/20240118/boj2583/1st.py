import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(i, j):
    q = deque([(i, j)])
    num = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                q.append((x+dx, y+dy))
                num += 1
    return num


N, M, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(x1, x2):
        for x in range(y1, y2):
            visited[x][y] = 1

ans_list = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            ans_list.append(bfs(i, j))
# print(ans_list)
ans_list.sort()
print(len(ans_list))
print(*ans_list)
