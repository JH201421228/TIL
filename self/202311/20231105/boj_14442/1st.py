import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


N, M, K = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
# print(maze)
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
# for inner in visited:
#     print(inner)

# 벽이 막혀 있으면
q = deque([(0, 0, 0)])
while q:
    x, y = q.popleft()
    for dx, dy in delta:
        if 0 <= x+dx < N and 0 <= y+dy < M: