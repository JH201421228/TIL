import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday(i, j):
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    que = deque([(i, j)])

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and treasure[x+dx][y+dy] == 'L' and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = visited[x][y] + 1
                que.append((x+dx, y+dy))
    return visited[x][y]




N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]
# print(treasure)
ans_list = []
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':
            ans_list.append(holiday(i, j))
print(max(ans_list)-1)