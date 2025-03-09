import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    try:
        V, E = map(int, input().split())
    except:
        break

    G = [[] for _ in range(V + 1)]
    D = [[float("inf")] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
        D[a][b] = D[b][a] = c  # 양방향 그래프


    def dijkstra(blocked_edge=None):
        dist = [float("inf")] * (V + 1)
        prev = [-1] * (V + 1)
        pq = []

        heapq.heappush(pq, (0, 1))  # (거리, 노드)
        dist[1] = 0

        while pq:
            cur_dist, node = heapq.heappop(pq)

            if cur_dist > dist[node]:
                continue

            for next_node, weight in G[node]:
                if (node, next_node) == blocked_edge or (next_node, node) == blocked_edge:
                    continue  # 선택된 간선을 제외하고 탐색

                new_dist = cur_dist + weight
                if new_dist < dist[next_node]:
                    dist[next_node] = new_dist
                    prev[next_node] = node
                    heapq.heappush(pq, (new_dist, next_node))

        return dist[V], prev


    # 첫 번째 최단 경로 찾기
    min_dist1, prev1 = dijkstra()

    # 최단 경로를 복원하여 가장 중요한 간선을 찾기
    path = []
    node = V
    while prev1[node] != -1:
        path.append((prev1[node], node))
        node = prev1[node]

    # 최적 경로 중 하나의 간선을 차단한 후 다시 다익스트라 실행
    min_dist2 = float("inf")
    for edge in path:
        dist2, _ = dijkstra(blocked_edge=edge)
        min_dist2 = min(min_dist2, dist2)

    print(min_dist1 + min_dist2)
