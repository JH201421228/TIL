import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def where_is_cheeze():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M:
                if not visited[x+dx][y+dy] and not cheeze[x+dx][y+dy]:
                    visited[x+dx][y+dy] = 1
                    q.append((x+dx, y+dy))
                elif cheeze[x+dx][y+dy]:
                    visited[x+dx][y+dy] += 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 1:
                cheeze[i][j] = 0
                cnt += 1
    if cnt:
        return False
    else:
        return True


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
# print(cheeze)
# visited = where_is_cheeze()
# for inner in visited:
#     print(inner)
ans = 0
while not where_is_cheeze():
    ans += 1
print(ans)