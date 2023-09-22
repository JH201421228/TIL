import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


INF = int(1e9)
def fxxking_artist(n1, n2):
    pq = [(0, n1)]
    distance = [INF] * (n+1)
    distance[n1] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance[n2]


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        p1, p2, point = map(int, input().split())
        graph[p1].append((p2, point))
        graph[p2].append((p1, point))
        if (p1 == h and p2 == g) or (p1 == g and p2 == h):
            gh = point

    canditates = []
    for _ in range(t):
        canditates.append(int(input()))
    # g와 h를 지나야 한다.
    # 시작지점은 s
    # 예술가들이 최단거리로 가는것이 힌트
    ans_list = []
    # print(canditates)
    for end in canditates:
        # print(fxxking_artist(s, end))
        # print(fxxking_artist(s, g) + fxxking_artist(h, end) + gh)
        # print(fxxking_artist(s, h) + fxxking_artist(g, end) + gh)
        # print('------------')
        # if end == g:
        #     if fxxking_artist(s, end) == fxxking_artist(s, h) + fxxking_artist(g, end) + gh:
        #         ans_list.append(end)
        # elif end == h:
        #     if fxxking_artist(s, end) == fxxking_artist(s, g) + fxxking_artist(h, end) + gh:
        #         ans_list.append(end)
        if fxxking_artist(s, end) == fxxking_artist(s, g) + fxxking_artist(h, end) + gh or fxxking_artist(s, end) == fxxking_artist(s, h) + fxxking_artist(g, end) + gh:
            ans_list.append(end)
    print(*sorted(ans_list))
