import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 각 섬의 좌표를 구분하여 넣는다.
# 섬의 좌표간 거리를 구한다.
# 상기 값의 최솟값이 답이 된다.


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    temp = [(x, y)]
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy] and Map[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                temp.append((x+dx, y+dy))
                q.append((x+dx, y+dy))
    for_ans.append(temp)


N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
# print(Map)
visited = [[0] * N for _ in range(N)]
for_ans = []
num_island = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and Map[i][j]:
            bfs(i, j)
            num_island += 1
# print(for_ans)
# print(len(for_ans))
# print(num_island)
ans = float('inf')
for i in range(num_island):
    for j in range(i+1, num_island):
        for x1, y1 in for_ans[i]:
            for x2, y2 in for_ans[j]:
                temp = abs(x1-x2) + abs(y1-y2)
                if temp < ans:
                    ans = temp
print(ans-1)
