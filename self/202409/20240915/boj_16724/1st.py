import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def dfs(x, y):
    global ans

    if x >= N or x < 0 or y >= M or y < 0:
        print(x, y)
        exit(0)

    if V[x][y]:
        if V[x][y] == -1:
            ans += 1
        return V[x][y]

    V[x][y] = -1
    dx, dy = T[MAP[x][y]]

    temp = dfs(x+dx, y+dy)

    if (temp == -1):
        V[x][y] = ans
        return -1
    else:
        V[x][y] = temp
        return temp


T = {
    'D': (1, 0),
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


N, M = map(int, input().split())
MAP = [input().rstrip() for _ in range(N)]

ans = 0

V = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not V[i][j]:
            dfs(i, j)

print(ans)