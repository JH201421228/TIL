from collections import deque

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:


for tc in range(1, T + 1):
    N = int(input())

    room = [list(map(int, input().split()))]

    room_length = 0
    room_num = 0

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j)
