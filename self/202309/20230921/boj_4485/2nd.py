import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def green_hood_is_zelda():
    pq = [(cave[0][0], 0, 0)]
    check_cave = [[float('inf')] * N for _ in range(N)]
    check_cave[0][0] = cave[0][0]

    while pq:
        dist, x, y = heapq.heappop(pq)
        if check_cave[x][y] < dist:
            continue
        if x == y == N-1:
            break
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                weight = cave[x+dx][y+dy]
                if check_cave[x+dx][y+dy] > dist + weight:
                    check_cave[x+dx][y+dy] = dist + weight
                    heapq.heappush(pq, (dist + weight, x+dx, y+dy))
    return dist

n = 1
while True:
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    # print(cave)
    print(f'Problem {n}: {green_hood_is_zelda()}')
    n += 1