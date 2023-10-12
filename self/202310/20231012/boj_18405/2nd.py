import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    cnt = 0
    q = deque(que)
    while q:
        if cnt == S:
            break
        for _ in range(len(q)):
            x, y, val = q.popleft()
            for dx, dy in delta:
                if 0 <= x+dx < N and 0 <= y+dy < N:
                    if not virus_list[x+dx][y+dy]:
                        virus_list[x+dx][y+dy] = virus_list[x][y]
                        q.append((x+dx, y+dy, virus_list[x+dx][y+dy]))
        cnt += 1
    return virus_list[X-1][Y-1]


N, K = map(int, input().split())
virus_list = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
que = []
for i in range(N):
    for j in range(N):
        if virus_list[i][j]:
            que.append((i, j, virus_list[i][j]))
que.sort(key=lambda x:x[2])
print(bfs())