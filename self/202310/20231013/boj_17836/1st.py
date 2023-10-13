# 그람이 있는 상태에서는 모든 벽이 없는 것이나 마찬가지
# 그람이 없으면 벽을 피해가야함


import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    visited1 = [[0] * M for _ in range(N)]
    visited2 = [[0] * M for _ in range(N)]
    visited1[0][0] = 1

    q = deque([(0, 0, 0)])
    while q:
        x, y, s = q.popleft()
        for dx, dy in delta:
            if x+dx == N-1 and y+dy == M-1:
                return max(visited1[x][y], visited2[x][y])
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if not s and not maze[x+dx][y+dy] and not visited1[x+dx][y+dy]:
                    visited1[x + dx][y + dy] = visited1[x][y] + 1
                    q.append((x+dx, y+dy, s))
                elif not s and maze[x+dx][y+dy] == 2:
                    visited2[x + dx][y + dy] = visited1[x][y] + 1
                    q.append((x+dx, y+dy, 1))
                elif s and not visited2[x+dx][y+dy]:
                    visited2[x + dx][y + dy] = visited2[x][y] + 1
                    q.append((x+dx, y+dy, 1))
    return False


N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
# for inner in visited:
#     print(inner)
if ans:
    if ans <= T:
        print(ans)
    else:
        print('Fail')
else:
    print('Fail')