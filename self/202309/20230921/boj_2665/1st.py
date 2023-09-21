import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def maze_maker():
    maze_checker = [[float('inf')] * n for _ in range(n)]
    maze_checker[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        dist, x, y = heapq.heappop(pq)
        if maze_checker[x][y] < dist:
            continue
        if x == y == n-1:
            break
        for dx, dy in delta:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                weight = 1 - maze[x+dx][y+dy]
                if maze_checker[x+dx][y+dy] > dist + weight:
                    maze_checker[x+dx][y+dy] = dist + weight
                    heapq.heappush(pq, (dist + weight, x+dx, y+dy))
    return maze_checker[-1][-1]


n = int(input())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
# print(maze)
print(maze_maker())