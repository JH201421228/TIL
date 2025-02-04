import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(n):
    V[n] = 1
    q = deque([n])

    while q:
        o = q.popleft()
        x, y = o // M, o % M
        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            if xx >= 0 and xx < N and yy >= 0 and yy < M and not V[xx*M+yy] and abs(MAP[x][y] - MAP[xx][yy]) <= K:
                V[xx*M+yy] = 1
                q.append(xx*M+yy)
    return


N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ans = 0

V = [0] * (N*M)
for i in range(N*M):
    if not V[i]:
        bfs(i)
        ans += 1

print(ans)
