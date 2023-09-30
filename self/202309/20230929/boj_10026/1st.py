import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def holiday1():
    area = 0
    que = deque([])
    for i in range(N):
        for j in range(N):
            if not visited1[i][j]:
                area += 1
                que.append((i, j))
                visited1[i][j] = area
                color = RGB[i][j]
            if que:
                while que:
                    x, y = que.popleft()
                    for dx, dy in delta:
                        if 0 <= x+dx < N and 0 <= y+dy < N and not visited1[x+dx][y+dy] and RGB[x+dx][y+dy] == color:
                            visited1[x+dx][y+dy] = area
                            que.append((x+dx, y+dy))
    return area


def holiday2():
    area = 0
    que = deque([])
    for i in range(N):
        for j in range(N):
            if not visited2[i][j]:
                area += 1
                que.append((i, j))
                visited1[i][j] = area
                color = RGB[i][j]
                if color != 'B':
                    color = 'RG'
            if que:
                while que:
                    x, y = que.popleft()
                    for dx, dy in delta:
                        if 0 <= x+dx < N and 0 <= y+dy < N and not visited2[x+dx][y+dy] and RGB[x+dx][y+dy] in color:
                            visited2[x+dx][y+dy] = area
                            que.append((x+dx, y+dy))
    return area


N = int(input())
RGB = [list(input().rstrip()) for _ in range(N)]
# print(RGB)
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
print(holiday1(), holiday2())