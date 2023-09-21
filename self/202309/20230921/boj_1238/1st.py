import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline



def insane_problem1(start):

    distance1[start] = 0
    pq = [(0, start)]
    while pq:
        dist, now = heapq.heappop(pq)
        if distance1[now] < dist:
            continue
        # if now == end:
        #     break
        for next, weight in graph1[now]:
            if distance1[next] > dist + weight:
                distance1[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance1


def insane_problem2(start):

    distance2[start] = 0
    pq = [(0, start)]
    while pq:
        dist, now = heapq.heappop(pq)
        if distance2[now] < dist:
            continue
        # if now == end:
        #     break
        for next, weight in graph2[now]:
            if distance2[next] > dist + weight:
                distance2[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance2


N, M, X = map(int, input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, point = map(int, input().split())
    graph1[start].append([end, point])
    graph2[end].append([start, point])
ans_list = []
distance1 = [float('inf')] * (N+1)
distance2 = [float('inf')] * (N+1)
for i in range(1, N+1):
    ans_list.append(insane_problem1(X)[i] + insane_problem2(X)[i])
print(max(ans_list))