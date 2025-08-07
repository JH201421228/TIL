import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def room_count(grid):
    global N

    res = 0
    V = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not V[i][j] and grid[i][j] == '.':
                res += 1

                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()
                    for dx, dy in delta:
                        xx, yy = x+dx, y+dy
                        if 0 <= xx < N and 0 <= yy < N and grid[xx][yy] == '.' and not V[xx][yy]:
                            V[xx][yy] = 1
                            q.append((xx, yy))

    return res


def solve():
    global N

    N = int(input())

    grid = [list(input().rstrip()) for _ in range(N)]

    init = room_count(grid)

    ans = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                grid[i][j] = '@'
                cnt = room_count(grid)
                grid[i][j] = '.'

                if cnt > init: ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()