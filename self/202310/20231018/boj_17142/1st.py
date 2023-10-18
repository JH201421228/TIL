import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    visited = [[0] * N for _ in range(N)]
    virus_num = num
    for i, j in q:
        visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy]:
                if not virus[x+dx][y+dy]:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    virus_num += 1
                if virus_num == cnt:
                    return visited[x][y]
                    q.append((x+dx, y+dy))
                elif virus[x+dx][y+dy] == 2:
                    visited[x+dx][y+dy] = visited[x][y]
                    q.append((x+dx, y+dy))
    return 0


N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
where = []
for i in range(N):
    for j in range(N):
        if not virus[i][j]:
            cnt += 1
        elif virus[i][j] == 2:
            where.append((i, j))
num = len(where)
cnt += num
location = list(combinations(range(num), M))
combi = len(location)
ans = []
for idx in range(combi):
    q = deque([])
    for i in location[idx]:
        q.append(where[i])
    # print(cnt)
    # print(bfs())
    temp = bfs()
    if temp:
        ans.append(temp)
if ans:
    print(min(ans))
else:
    print(-1)
