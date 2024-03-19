import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
room = list(input().rstrip() for _ in range(N))

visited = [[0]*M for _ in range(N)]
visited[x1-1][y1-1] = 1

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque([(x1-1, y1-1)])

ans = 0
while True:
    ans += 1
    temp = []
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy]:
                if room[x+dx][y+dy] == '0':
                    q.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = 1
                elif room[x+dx][y+dy] == '1':
                    visited[x+dx][y+dy] = 1
                    temp.append((x+dx, y+dy))
                else:
                    print(ans)
                    exit(0)
    q = deque([*temp])

