import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(where):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    count = 0

    for i, j in where:
        q.append((i, j))
        visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if virus[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == -1:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    q.append((x+dx, y+dy))
                    count = max(count, visited[x+dx][y+dy])
                elif virus[x+dx][y+dy] == 2 and visited[x+dx][y+dy] == -1:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    q.append((x+dx, y+dy))
    if list(sum(visited, [])).count(-1) != cnt:
        return float('inf')
    return count


N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
location = []
for i in range(N):
    for j in range(N):
        if virus[i][j] == 1:
            cnt += 1
        elif virus[i][j] == 2:
            location.append((i, j))
ans = float('inf')
for where in combinations(location, M):
    ans = min(ans, bfs(where))

if ans != float('inf'):
    print(ans)
else:
    print(-1)