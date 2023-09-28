import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday():
    pq = [(0, 0, 1)]
    ans_list = [[float('inf')] * (K+1) for _ in range(N+1)]
    # n번째 노드에 총k번 포장해서 갈 수 있는 시간
    ans_list[1][0] = 0

    while pq:
        time, cnt, now = heapq.heappop(pq)
        if ans_list[now][cnt] < time:
            continue
        for next, weight in graph[now]:
            if ans_list[next][cnt] > time + weight:
                ans_list[next][cnt] = time + weight
                heapq.heappush(pq, (time + weight, cnt, next))
            if cnt + 1 < K + 1 and ans_list[next][cnt+1] > time:
                ans_list[next][cnt+1] = time
                heapq.heappush(pq, (time, cnt + 1, next))
    return min(ans_list[-1])


N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# 도착지에 도착할 때 까지
# 포장 횟수가 변수
print(holiday())