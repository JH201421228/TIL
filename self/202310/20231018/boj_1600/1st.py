import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse_delta = [(2, 1), (1, 2), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]


def monkey_horse():
    q = deque([(0, 0, 0)])
    visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]
    visited[0][0][0] = 1
    while q:
        k, x, y = q.popleft()
        if x == H-1 and y == W-1:
            return visited[k][x][y] - 1
        for dx, dy in delta:
            if 0 <= x+dx < H and 0 <= y+dy < W and not board[x+dx][y+dy] and not visited[k][x+dx][y+dy]:
                visited[k][x+dx][y+dy] = visited[k][x][y] + 1
                q.append((k, x+dx, y+dy))
        for dx, dy in horse_delta:
            if k+1 <= K and 0 <= x+dx < H and 0 <= y+dy < W and not board[x+dx][y+dy] and not visited[k+1][x+dx][y+dy]:
                visited[k+1][x+dx][y+dy] = visited[k][x][y] + 1
                q.append((k+1, x+dx, y+dy))
    return -1


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# print(board)
print(monkey_horse())