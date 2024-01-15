import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(i, j, n):

    que = deque([(i, j)])

    while que:
        x, y = que.popleft()
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy] and area[x+dx][y+dy] > n:
                que.append((x+dx, y+dy))
                visited[x+dx][y+dy] = 1
    return


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

min_num = float('inf')
max_num = 0

for i in range(N):
    for j in range(N):
        max_num = max(max_num, area[i][j])
        min_num = min(min_num, area[i][j])

# print(max_num, min_num)

ans_list = []

for n in range(min_num, max_num):
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > n and not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j, n)
                ans += 1
    ans_list.append(ans)

# print(ans_list)
if ans_list:
    print(max(ans_list))
else:
    print(1)

# for n in range(min_num, max_num):
#     print(n)
