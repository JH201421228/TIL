import sys
import heapq
sys.stdin = open('input.txt')


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def swea_5250():
    ans_list = [[float('inf')] * N for _ in range(N)]
    ans_list[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        dist, x, y = heapq.heappop(pq)
        if ans_list[x][y] < dist:
            continue
        if x == y == N - 1:
            break
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                weight = gauge[x+dx][y+dy] - gauge[x][y]
                if weight < 0:
                    weight = 1
                else:
                    weight += 1
                if ans_list[x+dx][y+dy] > dist + weight:
                    ans_list[x+dx][y+dy] = dist + weight
                    heapq.heappush(pq, (dist + weight, x+dx, y+dy))
    return dist

T = int(input())
for test in range(T):
    N = int(input())
    gauge = [list(map(int, input().split())) for _ in range(N)]
    # print(gauge)
    print(f'#{test + 1} {swea_5250()}')