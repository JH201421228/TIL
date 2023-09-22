import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, D = map(int, input().split())
graph = [[(i+1, 1)] for i in range(10_001)]
road_info = [list(map(int, input().split())) for _ in range(N)]
gogo = list(range(10_001))
# print(road_info)
while road_info:
    # print(heapq.heappop(road_info))
    start, end, weight = heapq.heappop(road_info)
    # weight > end - start 이면 지름길 쓸 필요 없음
    # end가 고속도로 끝 지점보다 크면 지름길 쓰면 안됨
    #
    if start > D or end > D:
        continue
    elif weight >= end - start:
        continue
    if gogo[start] + weight < gogo[end]:
        gogo[end] = gogo[start] + weight
        for idx in range(end+1, 10_001):
                gogo[idx] = gogo[idx-1] + 1
print(gogo[D])
# print(gogo)