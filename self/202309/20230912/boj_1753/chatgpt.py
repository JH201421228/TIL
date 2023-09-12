import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dijkstra(start):
    # 시작 노드부터의 최단 거리를 저장하는 리스트
    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    # 우선순위 큐를 사용하여 노드를 선택
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 짧은 경로를 찾은 경우 무시
        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            # 현재 경로를 통해 다음 노드까지 가는 거리
            new_dist = dist + weight

            # 더 짧은 경로를 찾은 경우 업데이트
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return distance


V, E = map(int, input().split())
start_point = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    now, next_node, point = map(int, input().split())
    graph[now].append((next_node, point))

distances = dijkstra(start_point)

for idx in range(1, V + 1):
    if idx == start_point:
        print(0)
    elif distances[idx] == float('inf'):
        print('INF')
    else:
        print(distances[idx])
