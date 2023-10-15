import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 지팡이를 한번도 사용하지 않았고, 벽이 없는 경우
# 지팡이를 한번도 사용하지 않았고, 벽이 있는 경우
# 지팡이를 이미 사용한 경우


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    q = deque([(start_x, start_y, 0)])
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][start_x][start_y] = 1

    while q:
        x, y, status = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if x+dx == end_x and y+dy == end_y:
                    return max(visited[0][x][y], visited[1][x][y])
                    # return visited
                if not status and not maze[x+dx][y+dy] and not visited[status][x+dx][y+dy]:
                    visited[status][x+dx][y+dy] = visited[status][x][y] + 1
                    q.append((x+dx, y+dy, status))
                if not status and not visited[1][x+dx][y+dy]:
                    visited[1][x + dx][y + dy] = visited[status][x][y] + 1
                    q.append((x+dx, y+dy, 1))
                if status and not maze[x+dx][y+dy] and not visited[status][x+dx][y+dy]:
                    visited[status][x + dx][y + dy] = visited[status][x][y] + 1
                    q.append((x+dx, y+dy, status))
    return -1


N, M = map(int, input().split())
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())
start_x, start_y, end_x, end_y = start_x-1, start_y-1, end_x-1, end_y-1
maze = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
# visited = bfs()
# for inner in visited:
#     for inn in inner:
#         print(inn)
#     print('---------------')
# for inner in maze:
#     print(inner)