import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def wall():
    T = N*M
    for i in range(T):
        if not lab[i // M][i % M]:
            lab[i // M][i % M] = 1
        else:
            continue
        for j in range(i+1, T):
            if not lab[j // M][j % M]:
                lab[j // M][j % M] = 1
            else:
                continue
            for k in range(j+1, T):
                if not lab[k // M][k % M]:
                    lab[k // M][k % M] = 1
                else:
                    continue

                holiday()
                lab[k // M][k % M] = 0
            lab[j // M][j % M] = 0
        lab[i // M][i % M] = 0


def holiday():
    que = deque([])
    visited = [[0] * M for _ in range(N)]
    for i, j in virus_point:
        visited[i][j] = 1
        que.append((i, j))
    temp = 0
    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < M and not lab[x+dx][y+dy] and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = 1
                que.append((x+dx, y+dy))
                temp += 1
    global ans
    if temp < ans:
        ans = temp


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
virus_point = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus_point.append((i, j))
        elif not lab[i][j]:
            cnt += 1
ans = float('inf')
# print(virus_point)
# print(cnt)

wall()
print(cnt - ans - 3)