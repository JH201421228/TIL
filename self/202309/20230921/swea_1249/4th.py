import sys
from collections import deque

sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def solve_with_bfs(N, matrix):
    queue = deque([(0, 0)])
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = matrix[0][0]

    while queue:
        x, y = queue.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = dist[x][y] + matrix[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    queue.append((nx, ny))

    return dist[N-1][N-1]

T = int(input())
for test in range(T):
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    ans = solve_with_bfs(N, matrix)
    print(f'#{test+1} {ans}')
