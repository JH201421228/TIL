import sys
import heapq
from math import sqrt
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday():
    pq = [(0, 0)]
    visited = [0] * N
    ans = 0
    cnt = 0

    while pq:
        if cnt == N:
            break
        dist, now = heapq.heappop(pq)
        if visited[now]:
            continue
        visited[now] = 1
        ans += dist
        cnt += 1

        for next in range(N):
            if not visited[next]:
                heapq.heappush(pq, (star_map[now][next], next))

    return ans


N = int(input())
star_info = [tuple(map(float, input().split())) for _ in range(N)]
# print(star_info)
star_map = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        dist = sqrt((star_info[i][0] - star_info[j][0])**2 + (star_info[i][1] - star_info[j][1])**2)
        star_map[i][j] = star_map[j][i] = dist

# print(star_map)
# for inner in star_map:
#     print(inner)
print(f'{holiday():.2f}')
# print(holiday(1))