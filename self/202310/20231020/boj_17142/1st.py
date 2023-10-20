import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(total):
    visited = [[0] * N for _ in range(N)]
    for i, j in q:
        visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy]:
                if not lab[x+dx][y+dy]:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    q.append((x+dx, y+dy))
                    total += 1
                    if total == blank:
                        return visited[x][y]
                elif lab[x+dx][y+dy] == 2:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    q.append((x+dx, y+dy))
    return -1


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
# print(lab)
virus = []
blank = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
        if lab[i][j] != 1:
            blank += 1
# print(virus)
# print(blank)
total = len(virus)
ans = []
if total == blank:
    print(0)
    exit(0)
for picked in combinations(virus, M):
    q = deque(picked)
    temp = bfs(total)
    if temp != -1:
        ans.append(temp)
if ans:
    print(min(ans))
else:
    print(-1)
