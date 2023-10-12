import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(time):
    visited = [[0] * N for _ in range(N)]
    for x, y, c in que:
        visited[x][y] = 1
    while que:

        x, y, cnt = que.popleft()
        if cnt == time:
            return virus_list[X-1][Y-1]
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if not visited[x+dx][y+dy]:
                    visited[x+dx][y+dy] = cnt
                    virus_list[x+dx][y+dy] = virus_list[x][y]
                    que.append((x+dx, y+dy, cnt+1))
                elif visited[x+dx][y+dy] == cnt and virus_list[x+dx][y+dy] > virus_list[x][y]:
                    virus_list[x+dx][y+dy] = virus_list[x][y]
                    que.append((x+dx, y+dy, cnt+1))


N, K = map(int, input().split())
virus_list = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
que = deque([])
for i in range(N):
    for j in range(N):
        if virus_list[i][j]:
            que.append((i, j, 2))
# print(que)
# print(virus_list)
# 번호가 낮은 바이러스에게 우선순위가 있다.
# 이미 바이러스가 증식한 곳에는 바이러스가 들어갈 수 없다.
# for inner in virus_list:
#     print(inner)
# print('--------------')
# visited = bfs(S+2)
# for inner in visited:
#     print(inner)
# print('--------------')
# for inner in virus_list:
#     print(inner)
# print(visited)
print(bfs(S+2))
# 2 -> 0초
