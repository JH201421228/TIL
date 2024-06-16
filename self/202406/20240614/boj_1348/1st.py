import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def B(n, c):
    for x, t in G[n]:
        if V[x]:
            continue
        if t > c:
            continue
        V[x] = 1

        if not D[x] or B(D[x], c):
            D[x] = n
            return True

    return False


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
MAP = []
for _ in range(R):
    MAP.append(list(map(str, input().rstrip())))
C_n, P_n = 0, 0
C_list = []
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'C':
            C_list.append((i, j))
            C_n += 1
        elif MAP[i][j] == 'P':
            P_n += 1
            MAP[i][j] = P_n

G = [[] for _ in range(C_n + 1)]

for i in range(C_n):
    visited = [[0]*C for _ in range(R)]
    x, y = C_list[i]
    visited[x][y] = 1
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if x+dx >= 0 and x+dx < R and y+dy >= 0 and y+dy < C:
                if not visited[x+dx][y+dy] and MAP[x+dx][y+dy] != 'X':
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    q.append((x+dx, y+dy))
                    if isinstance(MAP[x+dx][y+dy], int):
                        G[i+1].append((MAP[x+dx][y+dy], visited[x][y]))

if C_n:
    D = [0] * (P_n + 1)
    isAvailable = True
    for i in range(1, C_n+1):
        V = [0] * (P_n + 1)
        if not B(i, float('inf')):
            isAvailable = False

    if isAvailable:
        start, end = 0, 2500
        while start <= end:
            mid = (start + end) >> 1
            D = [0] * (P_n + 1)
            isAvailable = True
            for i in range(1, C_n+1):
                V = [0] * (P_n + 1)
                if not B(i, mid):
                    isAvailable = False
            if isAvailable:
                end = mid - 1
            else:
                start = mid + 1

        print(start)

    else:
        print(-1)

else:
    print(0)